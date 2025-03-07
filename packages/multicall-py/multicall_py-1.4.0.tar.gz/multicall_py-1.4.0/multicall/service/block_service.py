from typing import Union, List, Dict, Any, Optional
from multicall import Multicall, BalanceCall
from requests import Session
from eth_utils.address import to_checksum_address


class BlockService:
    def __init__(
        self,
        provider_uri: str,
        mc: Optional[Multicall] = None,
        session: Optional[Session] = None,
    ):
        self.mc = mc or Multicall(provider_uri, session=session)

    def get_block(
        self,
        blocks: List[int],
        full_txs: bool = False,
        batch_size: int = -1,
        max_workers: int = 1,
    ) -> List[Dict[str, Any]]:
        calls = [
            BalanceCall(to_checksum_address(addr), request_id=addr)
            for addr in set(a.lower() for a in accounts)
        ]
        result = self.mc.agg(
            calls,
            as_dict=True,
            ignore_error=True,
            batch_size=batch_size,
            max_workers=max_workers,
        )
        assert isinstance(result, dict)

        return [
            {
                "token": "0x0000000000000000000000000000000000000000",
                "asset": "ETH",
                "account": key,
                "value": val,
            }
            for key, val in result.items()
            if val is not None and (val > 0 or keep_zero_balance is True)
        ]

# tests/test_fetcher.py
from abi_fetcher import get_contract_abi

def test_fetch_abi():
    abi = get_contract_abi("0xSomeContract", "ethereum")
    assert isinstance(abi, dict)  # Example test

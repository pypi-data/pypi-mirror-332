import argparse
import json
import os
from abi_fetcher.abi_fetcher import ABIFetcher

def list_networks():
    """Lists all available networks from chainlist.json."""
    fetcher = ABIFetcher()
    networks = [net["chainname"] for net in fetcher.networks["list"]]
    print("Available Networks:")
    for network in networks:
        print(f"- {network}")

def fetch_abi(contract_address, network, api_key, output_dir="ABI"):
    """Fetches and saves the ABI for a given smart contract."""
    fetcher = ABIFetcher()
    try:
        abi = fetcher.fetch_abi(contract_address, network, api_key)
        fetcher.save_abi(abi, contract_address, output_dir)
        print(f"✅ ABI saved: {output_dir}/{contract_address}.json")
    except Exception as e:
        print(f"❌ Error: {e}")

def display_help():
    """Displays help by printing README.md contents if available."""
    base_dir = os.path.dirname(os.path.abspath(__file__)) 
    readme_path = os.path.join(base_dir, "README.md")
    print('path utilisé',readme_path)
    if os.path.exists(readme_path):
        with open(readme_path, "r", encoding="utf-8") as f:
            print(f.read())  # ✅ Prints README.md content

def main():
    """Main CLI function to handle commands."""
    parser = argparse.ArgumentParser(
        prog="abi_fetcher",
        description="Fetch smart contract ABIs from EVM blockchain explorers",
        epilog="Example usage: abi_fetcher --contract 0x123... --network ethereum --api-key YOUR_KEY"
    )
    
    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    # Help Command (default argparse behavior)
    subparsers.add_parser("help", help="display help as in the readme")

    # List Networks Command
    subparsers.add_parser("list", help="List all available networks with their exact command name")

    # Fetch ABI Command
    fetch_parser = subparsers.add_parser("fetch", help="Fetch a smart contract ABI")
    fetch_parser.add_argument("--contract", required=True, help="Smart contract address")
    fetch_parser.add_argument("--network", required=True, help="Network name exactly as displayed in the list")
    fetch_parser.add_argument("--api-key", required=True, help="Your etherscan API key")
    fetch_parser.add_argument("--output", default="ABI", help="Output directory for ABI file (default: ABI/)")

    args = parser.parse_args()

    # Handle commands
    if args.command == "list":
        list_networks()
    elif args.command == "help":
        display_help()
    elif args.command == "fetch":
        fetch_abi(args.contract, args.network, args.api_key, args.output)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()

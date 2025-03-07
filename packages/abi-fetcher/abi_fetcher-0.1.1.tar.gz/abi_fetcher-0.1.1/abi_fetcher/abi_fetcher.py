from web3 import Web3
import requests
import json
import os


class ABIFetcher:

    def __init__(self, chainlist_file="chainlist.json"):
        base_dir = os.path.dirname(os.path.abspath(__file__))  # Get the script's directory
        chainlist_file = os.path.join(base_dir, "chainlist.json")  # Build full path
        self.networks = self.load_networks(chainlist_file)

    def load_networks(self,json_file):
        with open(json_file, 'r') as file:
            return json.load(file)

    def get_api_url(self, network_name):
        """Returns the API URL for a given network."""
        selected_network = next((net for net in self.networks["list"] if net["chainname"] == network_name), None)
        return selected_network["apiurl"] if selected_network else network_name  # Custom URL input

    def fetch_abi(self, contract_address, network, api_key):
        """Fetches ABI from the API"""
        api_url = self.get_api_url(network)
        if not api_url:
            raise ValueError("Invalid network or API URL")

        url = f"{api_url}&module=contract&action=getabi&address={contract_address}&apikey={api_key}"
        print('URL IS :', url)
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()
            if 'result' in data:
                return data['result']
            else:
                raise ValueError("API response does not contain 'result' key")
        else:
            raise ConnectionError(f"Error fetching ABI: {response.status_code}")

    def save_abi(self, abi, contract_address, output_dir="ABI"):
        """Saves ABI JSON to a file"""
        os.makedirs(output_dir, exist_ok=True)
        with open(f"{output_dir}/{contract_address}.json", 'w') as abi_file:
            json.dump(abi, abi_file, indent=4)

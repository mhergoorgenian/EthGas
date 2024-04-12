# Ethereum Gas Price Fetcher

This Python script allows you to fetch current Ethereum gas prices (safe low, standard, and fast) from Etherscan's API. It can be useful for determining appropriate gas prices for Ethereum transactions based on current network conditions.

## Prerequisites

- Python 3.x
- `requests` library (install using `pip install requests`)
- Etherscan API key (get one from [Etherscan](https://etherscan.io/apis))

## Usage

1. Clone this repository to your local machine:

2. Navigate to the cloned directory:

3. Run the script:

This will fetch and display the current safe low, standard, and fast gas prices in Gwei.

## Notes

- Gas prices are subject to change based on Ethereum network conditions. Always verify gas prices before making transactions.
- Handle exceptions appropriately in your application when using this script to fetch gas prices.

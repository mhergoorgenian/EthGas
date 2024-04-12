import requests

def get_eth_gas_price():
    
    url = 'https://api.etherscan.io/api'
    
    
    params = {
        'module': 'gastracker',
        'action': 'gasoracle',
        
    }
    
    try:
        response = requests.get(url, params=params)
        data = response.json()
        
        if data['status'] == '1':
            safe_low = int(data['result']['SafeGasPrice'])
            standard = int(data['result']['ProposeGasPrice'])
            fast = int(data['result']['FastGasPrice'])
            
            return safe_low, standard, fast
        else:
            print("Error: ", data['message'])
            return None
    except Exception as e:
        print("Exception occurred: ", str(e))
        return None


gas_prices = get_eth_gas_price()
if gas_prices:
    print("Safe Low Gas Price (Gwei):", gas_prices[0])
    print("Standard Gas Price (Gwei):", gas_prices[1])
    print("Fast Gas Price (Gwei):", gas_prices[2])

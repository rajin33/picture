import requests




def get_data(address):
    params = {
    'address': address,
    }
    response = requests.get('https://api.honeypot.is/v2/IsHoneypot', params=params)
    data = response.json()
    #print(type(data))
    name = data["token"]["name"]
    taddress = data["token"]["address"]
    holders = data["holderAnalysis"]["holders"]
    liquidity = data["pair"]["liquidity"]
    created_time = data["pair"]["createdAtTimestamp"]
    is_honeypot = data["honeypotResult"]["isHoneypot"]
    simulation_success = data["simulationSuccess"]
    buytax = data["simulationResult"]["buyTax"]
    selltax = data["simulationResult"]["sellTax"]
    transfertax = data["simulationResult"]["transferTax"]
    hightaxwallets = data["holderAnalysis"]["highTaxWallets"]
    is_honeypot2 = data["honeypotResult"]["isHoneypot"]
    pair_name = data["pair"]["pair"]["name"]

    datalist = [name,taddress,holders,liquidity,created_time,is_honeypot,simulation_success,buytax,selltax,transfertax,hightaxwallets,is_honeypot2,pair_name]
    return datalist










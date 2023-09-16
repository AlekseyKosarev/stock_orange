import json
import sys

import math

import requests

from STOCK.testFunc import check_companies

# import Image

api_server_url = 'https://datsorange.devteam.games/'

headers = {
    'token': "65007d3e62b8165007d3e62b83",
}

token = '----WebKitFormBoundary7MA4YWxkTrZu0gW'


def get5minutesNews():
    path = 'news/LatestNews5Minutes'
    response_text = requests.get(api_server_url + path, headers=headers).text
    data = json.loads(response_text)
    print(data)
    return data


def get1minutesNews():
    path = 'news/LatestNews1Minute'
    response_text = requests.get(api_server_url + path, headers=headers).text
    data = json.loads(response_text)
    print(data)
    return data


def getLatestNews():
    path = 'news/LatestNews'
    response_text = requests.get(api_server_url + path, headers=headers).text
    data = json.loads(response_text)
    print(data)
    return data

def getInfo():
    path = 'info'
    response_text = requests.get(api_server_url + path, headers=headers).text
    data = json.loads(response_text)
    print(data)
    return data

def getSellStock():
    path = 'sellStock'
    response_text = requests.get(api_server_url + path, headers=headers).text
    data = json.loads(response_text)
    print(data)
    return data

def getBuyStock():
    path = 'buyStock'
    response_text = requests.get(api_server_url + path, headers=headers).text
    data = json.loads(response_text)
    print(data)
    return data

def getSymbols():
    path = 'getSymbols'
    response_text = requests.get(api_server_url + path, headers=headers).text
    data = json.loads(response_text)
    print(data)
    return data

def limitPriceSell(symbolId: int, price: int, quantity: int):
    path = 'LimitPriceSell'
    data = {'symbolId': symbolId, 'price':price, 'quantity':quantity}
    return requests.post(api_server_url + path, headers=headers, data=json.dump(data)).text

def limitPriceBuy(symbolId: int, price: int, quantity: int):
    path = 'LimitPriceBuy'
    data = {'symbolId': symbolId, 'price':price, 'quantity':quantity}
    return requests.post(api_server_url + path, headers=headers, data=json.dump(data)).text

def bestPriceSell(symbolId: int, quantity: int):
    path = 'BestPriceSell'
    data = {'symbolId': symbolId, 'quantity':quantity}
    return requests.post(api_server_url + path, headers=headers, data=json.dump(data)).text

def bestPriceBuy(symbolId: int, quantity: int):
    path = 'BestPriceBuy'
    data = {'symbolId': symbolId, 'quantity':quantity}
    return requests.post(api_server_url + path, headers=headers, data=json.dump(data)).text


def main():
    print("Stock orange")
    getBuyStock()
    check_companies


if __name__ == "__main__":
    main()

import json
import companies_logic


def get_stock_info(response):  # buy and sells
    bids = {}
    for b in response:
        if b["bids"]:
            bids[b["id"]] = b["bids"]
    return bids

# ----
def get_all_id(get_sympols):
    id_list = [id for id in get_sympols]
    return id_list
    # print(id_list)


def get_all_sells(stock_resp):
    return get_stock_info(stock_resp)


def get_all_buys(stock_resp):
    return get_stock_info(stock_resp)


def get_all_news(news_resp, id_return):
    for news in news_resp:
        list_id = [get_id_from_ticker(id, id_return) for id in news["companiesAffected"]]
        news["companiesAffected"] = list_id
    return news_resp


def get_all_assets(info_resp):

    new_asset = {}
    for asset in info_resp["assets"]:
        new_asset[asset["id"]] = asset["quantity"]
    return new_asset


# --------
def get_id_from_ticker(finded_tiker, all_companies_id):
    for company in all_companies_id:
        id = company["id"]
        ticker = company["ticker"].split('/')[1]
        if finded_tiker == ticker:
            return id
    return None

def get_prices(info):  # info company about buy price
    price = {}
    for prices in info:
        price[prices["price"]] = prices["quantity"]
        # print(price)
    return price


# ----------------
def check_companies(get_symbols, sell_stock, buy_stock, news, info, companies: [companies_logic.Company]):
    list_company = []
    # get id
    id_return = get_all_id(get_symbols)
    # get sells
    sells_return = get_all_sells(sell_stock)
    # get buys
    buys_return = get_all_buys(buy_stock)
    # get news
    news_return = get_all_news(news, id_return)
    # get info
    info_return = get_all_assets(info)

    for company in id_return:
        id = company["id"]
        ticker = company["ticker"]
        buy_data = {}
        sell_data = {}
        news_data = {}
        quantity = 0
        if buys_return.__contains__(id):
            buy_data = get_prices(buys_return[id])
        if sells_return.__contains__(id):
            sell_data = get_prices(sells_return[id])
        not_null_news = [n for n in news_return if n["companiesAffected"].__contains__(id)]
        if not_null_news:
            news_data = not_null_news #возможно нужно удалять companiesAffected
        if id in info_return.keys():
            quantity = info_return[id]

        # check contains company
        contain_company = [qeq.id for qeq in companies]
        if (contain_company.__contains__(id)):  # update
            current_company = [find for find in companies if find.id == id][0]
            current_company.update(buy_data, sell_data, quantity, news_data)
        else:  # create
            list_company.append(companies_logic.Company(id, ticker, buy_data, sell_data, quantity, news_data))
    return list_company


get_sympols_response = json.load(open("jsons_base/get_sympols_response.json"))
sell_stock_response = json.load(open("jsons_base/sell_stock_response.json"))
buy_stock_response = json.load(open("jsons_base/buy_stock_response.json"))
news_response = json.load(open("jsons_base/news_response.json"))
info_response = json.load(open("jsons_base/info_response.json"))


companies = []

info_company = check_companies(get_sympols_response, sell_stock_response, buy_stock_response, news_response,
                               info_response, companies)

id_comp = 5
print(info_company[id_comp-2].id)
print(info_company[id_comp-2].ticker)
print(info_company[id_comp-2].sell_stock)
print(info_company[id_comp-2].buy_stock)
print(info_company[id_comp-2].quantity)
print("----------")
print(info_company[id_comp-2].top_sell_stock)
print(info_company[id_comp-2].top_buy_stock)

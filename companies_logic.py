import datetime
import json
from datetime import datetime

def check_all_min_costs(bids):
    m = {}
    for costs in bids.values():
        c = [(cost["price"], cost["quantity"]) for cost in costs]
        print(min(c))
    return c


class Company:
    # all buy and sells
    # best buy prices or TOP
    # best sell pr or TOP
    # тенденция цены
    # новости
    def __init__(self, _id: int, _ticker: str, _buy_stock: dict, _sell_stock: dict, _quantity: int, _news):
        self.id = _id
        self.ticker = _ticker
        self.buy_stock = _buy_stock  # dict price: quantity
        self.sell_stock = _sell_stock  # dict price: quantity
        self.quantity = _quantity  # quantity
        self.news = _news  # ["date", "text", "rate"]

        self.top_buy_stock = 0
        self.top_sell_stock = 0

        self.time = 0
        self.count_saves = 0


        self.update(_buy_stock, _sell_stock, _quantity, _news)

    def update(self, _buy_stock, _sell_stock, _quantity, _news):
        self.buy_stock = _buy_stock
        self.sell_stock = _sell_stock
        self.quantity = _quantity
        self.news = _news
        self.time = datetime.now().strftime('%H:%M:%S')
        # some func for save history
        self.calc_top_stock()
        self.save_history()


    def calc_top_stock(self):
        self.top_buy_stock = sorted(self.buy_stock)
        self.top_sell_stock = sorted(self.sell_stock)
        return

    def save_history(self):
        self.count_saves += 1;
        data = {'id': self.id,
                'ticker': self.ticker,
                'buy_stock': self.buy_stock,
                'sell_stock': self.sell_stock,
                'quantity': self.quantity,
                'top_buy_stock': self.top_buy_stock,
                'top_sell_stock': self.top_sell_stock,
                'time': self.time,
                'count_save': self.count_saves,
                'news': self.news}
        with open(f'saved_jsons/data_{self.id}_{self.count_saves}.json', 'w', encoding='utf-8') as file:
            file.write(json.dumps(data, indent=4, ensure_ascii=False))
        return

    def calc_buy_coeff(self):
        return

    def calc_sell_coeff(self):
        return

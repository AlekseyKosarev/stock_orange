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

        self.update(_buy_stock, _sell_stock, _quantity, _news)

    def update(self, _buy_stock, _sell_stock, _quantity, _news):
        self.buy_stock = _buy_stock
        self.sell_stock = _sell_stock
        self.quantity = _quantity
        self.news = _news
        # some func for save history
        self.save_history()
        self.calc_top_stock()

    def calc_top_stock(self):  # or min max,,,,,, можно заменить простой сортировкой
        self.top_buy_stock = sorted(self.buy_stock)
        self.top_sell_stock = sorted(self.sell_stock)
        return

    def save_history(self):
        return

    def calc_buy_coeff(self):
        return

    def calc_sell_coeff(self):
        return

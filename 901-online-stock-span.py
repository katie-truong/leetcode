class StockSpanner:

    def __init__(self):
        self.prices = []

    def next(self, price: int) -> int:
        val = 1
        while self.prices and self.prices[-1][0] <= price:
            val += self.prices.pop()[1]
        self.prices.append((price, val))
        return val
        
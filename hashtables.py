stock_prices = {}

with open("stock_prices.csv", "r") as f:
    for line in f:
        tokens = line.split(',')
        day = tokens[0]
        price = float(tokens[1])
        stock_prices[day] = price

print(stock_prices)


class HashTable:
    def __init__(self):
        self.MAX = 100
        self.arr = [None for i in range(self.MAX)]
    def get_hash(self, key):
            h = 0
            for char in key:
                h += ord(char)
            return h % self.MAX
    def add(self, key, val):
            h = self.get_hash(key)
            self.arr[h] = val
            return val

t = HashTable()
qval = t.add('2023-11-03', 100)
print(qval)
print(t.get_hash('apple'))
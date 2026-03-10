from collections import deque

class StockSpanner:

    def __init__(self):
        self.prices = []
        self.indices = deque()
        self.indices.append(-1)

    def next(self, price: int) -> int:

        self.prices.append(price)

        if len(self.prices) == 1:
            return 1

        if self.prices[-2] > price:
            self.indices.append(len(self.prices)-2)
            return 1
        
        count = 1
        idx = len(self.prices)-2
        while (idx >= 0 and price >= self.prices[idx]):
            count += idx-self.indices[-1]
            idx = self.indices.pop()

        self.indices.append(idx)

        return count

if __name__ == '__main__':
    ss = StockSpanner()
    # ls = [1, 2, 3, 4, 5]
    ls = [100, 80, 60, 70, 60, 75, 85]
    for elem in ls:
        print(ss.next(elem))


        
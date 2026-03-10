from sortedcontainers import SortedList
from typing import List

class MovieRentingSystem:
    def __init__(self, n: int, entries: List[List[int]]):
        self.available = dict()
        self.rented = SortedList()
        self.price = dict()

        for shop, movie, price in entries:
            if movie not in self.available:
                self.available[movie] = SortedList()
            self.price[(shop, movie)] = price
            self.available[movie].add((price, shop))

    def search(self, movie: int) -> List[int]:
        if movie not in self.available:
            return []
        
        ans = []
        for price, shop in self.available[movie][:5]:
            ans.append(shop)
        return ans

    def rent(self, shop: int, movie: int) -> None:
        price = self.price[(shop, movie)]
        self.available[movie].remove((price, shop))
        self.rented.add((price, shop, movie))

    def drop(self, shop: int, movie: int) -> None:
        price = self.price[(shop, movie)]
        self.rented.remove((price, shop, movie))
        self.available[movie].add((price, shop))

    def report(self) -> List[List[int]]:
        res = []
        for price, shop, movie in self.rented[:5]:
            res.append((shop, movie))
        return res

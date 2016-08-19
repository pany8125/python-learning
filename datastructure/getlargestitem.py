import heapq

grades = [32, 43, 654, 34, 132, 543, 77, 88]
print(heapq.nlargest(2,grades))

stocks = [
    {'ticker': 'AAPL', 'price': 201},
    {'ticker': 'GOOG', 'price': 800},
    {'ticker': 'F', 'price': 54},
    {'ticker': 'MSFT', 'price': 313},
    {'ticker': 'TUNA', 'price': 68},
]

print(heapq.nsmallest(2, stocks, key=lambda stocks: stocks['price']))
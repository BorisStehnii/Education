stock = {
    "banana": 6,
    "apple": 1,
    "orange": 32,
    "pear": 15
}
prices = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}
sum_buy = 0
for key_1 in stock.keys():
    for key_2 in prices.keys():
        if key_1 == key_2:
            sum_buy += stock[key_1]*prices[key_2]
print(sum_buy)

sum_buy_2 = [stock[key_1]*prices[key_2] for key_1 in stock.keys() for key_2 in prices.keys() if key_1 == key_2]

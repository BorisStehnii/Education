def create_dicts_product():
    stock_dict = {}
    prices_dict = {}
    while True:
        product = input("Введите продукт:")
        stock = input("Введите количество:")
        if not stock.isdigit():
            print("НЕВЕРНЫЙ формат количества")
            continue
        prices = input("Введите цену:")
        if not prices.isdigit():
            print("НЕВЕРНЫЙ формат цены")
            continue
        stock_dict.update({product: int(stock)})
        prices_dict.update({product: int(prices)})
        command = input("Введите 'E' если закончили ввод:").lower()
        if command == "e":
            break
    return stock_dict, prices_dict


stock_buy, prices_buy = create_dicts_product()
sum_buy = sum(stock_buy.get(key, 0)*prices_buy.get(key, 0) for key in stock_buy.keys())
print("Сумма покупок:", sum_buy)

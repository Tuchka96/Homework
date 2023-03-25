price1, price2, price3 = int(input("Цена первого товара:")), int(input("Цена второго товара: ")), int(
    input("Цена третьего товара: "))
price = price1 + price2 + price3
if (price1 < price2) and (price2 < price3):
    print("Акция! к оплате: ", price / 2)
elif (price1 > price2) and (price2 > price3):
    print("Акция! к оплате: ", price / 3)
else:
    print("К оплате:", price)

def localTrade4():
    global price
    salePrice = price*1.2
    print(price, salePrice, end="\n\n")
    price = 2000
    salePrice = price *1.2
    print(price, salePrice, end="\n\n")

price =1000
localTrade4()
print(price)
stock_price = float(input("what is the stock price? "))
update1 = float(input("by what precent did the stock change? "))
update2 = float(input("by what precent did the stock change? "))
update3 = float(input("by what precent did the stock change? "))

stock_price_update1= stock_price+(stock_price*(update1/100)) #update 1
#print(stock_price_update1)
stock_price_update2 = stock_price_update1+(stock_price*(update2/100)) #update 2
#print(stock_price_update2)
stock_price_update3 = stock_price_update2+(stock_price*(update3/100)) #update 3
#print(stock_price_update3)

if stock_price<stock_price_update1 and stock_price_update1<stock_price_update2 and stock_price_update2<stock_price_update3:
    print(f"the stock was profitable thruout all the updates and is now {stock_price_update3}")
else:
    print("the stock was not profitable thruout all the updates")
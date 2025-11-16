stock_price = float(input("what is the stock price? "))
update1 = float(input("by what precent did the stock change? "))
update2 = float(input("by what precent did the stock change? "))

stock_price = stock_price+(stock_price*(update1/100))
#print(stock_price)
stock_price = stock_price+(stock_price*(update2/100))
print(f"the stock price is {stock_price}")
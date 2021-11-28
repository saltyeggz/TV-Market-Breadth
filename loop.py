
#creating some initial variables
print("indicator('Market Breadth', overlay = false)")
print("sVa = input.int(20, 'Small Value')")
print("bVa = input.int(35, 'Big Value')")
#print("bm3 = input.source(close,'Select BM3')")

#creating list of tickers
fhand=open("Tickers.txt")
for line in fhand:
    line = line.rstrip()
    ticker = line
    print(f"{ticker} = input.symbol('{ticker}', title='{ticker}')")
print()
print()

#calculating pmo
print("//calculating pmo")
print("cusm1 = (close - close[1]) * (2/sVa)")
print("cusm2 = (close - close[1]) * (2/sVa) + cusm1[1]")
print("culegnth = ta.sma((((close/close[1])*100)-100), bVa)")
print("pmo = ta.sma(10 * culegnth, sVa)")

#importing ticker data
print("//importing ticker data")
print()
print()
fhand=open("Tickers.txt")
for line in fhand:
    line = line.rstrip()
    ticker = line
    print(f"{ticker}Data = request.security({ticker}, 'D', pmo)")

print()
print()

print("cntr = float(0)")
print()
print()

#counting bullish tickers
fhand=open("Tickers.txt")
for line in fhand:
    line = line.rstrip()
    ticker = line
    print(f"if {ticker}Data > 0")
    print("    cntr := cntr + 1")

#calculating %
print("prcnt= cntr/40")
print("plot(prcnt)")

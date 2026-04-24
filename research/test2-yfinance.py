import yfinance as yf

steel = yf.Ticker("MT")      # ArcelorMittal — proxy de precio acero
steel2 = yf.Ticker("X")      # US Steel
cement = yf.Ticker("SUM")    # Summit Materials — proxy cemento
cement2 = yf.Ticker("EXP")   # Eagle Materials

print(steel.history(period="5d", interval="1m"))
print(steel2.history(period="5d", interval="1m"))
print(cement.history(period="5d", interval="1m"))
print(cement2.history(period="5d", interval="1m"))
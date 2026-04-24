import yfinance as yf

copper = yf.Ticker("HG=F")  # Copper futures
aluminium = yf.Ticker("ALI=F")  # Aluminium futures
# Alternativas para lumber
lumber1 = yf.Ticker("LB=F")
lumber2 = yf.Ticker("LBR=F") 
lumber3 = yf.Ticker("LUMBER")

soybeans = yf.Ticker("ZS=F")  # Soybeans futures

print(copper.history(period="5d", interval="1m"))
print(aluminium.history(period="5d", interval="1m"))
print("LB=F:", lumber1.history(period="5d", interval="1m").shape)
print("LBR=F:", lumber2.history(period="5d", interval="1m").shape)
print("LUMBER:", lumber3.history(period="5d", interval="1m").shape)
print(soybeans.history(period="5d", interval="1m"))

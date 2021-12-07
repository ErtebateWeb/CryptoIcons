# https://screenerplus.ir/signals/tradeable-symbols/?exchange=Kucoin

# import requests module
import requests
import pandas as pd
import downloadicon 
import listdir


url = 'https://api.kucoin.com/api/v1/symbols'

# Making a get request
response = requests.get(url)
  
# print response
# print(response)
  
# print json content
list=response.json()
data = list['data']
# print(data)

i=0
s=[]
for symbol in data:
    # print(symbol['baseCurrency'])
    s.append(symbol['symbol'])
    i=i+1
# print('i=',i)
# print(s)
un=pd.unique(s).tolist()
un.remove('USDT-TUSD')
un.remove('USDT-UST')
un.remove('USDT-USDC')
un.remove('USDT-PAX')
un.remove('USDT-DAI')
print(un)

# print(un)
# print(un[1])
# print('len=',len(un))
for i in range(1, len(un)):
    
    print('symbols=',s[i])
    sym = s[i]
    # if '-BTC' in sym:
    #     filename_quote= sym.replace('-BTC','') 
    # if '-ETH' in sym:
    #     filename_quote= sym.replace('-ETH','') 
    # if '-USDT' in sym:
    #     filename_quote= sym.replace('-USDT','') 
    # if '-KCS' in sym:
    #     filename_quote= sym.replace('-KCS','') 
    filename_quote= sym.replace('-BTC','').replace('-ETH','') .replace('-KCS','') .replace('-USDT','') .replace('-PAX','') .replace('-UST','').replace('-USDC','')
    # filename_quote= sym.removesuffix('-BTC').removesuffix('-ETH').removesuffix('-KCS').removesuffix('-USDT')
    
    # filename=symbol.lower()+'.png'
    filename=filename_quote.lower()
    print('filename=',filename)
    # if s[i] in not listdir.isd
    
            
            
    if not listdir.isdownload(filename) :
        downloadicon.dl(s[i])

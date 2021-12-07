#                (?<=\b)[^\s]+?\.png
import time
from requests.models import Response
from selenium import webdriver
import urllib
from PIL import Image
from io import StringIO
from urllib3.util.url import Url
import requests



def dl(symbol):

    # symbol = input('Enter Symbol:')
    icon=symbol+'-USDT'
    ICON=icon.upper()
    print(ICON)
    Response = requests.get(f'https://trade.kucoin.com/{symbol}')
    print(Response.text)





dl('BTC')



    # driver = webdriver.Chrome("chromedriver.exe")  # Optional argument, if not specified will search path.
    # driver.get(f'https://trade.kucoin.com/{symbol}');
    # time.sleep(5) # Let the user actually see something!
    # imgs = driver.find_elements_by_xpath('//*[@width="20"]')

    # for img in imgs:
    #     URL=img.get_attribute("src")
    #     print(URL)

    # if '-BTC' in symbol:
    #     filename_quote= symbol.replace('-BTC','') 
    
    # if '-ETH' in symbol:
    #     filename_quote= symbol.replace('-ETH','') 
    # if '-USDT' in symbol:
    #     filename_quote= symbol.replace('-USDT','') 
    # if '-KCS' in symbol:
    #     filename_quote= symbol.replace('-KCS','') 

    # # filename=symbol.lower()+'.png'
    # filename=filename_quote.lower()+'.png'
    # r = requests.get(URL).content
    # # print(r)
    # with open (filename, 'wb') as f:
    #     f.write(r)

    # time.sleep(5) # Let the user actually see something!
    # driver.quit()


import glob, os
# os.chdir("/")



downloaded=[]
def downloaded_icons():
    for file in glob.glob("*.png"):
        crypto= file.replace('.png','')
        downloaded.append(crypto)
    print(downloaded)
    return downloaded

def isdownload(symbol):
    
    if symbol in downloaded:
        return True
    else:
        return False
downloaded_icons()        
# isdownload('nebl')
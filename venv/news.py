from bs4 import BeautifulSoup
import requests
from PIL import Image
from io import BytesIO
url="https://news.google.com/topics/CAAqIQgKIhtDQkFTRGdvSUwyMHZNREpmTjNRU0FtVnVLQUFQAQ?hl=en-KE&gl=KE&ceid=KE:en"
info=requests.get(url)
webInfo=BeautifulSoup(info.text,'html.parser')
allH=webInfo.find_all("h3")
n=len(allH)
#for heads in range(n):
 #   print(allH[heads].text)
# searching images links
allImgs=webInfo.find_all("img")
#for imLinks in range(len(allImgs)):
#    print(allImgs[imLinks]['src'])
imUrl=requests.get(allImgs[0]["src"])
imByte=BytesIO(imUrl.content)
image=Image.open(imByte)
image.show()
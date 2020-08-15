from urllib.request import urlopen, Request
apid = input("Amazon Product Id: ") 
url = "https://www.amazon.in//dp/"+apid+"/"
requestingURL = Request(url, headers={'User-Agent' : "APSV1"}) 
page = urlopen(requestingURL).read()
page = str(page)
import re
name = r'<span id="productTitle" class="a-size-extra-large">(.*?)</span>'
price = r'<span class="a-size-medium a-color-price inlineBlock-display offer-price a-text-normal price3P">\\xe2\\x82\\xb9\\xc2\\xa0(.*?)</span>'
instances0 = re.findall(name, page)
instances1 = re.findall(price,page)
print(instances0 + instances1)



from urllib.request import urlopen, Request
url = input("URL:")
requestingURL = Request(url, headers={'User-Agent' : "URLEV1"}) 
page = urlopen(requestingURL).read()
page = str(page)
import re
urllink = r'<a(.*?)>(.*?)</a>'
instances = re.findall(urllink, page)
nolinks = len(instances)
print("No.of Links in this webpage are:" + str(nolinks))
for i in range(1,nolinks+1):
	print(instances[i-1])
	nolinks = nolinks+1



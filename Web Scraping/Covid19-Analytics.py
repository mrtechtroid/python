from urllib.request import urlopen, Request
import re
import time
import sys
from datetime import date
def data(): 
	url = "https://www.worldometers.info/coronavirus/?utm_campaign=homeAdUOA?Si#c-all%22"
	requestingURL = Request(url, headers={'User-Agent' : "CVD19AN-MRT"}) 
	page = urlopen(requestingURL).read()
	page = str(page)
	countryno = r'<td style="font-size:12px;color: grey;text-align:center;vertical-align:middle;">(.*?)</td>'
	country = r'<td style="font-weight: bold; font-size:15px; text-align:left;"><a class="mt_a" href="country/(.*?)/">'
	newcases = r'<td style="font-weight: bold; text-align:right;background-color:#FFEEAA;">(.*?)</td>'
	totalcases = r'<td style="font-weight: bold; text-align:right">(.*?)</td>'
	totalrecovered = r'<td style="font-weight: bold; text-align:right">(.*?)</td>'
	instance0 = re.findall(countryno,page)
	instances1 = re.findall(country, page)
	instances2 = re.findall(newcases,page)
	instances3 = re.findall(totalcases,page)
	instances4 = re.findall(totalrecovered,page)
	if index == "1":
		noofcountry = 0
		print("CNo.Country Name  New Cases  Total Cases Total Recovered")
		for i in range(1,216):
			print(instance0[noofcountry] + "    "+ instances1[noofcountry] +"    "+ instances2[noofcountry] + "    " +instances3[8*noofcountry]+ "    " +instances4[(8*noofcountry)+1]+ "    ")
			noofcountry = noofcountry + 1
		exit
	elif index == "2":
		noofcountry = 0
		today = str(date.today())
		from datetime import datetime
		now = datetime.now()
		dtstr = str(now.strftime("%d-%m-%Y-%H-%M-%S"))
		f = open("Cov19-"+dtstr+'.txt', 'a')
		f.write("CNo.Country Name  New Cases  Total Cases Total Recovered\n")
		for i in range(1,216):
			output = instance0[noofcountry] + "    "+ instances1[noofcountry] +"    "+ instances2[noofcountry] + "    " +instances3[8*noofcountry]+ "    " +instances4[(8*noofcountry)+1]+ "    "
			noofcountry = noofcountry + 1
			f.write(output+" \n")
		f.close()
		print("File Exported")
		exit
	else:
		print("Error!! Please Try again soon...")
		exit()
def progressbar(it, prefix="", size=60, file=sys.stdout):
    count = len(it)
    def show(j):
        x = int(size*j/count)
        file.write("%s[%s%s] %i/%i\r" % (prefix, "#"*x, "."*(size-x), j, count))
        file.flush()        
    show(0)
    for i, item in enumerate(it):
        yield item
        show(i+1)
    file.write("\n")
    file.flush()
print("Covid19 Analytics By MrTechTroid")
print("Visit github.com/mrtechtroid for more apps")
print("Statistics are provided by WorldMeter.info")
print("This App is made for Educational Purposes and should not be used for malicious purposes..")
print("List of Contents")
print("1. Get Data")
print("2. Extract Data in a Text File")
print("3. Exit")
index = input("INDEX:")
if index == "3":
	exit()
else:
	for i in progressbar(range(100), "Computing: ", 40):
		time.sleep(0.1)
	print("It may take some time depending on your Network speed....")
	data()






import os
from selenium import webdriver








title = input('title : \n')

f = open('settings.txt', 'w')




U = os.getlogin()

if os.path.isdir(f"C:\\Users\\{U}\\Desktop\\wallpapers") == False :
	os.mkdir(f"C:\\Users\\{U}\\Desktop\\wallpapers")
else :
	pass

if not os.path.isdir(f"C:\\Users\\{U}\\Desktop\\wallpapers\\{title}"):
	os.mkdir(f"C:\\Users\\{U}\\Desktop\\wallpapers\\{title}")
else :
	pass

from selenium import webdriver



chrome_options = webdriver.ChromeOptions()
prefs = {'download.default_directory' : f'C:\\Users\\{U}\\Desktop\\wallpapers\\{title}'}
chrome_options.add_experimental_option('prefs', prefs)



driver = webdriver.Chrome(chrome_options=chrome_options)


url = f"https://wallpaperaccess.com/{title}"
driver.get(url)

from bs4 import BeautifulSoup as bs
soup = bs(driver.page_source, 'html.parser')
res = soup.find_all('div', attrs = {'class' : "wrapper"})
soup2 = bs(str(res), 'html.parser')
soup2.find_all('a')

import re
res2 = str(soup2.find_all('a'))
res3 = re.findall(r', <a href=.+', res2)
res4 = re.sub(r""">', ', <a href=""", '\n', str(res3))
res5 = re.sub(r"""<a href=""", '\n', str(res4))
res6 = res5.split('"')
res7 = []
for i in range(len(res6)):
	if i % 2 == 0 :
		pass
	elif i %2 == 1:
		print(f"[+] {res6[i]} downloaded")
		res7.append(res6[i])



# part 2


for sth in res7:
	driver.get("https://wallpaperaccess.com"+sth)

driver.close()



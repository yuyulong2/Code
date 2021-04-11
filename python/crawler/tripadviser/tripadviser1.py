import requests


url = 'https://www.tripadvisor.cn/Restaurant_Review-g60763-d4363835-Reviews-Piccola_Cucina_Osteria-New_York_City_New_York.html'
res = requests.get(url)
print(res.status_code)
fout = open('tripadviser1.html','w',encoding="utf-8")
fout.write(res.text)
fout.close()
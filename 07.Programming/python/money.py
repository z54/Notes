import requests
from bs4 import BeautifulSoup
import xlwt

response = requests.get('http://www.cgbchina.com.cn/Channel/16684283?nav=2?nav=2') # 广发理财
#response = requests.get('http://www.baidu.com')

soup = BeautifulSoup(response.content, features="html.parser") # 转换为bs4格式

f1 = open('f1', 'w')
f1.write(str(soup))

#print(soup.div.prettify())
#print(soup.find_all('div', class_="porData"))

f2 = open('f2', 'w')
f2.write(str(soup.find_all('div', class_="porData"))) # 定位到目标范围

f3 = open('f3', 'w')
f4 = open('f4', 'w')

list = [ [0]*22 for i in range(20)] # 二维数组
k = 0

# for i in soup.find('div', class_="porData").strings:
#     f3.write(i)
#     if i.find("%") != -1:
#         f4.write(i+"\n")
#     k += 1
#     print(k,"\n")

f5 = open('f5', 'w')
for i in soup.find_all('tr', class_="bg2"): # 定位到一行
    f5.write("---\n"+str(i)+"\n")
    k2 = 0
    for j in i.strings:
        list[k][k2] = str(j)
        # print(str(j))
        k2 += 1
        # print("k2", k2, "\n")
    k += 1
    # print("k1", k,"\n")

f6 = open('f6', 'w')
book = xlwt.Workbook(encoding='utf-8', style_compression=0) # excel支持
sheet = book.add_sheet('test', cell_overwrite_ok=True) # excel支持，其中test为tab名

for i in range(0, 12):
    for j in range(0, 22):
        # f6.write(list[i][j])
        sheet.write(i, j, list[i][j])
        # print(list[i][j], end="")
    # print("\n")

book.save(r'/users/zach/test1.xls')

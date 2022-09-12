# import requests #импортируем модуль
# fr = "efsdf.html"
# send=requests.post('https://www.gosnadzor.ru/industrial/oil/lessons/2017%20год/АО%20«Краснодарский%20НПЗ-Краснодарэконефть»%2025.12.2017.doc') #делаем запрос
# file = open(fr,'w') #создаем файл для записи результатов
# file.write(send.text) #записываем результат
# file.close() #закрываем файл
# Скачать стриницу в html

# import requests, shutil
#
# dirfile = input()
# file = input()
# fullpath = dirfile + file
# filereq = requests.get(fullpath,stream = True)
# with open(file,"wb") as receive:
#     shutil.copyfileobj(filereq.raw,receive)
#     del filereq
import os
import requests


os.mkdir("allFiles")
os.mkdir("fireFiles")

url_to_the_file = 'https://www.gosnadzor.ru/industrial/oil/lessons/2017 %D0%B3%D0%BE%D0%B4/%D0%90%D0%9E %C2%AB%D0%9A%D1%80%D0%B0%D1%81%D0%BD%D0%BE%D0%B4%D0%B0%D1%80%D1%81%D0%BA%D0%B8%D0%B9 %D0%9D%D0%9F%D0%97-%D0%9A%D1%80%D0%B0%D1%81%D0%BD%D0%BE%D0%B4%D0%B0%D1%80%D1%8D%D0%BA%D0%BE%D0%BD%D0%B5%D1%84%D1%82%D1%8C%C2%BB 25.12.2017.doc'
r = requests.get(url_to_the_file)
with open('allFiles/file.doc', 'wb') as f:
    f.write(r.content)
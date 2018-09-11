from urllib.request import urlopen
import re

url = 'https://lenta.ru/articles/2018/09/11/282/'
pattern_link = '<a.*href\=\"(?P<url>.*?)\".*>(.*)</a>'
pattern_url = '/(https?:\/\/)?(?P<domen>([\da-z\.-]+)\.([a-z\.]{2,6}))([\/\w \.-]*)*\/?'
urls = []

# Получение html страницы
response = urlopen(url)
html = str(response.read())

# Поиск всек ссылок в html
for searched_url in re.findall(pattern_link, html):
  urls.append(searched_url[0])

domen = re.search(pattern_url, url).group('domen')

# Удаление url с таким же доменом как и основной url
for url in urls:
  if url.find(domen) >= 0:
    urls.remove(url)

print(urls)
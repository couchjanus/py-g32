# 
from urllib.request import urlopen

url = "http://books.toscrape.com"
# To open the web page, pass url to urlopen():
page = urlopen(url)
# urlopen() returns an HTTPResponse object: print(page) <http.client.HTTPResponse object at 0x105fef820>
# To extract the HTML from the page, first use the HTTPResponse object’s 
# .read() method, which returns a sequence of bytes. 
html_bytes = page.read()
# Then use .decode() to decode the bytes to a string using UTF-8:
html = html_bytes.decode("utf-8")
print(html)
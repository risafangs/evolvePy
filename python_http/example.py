import bs4, pprint, requests, webbrowser

res = requests.get('http://www.example.com')
soup = bs4.BeautifulSoup(res.text, 'html.parser')

html = soup.prettify()
paragraph = html.select('p')
print(paragraph)
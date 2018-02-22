'''
http://httpbin.org/ip
Grab your current IP from httpbin.org/ip and stores it in a variable
Check for error on the HTTP requests, and if found with gracefully exit the program	Open a browser and send to the following query to Google: “ip locator <your ip>” (replace <your ip> with the IP variable from the previous step)

'''

import bs4, pprint, re, requests, webbrowser

res = requests.get('http://httpbin.org/ip')
soup = bs4.BeautifulSoup(res.text, 'html.parser')

ipRegex = re.compile(r'\d\d\d.\d\d\d.\d\d\d.\d\d\d')
ip = ipRegex.search(soup.prettify())
print(ip.group()) # this prints the IP address as a string

webbrowser.open('https://www.google.com/search?&q={}'.format(ip))

'''
if res.status_code not in ('100', '101', '200', '201', '202', '203', '204', '205', '206'):
	print('HTTP Error received. Exiting.')
else: 
	ipRegex = re.compile(r'\d\d\d.\d\d\d.\d\d\d.\d\d\d')
	ip = ipRegex.search(soup)
	print(ip.group()) # this prints the IP address as a string
'''
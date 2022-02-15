import requests as req
print('version of requests library is:'+req.__version__)

googleHomePage = req.get('http://www.google.com')

print('\n Google Home page Response+Content:')
print(googleHomePage)
print(googleHomePage.content)
print('\n Source Code:')
sourceCode = req.get(
    'https://raw.githubusercontent.com/Codyle212/404-lab-1-shining/main/lab1.py')

print(sourceCode.content.decode("utf-8"))

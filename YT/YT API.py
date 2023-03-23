# API http://suggestqueries.google.com/complete/search?hl=en&ds=yt&client=youtube&hjson=t&cp=1&q=query&format=5&alt=json
import requests

query = input('Enter a keyword Here:\n')
params = {
    'client':'firefox',
    'q':query,
    'h1':'en'
}
url = f'http://suggestqueries.google.com/complete/search?hl=en&ds=yt&client=youtube&hjson=t&cp=1&q={query}&format=5&alt'
resp = requests.get(url , params = params)
result = resp.json()[1]
print('\n')
print('\n')
for data in result:
    print(data , end=' ,\n ')
print('\n')
print('\n')
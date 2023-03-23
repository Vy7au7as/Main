import csv
import requests

query = input('Enter a keyword Here:\n')

params = {
    'client': 'firefox',
    'q': query,
    'h1': 'en',
}

url = f'http://suggestqueries.google.com/complete/search?hl=en&ds=yt&client=youtube&hjson=t&cp=1&q={query}&format=5&alt'
resp = requests.get(url, params=params)
result = resp.json()[1]

all_results = [result]

suggestions = [f'{query} a', f'{query} b', f'{query} c', f'{query} d', f'{query} e', f'{query} g', f'{query} h',
              f'{query} I', f'{query} J', f'{query} K', f'{query} M', f'{query} N', f'{query} O', f'{query} P',
              f'{query} Q', f'{query} R', f'{query}S', f'{query} T', f'{query} U', f'{query} V', f'{query} W',
              f'{query} X', f'{query} Y', f'{query}Z']

for suggestion in suggestions:
    params['q'] = suggestion
    resp = requests.get(url, params=params)
    result = resp.json()[1]
    all_results.append(result)

# Write results to CSV file
filename = f'{query}_suggestions.csv'
with open(filename, 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    for results in all_results:
        for keyword in results:
            writer.writerow([keyword])
print(f'\nAll suggestions have been saved to "{filename}"')

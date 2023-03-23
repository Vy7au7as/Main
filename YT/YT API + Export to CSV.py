import csv
import requests

query = input('Enter a keyword Here:\n')
# country_code = input('Enter two-letter country code (e.g., US, UK,CA,NZ,AU): ')

params = {
    'client': 'firefox',
    'q': query,
    'h1': 'en',
    # 'gl': country_code  # add country code parameter
}

url = f'http://suggestqueries.google.com/complete/search?hl=en&ds=yt&client=youtube&hjson=t&cp=1&q={query}&format=5&alt'
resp = requests.get(url, params=params)
result = resp.json()[1]

# Print initial suggestions
print('\nInitial suggestions:')
for data in result:
    print(data, end=' ,\n ')
print('\n')

# Additional suggestions
print(f'Additional suggestions for "{query}":')
suggestions = [f'{query} a', f'{query} b', f'{query} c', f'{query} d', f'{query} e', f'{query} g', f'{query} h',
              f'{query} I', f'{query} J', f'{query} K', f'{query} M', f'{query} N', f'{query} O', f'{query} P',
              f'{query} Q', f'{query} R', f'{query}S', f'{query} T', f'{query} U', f'{query} V', f'{query} W',
              f'{query} X', f'{query} Y', f'{query}Z']
all_results = [result]
for suggestion in suggestions:
    params['q'] = suggestion
    resp = requests.get(url, params=params)
    result = resp.json()[1]
    all_results.append(result)
    print(f'Suggestions for "{suggestion}":')
    for data in result:
        print(data, end=' ,\n ')
    print('\n')

# Write results to CSV file
filename = f'{query}_suggestions.csv'
with open(filename, 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    for results in all_results:
        writer.writerow(results)
print(f'\nAll suggestions have been saved to "{filename}"')

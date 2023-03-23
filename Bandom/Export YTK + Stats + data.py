import requests
import csv
from datetime import datetime

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
st = input("Do You want to get stats? (Y/N)")
if st == 'Y':
    # Write results to CSV file
    now = datetime.now()
    timestamp = now.strftime("%Y-%m-%d_%H-%M-%S")
    filename = f'{query}_suggestions_{timestamp}.csv'
    with open(filename, 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        for results in all_results:
            for keyword in results:
                writer.writerow([keyword])
    print(f'\nAll suggestions have been saved to "{filename}"')

    # Generating Details About keywords

    def numbers(s, delim):
        return s.partition(delim)[2]

    filename1 = f'{query}_details_{timestamp}.csv'
    with open(filename1, 'w', encoding='UTF8', newline='') as file:
        write = csv.writer(file, delimiter=',')
        write.writerow(['keyword','Competition', 'Volume', 'Score'])
        terms = []
    with open(filename, 'r') as file:
        data = csv.reader(file, delimiter='\n')
        for row in data:
            for i in row:
                terms.append(i)
    for term in terms:
        print(term)
        if ' ' in term:
            term = term.replace(" ", "+")
        url = "https://api.vidiq.com

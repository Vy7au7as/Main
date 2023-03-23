import requests
import csv
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
 filename = f'{query}_suggestions.csv'
 with open(filename, 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    for results in all_results:
        for keyword in results:
            writer.writerow([keyword])
 print(f'\nAll suggestions have been saved to "{filename}"')

 # Generating Details About keywords

 def numbers(s, delim):
        return s.partition(delim)[2]
 filename1 = f'{query}_details.csv'
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
    url = "https://api.vidiq.com/xwords/keyword_search/?term="+ term +"&part=questions&limit=300"
    auth = {'authorization': 'Bearer UKP!e728d052-d362-4d96-b5c2-fe3d8c60e002!8dc5e271-13d7-419e-aaa6-7a0c3b25b3e7'}
    page = requests.get(url, headers=auth)
    d = page.text
    # print(d)
    t = term.replace("+"," ")
    main = '"keyword":"'+t+'",'
    
    # print(url) 
    num = numbers(d, main)
    num= num.replace('"competition":','')
    num = num.replace('"volume":','')
    num = num.replace('"overall":', '')
    num = num.replace('"estimated_monthly_search":', '')
    num = num.replace("}", '')
    # num = num.replace("'","")
    num = num.split(',')
    # print(num)
    real = []
    for i in num:
        i = int(float(i))
        real.append(i)
    comp = real[0]
    score = real[2]
    vol = real[3]
    with open(filename1, 'a', encoding='UTF8', newline='') as file:
        write = csv.writer(file, delimiter=',')
        write.writerow([t, comp, vol, score])
    print("done")
 print(f'\nAll details have been saved to "{filename1}"')
 
import json 

with open('precipitation.json') as file:
    data = json.load(file)


for measurement in data:
    print(measurement['station'])
    
for measurement in data:   
    if measurement['station'] == 'GHCND:US1WAKG0038': 
        print(measurement)

for measurement in data:
    if measurement['value'] > 0:
        print(measurement['value'])

data_seattle = []


for measurement in data: 
    if measurement['station'] == 'GHCND:US1WAKG0038':
        print(measurement)
        data_seattle.append(measurement)
print(data_seattle)


# Filter for all data in January 
# Sum of all data in Januray 



all_months = [0] * 12

for measurement in data_seattle:
    for i in range(12):
        if '2010-' + str(i+1).rjust(2, '0') in measurement['date']:
            all_months[i]= all_months[i] + measurement['value']
    

print(sum(all_months))

with open('result1.json', 'w') as results_file: 
    json.dump(all_months, results_file)

# Calculate the sum of the precipitation over the whole year 

sum_all_precipitation = 11180

print(all_months)
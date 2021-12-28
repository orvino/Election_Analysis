counties = ['Arapaho','Denver', 'Jefferson']
if 'El Paso' not in counties and 'Arapahoe' in counties:
    print('Only Arapahoe are in the list of counties.')
else:
    print('El Paso in not in the list and Arapahoe is in the list of counties')

for county in counties:
    print(county)

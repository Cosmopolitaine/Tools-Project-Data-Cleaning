import pandas as pd

data = pd.read_csv('all_stocks_5yr.csv')

print('=' * 80)
print('Missing Values')
print('=' * 80)

for column in data.columns:
    print('Missing values for: "{}"'.format(column))
    print(data[data[column].isnull()])
    print('\n')


print('=' * 80)
print('Suspicious open close gap')
print('=' * 80)

data['open_close_change_pct'] = (data['open'] - data['close']) / data['open']
print(data[data['open_close_change_pct'].abs() >= 5])
print('\n')

print('=' * 80)
print('Suspicious high low gap')
print('=' * 80)
data['high_low_change_pct'] = (data['high'] - data['low']) / data['high']

print(data[data['high_low_change_pct'].abs() >= 5])
print('\n')

# Sample code to fill NA
#data['open'].fillna(0.)

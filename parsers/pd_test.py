import pandas

# df = pandas.read_csv('hrdata.csv')
# df = pandas.read_csv('hrdata.csv', index_col='Name')
df = pandas.read_csv('hrdata.csv', index_col='Name', parse_dates=['Hire Date'])
print(df)
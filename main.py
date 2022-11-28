import pandas as pd

# Grab our CSV files
csv1 = pd.read_csv('csv1.csv')
csv2 = pd.read_csv('csv2.csv')

# Use Pandas to concat them
(pd.concat([csv1, csv2], axis=1).to_csv(
  'csv3.csv', index=False,
  na_rep='N/A')  # Save our new horizontally joined CSV file as csv3.csv
 )

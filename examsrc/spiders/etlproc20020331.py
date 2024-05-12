import pandas as pd

column_name = ['title20020331', 'genre20020331', 'type20020331', 'priceex20020331', 'pricein20020331', 'tax20020331', 'ava20020331', 'review20020331']

inFile = 'csvdataexamsrc20020331.csv'
df = pd.read_csv(inFile, names=column_name)

df = df[['genre20020331', 'priceex20020331', 'ava20020331']]
print("Before splitting:")
print(df['priceex20020331'])

df['priceex20020331'] = df['priceex20020331'].astype(str).str.split("£")
print("After splitting:")
print(df['priceex20020331'])

df['priceex20020331'] = [float(x[1]) if len(x) > 1 else None for x in df['priceex20020331']]  # Adjusted logic to handle empty lists

df['ava20020331'] = df['ava20020331'].str.split("(")
df['ava20020331'] = [int(x[1].split(" ")[0]) for x in df['ava20020331']]

outFile = 'etldata20020331.csv'
df.to_csv(outFile, header=False, index=False)

print("Filename input: " + inFile)
print(df.info())
print(df.describe(include='all'))
print("Filename output: " + outFile)

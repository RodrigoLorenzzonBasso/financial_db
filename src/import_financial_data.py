import pandas as pd
import sqlite3

xls = pd.ExcelFile('stragegies.xlsx')

sheet_name = "Cópia de ABEV3 1"

df = xls.parse(sheet_name=sheet_name)

nome = df.columns[0]

print(nome)

for (column, data) in df.iteritems():
    if column == nome:
        continue
    print(column)
    print(data)
    break

# nome = df.columns[0]

# metodo_contabil = df.iat[4,6]

# divida_bruta = df.iat[89,6] + df.iat[122,6]

# ano = df.iat[2,6].year

# caixa = df.iat[10,1] + df.iat[11,1]

# divida_liquida = None
# if '-' in str(caixa):
#     divida_liquida = None
# else:
#     divida_liquida = divida_bruta - caixa

# print(caixa)
# print(ano)
# print(df.columns[0])
# print(metodo_contabil)
# print(df.iat[89,6])
# print(df.iat[122,6])
# print(divida_bruta)

# conn = sqlite3.connect('financial.db')

# cursor = conn.cursor()

# values = (sheet_name, nome, ano, metodo_contabil, divida_bruta)

# statement = f'insert into financial values ("{sheet_name}", "{ano}", "{nome}", "{metodo_contabil}", "{divida_bruta}")'

# print(statement)

# cursor.execute("""
# insert into financial
# values (?,?,?,?,?)
# """, values)

# conn.commit()

# conn.close()


# print(df.iat[0,0])


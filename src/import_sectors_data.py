import pandas as pd
import sqlite3

conn = sqlite3.connect('financial.db')

cursor = conn.cursor()

df = pd.read_excel('sectors.xlsx', 'Página1')

for line in df.iterrows():
    ticker = line[1].iloc[0]
    setor = line[1].iloc[3]
    subsetor = line[1].iloc[4]
    segmento = line[1].iloc[5]
    values = (setor, subsetor, segmento, ticker[:-1] + '%')
    cursor.execute("""
        UPDATE financial
        SET setor = ?, subsetor = ?, segmento = ?
        WHERE ticker LIKE ?
    """, values)

conn.commit()
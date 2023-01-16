import pandas as pd
import sqlite3

conn = sqlite3.connect('financial.db')

cursor = conn.cursor()

xls = pd.ExcelFile('financial_data.xlsx')

for sheet_name in xls.sheet_names:

    print(sheet_name)

    df = xls.parse(sheet_name=sheet_name)

    if len(df) != 439:
        continue

    nome = df.columns[0]
    for (column, data) in df.items():
        if column == nome:
            continue
        column_index = df.columns.get_loc(column)

        ano = df.iat[2, column_index].year
        ticker = sheet_name

        metodo_contabil = df.iat[4, column_index]

        ebit = None
        if df.iat[202, column_index] != '-':
            ebit = df.iat[202, column_index]

        pl = None
        if df.iat[161, column_index] != '-':
            pl = df.iat[161, column_index]

        lucro_liquido = None
        if df.iat[214, column_index] != '-':
            lucro_liquido = df.iat[214, column_index]

        receita_liquida = None
        if df.iat[192, column_index] != '-':
            receita_liquida = df.iat[192, column_index]

        quantidade_de_acoes = df.iat[427, column_index]

        divida_bruta = None
        if df.iat[89, column_index] != '-' and df.iat[122, column_index] != '-':
            divida_bruta = df.iat[89, column_index] + df.iat[122, column_index]

        caixa = None
        if df.iat[10, column_index] != '-' and df.iat[11, column_index] != '-':
            caixa = df.iat[10, column_index] + df.iat[11, column_index]

        divida_liquida = None
        if caixa != None and divida_bruta != None:
            divida_liquida = divida_bruta - caixa

        divida_liquida_ebit = None
        if divida_liquida != None and ebit != 0:
            divida_liquida_ebit = divida_liquida / ebit

        divida_bruta_pl = None
        if divida_bruta != None and pl != None:
            divida_bruta_pl = divida_bruta / pl

        margem_bruta = 0
        if receita_liquida != 0 and df.iat[194, column_index] != '-':
            margem_bruta = df.iat[194, column_index] / receita_liquida

        despesas_vga_lucro_bruto = None
        if df.iat[195, column_index] != '-' and df.iat[194, column_index] != 0:
            despesas_vga_lucro_bruto = df.iat[195, column_index] / df.iat[194, column_index]

        deprec_amort_lucro_bruto = None
        if df.iat[225, column_index] != '-'  and df.iat[194, column_index] != 0:
            deprec_amort_lucro_bruto = df.iat[225, column_index] / df.iat[194, column_index]

        margem_ebit = 0
        if receita_liquida != 0 and ebit != None and receita_liquida != None:
            margem_ebit = ebit / receita_liquida

        despesas_juros_ebit = 0
        if ebit != 0 and df.iat[203, column_index] != '-' and ebit != None:
            despesas_juros_ebit = (df.iat[203, column_index] * -1) / ebit

        margem_liquida = 0
        if receita_liquida != 0 and receita_liquida != None and lucro_liquido != None:
            margem_liquida = lucro_liquido / receita_liquida

        lpa = None
        if df.iat[214, column_index] != '-' and df.iat[427, column_index] != '-':
            lpa = df.iat[214, column_index] / df.iat[427, column_index]

        capex = None
        if df.iat[242, column_index] != '-':
            capex = df.iat[242, column_index] * -1

        capex_d_a = None
        if capex != None and df.iat[225, column_index] != '-' and df.iat[225, column_index] != 0:
            capex_d_a = capex / df.iat[225, column_index]

        capex_fco = None
        if capex != None and df.iat[222, column_index] != '-' and df.iat[222, column_index] != 0:
            capex_fco = capex / df.iat[222, column_index]

        reserva_lucros = None
        if df.iat[172, column_index] != '-':
            reserva_lucros = df.iat[172, column_index]

        values = (ticker, nome, ano, metodo_contabil, divida_bruta, divida_liquida, divida_liquida_ebit,
            divida_bruta_pl, receita_liquida, ebit, pl, lucro_liquido,
            margem_bruta, despesas_vga_lucro_bruto, deprec_amort_lucro_bruto,
            margem_ebit, despesas_juros_ebit, margem_liquida, lpa, capex, capex_d_a,
            capex_fco, reserva_lucros, quantidade_de_acoes)

        cursor.execute("""
            INSERT INTO financial (ticker, nome, ano, metodo_contabil, divida_bruta, divida_liquida, divida_liquida_ebit,
            divida_bruta_pl, receita_liquida, ebit, pl, lucro_liquido,
            margem_bruta, despesas_vga_lucro_bruto, deprec_amort_lucro_bruto,
            margem_ebit, despesas_juros_ebit, margem_liquida, lpa, capex, capex_d_a,
            capex_fco, reserva_lucros, quantidade_acoes)
            VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)
        """, values)
        
conn.commit()

conn.close()


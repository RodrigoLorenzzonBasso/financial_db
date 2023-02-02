import sqlite3

conn = sqlite3.connect('financial.db')

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE financial (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    ticker TEXT NOT NULL,
    nome TEXT NOT NULL,
    ano INTEGER NOT NULL,
    metodo_contabil TEXT NOT NULL,
    divida_bruta DECIMAL,
    divida_liquida DECIMAL,
    divida_liquida_ebit DECIMAL,
    divida_bruta_pl DECIMAL,
    receita_liquida DECIMAL,
    ebit DECIMAL,
    pl DECIMAL,
    lucro_liquido DECIMAL,
    margem_bruta DECIMAL,
    despesas_vga_lucro_bruto DECIMAL,
    deprec_amort_lucro_bruto DECIMAL,
    margem_ebit DECIMAL,
    despesas_juros_ebit DECIMAL,
    margem_liquida DECIMAL,
    lpa DECIMAL,
    capex DECIMAL,
    capex_d_a DECIMAL,
    capex_fco DECIMAL,
    reserva_lucros DECIMAL,
    quantidade_acoes DECIMAL,
    setor TEXT,
    subsetor TEXT,
    segmento TEXT
);
""")

print('Tabela criada com sucesso!')

conn.close()
import sqlite3

conn = sqlite3.connect('financial.db')

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE financial (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    ticker TEXT NOT NULL,
    nome TEXT NOT NULL,
    ano INTEGER NOT NULL,
    divida_liquida_ebit DECIMAL,
    divida_bruta_pl DECIMAL,
    margem_bruta DECIMAL,
    despesas_vga_lucro_bruto DECIMAL,
    despesas_juros_ebit DECIMAL,
    deprec_amort_lucro_bruto DECIMAL,
    margem_liquida DECIMAL,
    lucro_liquido DECIMAL,
    divida_bruta DECIMAL,
    divida_liquida DECIMAL,
    lpa DECIMAL,
    reserva_lucros DECIMAL,
    receita_liquida DECIMAL,
    ebit DECIMAL,
    pl DECIMAL,
    capex DECIMAL,
    capex_d_a DECIMAL,
    capex_fco DECIMAL,
    margem_ebit DECIMAL,
    quantidade_acoes DECIMAL,
    metodo_contabil TEXT NOT NULL,
    setor TEXT,
    subsetor TEXT,
    segmento TEXT
);
""")

print('Tabela criada com sucesso!')

conn.close()
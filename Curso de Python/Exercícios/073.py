tabela = ('Palmeiras','Internacional','Flamengo','Fluminense','Corinthians','Athletico-PR','Atlético-MG','São Paulo',
'Fortaleza','Botafogo','América-MG','Santos','Goiás','Bragantino','Coritiba','Cuiabá','Ceára SC','Atlético-GO','Avaí','Juventude')
print(f"Os 5 primeiros colocados são: {tabela[0:5]}")
print(f"Os últimos 4 colocados são: {tabela[-4:]}")
print(f"Odem alfabética: {sorted(tabela)}")
print(f"O Goiás está na {tabela.index('Goiás')+1}ª posição")
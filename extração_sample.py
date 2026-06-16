# O duckdb trabalha direto do .csv no hd a partir das queries de sql (sem carregar em ram)
import duckdb

# USING SAMPLE do duckdb cria a sample aleatória de 1M de linhas
# Dá pra especificar tb algo tipo USING SAMPLE 10% (10% da tabela)
query = """
    SELECT * FROM read_csv_auto('./Genius-song-lyrics-cleaned/song_lyrics 2.csv') 
    USING SAMPLE 1000000;
"""

# Executa a query e devolve um dataframe Pandas normal
df_sample = duckdb.query(query).df()

# Exporta pra um .csv novo
df_sample.to_csv("song_lyrics_sample_duckdb.csv", index=False)
print(df_sample.head())
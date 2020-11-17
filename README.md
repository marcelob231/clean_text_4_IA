# 3 pequenos programas para preparar textos do banco de dados para mineração.

# remove_extras.py
1. Elimina stopwords.
2. Elimina caracteres especiais.
3. Elimina palavras que iniciam com endereços e tags.
4. Normaliza para minúsculas.

# noduplicates.py
1. Elimina duplicatas no banco com base na id do tweet.

# preparation.py
1. Transforma json do MongoDb em Dataframe do Pandas.
2. Tokeniza as sentenças.
3. Stemming para reduzir palavras a sua forma base. 

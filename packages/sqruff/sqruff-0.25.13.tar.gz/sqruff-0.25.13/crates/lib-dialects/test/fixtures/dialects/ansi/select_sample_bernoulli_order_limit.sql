SELECT col1, col2
FROM foo TABLESAMPLE BERNOULLI (10)
ORDER BY col1
LIMIT 100

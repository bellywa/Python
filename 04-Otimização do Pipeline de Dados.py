Código 4: Otimização do Pipeline de Dados
from pyspark.sql import SparkSession
from pyspark.sql.functions import col

# Inicializa uma sessão Spark
spark = SparkSession.builder \
    .appName("Rei do Pitaco Optimized Pipeline") \
    .config("spark.sql.shuffle.partitions", "50") \
    .getOrCreate()

# Leitura dos dados otimizada
data_df = spark.read.parquet("/path/to/data_lake")

# Exemplo de cacheamento para otimização
cached_df = data_df.cache()

# Processamento de dados
processed_df = cached_df.withColumn("processed_column", col("original_column") * 2)

# Escrita dos dados processados
processed_df.write.parquet("/path/to/output", mode="overwrite")

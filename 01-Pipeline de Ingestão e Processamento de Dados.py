Código 1: Pipeline de Ingestão e Processamento de Dados

from pyspark.sql import SparkSession
from pyspark.sql.functions import col

# Inicializa uma sessão Spark
spark = SparkSession.builder \
    .appName("Rei do Pitaco Data Pipeline") \
    .getOrCreate()

# Configurações para leitura do Kafka
kafka_df = spark.readStream \
    .format("kafka") \
    .option("kafka.bootstrap.servers", "localhost:9092") \
    .option("subscribe", "recomendations-topic") \
    .load()

# Conversão dos dados para string
data_df = kafka_df.selectExpr("CAST(key AS STRING)", "CAST(value AS STRING)")

# Processamento básico de dados
processed_df = data_df.withColumn("processed_value", col("value").cast("string"))

# Escreve os dados processados em um Data Lake
query = processed_df.writeStream \
    .format("parquet") \
    .option("path", "/path/to/data_lake") \
    .option("checkpointLocation", "/path/to/checkpoint") \
    .start()

query.awaitTermination()


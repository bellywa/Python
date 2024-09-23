Código 6: Geração de Relatórios de Performance do Pipeline

from pyspark.sql import SparkSession
from pyspark.sql.functions import col, avg

# Inicializa uma sessão Spark
spark = SparkSession.builder \
    .appName("Rei do Pitaco Pipeline Performance Report") \
    .getOrCreate()

# Leitura dos logs de execução do pipeline
log_df = spark.read.json("/path/to/pipeline_logs")

# Calcula a média de tempo de execução por etapa do pipeline
performance_report = log_df.groupBy("stage").agg(avg("execution_time").alias("avg_execution_time"))

# Exibe o relatório
performance_report.show()

# Salva o relatório como CSV
performance_report.write.csv("/path/to/performance_report.csv", header=True)

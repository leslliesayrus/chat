from pyspark.sql import SparkSession
from pyspark.sql.functions import col, udf
from pyspark.sql.types import StructType, StructField, FloatType
import numpy as np

import os
from pyspark import SparkContext

# Inicializa a sessão do Spark
spark = SparkSession.builder \
    .appName("Test UDF") \
    .getOrCreate()




spark.sparkContext.addPyFile("/home/hadoop/numpy_package.zip")
# Adiciona o arquivo zip ao SparkContext


# Define a função calculate_stats_numpy
def calculate_stats_numpy(vl, tipoexec):
    vl_f = [num for num in vl if isinstance(num, (int, float)) and num is not None]
    x = np.array(vl_f)

    if len(x) == 0:
        return None, None, None, None

    if tipoexec == 0:
        _avg_ = float(np.mean(x))
        return _avg_, None, None, None
    else:
        _min_ = float(np.min(x))
        _avg_ = float(np.mean(x))
        _max_ = float(np.max(x))
        _pct50_ = float(np.median(x))

    return _avg_, _min_, _max_, _pct50_

# Registra a UDF
calculate_stats_udf = udf(calculate_stats_numpy, StructType([
    StructField("avg", FloatType(), nullable=True),
    StructField("min", FloatType(), nullable=True),
    StructField("max", FloatType(), nullable=True),
    StructField("pct50", FloatType(), nullable=True)
]))

# Cria um DataFrame de exemplo
data = [
    ([1, 2, 3, 4, 5], 1),
    ([None, 2, 3], 1),
    ([10, 20, None, 30], 1),
    ([5, 5, 5], 0),
    ([None], 1),
]

df = spark.createDataFrame(data, ["values", "tipoexec"])

# Aplica a UDF ao DataFrame
result_df = df.withColumn("stats", calculate_stats_udf(col("values"), col("tipoexec")))

# Seleciona as colunas de interesse
result_df = result_df.select("values", "tipoexec", "stats.*")

# Mostra o resultado
result_df.show(truncate=False)


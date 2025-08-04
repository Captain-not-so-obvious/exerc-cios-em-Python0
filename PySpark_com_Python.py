from pyspark import SparkContext
import numpy as np
from operator import add
spark_contexto = SparkContext()
vetor = np.array([10, 20, 30, 40, 50])
paralelo = spark_contexto.parallelize(vetor)
print(paralelo)
mapa = paralelo.map(lambda x : x**2+x)
mapa.collect()
paralelo = spark_contexto.parallelize(['distribuida', 'distribuida', 'spark', 'rdd', 'spark','spark'])
funcao_lambda = lambda x:(x,1)
mapa = paralelo.map(funcao_lambda).reduceByKey(add).collect()
for (w, c) in mapa:
     print('{}: {}'.format(w, c))
spark_contexto.stop()

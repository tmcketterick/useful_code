from pyspark.sql import SparkSession
from random import random


print("Hello world")

sp = SparkSession.builder.appName("PythonPi").getOrCreate()


def inside(p):
    x, y = random(), random()
    return x*x + y*y < 1

print("Here")

#sp.range(10).collect()

samples = 100000000
count = sp.sparkContext.parallelize(xrange(0, samples)).filter(inside).count()
print("Pi is roughly {}".format(4.0*count/samples))

sp.stop()

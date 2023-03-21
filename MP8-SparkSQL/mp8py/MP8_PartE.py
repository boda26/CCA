from pyspark import SparkContext, SQLContext
from pyspark.sql.types import StructType
from pyspark.sql.types import StructField
from pyspark.sql.types import StringType, IntegerType
from pyspark.sql import SparkSession

sc = SparkContext()
sqlContext = SQLContext(sc)

####
# 1. Setup (10 points): Download the gbook file and write a function to load it in an RDD & DataFrame
####

# RDD API
# Columns:
# 0: place (string), 1: count1 (int), 2: count2 (int), 3: count3 (int)


# Spark SQL - DataFrame API


####
# 5. Joining (10 points): The following program construct a new dataframe out of 'df' with a much smaller size.
####

gbooks = sc.textFile("gbooks").map(lambda x: x.split()).map(lambda y: (y[0], int(y[1]), int(y[2]), int(y[3])))
schema = StructType([StructField("word", StringType()), StructField("count1", IntegerType()), StructField("count2", IntegerType()), StructField("count3", IntegerType())])
spark = SparkSession(sc)
df = spark.createDataFrame(gbooks, schema)

df2 = df.select("word", "count1").distinct().limit(100);
df2.createOrReplaceTempView('dfv2')

query = spark.sql("SELECT count(1) FROM dfv2 as d1 JOIN dfv2 as d2 ON d1.count1=d2.count1")

print(query.first()['count(1)'])

# Now we are going to perform a JOIN operation on 'df2'. Do a self-join on 'df2' in lines with the same #'count1' values and see how many lines this JOIN could produce. Answer this question via DataFrame API and #Spark SQL API
# Spark SQL API

# output: 210


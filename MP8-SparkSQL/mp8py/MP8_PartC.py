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
# 3. Filtering (10 points) Count the number of appearances of word 'ATTRIBUTE'
####

# Spark SQL

# +--------+                                                                      
# |count(1)|
# +--------+
# |     201|
# +--------+

gbooks = sc.textFile("gbooks").map(lambda x: x.split()).map(lambda y: (y[0], int(y[1]), int(y[2]), int(y[3])))
schema = StructType([StructField("word", StringType()), StructField("count1", IntegerType()), StructField("count2", IntegerType()), StructField("count3", IntegerType())])
spark = SparkSession(sc)
df = spark.createDataFrame(gbooks, schema)
df.createOrReplaceTempView("dfv")
query = spark.sql("SELECT count(*) FROM dfv WHERE word LIKE '%ATTRIBUTE%'")
query.show()


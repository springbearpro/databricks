# Databricks notebook source

print("notebook created from databricks")
df = spark.read.parquet("s3://dp-ue1-gen-galaxyp13n-aegis-dev/demo/seed_output/")
df.show(100, False)
print("spark show is done")
# COMMAND ----------



# Databricks notebook source
dbutils.widgets.text("catalog", "dev_lab")
catalog = dbutils.widgets.get("catalog")

print(f"target catalog: {catalog}")

# COMMAND ----------

from pyspark.sql import functions as F

df = spark.createDataFrame(
    [
        ("FIC101.PV", "2026-01-01 00:00:00", 12.5),
        ("TIC202.PV", "2026-01-01 00:00:00", 88.1),
        ("PIC303.PV", "2026-01-01 00:00:00", 3.7),
    ],
    "tag_name string, event_ts string, value double",
)

df = df.withColumn("_ingested_at", F.current_timestamp())

df.write.mode("overwrite").option("mergeSchema", "true").saveAsTable(f"{catalog}.bronze.tag_readings")
print(f"wrote {df.count()} rows to {catalog}.bronze.tag_readings")
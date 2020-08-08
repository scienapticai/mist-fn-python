from mistpy.decorators import *
import random
from pyspark.sql import SQLContext

@with_args(
    arg("input_path", type_hint=str)
)
@on_spark_context
def application(sc, input_path):
    sqlContext = SQLContext(sc)
    df = sqlContext.read.format("csv").option("header", "true").load(input_path)
    output_path = input_path.rsplit(".")[0] + ".parquet"
    df.write.mode("overwrite").parquet(output_path)
    return {"output_path":output_path}
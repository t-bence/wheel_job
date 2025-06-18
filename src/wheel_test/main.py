from pyspark.sql import DataFrame, SparkSession


def get_taxis(spark: SparkSession) -> DataFrame:
    return spark.read.table("samples.nyctaxi.trips")


# Create a new Databricks Connect session. If this fails,
# check that you have configured Databricks Connect correctly.
# See https://docs.databricks.com/dev-tools/databricks-connect.html.
def get_spark() -> SparkSession:
    try:
        from databricks.connect import DatabricksSession

        return DatabricksSession.builder.profile("private").serverless().getOrCreate()
    except ImportError:
        return SparkSession.builder.getOrCreate()


def main(**kwargs):
    import argparse

    print(kwargs)

    parser = argparse.ArgumentParser()
    parser.add_argument("--message", default=kwargs.get("message"))
    args = vars(parser.parse_args())

    print(args["message"])


if __name__ == "__main__":
    main(message="Hello there")

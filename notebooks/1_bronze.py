from pyspark.sql.functions import *

# Azure Event Hub Configuration
event_hub_namespace = "<<Namespace_hostname>>"
event_hub_name="<<Eventhub_Name>>"  
event_hub_conn_str = "<<Connection_string>>"

# Configure Kafka connection options for reading from Azure Event Hubs.
kafka_options = {
    'kafka.bootstrap.servers': f"{event_hub_namespace}:9093", # Specifies the Event Hub namespace and port.
    'subscribe': event_hub_name,    # Sets the Event Hub name to consume events from.
    'kafka.security.protocol': 'SASL_SSL',    # Define secure communication using SASL over SSL with PLAIN mechanism.
    'kafka.sasl.mechanism': 'PLAIN',    # Provides authentication credentials using the Event Hub connection string.
    'kafka.sasl.jaas.config': f'kafkashaded.org.apache.kafka.common.security.plain.PlainLoginModule required username="$ConnectionString" password="{event_hub_conn_str}";',
    'startingOffsets': 'latest',    # Starts reading from the latest available offset.
    'failOnDataLoss': 'false'    # Prevents job failure if data loss is detected (e.g., due to retention limits).
}
#Read stream from eventhub
raw_df = (spark.readStream
          .format("kafka")
          .options(**kafka_options)
          .load()
          )

#Cast data to json
json_df = raw_df.selectExpr("CAST(value AS STRING) as raw_json")

#ADLS configuration 
spark.conf.set(
  "fs.azure.account.key.<<Storageaccount_name>>.dfs.core.windows.net",
  "<<Storage_Account_access_key>>"
)

bronze_path = "abfss://<<container>>@<<Storageaccount_name>>.core.windows.net/<<path>>"

#Write stream to bronze
(
    json_df
    .writeStream
    .format("delta")
    .outputMode("append")
    .option("checkpointLocation", "dbfs:/mnt/bronze/_checkpoints/patient_flow")
    .start(bronze_path)
)

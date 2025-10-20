import json
import random
import uuid
import time
from datetime import datetime, timedelta
from kafka import KafkaProducer

#Eventhub Configuration
EVENTHUBS_NAMESPACE = "<<NAMESPACE_HOSTNAME>>"
EVENT_HUB_NAME="<<EVENT_HUB_NAME>>"  
CONNECTION_STRING = "<<NAMESPACE_CONNECTION_STRING>>"

producer = KafkaProducer(
    bootstrap_servers=[f"{EVENTHUBS_NAMESPACE}:9093"],
    security_protocol="SASL_SSL",
    sasl_mechanism="PLAIN",
    sasl_plain_username="$ConnectionString",
    sasl_plain_password=CONNECTION_STRING,
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

# Departments in hospital
departments = ["Emergency", "Surgery", "ICU", "Pediatrics", "Maternity", "Oncology", "Cardiology"]

# Gender categories 
genders = ["Male", "Female"]

# Helper function to introduce dirty data
def inject_dirty_data(record):

    # 5% chance to have invalid age
    if random.random() < 0.05:
        record["age"] = random.randint(101, 150)

    # 5% chance to have future admission timestamp
    if random.random() < 0.05:
        record["admission_time"] = (datetime.utcnow()+ timedelta(hours=random.randint(1, 72))).isoformat()

    return record

# Function to generate patient admission and discharge events`
def generate_patient_event():
    admission_time = datetime.utcnow() - timedelta(hours=random.randint(0, 72))
    discharge_time = admission_time + timedelta(hours=random.randint(1, 72))
# Create patient event record
    event = {
        "patient_id": str(uuid.uuid4()),
        "gender": random.choice(genders),
        "age": random.randint(1, 100),
        "department": random.choice(departments),
        "admission_time": admission_time.isoformat(),
        "discharge_time": discharge_time.isoformat(),
        "bed_id": random.randint(1, 500),
        "hospital_id": random.randint(1, 7)  # Assuming 7 hospitals in network
    }

    return inject_dirty_data(event)

if __name__ == "__main__":
    while True:
        event = generate_patient_event()
        producer.send(EVENT_HUB_NAME, event) # Send event to Event Hub
        print(f"Sent to Event Hub: {event}")
        time.sleep(1)
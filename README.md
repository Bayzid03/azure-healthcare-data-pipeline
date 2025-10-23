# 🏥 Azure Healthcare Data Pipeline

> **Enterprise real-time streaming data platform for healthcare analytics with Medallion Architecture**

[![Azure](https://img.shields.io/badge/Azure-Cloud%20Platform-0078D4?style=flat-square&logo=microsoft-azure)](https://azure.microsoft.com/)
[![Databricks](https://img.shields.io/badge/Databricks-Data%20Engineering-FF3621?style=flat-square&logo=databricks)](https://databricks.com/)
[![Synapse](https://img.shields.io/badge/Synapse-Analytics-0078D4?style=flat-square)](https://azure.microsoft.com/en-us/products/synapse-analytics/)
[![Delta Lake](https://img.shields.io/badge/Delta%20Lake-Lakehouse-00ADD8?style=flat-square)](https://delta.io/)

## 🎯 Overview

A **production-ready streaming data platform** processing real-time healthcare data through a complete **Bronze → Silver → Gold** medallion architecture. Built with Azure Event Hubs, Databricks, Delta Lake, and Synapse Analytics for scalable patient flow analytics and operational insights.

### ✨ Key Features

- **⚡ Real-time Streaming** - Event Hubs + Kafka for continuous data ingestion
- **🏗️ Medallion Architecture** - Bronze (raw) → Silver (cleaned) → Gold (dimensional)
- **🔄 Schema Evolution** - Automatic adaptation to changing data structures
- **📊 Dimensional Modeling** - Star schema with SCD Type 2 for patient history
- **🛡️ Data Quality** - Automated validation, cleansing, and dirty data handling
- **☁️ Azure-Native** - Fully managed cloud services with enterprise security
- **📈 Power BI Integration** - Real-time dashboards for hospital operations

## 🏗️ Architecture

```
┌──────────────────────────────────────────────────────────────┐
│                   DATA GENERATION LAYER                      │
├──────────────────────────────────────────────────────────────┤
│  🎲 Patient Data Simulator                                   │
│  ├── Real-time event generation (1 event/sec)                │
│  ├── 7 departments, 500 beds, 7 hospitals                    │
│  └── Dirty data injection (5% invalid records)               │
└──────────────────────────────────────────────────────────────┘
                            ↓
                  🔐 Azure Key Vault
              (Secure connection strings)
                            ↓
┌──────────────────────────────────────────────────────────────┐
│                   STREAMING INGESTION                        │
├──────────────────────────────────────────────────────────────┤
│  📡 Azure Event Hubs (Kafka Protocol)                        │
│  • Real-time message broker                                  │
│  • SASL_SSL security                                         │
│  • Fault-tolerant streaming                                  │
└──────────────────────────────────────────────────────────────┘
                            ↓
┌──────────────────────────────────────────────────────────────┐
│                   BRONZE LAYER (Raw Data)                    │
├──────────────────────────────────────────────────────────────┤
│  🗄️ Delta Lake on ADLS Gen2                                 │
│  • Raw JSON ingestion                                        │
│  • Checkpointing for recovery                                │
│  • Append-only writes                                        │
│  Script: 1_bronze.py                                         │
└──────────────────────────────────────────────────────────────┘
                            ↓
                  🔄 PySpark Transformations
                            ↓
┌──────────────────────────────────────────────────────────────┐
│                   SILVER LAYER (Cleaned Data)                │
├──────────────────────────────────────────────────────────────┤
│  ✨ Data Quality & Cleansing                                 │
│  • Schema validation & evolution                             │
│  • Type conversions (string → timestamp)                     │
│  • Invalid data correction                                   │
│    - Future admission times → current_timestamp              │
│    - Age > 100 → random valid age (1-90)                     │
│  • Missing column injection (schema drift handling)          │
│  Script: 2_silver.py                                         │
└──────────────────────────────────────────────────────────────┘
                            ↓
                  🏗️ Dimensional Modeling
                            ↓
┌──────────────────────────────────────────────────────────────┐
│                   GOLD LAYER (Business Data)                 │
├─────────────────────────┬────────────────────────────────────┤
│  📊 DIMENSIONS          │  ⭐ FACTS                          │
├─────────────────────────┼────────────────────────────────────┤
│ • dim_patient          │ • fact_patient_flow                │
│   - SCD Type 2         │   - Admission/discharge events     │
│   - Patient history    │   - Length of stay metrics         │
│   - Surrogate keys     │   - Bed occupancy tracking         │
│ • dim_department       │   - Real-time admission status     │
│   - Hospital locations │                                    │
│   Script: 3_gold.py    │                                    │
└─────────────────────────┴────────────────────────────────────┘
                            ↓
                  🔗 Azure Data Factory
            (Orchestration & Scheduling)
                            ↓
┌──────────────────────────────────────────────────────────────┐
│               AZURE SYNAPSE SQL POOL                         │
├──────────────────────────────────────────────────────────────┤
│  🗄️ Enterprise Data Warehouse                               │
│  • External tables on Delta Lake                             │
│  • Pre-aggregated views for KPIs                             │
│  • Optimized for BI queries                                  │
│  Scripts: sql_pool_queries.sql, views.sql                    │
└──────────────────────────────────────────────────────────────┘
                            ↓
┌──────────────────────────────────────────────────────────────┐
│                   POWER BI DASHBOARDS                        │
├──────────────────────────────────────────────────────────────┤
│  📊 Hospital Operations Analytics                            │
│  • Bed occupancy rates by gender                             │
│  • Patient volume trends                                     │
│  • Average treatment duration by department                  │
│  • Overstay patient tracking                                 │
│  • Department inflow analysis                                │
└──────────────────────────────────────────────────────────────┘
```

## 🛠️ Technical Stack

### **Cloud & Data Services**
- **☁️ Azure Event Hubs** - Kafka-compatible streaming ingestion
- **🔥 Azure Databricks** - Unified data processing and analytics
- **💾 Azure Data Lake Storage Gen2** - Scalable data lake with Delta Lake
- **🔑 Azure Key Vault** - Secure secrets management
- **🔐 Azure Active Directory** - Identity & access management
- **📊 Azure Synapse Analytics** - Enterprise data warehouse
- **🔄 Azure Data Factory** - ETL orchestration and automation

### **Data Engineering**
- **⚡ Apache Spark** - Distributed data processing (PySpark)
- **🌊 Structured Streaming** - Real-time data pipelines
- **🗄️ Delta Lake** - ACID transactions, time travel, schema evolution
- **📊 Star Schema** - Dimensional modeling with SCD Type 2
- **🔧 Kafka Protocol** - Reliable event streaming

### **Analytics & Visualization**
- **💼 Power BI** - Interactive dashboards and reports
- **📈 SQL Views** - Pre-aggregated KPIs for fast querying
- **🎯 Real-time Metrics** - Hospital operational intelligence

## 📊 Data Model

### **Dimensional Tables**
| Table | Columns | SCD Type | Purpose |
|-------|---------|----------|---------|
| `dim_patient` | patient_id, gender, age, effective_from/to, is_current | Type 2 | Patient demographics with history tracking |
| `dim_department` | department, hospital_id | Type 1 | Hospital department catalog |

### **Fact Table**
| Table | Grain | Metrics |
|-------|-------|---------|
| `fact_patient_flow` | One row per admission event | length_of_stay_hours, is_currently_admitted, bed_id |

### **Generated Data Entities**
- **👤 Patients** - UUID-based identifiers, age, gender
- **🏥 Departments** - Emergency, Surgery, ICU, Pediatrics, Maternity, Oncology, Cardiology
- **🛏️ Resources** - 500 beds across 7 hospitals
- **📅 Events** - Admission/discharge with timestamps

## 🚀 Quick Start

### Prerequisites
- Azure subscription with appropriate permissions
- Azure Databricks workspace
- Azure Event Hubs namespace
- Azure Data Lake Storage Gen2 account
- Python 3.8+ (for data generator)

### Setup

```bash
# 1. Configure Azure resources
# Create Event Hub namespace and hub
# Create ADLS Gen2 storage with containers: bronze, silver, gold
# Create Azure Key Vault and store connection strings

# 2. Run data generator
cd data_generator/
pip install kafka-python
python patient_data_generator.py

# 3. Deploy Databricks notebooks
# Upload notebooks to Databricks workspace
# Configure ADLS access keys in notebooks
# Run in sequence: 1_bronze.py → 2_silver.py → 3_gold.py

# 4. Setup Synapse Analytics
# Create dedicated SQL pool
# Run sql_pool_queries.sql to create external tables
# Run views.sql to create analytical views

# 5. Connect Power BI
# Link to Synapse SQL Pool
# Build dashboards from views
```

## 📈 Key Performance Indicators

### **Pre-built Analytics Views**

```sql
-- 1. Bed Occupancy Rate by Gender
vw_bed_occupancy

-- 2. Bed Turnover Rate (admissions per bed)
vw_bed_turnover_rate

-- 3. Current Patient Count by Demographics
vw_patient_demographics

-- 4. Average Treatment Duration by Department
vw_avg_treatment_duration

-- 5. Patient Volume Trends Over Time
vw_patient_volume_trend

-- 6. Department Patient Inflow Analysis
vw_department_inflow

-- 7. Overstay Patients (> 50 hours)
vw_overstay_patients
```

## 🔧 Data Quality Features

### **Automated Cleansing**
- **📅 Invalid Timestamps** - Future admission times replaced with current_timestamp
- **👴 Invalid Age** - Values > 100 replaced with random valid age (1-90)
- **📋 Schema Evolution** - Missing columns automatically added with null values
- **🔄 Type Conversions** - String → Timestamp for temporal columns

### **Dirty Data Handling**
- **5% Invalid Records** - Intentionally injected for testing data quality logic
- **Validation Rules** - Age range (1-100), timestamp logic checks
- **Error Recovery** - Checkpointing for fault tolerance in streaming

## 📁 Project Structure

```
azure-healthcare-data-pipeline/
├── data_generator/
│   └── patient_data_generator.py    # Kafka producer for Event Hubs
├── notebooks/
│   ├── 1_bronze.py                  # Raw data ingestion
│   ├── 2_silver.py                  # Data cleansing & validation
│   └── 3_gold.py                    # Dimensional modeling (SCD Type 2)
├── sqlpool_queries/
│   ├── sql_pool_queries.sql         # External table creation
│   └── views.sql                    # KPI views for Power BI
└── Healthcare Data Engineer Project.docx  # Project documentation
```

## 🌟 Advanced Features

### **Schema Evolution**
```python
# Automatic adaptation to new columns
expected_cols = ["patient_id", "gender", "age", "department", ...]
for col_name in expected_cols:
    if col_name not in clean_df.columns:
        clean_df = clean_df.withColumn(col_name, lit(None))
```

### **SCD Type 2 Implementation**
```python
# Patient dimension with full history tracking
# - effective_from / effective_to timestamps
# - is_current flag for latest version
# - surrogate keys for fact table joins
# - Hash-based change detection
```

### **Real-time Metrics**
```python
# Calculate length of stay in real-time
length_of_stay_hours = (discharge_time - admission_time) / 3600

# Track currently admitted patients
is_currently_admitted = discharge_time > current_timestamp()
```

## 🔐 Security & Governance

- **🔑 Azure Key Vault** - Centralized secrets management
- **🛡️ Managed Identity** - Secure service-to-service authentication
- **🔐 SASL_SSL** - Encrypted data transmission
- **📋 Access Control** - Azure AD integration for role-based access
- **📊 Audit Logs** - Complete data lineage tracking

## 🎯 Real-world Use Cases

- **🏥 Hospital Operations** - Real-time bed management and capacity planning
- **📊 Executive Dashboards** - Daily operational metrics and KPIs
- **💼 Resource Optimization** - Department staffing based on patient flow
- **⚕️ Clinical Analytics** - Treatment duration analysis by department
- **📈 Trend Analysis** - Patient volume forecasting and seasonality

## 🚀 Future Enhancements

- [ ] **🤖 Predictive Analytics** - ML models for admission forecasting
- [ ] **📱 Mobile Alerts** - Real-time notifications for bed capacity
- [ ] **🔗 HL7/FHIR Integration** - Standard healthcare data formats
- [ ] **🌍 Multi-region Support** - Global hospital network analytics
- [ ] **🧪 A/B Testing** - Treatment effectiveness analysis
- [ ] **🔔 Anomaly Detection** - Alert on unusual patient flow patterns

## 🤝 Contributing

Contributions welcome! Focus areas:
- **📊 Additional KPIs** - New analytical views and metrics
- **🔧 Performance Tuning** - Spark optimization and partitioning strategies
- **🛡️ Security Enhancements** - Additional governance features
- **📈 ML Integration** - Predictive models using Databricks ML

## 📄 License

MIT License - See [LICENSE](LICENSE) for details.

---

**Enterprise healthcare analytics powered by Azure cloud services** ⚕️☁️

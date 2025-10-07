# Capstone Project: Scalable Data Pipeline with PySpark & Azure

Built a scalable, cloud-ready data pipeline using PySpark and Azure services to ingest, process, and store OpenFDA Adverse Event data.

```bash
✅ End-to-end ETL pipeline from raw JSON to clean Parquet
✅ Designed for scale using Azure Databricks and Blob Storage
✅ Emphasis on production readiness, unit testing, and cloud integration
```
## Project Highlights

- Dataset: OpenFDA Adverse Event Data(~50GB)
- Pipeline: Python prototype → PySpark ETL → Azure Databricks
- Storage: Azure Blob Storage for raw & processed data
- Output Format: Apache Parquet
- Testing: Pytest with mocks and Spark local sessions

## Architecture Overview

**Pipeline Flow:**
- Ingest: Download OpenFDA JSON data and upload to Azure Blob using AzCopy
- Prototype: Develop local ETL pipeline in Python for exploration
- Scale: Refactor to PySpark, deploy on Azure Databricks
- Store: Save cleaned data in Parquet format back to Azure Blob

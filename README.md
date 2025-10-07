# Capstone Project: Scalable Data Pipeline with PySpark & Azure

Built a scalable, cloud-ready data pipeline using PySpark and Azure services to ingest, process, and store OpenFDA Adverse Event data.
- End-to-end ETL pipeline from raw JSON to clean Parquet
- Designed for scale using Azure Databricks and Blob Storage
- Emphasis on production readiness, unit testing, and cloud integration

## Project Highlights

- Dataset: OpenFDA Adverse Event Data(~50GB)
- Pipeline: Python prototype → PySpark ETL → Azure Databricks
- Storage: Azure Blob Storage for raw & processed data
- Output Format: Apache Parquet
- Testing: Pytest with mocks and Spark local sessions

## Architecture Overview

**Pipeline Flow:**
- **Ingest**: Download OpenFDA JSON data and upload to Azure Blob using AzCopy
- **Prototype**: Develop local ETL pipeline in Python for exploration
- **Scale**: Refactor to PySpark, deploy on Azure Databricks
- **Store**: Save cleaned data in Parquet format back to Azure Blob

## Technologies Used

| Category        | Tools & Services                          |
| --------------- | ----------------------------------------- |
| Programming     | Python, PySpark                           |
| Cloud & Storage | Azure Blob Storage, AzCopy                |
| Compute         | Azure Databricks (Single-node cluster)    |
| Data Formats    | JSON (input), Parquet (output)            |
| Testing         | Pytest, PySpark Local, Mocking Azure APIs |
| Deployment      | Databricks Jobs, Spark Configurations     |


## Testing & Validation

- Unit tests written with pytest
- Covers extractor, transformer, and loader modules
- Includes edge cases and failure scenarios
- Uses mocks for Azure Blob and PySpark sessions
- Code coverage reports with pytest-cov

Run tests locally:<br> 
  pytest --cov=etl --cov-report=term-missing -v tests/

# 🌊 Spark Data Lake Pipeline (Medallion Architecture)

[![CI Pipeline](https://github.com/MSBHOSLE/spark-data-lake-pipeline/actions/workflows/ci.yml/badge.svg)](https://github.com/MSBHOSLE/spark-data-lake-pipeline/actions)
[![PySpark](https://img.shields.io/badge/PySpark-3.5%2B-E25A1C?logo=apache-spark&logoColor=white)](https://spark.apache.org/)
[![Delta Lake](https://img.shields.io/badge/Delta%20Lake-ACID%20Storage-00ADD8?logo=delta&logoColor=white)](https://delta.io/)
[![Python](https://img.shields.io/badge/Python-3.11%2B-blue?logo=python&logoColor=white)](https://python.org)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

An enterprise-grade **PySpark ETL Lakehouse Pipeline** implementing the **Bronze / Silver / Gold Medallion Architecture** backed by **Delta Lake**. Features automated schema enforcement, deduplication, incremental transformations, and business KPI aggregations.

---

## 🏗️ Medallion Architecture Overview

```mermaid
flowchart LR
    Raw["Raw Event Stream"] --> Bronze["🥉 Bronze Layer (Raw Logs & Metadata)"]
    Bronze --> Silver["🥈 Silver Layer (Cleansed, Deduplicated, Validated)"]
    Silver --> Gold["🥇 Gold Layer (Aggregated Business Metrics & KPIs)"]
```

---

## ⚡ Highlights

- **Bronze Layer**: Append-only raw event ingestion preserving original payload fidelity.
- **Silver Layer**: Data cleansing, schema conformity, deduplication, and anomaly rejection.
- **Gold Layer**: Aggregated star-schema / dimensional metrics computed for business intelligence and analytics.

---

## 🚀 Running Tests

```bash
python -m unittest discover tests
```

---

## 👤 Author

**Mahesh Sanjayrao Bhosle**
- **GitHub:** [@MSBHOSLE](https://github.com/MSBHOSLE)
- **LinkedIn:** [Mahesh Bhosle](https://linkedin.com/in/mahesh-bhosle-916991198)
- **Email:** msbhosle.2@gmail.com
- **Education:** M.Sc. Data & Computer Science, Heidelberg University

---

## 📄 License

MIT License - see [LICENSE](LICENSE).

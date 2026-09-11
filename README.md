# Logistics Data Analysis, Cleaning & Preprocessing

**Yuva Intern Logistics Data Analyst Internship – Week 1 & Week 2**

This portfolio project demonstrates a practical logistics analytics workflow using Python and pandas. Week 2 focuses on data collection simulation, data-quality assessment, cleaning, missing-value handling, duplicate removal, categorical normalization, date conversion, and outlier treatment.

## Project Objective

Prepare a logistics shipment dataset for reliable downstream analysis by identifying and correcting common data-quality problems while keeping the preprocessing workflow reproducible.

## Dataset

The repository contains a **synthetic logistics dataset** created for demonstration and internship purposes. It represents shipment, transportation, delivery-time, inventory, and cost records. It intentionally includes realistic quality issues so that the preprocessing pipeline can be demonstrated.

> The dataset is synthetic and should not be presented as confidential company data.

## Week 2 Data-Quality Issues

- Missing numerical and categorical values
- Duplicate shipment records
- Inconsistent category formatting
- Invalid/mixed date values
- Extreme numerical observations/outliers
- Incorrect or inconsistent data types

## Preprocessing Workflow

1. Load the raw CSV with pandas.
2. Inspect shape, columns, data types, missing values, and duplicates.
3. Standardize column names and categorical text.
4. Convert shipment and delivery dates to datetime.
5. Calculate shipment duration in days.
6. Impute numerical missing values with the median where appropriate.
7. Fill missing categorical values with `Unknown`.
8. Remove duplicate shipment records.
9. Detect numerical outliers using the IQR method.
10. Cap extreme values at IQR-based lower/upper bounds rather than deleting valid records automatically.
11. Validate the cleaned dataset.
12. Export the cleaned data for further analysis.

## Repository Structure

```text
logistics-data-analysis/
├── data/
│   └── logistics_data.csv
├── notebooks/
├── reports/
│   └── figures/
├── src/
│   └── analysis.py
├── requirements.txt
└── README.md
```

## How to Run

```bash
git clone https://github.com/ankitsharma-data/logistics-data-analysis.git
cd logistics-data-analysis
pip install -r requirements.txt
python src/analysis.py
```

The script creates `data/logistics_data_cleaned.csv` after preprocessing.

## Key KPIs for Future Analysis

- On-Time Delivery Rate
- Average Delivery Time
- Cost per Shipment
- Delay Rate
- Average Shipping Distance
- Average Shipment Weight

## Business Questions

- Which warehouses have the highest delay rates?
- Does delivery distance affect delivery time?
- Which traffic and weather conditions are associated with delays?
- Which operational areas require additional resources?
- How can predictive analytics support proactive delay management?

## Planned Extensions

- Exploratory Data Analysis (EDA)
- Power BI dashboard
- Regression for delivery-time prediction
- Classification for delay prediction
- K-Means clustering for shipment segmentation
- Route and resource optimization

## Author

**Ankit Sharma**  
BCA Student | Aspiring Data Analyst

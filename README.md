# 📊 Vendor Performance Analysis & Data Pipeline

🚀 A complete **Data Analysis + Data Ingestion Project** built using Python to analyze vendor performance and generate business insights.

---

## 📌 Project Description

This project focuses on:

* 📥 Loading raw CSV data into a database
* 🗄️ Managing structured data using SQLite
* 📊 Performing Exploratory Data Analysis (EDA)
* 📈 Creating visualizations to understand vendor performance
* 📝 Logging ingestion process for monitoring

---

## 🛠️ Tech Stack

* **Python**
* **Pandas**
* **NumPy**
* **Matplotlib / Seaborn**
* **SQLite**
* **SQLAlchemy**
* **Jupyter Notebook**

---

## 📂 Project Structure

```
vendor-performance-analysis/
│
├── data/                      # Raw CSV files
├── notebooks/
│   ├── Exploratory Data Analysis.ipynb
│   └── Vendor Performance analysis.ipynb
│
├── src/
│   └── ingestion.py          # Data ingestion script
│
├── requirements.txt
└── README.md
```

---

## ⚙️ Setup Instructions

### 1️⃣ Clone the Repository

```
git clone https://github.com/your-username/vendor-performance-analysis.git
cd vendor-performance-analysis
```

### 2️⃣ Install Dependencies

```
pip install -r requirements.txt
```

---

## 📥 Data Ingestion

The ingestion script performs:

* Reads CSV files from a directory
* Loads data into SQLite database (`inventory.db`)
* Automatically creates tables
* Logs ingestion details

### ▶️ Run Script

```
python src/ingestion.py
```

---

## 📊 Exploratory Data Analysis (EDA)

EDA is performed using Jupyter notebooks to analyze:

* Vendor performance
* Sales distribution
* Revenue trends
* Order patterns

### 📓 Notebooks

* `Exploratory Data Analysis.ipynb`
* `Vendor Performance analysis.ipynb`

---

## 📈 Key Visualizations

### 🔹 Vendor Revenue Analysis

* **X-axis:** Vendor Name
* **Y-axis:** Revenue
* **Insight:** Identifies top-performing vendors

---

### 🔹 Sales vs Orders

* **X-axis:** Number of Orders
* **Y-axis:** Revenue
* **Insight:** Shows correlation between demand and earnings

---

### 🔹 Monthly Trends

* **X-axis:** Time (Months)
* **Y-axis:** Sales/Revenue
* **Insight:** Detects seasonal patterns

---

## 🖼️ Sample Graphs

> (Upload your graph screenshots in `images/` folder)

```
![Revenue Graph](images/revenue.png)
![Trend Graph](images/trend.png)
```

---

## 📝 Logging

* Logs ingestion process
* Tracks execution time
* Helps in debugging

---

## ⚡ Features

✔ Automated data ingestion
✔ Clean and structured pipeline
✔ Insightful visualizations
✔ Real-world project structure

---

## 🔮 Future Improvements

* Build dashboard using Streamlit
* Deploy on cloud
* Add real-time data processing
* Improve data validation

---

## 👨‍💻 Author

**Vishal Biswas**

---

## ⭐ Support

If you like this project, give it a ⭐ on GitHub!

---

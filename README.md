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




<img width="1488" height="990" alt="2a516b8369169701c046f55e77d1dce2d2a9396e" src="https://github.com/user-attachments/assets/5de96920-fc61-4753-9df5-583312998ad3" />

<img width="1491" height="490" alt="1c37e0e55c546d6c8864510fbfb6e68bb48d50ec" src="https://github.com/user-attachments/assets/1576cf83-874f-4b93-b23f-e72799c64618" />

<img width="1489" height="989" alt="68ad3909fd257f035a49f25653c9ae39327b964c" src="https://github.com/user-attachments/assets/29ffc684-f02c-40f8-a2c9-f4d40cb5cee2" />

<img width="1038" height="592" alt="2802e87255fdbcc1c631dceb2d60c94ad4639268" src="https://github.com/user-attachments/assets/fcb6697d-4fe6-4417-8701-5b44da032b8e" />

<img width="850" height="547" alt="3665bebd46d41f9972be63dfa676a09e30e06d1e" src="https://github.com/user-attachments/assets/f629ea60-3098-4bbe-ae8f-6e347c5d2ddc" />

<img width="897" height="756" alt="169916ef0a522fed492352b36b1d0f3359444e9a" src="https://github.com/user-attachments/assets/94935de4-9992-43c6-8c7a-5ebfcd0bbadc" />

<img width="859" height="547" alt="a0d781a2e753fdd137f8af21f0ffb2d11b3e680e" src="https://github.com/user-attachments/assets/b3b0c15a-1b47-48b6-8fac-f9773bd06cd8" />

<img width="1189" height="490" alt="a457fd1e47817688c0f7678217569717a5bf7c3b" src="https://github.com/user-attachments/assets/5f500a67-b229-4671-ad2c-d596089423ec" />

<img width="1488" height="990" alt="a0819649b7996e2de1d11da360d098ad7a0a58c0" src="https://github.com/user-attachments/assets/3558d3ed-0d39-4097-b7d4-36c33222cc03" />


<img width="983" height="658" alt="f4469f52695ccc422cee71c1319417c8820a4a2b" src="https://github.com/user-attachments/assets/f5c2ac39-71b3-443a-ac0c-1dc0a916f7cb" />


<img width="1005" height="547" alt="cb6b729223e8a5fd836daf7a9ccce4283614b00c" src="https://github.com/user-attachments/assets/0a3a9db1-6db1-4926-9720-8bf4866a85ac" />













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

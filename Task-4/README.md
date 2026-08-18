# Week 4 Capstone — Sales Analytics

## 📌 Project Overview

This project completes the Week 4 Sales Analytics Capstone. It covers:

* Data cleaning and preprocessing
* Exploratory Data Analysis (EDA)
* Business KPI analysis
* Data visualization
* Sales regression modeling
* Business insights and recommendations
* Excel dashboard
* Power BI dashboard preparation
* Stakeholder-ready project report

---

## 📂 Project Structure

```text
week4_capstone/
│
├── data/
│   └── Sample-Superstore.csv
│
├── charts/
│   ├── monthly_sales.png
│   ├── category_sales.png
│   ├── region_profit.png
│   ├── discount_profit.png
│   └── actual_vs_predicted.png
│
├── notebook/
│   └── Week4_Capstone_Analysis.ipynb
│
├── report/
│   └── Week4_Capstone_Report.pdf
│
├── powerbi/
│   ├── Cleaned_Superstore.csv
│   ├── Category_Summary.csv
│   ├── Region_Summary.csv
│   ├── Monthly_Summary.csv
│   └── PowerBI_Dashboard_Setup.md
│
├── Week4_Capstone.xlsx
└── README.md
```

---

## 📊 Dataset

The project uses the **Sample Superstore** dataset containing sales transactions and business attributes such as:

* Order Date
* Ship Date
* Customer
* Segment
* Region
* Category
* Sub-Category
* Sales
* Quantity
* Discount
* Profit

The dataset contains **9,994 transaction records** used for analysis.

> **Dataset note:** The Week 4 assignment document references a Google Sheets dataset. That sheet was not directly accessible during project preparation, so the standard Sample Superstore dataset was used as a working substitute. If the instructor requires the exact Google Sheets dataset, replace `data/Sample-Superstore.csv` with the required export and rerun the notebook.

---

## 📈 Key Results

| Metric          |        Result |
| --------------- | ------------: |
| Total Sales     | $2,297,200.86 |
| Total Profit    |   $286,397.02 |
| Orders          |         5,009 |
| Customers       |           793 |
| Profit Margin   |        12.47% |
| Returned Orders |           296 |
| Return Rate     |         5.91% |
| Regression R²   |         0.260 |

---

## 🔎 Key Business Findings

### 1. Technology is the strongest sales category

Technology generated the highest sales among the three major categories.

### 2. West is the strongest region by profit

The West region produced the highest overall profit and should be considered an important market for continued growth.

### 3. Some sub-categories require profitability review

Lower-profit sub-categories, particularly **Tables**, should be reviewed for:

* Pricing
* Discount levels
* Product costs
* Shipping costs
* Customer demand

### 4. Discounts affect profitability

The analysis shows that higher discount levels are associated with weaker profitability. Discounting should therefore be controlled using appropriate pricing guardrails.

### 5. Seasonal sales patterns exist

Monthly sales analysis identifies periods of stronger demand that can be used for:

* Inventory planning
* Staffing
* Promotions
* Sales forecasting

---

## 🤖 Regression Model

A **Random Forest Regression** model was developed to predict sales.

### Features used

* Quantity
* Discount
* Year
* Month
* Quarter
* Ship Mode
* Segment
* Region
* Category
* Sub-Category

`Profit` was deliberately excluded from the model to avoid target leakage.

### Train/Test Strategy

A time-based split was used:

* **Training:** 2015–2017
* **Testing:** 2018

### Model Performance

| Metric |              Result |
| ------ | ------------------: |
| MAE    | See report/workbook |
| RMSE   | See report/workbook |
| R²     |               0.260 |

The model provides a useful baseline for sales forecasting. Additional variables such as marketing activity, customer history, inventory levels and product lifecycle information could improve future predictions.

---

## 📊 Dashboard

The Excel workbook contains:

* Total Sales KPI
* Total Profit KPI
* Number of Orders
* Number of Customers
* Profit Margin
* Returned Orders
* Return Rate
* Model R²
* Monthly Sales Trend
* Sales by Category
* Profit by Region
* Discount vs Profit

The workbook is available as:

`Week4_Capstone.xlsx`

---

## 📉 Power BI

The `powerbi` folder contains files needed to create the Power BI dashboard.

Recommended visuals:

1. **KPI Cards**

   * Total Sales
   * Total Profit
   * Profit Margin
   * Orders
   * Customers
   * Returned Orders

2. **Line Chart**

   * Month → Sales

3. **Bar Chart**

   * Category → Sales

4. **Bar Chart**

   * Region → Profit

5. **Scatter Plot**

   * Discount → Profit

6. **Slicers**

   * Year
   * Region
   * Category
   * Segment

### Useful DAX Measures

```DAX
Total Sales = SUM(Cleaned_Superstore[Sales])

Total Profit = SUM(Cleaned_Superstore[Profit])

Orders = DISTINCTCOUNT(Cleaned_Superstore[Order ID])

Customers = DISTINCTCOUNT(Cleaned_Superstore[Customer ID])

Profit Margin = DIVIDE([Total Profit], [Total Sales])

Returned Orders =
CALCULATE(
    DISTINCTCOUNT(Cleaned_Superstore[Order ID]),
    Cleaned_Superstore[Returned] = 1
)
```

A native `.pbix` file must be created and saved using Power BI Desktop.

---

## 📓 Jupyter Notebook

The complete analysis is available in:

```text
notebook/Week4_Capstone_Analysis.ipynb
```

The notebook includes:

1. Data loading
2. Data cleaning
3. Feature engineering
4. Exploratory Data Analysis
5. Visualizations
6. Regression modeling
7. Model evaluation
8. Business recommendations

---

## 📄 Final Report

The stakeholder-ready report is located at:

```text
report/Week4_Capstone_Report.pdf
```

It summarizes:

* Dataset preparation
* Business KPIs
* EDA findings
* Visualizations
* Regression results
* Business recommendations

---

## 💡 Recommendations

Based on the analysis:

1. Continue investing in the Technology category.
2. Review pricing and discount strategies for low-profit sub-categories.
3. Introduce discount guardrails to protect profit margins.
4. Use monthly sales trends for inventory and staffing planning.
5. Improve future forecasting by adding marketing, customer and inventory variables.
6. Monitor returns and investigate products or customer segments with unusually high return rates.

---

## 🚀 How to Run the Project

### 1. Clone the repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
cd week4_capstone
```

### 2. Install required Python packages

```bash
pip install pandas numpy matplotlib scikit-learn openpyxl reportlab jupyter
```

### 3. Open the notebook

```bash
jupyter notebook
```

Then open:

```text
notebook/Week4_Capstone_Analysis.ipynb
```

### 4. Run all notebook cells

The notebook performs the analysis and generates the model results and visualizations.

---

## 📤 GitHub Submission

Upload the **entire `week4_capstone` folder** to your GitHub repository.

Make sure the repository contains:

* `README.md`
* Dataset
* Jupyter notebook
* Excel dashboard
* PDF report
* Charts
* Power BI files

### Do not upload

* Passwords
* API keys
* Personal credentials
* Other confidential information

---

## 👤 Project

**Week 4 Sales Analytics Capstone**

Completed deliverables:

✅ Data Cleaning
✅ Exploratory Data Analysis
✅ Business KPIs
✅ Data Visualization
✅ Regression Model
✅ Model Evaluation
✅ Excel Dashboard
✅ Power BI Preparation
✅ Business Recommendations
✅ Final Report
✅ GitHub README

# Power BI Dashboard Setup

Import `Cleaned_Superstore.csv`.

DAX measures:
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

Visuals: KPI cards; Month vs Sales line chart; Category vs Sales bar chart; Region vs Profit bar chart; Discount vs Profit scatter; slicers for Year, Region, Category and Segment.

Python benchmark: MAE $189.91, RMSE $503.26, R² 0.260.
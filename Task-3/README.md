# Week 3 – Task 3: Python & Data Wrangling

## Assignment

The objective of this task is to clean a messy dataset using **Pandas**, handle missing values, filter rows, and create new columns.

## Project Overview

This project demonstrates a basic data-wrangling workflow using Python and Pandas.

The following operations are performed:

* Read a CSV dataset using Pandas
* Standardize column names
* Remove unnecessary whitespace from text values
* Normalize categorical values
* Convert columns to appropriate data types
* Handle missing values
* Remove duplicate records
* Create a new calculated column
* Filter rows based on conditions
* Save the cleaned dataset as a CSV file

## Data Cleaning Steps

### 1. Load the Dataset

The dataset is loaded using Pandas:

```python
df = pd.read_csv("messy_dataset.csv")
```

### 2. Standardize Column Names

Column names are converted to lowercase and spaces are replaced with underscores.

Example:

```text
Order ID → order_id
Customer Name → customer_name
Unit Price → unit_price
```

### 3. Clean Text Data

Extra spaces are removed from text fields and categorical values such as region and order status are standardized.

### 4. Handle Missing Values

Missing numeric values are replaced using the median of the respective column.

Missing text values are replaced with:

```text
Unknown
```

Missing order dates are filled using the median date.

### 5. Remove Duplicates

Duplicate records are identified and removed using Pandas `drop_duplicates()`.

### 6. Create a New Column

A new column called `total_sales` is created:

```python
df["total_sales"] = df["quantity"] * df["unit_price"]
```

This calculates the total sales value for each order.

### 7. Filter the Dataset

The final dataset keeps orders where:

```text
Status = Completed
Total Sales > 1000
```

### 8. Export the Cleaned Dataset

The final data is saved as:

```text
cleaned_dataset.csv
```

## Files in This Project

| File                      | Description                                       |
| ------------------------- | ------------------------------------------------- |
| `task3_data_wrangling.py` | Python program containing the complete solution   |
| `messy_dataset.csv`       | Input dataset containing intentionally messy data |
| `cleaned_dataset.csv`     | Cleaned and filtered output dataset               |
| `results.txt`             | Execution summary and results                     |
| `requirements.txt`        | Required Python package                           |
| `.gitignore`              | Files ignored by Git                              |

## Results

The original dataset contains:

* **15 rows**
* **8 columns**

After cleaning and applying the filtering conditions:

* **10 rows** remain
* **9 columns** remain
* **0 missing values** remain

The additional column is:

```text
total_sales
```

## How to Run

Install the required package:

```bash
pip install -r requirements.txt
```

Run the Python script:

```bash
python task3_data_wrangling.py
```

The program will generate:

```text
cleaned_dataset.csv
```

## Dataset Note

The Week 3 assignment material references an external dataset, but the actual dataset was not included in the uploaded Week 3 ZIP file.

Therefore, `messy_dataset.csv` in this project is an intentionally created practice dataset designed to demonstrate the required Pandas data-wrangling operations.

If the original internship dataset is provided separately, it can be substituted for `messy_dataset.csv`, with the column names and cleaning rules adjusted if necessary.

## Technologies Used

* Python
* Pandas
* CSV
* Git & GitHub

## Internship Repository

This project is part of my **Data Analytics Internship – Week 3** work.

It should be placed inside the `Task-3` folder of the existing internship repository.

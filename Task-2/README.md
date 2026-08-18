# Week 2 – Task 2: Handling Missing Values and Duplicates with Pandas

## Task

**Handle missing values and duplicates using Pandas.**

This project demonstrates a reusable Pandas workflow for:

1. Loading a CSV file.
2. Detecting missing values.
3. Treating blank strings as missing values.
4. Filling missing numeric values with the column median.
5. Filling missing categorical values with the column mode.
6. Detecting and removing exact duplicate rows.
7. Detecting and removing duplicate `order_id` values.
8. Saving the cleaned dataset.

## Files

* `task2_missing_duplicates.py` – main solution.
* `sample_dataset.csv` – sample dataset used for the task.
* `cleaned_sample_dataset.csv` – cleaned output dataset.
* `requirements.txt` – Python dependency.
* `results.txt` – result from running the solution.

## Run Locally

```bash
pip install -r requirements.txt
python task2_missing_duplicates.py
```

The script creates:

`cleaned_sample_dataset.csv`

## Results

The script checks the dataset for:

* Missing values
* Blank values
* Exact duplicate rows
* Duplicate `order_id` values

The cleaned dataset is saved as:

`cleaned_sample_dataset.csv`

## GitHub

This project is part of my **Data Analytics Internship – Week 2** work.

The files are organized under the `Task-2` folder in the internship repository.

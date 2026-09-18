# Audible Data Cleaning

A data cleaning and preprocessing project based on an Audible audiobook dataset.

## Overview

The project focuses on transforming a raw audiobook dataset into a cleaner and more consistent format using Python and Pandas.

The main cleaning steps include handling duplicates, standardizing text fields, converting dates and durations, cleaning ratings, and removing unwanted records.

## Data Cleaning

The following transformations were applied:

- Checked for duplicate records
- Cleaned `author` and `narrator` names
- Standardized the `language` column
- Cleaned price values
- Converted `releasedate` to datetime format
- Converted audiobook duration into minutes
- Removed records with names starting with non-Latin characters or numbers
- Extracted numerical values from the `stars` column
- Filled missing star ratings with the mean rating

The cleaned dataset was exported as `cleaned_data1.csv`.

## Technologies

- Python
- Pandas
- NumPy
- Scikit-learn
- Jupyter Notebook

## Project Structure

```text
Data Cleaning project/
│
├── Data_cleaning.ipynb
├── data/
│   ├── audible_uncleaned.csv
│   └── cleaned_data1.csv
└── README.md
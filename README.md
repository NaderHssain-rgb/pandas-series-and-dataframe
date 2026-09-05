# Pandas Series vs DataFrame

A beginner-friendly Python project for understanding the difference between **Pandas Series and DataFrame**.

## 📌 Project Overview

This project introduces two of the most important data structures in Pandas:

* Series
* DataFrame

It also demonstrates how to use custom indexes and organize data into a table.

## 🧠 Topics Covered

### 1. Importing Pandas

Pandas can be imported using:

```python
import pandas as pd
```

The `pd` alias is commonly used when working with Pandas.

---

## 2. Pandas Series

A Series is a one-dimensional labeled data structure.

Example:

```python
age = pd.Series(
    [11, 22, 33],
    index=["A", "B", "C"]
)
```

The data can be represented as:

```text
A → 11
B → 22
C → 33
```

Each value has a corresponding index label.

---

## 3. Custom Index

Pandas allows us to define our own index labels.

Example:

```python
age = pd.Series(
    [11, 22, 33],
    index=["A", "B", "C"]
)
```

Instead of using the default index:

```text
0
1
2
```

we use:

```text
A
B
C
```

This allows us to access data using labels.

For example:

```python
age["B"]
```

returns:

```text
22
```

---

## 4. Pandas DataFrame

A DataFrame is a two-dimensional labeled data structure.

It can be thought of as a table similar to a spreadsheet.

Example:

```python
student_data = pd.DataFrame(
    {
        "Name": ["Nder", "Ahmed", "Abdallah"],
        "Age": [24, 13, 11],
        "IsGraduated": [True, False, False]
    },
    index=["A", "AA", "AAA"]
)
```

The resulting table looks like:

```text
        Name       Age    IsGraduated
A       Nder        24        True
AA      Ahmed       13        False
AAA     Abdallah    11        False
```

---

## 5. Understanding DataFrame Columns

Each key in the dictionary becomes a column.

For example:

```python
"Name": ["Nder", "Ahmed", "Abdallah"]
```

creates the `Name` column.

```python
"Age": [24, 13, 11]
```

creates the `Age` column.

```python
"IsGraduated": [True, False, False]
```

creates the `IsGraduated` column.

---

## 6. Series vs DataFrame

The main difference can be summarized as:

| Series                        | DataFrame                |
| ----------------------------- | ------------------------ |
| One-dimensional               | Two-dimensional          |
| Usually represents one column | Represents a table       |
| Has an index                  | Has an index and columns |
| `pd.Series()`                 | `pd.DataFrame()`         |

A simple way to remember:

```text
Series    → Column
DataFrame → Table
```

---

## 🛠️ Technologies Used

* Python 3
* Pandas

## 📦 Installation

Install Pandas using:

```bash
pip install pandas
```

Or install the project requirements:

```bash
pip install -r requirements.txt
```

## ▶️ How to Run

Run the Python file:

```bash
python pandas_series_and_dataframe.py
```

## 📁 Project Structure

```text
pandas-series-and-dataframe/
│
├── pandas_series_and_dataframe.py
├── requirements.txt
└── README.md
```

## 🎯 Project Goal

The goal of this project is to understand the basic data structures used in Pandas and learn the difference between a Series and a DataFrame.

## 📚 What I Learned

Through this project, I practiced:

* Importing Pandas
* Creating a Series
* Creating a DataFrame
* Using custom indexes
* Understanding Series
* Understanding DataFrames
* Creating DataFrame columns
* Working with labeled data
* Understanding the difference between Series and DataFrame

## 🚀 Future Improvements

Future versions may include:

* Selecting columns
* Selecting rows
* `.loc`
* `.iloc`
* Adding columns
* Removing columns
* Filtering data
* Reading CSV files
* Exploring DataFrames with `head()` and `info()`
* Data cleaning

## 👨‍💻 Author

**Nader**

This project is part of my Python, NumPy, and Pandas learning journey.

---

⭐ If you find this project useful, feel free to star the repository!

# Employee data cleaning with NumPy

Saad, pehle data dekho, phir problem identify karo, phir cleaning ka decision lo.

## Dataset

[employees_dirty.csv](employees_dirty.csv) contains **60 rows and 10 columns**, including two exact duplicate rows. All records are fictional. The CSV structure is valid; the values intentionally contain mistakes.

Columns: employee_id, name, department, age, salary_pkr, experience_years, hours_per_week, performance_score, attendance_percent, city.

Salary means monthly salary in PKR. You will find blanks, NaN/nan, N/A, null, invalid numeric text, infinity, unrealistic values, inconsistent capitalization/spaces, missing identifiers and duplicate identifiers.

## Start here

Install NumPy if needed:

```powershell
python -m pip install numpy
```

Save your practice script as `numpy/employee_practice.py`. This loader works regardless of the terminal's current directory:

```python
from pathlib import Path
import numpy as np

csv_path = Path(__file__).with_name("employees_dirty.csv")

data = np.genfromtxt(
    csv_path,
    delimiter=",",
    skip_header=1,
    dtype=str,
    encoding="utf-8",
)

print("Shape:", data.shape)  # (60, 10)
print(data[:5])
print("Age values:", data[:, 3])
```

Run from the repository root:

```powershell
python numpy/employee_practice.py
```

`dtype=str` keeps the raw entries available for inspection. At this stage, "NaN" is text, not a floating-point NaN. Directly applying `np.isnan` to strings will fail.

For a separate numeric view of the six measurement columns:

```python
numbers = np.genfromtxt(
    csv_path,
    delimiter=",",
    skip_header=1,
    usecols=(3, 4, 5, 6, 7, 8),
    dtype=float,
    filling_values=np.nan,
    loose=True,
    encoding="utf-8",
)

print(numbers.shape)  # (60, 6)
# Numeric column 0 = age, 1 = salary, ... 5 = attendance.
```

Unconvertible text becomes NaN in this numeric view, so keep the raw string array to distinguish missing entries from typing errors. Infinity remains infinity.

## Practice rules

These are invented rules for this exercise, not real employment requirements or salary benchmarks. Bounds are inclusive.

| Field | Valid value for this exercise |
| --- | --- |
| employee_id | Nonempty positive integer; unique per employee |
| name | Nonempty after trimming |
| department | IT, HR, Finance, Sales, Operations |
| age | Whole number from 18 to 65 |
| salary_pkr | 30000 to 500000 per month |
| experience_years | Whole number from 0 to 45, also no more than age minus 18 |
| hours_per_week | 1 to 60 |
| performance_score | 1 to 5 |
| attendance_percent | 0 to 100 |
| city | Karachi, Lahore, Islamabad, Multan, Hyderabad |

All numeric measurements must be finite. Normalize case and spaces before checking categories. Flag uncertain spellings for review. Do not invent missing names or IDs.

## Tasks: easy to harder

1. Print the shape, first five rows and each numeric column separately.
2. Count blank and missing-marker entries in the raw data after stripping spaces and normalizing case.
3. Count NaNs per numeric column. Which raw values became NaN during conversion?
4. Find positive and negative infinity. Explain why `np.isnan` alone misses them.
5. Build boolean masks for out-of-range ages, salaries, scores and attendance.
6. Check experience against both its own range and the employee's age.
7. Normalize department/city spaces and capitalization. List unknown categories.
8. Find exact duplicate rows, then separately find repeated nonempty employee IDs. A repeated ID with different details needs review.
9. Decide which rows to remove or flag and which numeric cells to replace. Record the reason for each choice.
10. For optional median imputation, use only finite, in-range values after duplicate handling. Do not use bad values when computing the median. Flag cross-field inconsistencies for review.
11. Compare mean, median, minimum and maximum salary before and after cleaning. Explain any NaN/infinity result before cleaning.
12. Save your result to `employees_cleaned.csv` and write a small summary: rows before/after, missing counts and unresolved issues.

Hints: `np.isnan`, `np.isinf`, `np.isfinite`, boolean masks, `np.unique(..., return_counts=True)`, `np.nanmedian`, `np.nanmean`, `np.char.strip`, `np.char.lower`, `np.savetxt`.

`np.nanmean` ignores NaN but does not ignore infinity or unrealistic finite values. Missing salary does not mean zero salary.

**First session:** complete tasks 1–3 yourself. Print intermediate arrays so you can see what each line does. Solutions are deliberately left for your practice.

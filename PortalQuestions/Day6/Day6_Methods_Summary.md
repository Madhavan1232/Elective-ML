# Day 6 - Methods & Functions

## Core Methods

| Method | Purpose |
|--------|---------|
| `pymysql.connect()` | Connect to MySQL database |
| `pd.read_sql()` | Read SQL query into DataFrame |
| `pd.to_datetime()` | Convert to datetime format |
| `.astype(float)` | Convert to float |
| `.fillna(method='ffill')` | Forward fill missing values |
| `.rename()` | Rename columns |
| `.replace()` | Replace values in column |
| `pd.pivot_table()` | Create summary pivot table |
| `.groupby()` | Group and aggregate data |
| `.sort_values()` | Sort DataFrame |
| `.value_counts()` | Count unique values |
| `.describe()` | Statistical summary |

## Key Operations Used

1. **Filtering** - `df[df['col'] == 'value']`
2. **Aggregation** - `.sum()`, `.mean()`, `.count()`
3. **Pivoting** - Summarize by multiple dimensions
4. **Grouping** - Group by city, payment method, month
5. **Sorting** - Sort by revenue, rating, amount

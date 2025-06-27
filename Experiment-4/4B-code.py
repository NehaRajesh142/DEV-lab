import pandas as pd
df = pd.read_csv('employee_department_hours.csv')
summary = df.groupby('department').agg(
    total_hours=('hours', 'sum'),
    average_hours=('hours', 'mean'),
    employee_count=('employee', 'count')
).reset_index()
pivot = summary.set_index('department')
max_avg = summary.loc[summary['average_hours'].idxmax()]
print("Available Columns:", list(df.columns))
print("\n◇ Summary Report:")
print(summary)
print("\n" + "="*50)
print("\n Pivot Table Summary:\n")
print(pivot)
print("\n" + "="*50)
print(f"\n Department with Highest Average Working Hours: {max_avg['department']} ({max_avg['average_hours']:.2f} hours)")

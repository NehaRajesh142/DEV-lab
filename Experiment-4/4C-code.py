import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
df = pd.read_csv('employee_department_hours.csv')
summary = df.groupby('department').agg(
    total_hours=('hours', 'sum'),
    average_hours=('hours', 'mean'),
    employee_count=('employee', 'count')
).reset_index()
sns.set(style='whitegrid')
plt.figure(figsize=(8, 5))
sns.barplot(data=summary, x='department', y='total_hours', palette='viridis')
plt.title('Total Work Hours by Department')
plt.ylabel('Total Hours')
plt.xlabel('Department')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
plt.figure(figsize=(8, 5))
sns.barplot(data=summary, x='department', y='average_hours', palette='coolwarm')
plt.title('Average Work Hours by Department')
plt.ylabel('Average Hours')
plt.xlabel('Department')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
max_avg = summary.loc[summary['average_hours'].idxmax()]
print(f"\n Department with Highest Average Working Hours: {max_avg['department']} ({max_avg['average_hours']:.2f} hours)")

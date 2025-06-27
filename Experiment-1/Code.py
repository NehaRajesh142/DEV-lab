import pandas as pd
import matplotlib.pyplot as plt
data = {
    'Category': ['A', 'B', 'A', 'B', 'C'],
    'Value': [10, 15, 20, 25, 30]
}
df = pd.DataFrame(data)
print("Data:")
print(df)
avg_values = df.groupby('Category')['Value'].mean()
avg_values.plot(kind='bar', color='green')
plt.title('Average Value per Category')
plt.xlabel('Category')
plt.ylabel('Average Value')
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()

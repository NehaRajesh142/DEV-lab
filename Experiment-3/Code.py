import numpy as np
arr1 = np.array([1, 2, 3, 4, 5])
arr2 = np.array([[1, 2, 3], [4, 5, 6]])
print("Original Array:", arr1)
print("Array + 5:", arr1 + 5)
print("Sliced Array:", arr1[1:4])
print("Reshaped 2D Array:\n", arr2.reshape(3, 2))
import pandas as pd
data = {
    'Name': ['Pavithra', 'Neha', 'Pooja'],
    'Age': [20, 19, 25],
    'Score': [85, 90, 88]
}
df = pd.DataFrame(data)
print("\nDataFrame:")
print(df)
print("\nDataFrame Info:")
print(df.info())
print("\nStatistics:")
print(df.describe())
import matplotlib.pyplot as plt
%matplotlib inline
plt.style.use('ggplot')
plt.figure(figsize=(8, 5))
plt.plot(df['Name'], df['Score'], marker='D', linestyle='-', color='teal')
plt.title('Scores of Students')
plt.xlabel('Name')
plt.ylabel('Score')
plt.grid(True)
plt.tight_layout()
plt.show()
plt.figure(figsize=(8, 5))
bars = plt.barh(df['Name'], df['Age'], color='skyblue')
plt.title('Ages of Students')
plt.xlabel('Age')
for bar in bars:
    plt.text(bar.get_width() + 0.5, bar.get_y() + bar.get_height()/2, f'{bar.get_width()}', va='center')
plt.tight_layout()
plt.show()
colors = ['#ff9999','#66b3ff','#99ff99']
explode = [0.05, 0.05, 0.05]
plt.figure(figsize=(6, 6))
plt.pie(df['Score'], labels=df['Name'], autopct='%1.1f%%', startangle=140, explode=explode, shadow=True, colors=colors)
plt.title('Score Distribution')
plt.tight_layout()
plt.show()

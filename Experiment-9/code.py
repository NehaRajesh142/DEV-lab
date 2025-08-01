import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
url = "https://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-red.csv"
df = pd.read_csv(url, sep=';')
print("Dataset shape:", df.shape)
print("\nColumn names:", df.columns.tolist())
print("\nInfo:")
print(df.info())
print("\nSummary statistics:")
print(df.describe())
print("\nMissing values:\n", df.isnull().sum())
plt.figure(figsize=(8, 5))
sns.countplot(x='quality', data=df, palette='magma')
plt.title("Distribution of Wine Quality Scores")
plt.xlabel("Wine Quality")
plt.ylabel("Count")
plt.grid(True)
plt.show()
plt.figure(figsize=(12, 8))
corr_matrix = df.corr()
sns.heatmap(corr_matrix, annot=True, fmt=".2f", cmap='coolwarm')
plt.title("Feature Correlation Matrix")
plt.show()
features = ['volatile acidity', 'citric acid', 'residual sugar', 'alcohol']
plt.figure(figsize=(16, 10))
for i, feature in enumerate(features):
    plt.subplot(2, 2, i+1)
    sns.boxplot(x='quality', y=feature, data=df, palette='Set2')
    plt.title(f'{feature} vs Wine Quality')
plt.tight_layout()
plt.show()
sns.pairplot(df[['quality', 'alcohol', 'sulphates', 'citric acid', 'density']], hue='quality', palette='husl')
plt.show()

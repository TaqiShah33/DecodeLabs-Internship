import numpy as np
import pandas as pd
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import confusion_matrix, classification_report, f1_score

# Load data
iris = load_iris()
X = iris.data  # Features: sepal/petal dimensions
y = iris.target  # Labels: 0, 1, 2

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

X_train, X_test, y_train, y_test = train_test_split(
    X_scaled, y, test_size=0.20, random_state=42, stratify=y
)

model = KNeighborsClassifier(n_neighbors=5)

# FIT: Let the machine derive the classification boundary logic
model.fit(X_train, y_train)

# PREDICT: Apply the trained logic to the unseen test matrix
predictions = model.predict(X_test)

# Diagnostics
conf_matrix = confusion_matrix(y_test, predictions)
macro_f1 = f1_score(y_test, predictions, average='macro')

print("--- Confusion Matrix ---")
print(conf_matrix)
print(f"\nMacro F1-Score: {macro_f1:.4f}")
print("\n--- Detailed Classification Report ---")
# CORRECT
print(classification_report(y_test, predictions, target_names=iris.target_names))
import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor

# Load dataset
df = pd.read_csv("dataset/house_price.csv")

# Features
X = df.drop("Price_INR", axis=1)

# Target
y = df["Price_INR"]

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# Model
model = RandomForestRegressor(
    n_estimators=300,
    random_state=42
)

# Train
model.fit(X_train, y_train)

# Save model
joblib.dump(model, "model.pkl")

print("Model Saved Successfully")
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import joblib

# Load features
df = pd.read_csv("training/features.csv")

X = df.drop("emotion", axis=1)
y = df["emotion"]

# Split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Train model
model = RandomForestClassifier(
    n_estimators=200,
    random_state=42
)

model.fit(X_train, y_train)

# Evaluate
y_pred = model.predict(X_test)
acc = accuracy_score(y_test, y_pred)

print(f"🎯 Model Accuracy: {acc * 100:.2f}%")

# Save model
joblib.dump(model, "training/emotion_model.pkl")
print("✅ emotion_model.pkl saved")

import os
import joblib
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
)


DATA_PATH = "data/raw/transactions.csv"
MODEL_DIR = "artifacts/models"
MODEL_PATH = os.path.join(MODEL_DIR, "fraud_model.pkl")


def load_data():
    df = pd.read_csv(DATA_PATH)

    X = df.drop("fraud", axis=1)
    y = df["fraud"]

    return X, y


def train_model():
    X, y = load_data()

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.2,
        random_state=42,
        stratify=y,
    )

    model = RandomForestClassifier(
        n_estimators=100,
        random_state=42,
        n_jobs=-1,
    )

    model.fit(X_train, y_train)

    predictions = model.predict(X_test)

    metrics = {
        "accuracy": accuracy_score(y_test, predictions),
        "precision": precision_score(y_test, predictions),
        "recall": recall_score(y_test, predictions),
        "f1": f1_score(y_test, predictions),
    }

    os.makedirs(MODEL_DIR, exist_ok=True)

    joblib.dump(model, MODEL_PATH)

    print("\nModel training completed.")
    print(f"Model saved to: {MODEL_PATH}")

    print("\nModel metrics:")
    for name, value in metrics.items():
        print(f"{name}: {value:.4f}")

    return model, metrics


if __name__ == "__main__":
    train_model()
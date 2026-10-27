import numpy as np
import pandas as pd


def generate_dataset(n_samples=5000, random_state=42):
    rng = np.random.default_rng(random_state)

    age = rng.integers(18, 70, n_samples)
    income = rng.normal(50000, 15000, n_samples)
    transaction_amount = rng.exponential(100, n_samples)
    transaction_count = rng.poisson(3, n_samples)
    account_age = rng.integers(1, 120, n_samples)

    risk_score = (
        0.02 * transaction_amount
        + 0.3 * transaction_count
        - 0.01 * account_age
        + 0.00001 * income
        - 0.01 * age
    )

    probability = 1 / (1 + np.exp(-risk_score + 2))

    fraud = rng.binomial(1, probability)

    data = pd.DataFrame({
        "age": age,
        "income": income,
        "transaction_amount": transaction_amount,
        "transaction_count": transaction_count,
        "account_age": account_age,
        "fraud": fraud,
    })

    return data


if __name__ == "__main__":
    df = generate_dataset()

    output_path = "data/raw/transactions.csv"

    import os
    os.makedirs("data/raw", exist_ok=True)

    df.to_csv(output_path, index=False)

    print(f"Dataset generated: {output_path}")
    print(f"Rows: {len(df)}")
    print(df.head())
import pandas as pd
import numpy as np

np.random.seed(42)
n = 100  # number of respondents

# --- Helper to generate correlated Likert-style items ---
def make_correlated_items(base):
    return np.clip(base + np.random.randint(-1, 2, n), 1, 5)

# --- Correlated base values for multi-item scales ---
support_base = np.random.randint(1, 6, n)
micro_base = np.random.randint(1, 6, n)
validation_base = np.random.randint(1, 6, n)
psych_safety_base = np.random.randint(1, 6, n)

# --- Build dataset ---
data = {
    # Demographics
    'tenure_years': np.random.choice([0, 1, 2, 3, 5, 10, 15, 20], size=n, p=[0.1, 0.2, 0.2, 0.2, 0.15, 0.1, 0.03, 0.02]),
    'age_group': np.random.choice(['18–25', '26–35', '36–45', '46–55', '56+'], size=n, p=[0.2, 0.35, 0.25, 0.15, 0.05]),
    'department': np.random.choice(['Engineering', 'Sales', 'HR', 'Marketing', 'Operations'], size=n),
    'role_level': np.random.choice(['Entry', 'Mid', 'Manager', 'Director', 'Executive'], size=n, p=[0.3, 0.3, 0.25, 0.1, 0.05]),

    # Manager Support (correlated)
    'support_1': make_correlated_items(support_base),
    'support_2': make_correlated_items(support_base),
    'support_3': make_correlated_items(support_base),

    # Micromanagement (correlated)
    'micro_1': make_correlated_items(micro_base),
    'micro_2': make_correlated_items(micro_base),
    'micro_3': make_correlated_items(micro_base),

    # Validation/Recognition (correlated)
    'validation_1': make_correlated_items(validation_base),
    'validation_2': make_correlated_items(validation_base),
    'validation_3': make_correlated_items(validation_base),

    # Psychological Safety (correlated)
    'psych_safety_1': make_correlated_items(psych_safety_base),
    'psych_safety_2': make_correlated_items(psych_safety_base),

    # Single-item workplace factors
    'inclusion': np.random.randint(1, 6, n),
    'recognition': np.random.randint(1, 6, n),
    'work_life_balance': np.random.randint(1, 6, n),
    'resources_tools': np.random.randint(1, 6, n),

    # Job attitudes & self-evaluations
    'satisfaction': np.random.randint(1, 6, n),
    'engagement': np.random.randint(1, 6, n),
    'burnout': np.random.randint(1, 6, n),
    'intent_to_stay': np.random.randint(1, 6, n),
    'commitment': np.random.randint(1, 6, n),
    'self_rated_performance': np.random.randint(1, 6, n),
    'competence_confidence': np.random.randint(1, 6, n),

    # Simulated performance score
    'performance_score': np.random.randint(60, 101, n)
}

# --- Create and save the DataFrame ---
df = pd.DataFrame(data)
df.to_csv("mock_survey_data.csv", index=False)
print("✅ CSV with realistic mock survey data created!")

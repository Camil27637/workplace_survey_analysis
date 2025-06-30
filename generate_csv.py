import pandas as pd
import numpy as np

np.random.seed(42)

n = 100  # number of respondents

data = {
    'support_1': np.random.randint(1, 6, n),
    'support_2': np.random.randint(1, 6, n),
    'support_3': np.random.randint(1, 6, n),
    'micro_1': np.random.randint(1, 6, n),
    'micro_2': np.random.randint(1, 6, n),
    'micro_3': np.random.randint(1, 6, n),
    'validation_1': np.random.randint(1, 6, n),
    'validation_2': np.random.randint(1, 6, n),
    'validation_3': np.random.randint(1, 6, n),
    'satisfaction': np.random.randint(1, 6, n),
    'performance': np.random.randint(60, 101, n),  # 0–100 score
}

df = pd.DataFrame(data)
df.to_csv("mock_survey_data.csv", index=False)
print("CSV file created!")

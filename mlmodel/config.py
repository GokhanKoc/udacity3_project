TEST_SIZE = 0.2
TARGET = "salary"
MODEL_PATH = "model/classifier.pkl"
DATA_PATH = "data/census_clean.csv"
METRICS_PATH = "model/metrics_by_slice.csv"

all_columns = [
    "age", "workclass", "fnlgt", "education", "education_num",
    "marital_status", "occupation", "relationship", "race", "sex",
    "capital_gain", "capital_loss", "hours_per_week", "native_country",
]

cat_features = [
    "workclass",
    "education",
    "marital_status",
    "occupation",
    "relationship",
    "race",
    "sex",
    "native_country",
]
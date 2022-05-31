import os
from pathlib import Path

TARGET = "salary"
TEST_SIZE = 0.2

__MAIN_DIR = Path(__file__).parent.parent.absolute()
__DATA_FILE = 'census_clean.csv'
__MODEL_FILE = 'classifier.pkl'
__METRICS_FILE = "slice_output.txt"

DATA_PATH = os.path.join(__MAIN_DIR, 'data', __DATA_FILE)
MODEL_PATH = os.path.join(__MAIN_DIR, 'model', __MODEL_FILE)
METRICS_PATH = os.path.join(__MAIN_DIR, 'model', __METRICS_FILE)

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
# Script to train machine learning model.
import pandas as pd
import pickle
import os
from sklearn.model_selection import train_test_split
from ml.data import process_data
from ml.model import train_model, inference, compute_model_metrics


# Add the necessary imports for the starter code.
import config

# Add code to load in the data.
file_dir = os.path.dirname(__file__)
data = pd.read_csv(os.path.join(file_dir, '../data/census_clean.csv'))


# Add code to load in the data.

# Optional enhancement, use K-fold cross validation instead of a train-test split.
train, test = train_test_split(data, test_size=config.TEST_SIZE)


X_train, y_train, encoder, lb = process_data(
    train, categorical_features=config.cat_features, label=config.TARGET, training=True
)

# Proces the test data with the process_data function.

# Train and save a model.
rf_model = train_model(X_train, y_train)

model_path = os.path.join(file_dir, '../model/rf_model.pkl')
pickle.dump(rf_model, open(model_path, 'wb'))

encoder_path = os.path.join(file_dir, '../model/encoder.pkl')
pickle.dump(encoder, open(encoder_path, 'wb'))

lb_path = os.path.join(file_dir, '../model/lb.pkl')
pickle.dump(lb, open(lb_path, 'wb'))

# Evaluation
X_test, y_test, encoder, lb = process_data(
    test,
    categorical_features=cat_features,
    label="salary",
    training=False,
    encoder=encoder,
    lb=lb
)

preds = inference(rf_model, X_test)

print('precision: {}, recall: {}, fbeta: {}'.format(
    *compute_model_metrics(y_test, preds)
))
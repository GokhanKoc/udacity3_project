# Model Card

For additional information see the Model Card paper: https://arxiv.org/pdf/1810.03993.pdf

## Model Details

- Try to predict whether employer's  income exceeds $50K/year.
- **Random Forest** is used.
- A binary classification approach was taken, whereby a sample showing a probability of 1.0 being positive and 0.0 being negative case.

## Intended Use

- What features effects the income of a person.
- Just for Test Project use

## Training Data

- The data utilized for training this model came from the Census, and consists of salary information - More information here: https://archive.ics.uci.edu/ml/datasets/census+income

## Evaluation Data

- Split the train data using sklearn `train_test_split` 
- 20% split of the samples not used during training.

## Metrics

-  **Precision**, **Recall** and **F1 score** are used.

All results shown are calculated for class 1 (>50K) using sklearn metrics
|				|Train   |
|---------------|--------|
|Precision		|0.720183|
|Recall         |0.61851 |
|F1          	|0.665489|

- Precision: Ratio between correct predictions and the total predictions
- Recall: Ratio of the correct predictions and the total number of correct items in the set
- F1: Harmoinc mean between Precision and Recall to show the balance between them.

## Ethical Considerations

- There may be a bias may be embedded within the data, particularly around race, sex and ethnicity. Should be checked before using in production

## Caveats and Recommendations

- The data was collected in 1996 which is definetely old for nowadays conditions
- With respect to ehe ethical considretions should be investigated carefully



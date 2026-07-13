# Model Card

For additional information see the Model Card paper: https://arxiv.org/pdf/1810.03993.pdf

## Model Details
This is a classification model using the random forest algorithm on the Census Income data. This model can make financial predictions for individuals from 1994.
## Intended Use
Intended for use for those needed practice with ML pipelines.
## Training Data
The split for the training data was .80 or 80%.
## Evaluation Data
The split for testing data was .20 or 20%.
## Metrics
Evaluation metrics for the model were precision, recall, and F1 score.
The model scored 0.7419 on precision, which can be an acceptable score.
The model scored 0.6384 on recall, which is a bit low.
The model scored 0.6863 on the F1 score.
## Ethical Considerations
This model trains and tests on information collected on real people through a survey from 1994. 
## Caveats and Recommendations
As this information is over 30 years old, it may be inaccurate to todays' reality. It would give a fuller picture to include features to describe a persons' medical and caretaker status.
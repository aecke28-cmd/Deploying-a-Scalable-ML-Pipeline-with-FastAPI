import pytest
from unittest.mock import patch
from unittest.mock import MagicMock
import pandas as pd

# TODO: add necessary import
@patch('train_model.data')
# TODO: implement the first test. Change the function name and input as needed
def test_nan(data):
    """
    # checks that null values do not exceed 30% of the dataset
    """
    # Your code here
    assert data.isna().mean() * (100).__lt__(30)
    pass


@patch('train_model.p')
@patch('train_model.r')
@patch('train_model.fb')
# TODO: implement the second test. Change the function name and input as needed
def test_metrics(p, r, fb):
    """
    # ascertains that the precision, recall and f1 score are all between 0 and 1
    """
    # Your code here
    min = 0
    max = 1
    assert min.__lt__(p) and p.__lt__(max)
    assert min.__lt__(r) and r.__lt__(max)
    assert min.__lt__(fb) and fb.__lt__(max)
    pass


# TODO: implement the third test. Change the function name and input as needed
def test_age():
    """
    # makes sure that the age value in the dataset is a possible value
    """
    # Your code here
    data = pd.read_csv('data/census.csv')
    assert data['age'].min() >= 0
    assert data['age'].max() <= 115
    pass


# test_evaluation.py

import pytest
from easy_transformers_finetune import evaluate_model

def test_evaluate_model():
    # Test case 1: Check evaluation with a basic set of predictions and labels
    predictions = [0, 1, 0, 1]
    labels = [0, 1, 0, 0]
    
    accuracy, f1_score = evaluate_model(predictions, labels)
    
    # Test that the accuracy and F1 score are numeric
    assert isinstance(accuracy, float)
    assert isinstance(f1_score, float)

    # Test case 2: Check for perfect accuracy and F1 score
    predictions = [1, 1, 1, 1]
    labels = [1, 1, 1, 1]
    
    accuracy, f1_score = evaluate_model(predictions, labels)
    
    # Accuracy should be 1.0 and F1 score should be 1.0 for perfect predictions
    assert accuracy == 1.0
    assert f1_score == 1.0

    # Test case 3: Check with completely incorrect predictions
    predictions = [0, 0, 0, 0]
    labels = [1, 1, 1, 1]
    
    accuracy, f1_score = evaluate_model(predictions, labels)
    
    # Accuracy should be 0.0 and F1 score should be 0.0 for completely incorrect predictions
    assert accuracy == 0.0
    assert f1_score == 0.0

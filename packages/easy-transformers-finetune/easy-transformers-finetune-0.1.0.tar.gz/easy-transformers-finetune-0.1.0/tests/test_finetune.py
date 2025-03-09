# test_finetune.py
import pytest
from easy_transformers_finetune.finetune import fine_tune_model

def test_finetune_model():
    model = fine_tune_model('bert-base-uncased', 'text-classification')
    assert model is not None

# easy_transformers_finetune/utils.py

from transformers import AutoTokenizer
from datasets import load_dataset
import torch

def load_data(dataset_name='imdb', tokenizer=None, batch_size=16):
    """
    Load and preprocess dataset using the provided tokenizer.
    """
    # Load dataset
    dataset = load_dataset(dataset_name)
    
    # Tokenize the data
    def tokenize_function(examples):
        return tokenizer(examples['text'], padding="max_length", truncation=True)

    tokenized_datasets = dataset.map(tokenize_function, batched=True)
    
    # Return tokenized train and validation sets
    return tokenized_datasets['train'], tokenized_datasets['test']


def save_model(model, model_name='fine_tuned_model'):
    """
    Save the model to the specified path.
    """
    model.save_pretrained(model_name)
    print(f"Model saved to {model_name}")


def load_model(model_name='fine_tuned_model'):
    """
    Load a pre-trained model from the specified path.
    """
    from transformers import AutoModelForSequenceClassification
    model = AutoModelForSequenceClassification.from_pretrained(model_name)
    return model


def setup_tokenizer(model_name='bert-base-uncased'):
    """
    Load tokenizer for the specified model name.
    """
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    return tokenizer


def collate_fn(batch):
    """
    Custom collate function for handling batches of data.
    """
    # Default padding using tokenizer
    input_ids = torch.stack([x['input_ids'] for x in batch])
    attention_mask = torch.stack([x['attention_mask'] for x in batch])
    labels = torch.tensor([x['label'] for x in batch])
    
    return {'input_ids': input_ids, 'attention_mask': attention_mask, 'labels': labels}

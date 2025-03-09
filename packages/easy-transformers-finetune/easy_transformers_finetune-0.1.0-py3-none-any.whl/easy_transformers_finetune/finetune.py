from transformers import Trainer, TrainingArguments, AutoModelForSequenceClassification, AutoTokenizer
from datasets import load_dataset

def fine_tune_model(model_name, task, dataset_name='imdb'):
    # Load pretrained model and tokenizer
    model = AutoModelForSequenceClassification.from_pretrained(model_name)
    tokenizer = AutoTokenizer.from_pretrained(model_name)

    # Load dataset
    dataset = load_dataset(dataset_name)

    # Preprocess dataset (tokenization)
    def tokenize_function(examples):
        return tokenizer(examples['text'], padding="max_length", truncation=True)

    tokenized_datasets = dataset.map(tokenize_function, batched=True)

    # Define training arguments
    training_args = TrainingArguments(
        output_dir='./results',        
        num_train_epochs=3,              
        per_device_train_batch_size=16,  
        per_device_eval_batch_size=64,   
        warmup_steps=500,                
        weight_decay=0.01,               
        logging_dir='./logs',            
        logging_steps=10,
    )

    # Create Trainer instance
    trainer = Trainer(
        model=model,                         
        args=training_args,                  
        train_dataset=tokenized_datasets['train'],         
        eval_dataset=tokenized_datasets['test']            
    )

    # Fine-tune the model
    trainer.train()
    return model

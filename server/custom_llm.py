import pandas as pd
import numpy as np
import re
import os

from transformers import TextDataset, DataCollatorForLanguageModeling
from transformers import GPT2Tokenizer, GPT2LMHeadModel
from transformers import Trainer, TrainingArguments
from transformers import PreTrainedTokenizerFast, GPT2LMHeadModel, GPT2TokenizerFast
from transformers import BertTokenizerFast

def load_dataset(file_path, tokenizer, block_size = 128):
    dataset = TextDataset(
        tokenizer = tokenizer,
        file_path = file_path,
        block_size = block_size,
    )
    return dataset

def load_data_collator(tokenizer, mlm = False):
    data_collator = DataCollatorForLanguageModeling(
        tokenizer=tokenizer, 
        mlm=mlm,
    )
    return data_collator

def train(train_file_path,model_name,
          output_dir,
          overwrite_output_dir,
          per_device_train_batch_size,
          num_train_epochs,
          save_steps):
    tokenizer = GPT2Tokenizer.from_pretrained(model_name)
    train_dataset = load_dataset(train_file_path, tokenizer)
    data_collator = load_data_collator(tokenizer)

    tokenizer.save_pretrained(output_dir)
        
    model = GPT2LMHeadModel.from_pretrained(model_name)

    model.save_pretrained(output_dir)

    training_args = TrainingArguments(
            output_dir=output_dir,
            overwrite_output_dir=overwrite_output_dir,
            per_device_train_batch_size=per_device_train_batch_size,
            num_train_epochs=num_train_epochs,
        )

    trainer = Trainer(
            model=model,
            args=training_args,
            data_collator=data_collator,
            train_dataset=train_dataset,
    )
        
    trainer.train()
    trainer.save_model()

# inference
def load_model(model_path):
    model = GPT2LMHeadModel.from_pretrained(model_path)
    return model


def load_tokenizer(tokenizer_path):
    tokenizer = GPT2Tokenizer.from_pretrained(tokenizer_path)
    return tokenizer

def generate_text(model_path, sequence, max_length):
    model = load_model(model_path)
    tokenizer = load_tokenizer(model_path)
    ids = tokenizer.encode(f'{sequence}', return_tensors='pt')
    final_outputs = model.generate(
        ids,
        do_sample=True,
        max_length=max_length,
        pad_token_id=model.config.eos_token_id,
        top_k=50,
        top_p=0.95,
    )
    generated_text = set((tokenizer.decode(final_outputs[0], skip_special_tokens=True).split("\n")))
    clean_generated_text(generated_text)

def clean_generated_text(generated_text):
    for sent in generated_text:
        if not sent.endswith('.'):
            sent += "."
        if len(sent) > 50:
            print(sent)

def inference(train_filename):
    sequence1 = "Create a project description with bullet points"
    max_len = 75
    generate_text(train_filename, sequence1, max_len) 

def main():
    #Train
    train_filename = '/Users/kellybecker/Desktop/NLP/CSC482Final/data/train_85_epochs.txt'

    # train_file_path = "/Users/kellybecker/Desktop/NLP/CSC482Final/data/bulletpoints.txt"
    # model_name = 'gpt2'
    # overwrite_output_dir = False
    # per_device_train_batch_size = 8
    # num_train_epochs = 85.0
    # save_steps = 50000
    # train(
    #     train_file_path=train_file_path,
    #     model_name=model_name,
    #     output_dir=train_filename,
    #     overwrite_output_dir=overwrite_output_dir,
    #     per_device_train_batch_size=per_device_train_batch_size,
    #     num_train_epochs=num_train_epochs,
    #     save_steps=save_steps
    # )
    inference(train_filename)

if __name__ == "__main__":
    main()
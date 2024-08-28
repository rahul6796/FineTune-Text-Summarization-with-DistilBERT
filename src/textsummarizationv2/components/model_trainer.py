

from src.textsummarizationv2.entity import ModelTrainerConfig
import os

from transformers import Trainer, TrainingArguments
from transformers import DataCollatorForSeq2Seq
from transformers import AutoModelForSeq2SeqLM, AutoTokenizer
from datasets import load_dataset, load_from_disk
import torch
os.environ['PYTORCH_MPS_HIGH_WATERMARK_RATIO'] = '0.0'


class ModelTrainer:

    def __init__(self, config:ModelTrainerConfig):
        self.config = config



    def train(self):

        tokenizer = AutoTokenizer.from_pretrained(self.config.model_ckpt)
        model_pegasus = AutoModelForSeq2SeqLM.from_pretrained(self.config.model_ckpt)

        seq2seq_data_collector = DataCollatorForSeq2Seq(tokenizer=tokenizer, model=model_pegasus)

        # load dataset:
        data_samsum_pt = load_from_disk(self.config.data_path)

        trainer_args = TrainingArguments(
            output_dir=self.config.root_dir, num_train_epochs=self.config.num_train_epochs, warmup_steps=self.config.warmup_steps,
            per_device_train_batch_size=self.config.per_device_train_batch_size, per_device_eval_batch_size=self.config.per_device_train_batch_size,
            weight_decay=self.config.weight_decay, logging_steps=self.config.logging_steps,
            evaluation_strategy=self.config.evaluation_strategy, eval_steps=self.config.eval_steps, save_steps=1e6,
            gradient_accumulation_steps=self.config.gradient_accumulation_steps,
        )

        trainer = Trainer(model=model_pegasus, 
                          args=trainer_args,
                        tokenizer=tokenizer, 
                        data_collator=seq2seq_data_collector,
                    train_dataset=data_samsum_pt["train"], 
                    eval_dataset=data_samsum_pt["validation"])
        
        trainer.train()

        # Save model
        model_pegasus.save_pretrained(os.path.join(self.config.root_dir,"pegasus-samsum-model"))
        
        # Save tokenizer
        tokenizer.save_pretrained(os.path.join(self.config.root_dir,"tokenizer"))
    

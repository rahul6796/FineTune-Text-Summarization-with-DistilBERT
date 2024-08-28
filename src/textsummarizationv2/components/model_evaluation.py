

from transformers import AutoModelForSeq2SeqLM, AutoTokenizer
from datasets import load_dataset, load_from_disk, load_metric
from src.textsummarizationv2.entity import ModelEvaluatorConfig
from tqdm import tqdm 
import pandas as pd




class ModelEvaluation:

    def __init__(self, config: ModelEvaluatorConfig):
        self.config = config


    def get_batch_size_chunk(self, list_of_element, batch_size):
        """
        split the dataset into smaller batch of chunk

        """

        for i in range(0, len(list_of_element), batch_size):
            yield list_of_element[i:i + batch_size]

    
    def calculate_metric_on_test_ds(self, dataset, metric, model, tokenizer, batch_size, column_text = "dialogue",
                                    column_summary = "summary"):
        
        article_batches = list(self.get_batch_size_chunk(dataset[column_text], batch_size=batch_size))
        summary_batches = list(self.get_batch_size_chunk(dataset[column_summary], batch_size=batch_size))


        for article, summary in tqdm(zip(article_batches, summary_batches), total=len(article_batches)):

            inputs = tokenizer(article, max_length = 1024, truncation = True,
                               padding = "max_length", return_tensors = 'pt')
            
            summaries = model.generate(input_ids = inputs['input_ids'],
                                       attention_mask = inputs['attention_mask'],
                                       length_penalty = 0.8, num_beams = 8, max_length = 128)
            
            """ length penalty ensure that the model does not generate sequence that are to long"""
            

            decoded_summaries = [tokenizer.decode(s, skip_special_tokens=True,
                                                  clean_up_tokenization_spaces = True) for s in summaries]
            
            decoded_summaries = [d.replace("", " ") for d in decoded_summaries]

            metric.add_batch(predictions = decoded_summaries, references  = summary)
            
            score = metric.compute()
            return score
        


    def evaluation(self):

        tokenizer = AutoTokenizer.from_pretrained(self.config.tokenizer_path)
        model = AutoModelForSeq2SeqLM.from_pretrained(self.config.model_path)

        dataset_samsum_pt = load_from_disk(self.config.data_path)

        rouge_names = ['rouge1', 'rouge2', 'rougeL', 'rougeLsum']

        rouge_metric = load_metric('rouge')

        socre = self.calculate_metric_on_test_ds(
            dataset=dataset_samsum_pt['test'][0:10],
            metric=rouge_metric,
            tokenizer=tokenizer,
            model=model,
            batch_size=2,


        )


        rouge_dict = dict((rn, socre[rn].mid.fmeasure) for rn in rouge_names)

        df = pd.DataFrame(rouge_dict, index=['pegasus'])
        df.to_csv(self.config.metric_file_name, index=False)














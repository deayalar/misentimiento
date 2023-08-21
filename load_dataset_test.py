from datasets import load_dataset

dataset = load_dataset("csv", data_files={
    "train": "/Users/david.e.ayala/Documents/learning/misentimiento/data/sentiment-analysis-gpt/train.csv", 
    "test": "/Users/david.e.ayala/Documents/learning/misentimiento/data/sentiment-analysis-gpt/test.csv",
    "val": "/Users/david.e.ayala/Documents/learning/misentimiento/data/sentiment-analysis-gpt/val.csv"
})
print(dataset)
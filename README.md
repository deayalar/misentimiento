# Misentimiento

I would like to build a system that serves as a pre-trained model for the following tasks:

- Sentiment analysis on complete sentences
- Targeted sentiment analysis for named entities

Tasks to be completed:

- Build a dataset using a generative model for both complete sentence sentiment analysis and named entities sentiment analysis.
- Create a complete MLOps pipeline that allows for receiving new data, retraining the model, evaluating, deploying, and monitoring.
- Develop a Streamlit application to showcase the model, select a version, and make inferences.
- Deploy the model on HuggingFace Spaces.
- Create a repository to demonstrate all the functionality.
- Base the code on Pysentimiento to release a model that can be freely trained and used for commercial purposes in both NLP tasks.

**Principles**:

- Open-source and available for commercial use.
- Start small and make it complex:
  - Begin with encoder-based models (BERT, Roberta, Electra, etc.).
  - Experiment with more complex models.
- Project for learning MLOps and HuggingFace.
- Usable through a graphical interface.
- Inspired by pysentimiento, but anyone should be able to train it with their own data. Do not use TASS2020.
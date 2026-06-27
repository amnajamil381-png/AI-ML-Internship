# Empathetic Chatbot using DistilGPT2

## Task Objective

The objective of this project is to build an AI-powered empathetic chatbot by fine-tuning a pre-trained **DistilGPT2** language model on the **EmpatheticDialogues** dataset. The chatbot is designed to generate context-aware and empathetic responses to users based on their emotions and conversational input.

---

## Dataset Used

- **Dataset:** EmpatheticDialogues
- **Source:** Hugging Face Datasets
- **Description:** A collection of approximately 25,000 empathetic conversations where one speaker shares a personal experience and the other responds empathetically.

---

## Model Used

- **Base Model:** DistilGPT2
- **Framework:** Hugging Face Transformers
- **Fine-Tuning Method:** Supervised Fine-Tuning (SFT)
- **Development Environment:** Google Colab / Kaggle Notebook
- **Deployment:** Streamlit

---

## Project Workflow

1. Loaded the EmpatheticDialogues dataset.
2. Explored the dataset structure and conversations.
3. Grouped utterances by conversation ID.
4. Created input-response training pairs.
5. Tokenized the dataset using the DistilGPT2 tokenizer.
6. Fine-tuned the DistilGPT2 model using Hugging Face Trainer API.
7. Saved the fine-tuned model and tokenizer.
8. Built an interactive Streamlit chatbot interface.
9. Prepared the project for GitHub and Hugging Face deployment.

---

## Key Results

- Successfully fine-tuned DistilGPT2 on empathetic conversations.
- Generated context-aware conversational responses.
- Built an interactive chatbot interface using Streamlit.
- Saved the trained model for future inference and deployment.

---

## Project Structure

```
Task-5-Empathetic-Chatbot/
│
├── Task5_Empathetic_Chatbot.ipynb
├── app.py
├── requirements.txt
├── README.md
└── empathetic_chatbot/
```

---

## How to Run

### 1. Clone the Repository

```bash
git clone <repository-url>
cd Task-5-Empathetic-Chatbot
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the Application

```bash
streamlit run app.py
```

---

## Technologies Used

- Python
- Hugging Face Transformers
- Hugging Face Datasets
- PyTorch
- Streamlit
- Google Colab
- Kaggle
- GitHub

---

## Future Improvements

- Improve response quality with larger language models.
- Incorporate emotion classification before response generation.
- Maintain multi-turn conversation history.
- Deploy the chatbot as a public web application.

---

## Author

**Amna Jamil**

AI/ML Internship Task 5 – Empathetic Chatbot using DistilGPT2

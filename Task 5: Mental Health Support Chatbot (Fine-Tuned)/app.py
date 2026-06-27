import streamlit as st
import torch
from transformers import AutoTokenizer, AutoModelForCausalLM

# ----------------------------
# Page Configuration
# ----------------------------
st.set_page_config(
    page_title="Empathetic Chatbot",
    page_icon="🤖"
)

st.title("🤖 Empathetic Chatbot")
st.write("An AI chatbot fine-tuned on the EmpatheticDialogues dataset.")

# ----------------------------
# Load Fine-Tuned Model
# ----------------------------
@st.cache_resource
def load_model():

    model_path = "empathetic_chatbot"

    tokenizer = AutoTokenizer.from_pretrained(model_path)
    model = AutoModelForCausalLM.from_pretrained(model_path)

    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    model.to(device)

    return tokenizer, model, device

tokenizer, model, device = load_model()

# ----------------------------
# User Inputs
# ----------------------------
emotion = st.selectbox(
    "Select your emotion",
    [
        "sad",
        "happy",
        "angry",
        "afraid",
        "excited",
        "lonely",
        "proud",
        "anxious"
    ]
)

user_input = st.text_area(
    "Tell me what's on your mind:"
)

# ----------------------------
# Generate Response
# ----------------------------
if st.button("Generate Response"):

    if user_input.strip() == "":
        st.warning("Please enter a message.")
    else:

        prompt = f"Emotion: {emotion}\nUser: {user_input}\nAssistant:"

        inputs = tokenizer(
            prompt,
            return_tensors="pt"
        ).to(device)

        output = model.generate(

            **inputs,

            max_new_tokens=60,

            temperature=0.7,

            top_k=50,

            top_p=0.9,

            repetition_penalty=1.2,

            no_repeat_ngram_size=3,

            do_sample=True,

            pad_token_id=tokenizer.eos_token_id
        )

        response = tokenizer.decode(
            output[0],
            skip_special_tokens=True
        )

        # Remove prompt from generated text
        response = response.replace(prompt, "").strip()

        st.success("Chatbot Response")

        st.write(response)

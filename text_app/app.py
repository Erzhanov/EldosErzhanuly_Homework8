import streamlit as st
from transformers import pipeline
from transformers import AutoTokenizer, AutoModelForTokenClassification


tokenizer = AutoTokenizer.from_pretrained("dslim/bert-base-NER")
model = AutoModelForTokenClassification.from_pretrained("dslim/bert-base-NER")



@st.cache_resource
def get_ner_pipeline():
    return pipeline(
        task="ner",
        model=model,
        tokenizer=tokenizer,
        grouped_entities=True,
        device=-1,  # Use CPU
    )

def main():
    st.set_page_config(page_title="NER App", layout="centered")
    st.title("🧠 Мәтіннен Атауларды Анықтау (NER)")
    
    text = st.text_area("Мәтінді енгізіңіз:", height=200, placeholder="Қасым-Жомарт Кемелұлы Тоқаев...")
    st.button("Анықтау", key="ner-button")
    
    if text:
        with st.spinner("Анықтап жатырмыз..."):
            ner_pipeline = get_ner_pipeline()
            results = ner_pipeline(text)
        
        st.subheader("🔍 Табылған атаулар:")
        for entity in results:
            st.markdown(f"• **Сөз:** `{entity['word']}`  \n  **Түрі:** `{entity['entity_group']}`  \n  **Дәлдік:** `{entity['score']:.2f}`")

if __name__ == "__main__":
    main()

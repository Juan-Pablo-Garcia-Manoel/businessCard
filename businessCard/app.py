import streamlit as st
from src.services.business_card_service import analyze_business_card
from src.services.bloob_Service import upload_blob

def configure_interface():
    st.title("Upload de arquivos - Azure - Fake Docs")
    uploaded_file = st.file_uploader("Escolha um arquivo", type=["png","jpg","jpeg"])

    if uploaded_file is not None:
        fileName = uploaded_file.name
        # Enviar para o blob storage do azure
        blob_url = upload_blob(uploaded_file, fileName)
        if blob_url:
            st.write(f"Arquivo {fileName} enviado com sucesso para o Azure Blob Storage")
            business_card_info = analyze_business_card(blob_url) # Chamar função de detecção de cartão de credito
            show_image_and_validation(blob_url,business_card_info)
        else:
            st.write(f"Erro ao enviar o {fileName} para o Azure Blob Storage")
    
def show_image_and_validation(blob_url, business_card_info):
    st.image(blob_url, caption="Imagem enviada", use_container_width=True)
    st.write("Resultado da validação:")
    if business_card_info and business_card_info:
        st.markdown(f"<h1 style='color: green;'>Card Válido</h1>",unsafe_allow_html=True)
        st.write(f"Nome: {business_card_info['contact_names']}")
        st.write(f"E-mail: {business_card_info['emails']}")
        st.write(f"Telefone: {business_card_info['work_phones']}")
    else:
        st.markdown(f"<h1 style='color: green;'>Card Inválido</h1>",unsafe_allow_html=True)
        st.write(f"Este não é um cartão de visitas válido.")

if __name__ == "__main__":
    configure_interface()

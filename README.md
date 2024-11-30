# Validador de Documentos - Azure

Este projeto é um estudo prático que utiliza a linguagem Python para realizar a validação de um cartão de visitas através da integração com os serviços da Azure. O sistema permite enviar arquivos de imagem para um contêiner de armazenamento na Azure e realiza a validação desses documentos, retornando campos pré-selecionados.

## Pré-requisitos

Antes de executar o projeto, certifique-se de ter o Python instalado e siga os passos abaixo para configurar o ambiente.

## Passos para Configuração e Execução

### 1. Instale o Streamlit (servidor web):

```bash
pip install streamlit
```
### 2. Instale os pacotes necessários:
Utilize o arquivo requirements.txt para instalar as dependências específicas do projeto:

```bash
pip install -r requirements.txt
```

### 3. Execute o servidor Streamlit:
Inicie o servidor para rodar o projeto em seu navegador:

```bash
python -m streamlit run .\app.py
```

### Como Utilizar
Após executar o servidor, uma página web será aberta automaticamente no seu navegador.
Na página, você poderá enviar arquivos nos formatos "png", "jpg" ou "jpeg".
O sistema enviará o arquivo para o contêiner de armazenamento de arquivos da Azure.
A imagem será enviada para o validador de documentos, com tamanho máximo permitido de até 200 MB.
O sistema retornará os campos pré-selecionados configurados no projeto.

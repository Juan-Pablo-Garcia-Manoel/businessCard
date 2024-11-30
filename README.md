# Validador de Documentos - Azure

Este projeto é um estudo prático desenvolvido em Python, seguindo o projeto do professor Henrique Eduardo Souza, relacionado à validação de cartão de crédito. O sistema permite realizar a validação de um cartão de visitas por meio da integração com os serviços da Azure. Ele possibilita o envio de arquivos de imagem para um contêiner de armazenamento na Azure e realiza a validação desses documentos, retornando campos pré-selecionados. Para utilizá-lo, é necessário configurar as credenciais do Azure nas classes específicas do projeto.

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

## ⚠️ **Importante**: Custo dos Serviços Azure

**ATENÇÃO**: O uso dos serviços Azure pode gerar custos, que são cobrados diretamente pela plataforma. **Antes de usar o software, consulte as tarifas e encargos relacionados ao uso dos serviços conforme sua configuração na Azure.**

** O Streamlit coleta dados estatísticos de uso. Para desativar essa coleta, siga os passos abaixo:**

1. Acesse a pasta do Streamlit em seu computador: `C:\Users\seu_usuario\.streamlit`.

2. Crie um arquivo chamado `config.toml` (caso não exista) e adicione a seguinte linha:

   ```toml
   [browser]gatherUsageStats = false
   
3. No arquivo credentials.toml (também localizado na mesma pasta), adicione a mesma linha acima.

Nota importante:

Sempre após executar o projeto, verifique e, se necessário, crie o arquivo config.toml contendo o campo mencionado acima.
Se você interromper o servidor, será necessário excluir o arquivo, executar o projeto novamente e recriar o arquivo config.toml.
Certifique-se de que ambos os arquivos estejam no formato .toml e salve as alterações. Isso impedirá a coleta de dados de uso pelo Streamlit.
A criação deste arquivo é orientada pelo proprio Streamlit, no caso da recusa da coleta de dados.

Esteja ciente de que o consumo dos serviços é cobrado com base nas suas configurações e uso na plataforma da Azure.

## Observações:

- Este software está em constante aprimoramento e novos recursos serão adicionados conforme o avanço nos meus estudos.

- Espero que o software seja útil para suas necessidades na validação de documentos utilizando os serviços da Azure!

***

# Document Validator - Azure

This project is a practical study developed in Python, following the project by Professor Henrique Eduardo Souza, related to credit card validation. The system allows the validation of a business card through integration with Azure services. It enables the uploading of image files to an Azure storage container and performs validation of these documents, returning pre-selected fields. To use it, it is necessary to configure Azure credentials in the specific classes of the project.

## Prerequisites

Before running the project, make sure Python is installed and follow the steps below to set up the environment.

## Setup and Execution Steps

### 1. Install Streamlit (web server):

```bash
pip install streamlit
```

### 2. Install the necessary packages:

Use the requirements.txt file to install the project's specific dependencies:

```bash
pip install -r requirements.txt
```

### 3. Run the Streamlit server:

Start the server to run the project in your browser:

```bash
python -m streamlit run .\app.py
```

### How to Use

After running the server, a web page will automatically open in your browser. On the page, you can upload files in "png", "jpg", or "jpeg" formats. The system will send the file to the Azure storage container. The image will then be sent to the document validator, with a maximum file size of up to 200 MB. The system will return the pre-selected fields configured in the project.

## ⚠️ **Important**: Azure Services Cost

**ATTENTION**: Using Azure services may incur costs, which are charged directly by the platform. Before using the software, review the rates and charges related to the use of the services according to your Azure configuration.**

** Streamlit collects usage statistics. To disable this collection, follow the steps below: **

1. Navigate to the Streamlit folder on your computer: `C:\Users\your_user\.streamlit`.

2. Create a file named `config.toml`  (if it doesn’t exist) and add the following line:

   ```toml
   [browser]gatherUsageStats = false
   
3. In the credentials.toml file (also located in the same folder), add the same line above.

Important Note:

After running the project, always check and, if necessary, create the config.toml file with the mentioned field. If you stop the server, you will need to delete the file, run the project again, and recreate the config.toml file. Ensure both files are in .toml format and save the changes. This will prevent Streamlit from collecting usage data. This file creation is suggested by Streamlit in case you refuse the data collection.

Be aware that the consumption of services is billed based on your configurations and usage on the Azure platform.

## Observations:

- This software is constantly being improved, and new features will be added as my studies progress.

- I hope this software proves useful for your document validation needs using Azure services!


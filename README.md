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
A criação deste arquivo é orientada pelo proprio Streamlit no caso da recusa da coleta de dados.

Esteja ciente de que o consumo dos serviços é cobrado com base nas suas configurações e uso na plataforma da Azure.

## Observações:

- Este software está em constante aprimoramento e novos recursos serão adicionados conforme o avanço nos meus estudos.

Espero que o software seja útil para suas necessidades na validação de documentos utilizando os serviços da Azure!

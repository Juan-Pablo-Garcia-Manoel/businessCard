from azure.core.credentials import AzureKeyCredential
from azure.ai.documentintelligence.models import AnalyzeDocumentRequest
from azure.ai.formrecognizer import DocumentAnalysisClient
from src.utils.Config import config

def analyze_business_card(card_url):
    
    endpoint = config.ENDPOINT
    key = config.KEY
    formUrl = card_url
    
    document_analysis_client = DocumentAnalysisClient(endpoint=endpoint,credential = AzureKeyCredential(key))
    
    poller = document_analysis_client.begin_analyze_document_from_url("prebuilt-businessCard", formUrl)
    business_card = poller.result()

    results = {
        "emails": [],
        "contact_names": [],
        "work_phones": []
    }

    for document in business_card.documents:
        
        fields = document.fields
        emails = fields.get("Emails")
        contact_names = fields.get("ContactNames")
        work_phones = fields.get("WorkPhones")

        if contact_names and contact_names.value: 
            for contact_names in contact_names.value:
                print(
                    "Nome: {} has confidence: {}".format(
                        contact_names.value, contact_names.confidence
                        )
                    )
                results["contact_names"].append(contact_names.content)

        if emails:
            for email in emails.value:
                print(
                    "Email: {} has confidence: {}".format(email.value, email.confidence)
                )
                results["emails"].append(email.content)

        if work_phones:
            for work_phone in work_phones.value:
                print(
                    "Work phone number: {} has confidence: {}".format(
                        work_phone.content, work_phone.confidence
                    )
                )
                results["work_phones"].append(work_phone.content)
        
    return results
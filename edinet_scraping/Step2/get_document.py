import requests

END_POINT="https://disclosure.edinet-fsa.go.jp/api/v2"

#docID: 書類を特定するID
def get_document(docID):
    document_endpoint = f'{END_POINT}/documents/{docID}'
    document_request_parameters = {
        'type': 1
    }
    document_response = requests.get(document_endpoint, document_request_parameters)
    return document_response
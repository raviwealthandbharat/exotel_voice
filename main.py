import requests

EXOTEL_SID = 'raviyadav2'  
EXOTEL_AUTH_TOKEN = '37cabef694c1dfe35e493750ebe8bcb3fae855c751528165'  

EXOTEL_API_URL = f'https://api.exotel.com/v1/Accounts/{EXOTEL_SID}/Calls.json'

to_number = '+918601312209'

url = 'https://raviwealthandbharat.github.io/exotel_voice/voice_message.xml'  

data = {
    'To': to_number,  
    'Url': url,       
}

response = requests.post(
    EXOTEL_API_URL,
    data=data,
    auth=(EXOTEL_SID, EXOTEL_AUTH_TOKEN)  
)

if response.status_code == 200:
    print("Call initiated successfully!")
else:
    print(f"Failed to initiate call. Status code: {response.status_code}, Response: {response.text}")

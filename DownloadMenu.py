from google.oauth2 import service_account
from googleapiclient.discovery import build

# Replace with the ID of your Google Doc
document_id = '1zZYsO8MExaJcIDUkpOG1zQsjbcr_5ZI4qogzqaGfkxM'

# Path to the service account key file
credentials = service_account.Credentials.from_service_account_file('TwentyThird.json')

# Authenticate and create the Drive API client
service = build('drive', 'v3', credentials=credentials)

# Download the Google Doc as a text file
file_id = document_id
request = service.files().export_media(fileId=file_id, mimeType='text/plain')
content = request.execute()

# Save the text file to the current drive (wb stands for write binary and will overwrite the current file)
with open('CurrentMenu.txt', 'wb') as f:
    f.write(content)

from googleapiclient.discovery import build
from googleapiclient.http import MediaIoBaseDownload
from google.oauth2.credentials import Credentials


SCOPES = ["https://www.googleapis.com/auth/drive.readonly"]

#Para ler nossas credenciais
creds = Credentials.from_authorized_user_file("token.json",SCOPES)

#Escolhendo a API e a versao.
service = build('drive', "v3", credentials=creds)

#Colocar o ID da pasta do drive, clicando na URL(dentro da pasta) pegando a parte depois de folder/
folder_id = '1Mn2gPP4AWQjVBBf3V5JuLWRN7J4d-llL'

#Buscando os arquivos trazendo o ID e o nome deles
results = service.files().list(
    q=f"'{folder_id}' in parents", fields='files(id, name)'
).execute()

#salvando os arquiv
files = results.get('files', [])

#Verificando se tem arquivos, e baixando os curriculos se existirem, salvando eles em uma pasta(curriculos)
if not files:
    raise FileNotFoundError('not files in results')
else:
    for file in files:
        request = service.files().get_media(fileId = file['id'])
        file_path = f'./curriculos/{file['name']}'
        with open(file_path, 'wb') as file:
            downloader = MediaIoBaseDownload(file, request)
            done = False 
            while not done:
                status, done = downloader.next_chunk()
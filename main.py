from pydrive2.auth import GoogleAuth
from pydrive2.drive import GoogleDrive

credentials_auth = "credentials_module.json"

folder_id = "1PTqJKiyuJuh1AyHdYcanKJwrLrlbIYt3"

def login():
    gauth = GoogleAuth()
    gauth.LoadCredentialsFile(credentials_auth)

    if gauth.access_token_expired:
        gauth.Refresh()
        gauth.SaveCredentialsFile(credentials_auth)
    
    else:
        gauth.Authorize()
    
    return GoogleDrive(gauth)

def list_content(query):
    results = []
    gdrive = login()

    file_list = gdrive.ListFile({ 'q': query }).GetList()

    for file in file_list:
        results.append({ 'id': file['id'], 'name': file['originalFilename']})
    
    return results

def main():
    url_template = "https://drive.google.com/uc?export=download&id="

    
    query = f"'{folder_id}' in parents and trashed=false"

    results = list_content(query)

    print(results)


if __name__ == "__main__":
    main()
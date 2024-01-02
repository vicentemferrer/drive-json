from pydrive2.auth import GoogleAuth
from pydrive2.drive import GoogleDrive
import json

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

def list_content(query: str):
    results = []
    gdrive = login()

    file_list = gdrive.ListFile({ 'q': query }).GetList()

    for file in file_list:
        results.append({ 'id': file['id'], 'name': file['originalFilename']})
    
    return results

def format_data(results_list: list):
    url_template = "https://drive.google.com/uc?export=download&id="

    def add_url(file_dict: dict):
        file_list = list(file_dict.items())

        file_list.append(['url', url_template + file_dict['id']])

        return { prop[0]: prop[1] for prop in file_list }
    
    return list(map(add_url, results_list))

def write_json(data):
    data_to_dump = { 'files': data }
    
    with open('drive-files.json', 'w') as file:
        json.dump(data_to_dump, file, indent=4)

def main():
    query = f"'{folder_id}' in parents and trashed=false"

    results = format_data(list_content(query))

    write_json(results)

if __name__ == "__main__":
    main()
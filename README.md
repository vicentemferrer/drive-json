# <p align="center">JSON for Google Drive</p>
<p align="center">Embed your static files from your Google Drive storage 🚀</p>

## Overview
It eases a way to use Google Drive storage as a static files server like images (overall created to provide images). 
It caught files info and add them an url to embed in your web pages to finally dump the data collection into a JSON 
file which you can use to include your files using Google Drive as an external provider.

## How to use
### Clone repo in your local machine
```git
git clone https://github.com/vicentemferrer/drive-json.git
```
### Repo content
The repo has 3 core files to work:
  - _init.py_ - to generate OAuth credentials file
  - _settings.yaml_ - to configure OAuth credentials generation
  - _main.py_ - to generate final JSON file with file info

### Setting up
1. Be sure to have Python installed, pip package manager updated, and PyDrive2 library installed.
2. You need to generate an OAuth client in Google Cloud Platform console. [Brief guide in spanish here ↗](https://www.youtube.com/watch?v=ZI4XjwbpEwU)
3. Download client JSON file, rename it as _client_secrets.json_, and move it to cloned repo.
4. In your text editor, complete positions commented in _settings.yaml_.
5. In _main.py_, store in _folder_id_ the Drive ID from content folder which you can found in its sharing link.
    - Example: ```https://drive.google.com/file/d/ -> 17Iq_gEupqzgZ7Gi847cSlqsZLUoWnooS <- /view?usp=drive_link```

### Using
1. Start _init.py_ with ```python init.py```. It will generate a JSON file named _credentials_module.json_ which will be used by _main.py_.
2. Start _main.py_ with ```python main.py```. It will generate your final JSON file called _drive-files.json_, ready to be used in your project.

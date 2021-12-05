import zipfile
import os

def unzip_file(zip_file: str, extract: str) -> None:
    with zipfile.ZipFile(zip_file, 'r') as zip_ref:
        zip_ref.extractall(extract)
    os.remove(zip_file)

for i in range(2021):
    unzip_file(os.listdir('./')[0], './')
    

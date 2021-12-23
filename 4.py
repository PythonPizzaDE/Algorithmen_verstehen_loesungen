import zipfile

def unzip_file(zip_file: str, extract: str, password: str) -> None:
    with zipfile.ZipFile(zip_file, 'r') as zip_ref:
        zip_ref.extractall(extract, pwd=password.encode())

def main():
    with open('rockyou.txt', encoding='latin-1') as file:
        passwords = file.read().split('\n')
    
    for password in passwords:
        try:
            unzip_file('geschenk.zip', 'geschenk', password)
            print(f'Password is: {password}')
            break
        except Exception as e:
            ...

if __name__ == '__main__':
    main()

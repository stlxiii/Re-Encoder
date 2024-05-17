import os, shutil

FILE_EXTENSION    = 'txt'
ENCODING_TO_READ  = 'utf-8-sig'
ENCODING_TO_WRITE = 'utf-8'

def main():
    this_file    = os.path.abspath(__file__)
    folder_path  = os.path.dirname(this_file)

    # Iterate folder and subfolders
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            file_path = os.path.join(root, file)
            if os.path.isfile(file_path):
                if file_path.lower().endswith(FILE_EXTENSION.lower()):
                    print(f'Processing {file_path}')
                    
                    # Make a backup
                    i = 1
                    while os.path.exists(f'{file_path}.{i}.bak'):
                        i += 1
                    shutil.copy(file_path, f'{file_path}.{i}.bak')

                    # Read content
                    with open(file_path, 'r', encoding=ENCODING_TO_READ) as f:
                        content = f.read()
                    
                    # Write content
                    with open(file_path, 'w', encoding=ENCODING_TO_WRITE) as f:
                        f.write(content)


if __name__ == '__main__':
    main()
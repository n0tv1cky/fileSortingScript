import os
import shutil
from dotenv import load_dotenv, dotenv_values

load_dotenv()
cwd = os.getenv("CWD")

file_data = {
    'Media': {
        'extensions': ['.jpg', '.jpeg', '.png', 'mpeg', '.mp4', '.mp3', '.mov', '.CR2', '.ARW'],
        'path': os.path.join(cwd, "Media")
    },
    'Docs': {
        'extensions': ['.pdf', '.PDF', '.docx', '.doc', '.pptx', '.xlsx', '.xls'],
        'path': os.path.join(cwd, "Docs")
    },
    'DMG files': {
        'extensions': ['.dmg'],
        'path': os.path.join(cwd, "DMG files")
    },
    'App installations': {
        'extensions': ['.app'],
        'path': os.path.join(cwd, "App installations")
    },
    'Compressed files': {
        'extensions': ['.zip', '.7z', '.rar'],
        'path': os.path.join(cwd, "Compressed files")
    },
    'Misc': {
        'extensions': [],  # An empty list since there are no specific extensions for Misc
        'path': os.path.join(cwd, "Misc")
    }
}

excluded_files = ['.DS_Store', '.localized']

for folder, data in file_data.items():
    if not os.path.isdir(data['path']):
        os.makedirs(data['path'])
        print(f"<< {folder} folder created >>")

if files := [
    f
    for f in os.listdir(cwd)
    if (
        (os.path.isfile(os.path.join(cwd, f)) or f.endswith('.app'))
        and (f not in excluded_files)
    )
]:
    for file in files:
        if file not in excluded_files:
            file_path = os.path.join(cwd, file)
            moved = False

            for file_type, file_info in file_data.items():
                extensions = file_info['extensions']
                destination_path = file_info['path']

                if file_path.endswith(tuple(extensions)):
                    print(f"<< Moved {file} to {file_type} folder >>")
                    shutil.move(file_path, destination_path)
                    moved = True
                    break
            if not moved:
                print(f"<< Moved {file} to 'Misc' folder >>")
                shutil.move(file_path, file_data['Misc']['path'])

    print("<- Sorting operation completed succesfully ->")
else:
    print("<- No files to sort ->")

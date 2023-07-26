import os
import shutil

cwd = "/Users/n0tv1cky/Downloads"

file_types = {
    'Media': ['.jpg', '.jpeg', '.png', 'mpeg', 'mp4', '.mov'],
    'Docs': ['.pdf', '.docx', '.pptx'],
    'DMG files': ['.dmg'],
    'App installations': ['.app'],
    'Compressed files': ['.zip', '.7z', '.rar'],
    'Misc': []
}

paths = {
    'Media': os.path.join(cwd, "Media"),
    'Docs': os.path.join(cwd, "Docs"),
    'DMG files': os.path.join(cwd, "DMG files"),
    'App installations': os.path.join(cwd, "App installations"),
    'Compressed files': os.path.join(cwd, "Compressed files"),
    'Misc': os.path.join(cwd, "Misc")
}

excluded_files = {'.DS_Store', '.localized'} 

for folder in file_types:
    if not os.path.isdir(paths[folder]):
        os.makedirs(paths[folder])
        print(f"{folder} folder created")

files = [f for f in os.listdir(cwd) if os.path.isfile(os.path.join(cwd, f))]

if files:
    for file in files:
        if file not in excluded_files:
            file_path = os.path.join(cwd, file)

            for file_type, extensions in file_types.items():
                if file_path.endswith(tuple(extensions)):
                    print(f"Moved {file} to {file_type} folder")
                    shutil.move(file_path, paths[file_type])
                else:
                    print(f"Moved {file} to 'Misc' folder")
                    shutil.move(file_path, paths['Misc'])
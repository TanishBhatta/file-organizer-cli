import shutil
import os
import argparse

extension_map = {

    ".png" : "Images",
    ".jpeg" : "Images",
    ".jpg" : "Images",
    ".gif" : "Images",
    ".svg" : "Images",
    ".webp" : "Images",
    ".bmp" : "Images",
    ".tiff" : "Images",

    ".mp3" : "Audios",
    ".wav" : "Audios",
    ".flac" : "Audios",
    ".aac" : "Audios",
    ".m4a" : "Audios",
    ".ogg" : "Audios",
    ".wma" : "Audios",

    ".mp4" : "Videos",
    ".mkv" : "Videos",
    ".avi" : "Videos",
    ".mov" : "Videos",
    ".wmv" : "Videos",
    ".flv" : "Videos",
    ".mpeg" : "Videos",

    ".pdf" : "Office Documents",
    ".doc" : "Office Documents",
    ".docx" : "Office Documents",
    ".rtf" : "Office Documents",
    ".odt" : "Office Documents",

    ".xlsx" : "Spreadsheets",
    ".xls" : "Spreadsheets",
    ".csv" : "Spreadsheets",
    ".ods" : "Spreadsheets",

    ".pptx" : "Presentations",
    ".ppt" : "Presentations",
    ".odp" : "Presentations",
    
    ".py" : "Code",
    ".js" : "Code",
    ".html" : "Code",
    ".css" : "Code",
    ".json" : "Code",
    ".sql" : "Code",
    ".c" : "Code",
    ".cpp" : "Code",
    ".java" : "Code",
    ".php" : "Code",
    ".sh" : "Code",

    ".exe" : "Installers",
    ".msi" : "Installers",
    ".dmg" : "Installers",
    ".deb" : "Installers",
    ".pkg" : "Installers",
    ".apk" : "Installers",

    ".zip" : "Archives",
    ".rar" : "Archives",
    ".7z" : "Archives",
    ".tar" : "Archives",
    ".gz" : "Archives",
    ".iso" : "Archives",

}

def create_folder(folder_name):
    
    os.makedirs(folder_name, exist_ok=True)

def move_file(file, target):
    
    try:

        shutil.move(file, target)

    except Exception as e:
        print(f"There was a error in moving {file}: {e}")

def get_target_folder(filename):

    extension = filename.split(".")[-1]

    return extension_map.get("." + extension, "Unknown Files")

parser = argparse.ArgumentParser(description="Organize files by extension.")
parser.add_argument("--path", type=str, default=".", help="Path to the folder to organize")
args = parser.parse_args()

files = os.listdir(args.path)

for file in files:

    target = get_target_folder(file)
    print(f"{file} -> {target}")
    full_path = os.path.join(args.path, file)
    target_path = os.path.join(args.path, target)

    if target != "Unknown Files":
        create_folder(target_path)
        move_file(full_path, target_path)

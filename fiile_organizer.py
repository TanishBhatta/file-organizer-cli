import shutil
import os

extension_map = {
    ".pdf" : "PDFs",
    ".mp3" : "Audios",
    ".mp4" : "Videos",
    ".png" : "Images",
    ".exe" : "Executions",
    ".py" : "Python Files",
    ".wav" : "Wave Files",
    ".fl" : "FlStudio Files",
    ".html" : "HTML Files",
    ".css" : "CSS Files"

}

def create_folder(folder_name):
    
    os.makedirs(folder_name, exist_ok=True)

def move_file(file, target):
    
    try:

        shutil.move(file, target)

    except Exception as e:
        print(f"There was a error in moving {file}: {e}")

files = os.listdir(".")

def get_target_folder(filename):

    extension = filename.split(".")[-1]

    return extension_map.get("." + extension, "Unknown Files")

for file in files:
    target = get_target_folder(file)
    print(f"{file} -> {target}")
    if target != "Unknown Files":
        create_folder(target)
        move_file(file, target)

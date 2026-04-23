extension_map = {
    ".mp3": "Audios",
    ".mp4": "Videos",
    ".png": "Images",
    ".pptx": "Presentations",
    ".docx": "Documents",
    ".pdf": "PDFs",
}

def get_targeted_folder(filename):
    
    
    extension = filename.split(".")[-1]

    return extension_map.get("." + extension, "Unknown")

print(get_targeted_folder("report.pdf"))
print(get_targeted_folder("song.mp3"))
print(get_targeted_folder("unknown.xyz"))


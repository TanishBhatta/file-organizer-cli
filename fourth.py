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

def get_target_folder(files):

    extension = files.split(".")[-1]

    return extension_map.get("." + extension, "Unknown Files")

for get_target_foler in extension_map:
    print(get_target_folder)


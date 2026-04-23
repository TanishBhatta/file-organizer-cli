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
# sakshyam.mp4 = "sakshyam", ".mp4"

def get_target_folder(filename):

    extension = filename.split(".")[-1]

    return extension_map.get("." + extension, "Unknown Files")

print(get_target_folder("aarush.png"))
print(get_target_folder("HotelCalifornia.fl"))

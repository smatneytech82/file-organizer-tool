import os
import shutil

downloads_folder = r"C:\Users\matne\Downloads"

file_types = {
    "Images": [".png", ".jpg", ".jpeg", ".gif"],
    "Documents": [".pdf", ".docx", ".txt"],
    "Videos": [".mp4", ".mov"],
    "Music": [".mp3"],
    "Archives": [".zip", ".rar"]
}

for filename in os.listdir(downloads_folder):

    file_path = os.path.join(downloads_folder, filename)

    if os.path.isfile(file_path):

        extension = os.path.splitext(filename)[1].lower()

        for folder_name, extensions in file_types.items():

            if extension in extensions:

                destination_folder = os.path.join(downloads_folder, folder_name)

                os.makedirs(destination_folder, exist_ok=True)

                shutil.move(
                    file_path,
                    os.path.join(destination_folder, filename)
                )

                print(f"Moved: {filename} -> {folder_name}")

                break
import requests, os, shutil
from datetime import datetime

folder_name = "daniel_sarpong"
local_file_path = os.path.join(folder_name, "daniel_sarpong.txt")
url = "https://raw.githubusercontent.com/sdg000/pydevops_intro_lab/main/change_me.txt"

# Clean up previous directory and create a new directory
if os.path.exists(folder_name):
    try:
        shutil.rmtree(folder_name)
        print(f"Directory '{folder_name}' has been removed successfully.")
    except Exception as e:
        print(f"Error: {e}")

if not os.path.exists(folder_name):
    os.makedirs(folder_name)
    print(f"Directory: {folder_name} created.")

# Download the file
response = requests.get(url)

if response.status_code == 200:
    print(f"File successfully downloaded.")
    with open(local_file_path, "wb") as file:
        file.write(response.content)
        print('File saved successfully.')
else:
    print(f"Failed to download file. Status code: {response.status_code}")

# Overwrite file content
user_input = input("Describe what you have learned so far in a sentence: ")
now = datetime.now()
current_time = now.strftime("%Y-%m-%d %H:%M:%S")

with open(local_file_path, "w") as file:
    file.write(user_input + "\n")
    file.write(f"Last modified on: {current_time}")
    print("File successfully modified.")

# Display new file content
with open(local_file_path, "r") as file:
    print("\nYou Entered: ", end=' ')
    print(file.read())

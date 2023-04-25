

import os
import shutil
from datetime import datetime, timedelta

# Get the current date
now = datetime.now()

# Get the path of the downloads folder
downloads_folder_path = os.path.join(os.path.expanduser('~'), 'Downloads')

# Create the to-delete folder path
to_delete_folder_path = os.path.join(os.path.expanduser('~'), 'to-delete')

# Create the to-delete folder if it doesn't exist
if not os.path.exists(to_delete_folder_path):
    os.mkdir(to_delete_folder_path)

# Go through all files in the downloads folder
for file in os.listdir(downloads_folder_path):
    file_path = os.path.join(downloads_folder_path, file)
    # Get the modification date of the file
    mod_date = datetime.fromtimestamp(os.path.getmtime(file_path))
    # Check if the file is older than 30 days
    if (now - mod_date) > timedelta(days=30):
        # Move the file to the to-delete folder
        shutil.move(file_path, to_delete_folder_path)
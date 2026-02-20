import shutil
import os
from datetime import datetime

# Update these paths before running locally
SOURCE_FOLDER = "C:/Users/Anu/OneDrive/SourceFolder"
BACKUP_FOLDER = "C:/Users/Anu/OneDrive/Backup"

today = datetime.today().strftime('%Y-%m-%d')
destination = os.path.join(BACKUP_FOLDER, today)

os.makedirs(destination, exist_ok=True)

for file in os.listdir(SOURCE_FOLDER):
    source_path = os.path.join(SOURCE_FOLDER, file)
    if os.path.isfile(source_path):
        shutil.copy(source_path, destination)
        print(f"Copied: {file}")

print(f"\nBackup completed successfully to: {destination}")
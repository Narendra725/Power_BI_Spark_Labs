import os
import shutil
import zipfile

def zip_definition(source_dir, output_zip_path):
    """Zips a Fabric definition folder for download."""
    if output_zip_path.endswith('.zip'):
        output_zip_path = output_zip_path[:-4]
    shutil.make_archive(output_zip_path, 'zip', source_dir)
    print(f"Created: {output_zip_path}.zip")

def push_to_github(repo_dir, commit_message="Update report"):
    """Performs a standard add, commit, and push sequence."""
    original_dir = os.getcwd()
    os.chdir(repo_dir)
    try:
        os.system('git config --global user.email "narendradasari725@gmail.com"')
        os.system('git config --global user.name "Narendra725"')
        os.system('git add .')
        os.system(f'git commit -m "{commit_message}"')
        os.system('git push origin main')
        print("Push sequence complete.")
    finally:
        os.chdir(original_dir)
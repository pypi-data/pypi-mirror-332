import subprocess
import os
def run(app):
    current_file_path = os.path.abspath(__file__)
    app_path = current_file_path
    subprocess.run(["streamlit", "run", app_path])
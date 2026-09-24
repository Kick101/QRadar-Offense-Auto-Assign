import time
import subprocess
import pyautogui

# Path to your script
script_path = "qradar-offense-auto-assign.py"

while True:
    try:
        # Run the script
        subprocess.run(["python", script_path], check=True)
        print(f"Script ran successfully at {time.strftime('%Y-%m-%d %H:%M:%S')}")
    except subprocess.CalledProcessError as e:
        print(f"Error running script: {e}")

    # Wait 10 minutes (600 seconds)
    time.sleep(600)


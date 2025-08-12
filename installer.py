import os
import shutil
import subprocess
import sys

def run_steamcmd(commands):
    process = subprocess.run(commands)
    if process.returncode != 0:
        print("SteamCMD encountered an error.")
        sys.exit(1)

# First run to check for steamcmd updates
update_cmd = [os.path.join(os.getcwd(), "steamcmd.exe"), "+quit"]
print("Checking for SteamCMD updates...")
run_steamcmd(update_cmd)

# Second run to execute the actual commands
username = input("Enter your Steam username: ")
password = input("Enter your Steam password: ")

cmd = [
    os.path.join(os.getcwd(), "steamcmd.exe"),
    f"+login {username} {password}",
    "+download_depot 945360 945361 5207443046106116882",
    "+quit"
]

run_steamcmd(cmd)

root_dir = os.getcwd()
src_dir = os.path.join(root_dir, "steamapps", "content", "app_945360", "depot_945361")

if not os.path.isdir(src_dir):
    input("Depot Files not found, installation failed\nPress Enter to exit...")
    sys.exit(1)

for item in os.listdir(src_dir):
    s = os.path.join(src_dir, item)
    d = os.path.join(root_dir, item)
    shutil.move(s, d)
print("Depot files moved to folder root directory")


locallow = os.path.join(os.getenv("USERPROFILE"), "AppData", "LocalLow")
file_path = os.path.join(locallow, "Innersloth", "Among Us", "settings.amogus")

if os.path.exists(file_path):
    os.remove(file_path)
    print("File 'settings.amogus' deleted.")
else:
    print("settings.amogus file not found.")

input("Press Enter to exit...")
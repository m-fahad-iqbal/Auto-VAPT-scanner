import subprocess
from tqdm import tqdm
import time
import colorama

colorama.init()

def display_loading(message, duration=5):
    for _ in tqdm(range(duration), desc=message, colour='cyan'):
        time.sleep(1)

def run_command(command):
    result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True, text=True)
    return result.stdout, result.stderr

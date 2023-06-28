import subprocess
import time
import os
import signal
import pickle

Donations = 'bc1qus09g0n5jwg79gje76zxqmzt3gpw80dcqspsmm'

# Function to save checkpoint
def save_checkpoint(start_keyspace, end_keyspace):
    checkpoint = {
        'start_keyspace': start_keyspace,
        'end_keyspace': end_keyspace
    }
    with open('checkpoint.pkl', 'wb') as f:
        pickle.dump(checkpoint, f)

# Function to load checkpoint
def load_checkpoint():
    if os.path.exists('checkpoint.pkl'):
        with open('checkpoint.pkl', 'rb') as f:
            checkpoint = pickle.load(f)
            return checkpoint['start_keyspace'], checkpoint['end_keyspace']
    else:
        return None

def run_bitcrack(start_keyspace, end_keyspace):
    command = [
        'BitCrack.exe', '-b', '96', '-t', '256', '-p', '256', '--stride', '1',
        '-r', f'--keyspace', f'{start_keyspace}:{end_keyspace}', '-o', 'FOUND.txt',
        '-c', '13zb1hQbWVsc2S7ZTZnP2G4undNNpdh5so'
    ]

    process = subprocess.Popen(command, shell=True, creationflags=subprocess.CREATE_NEW_PROCESS_GROUP)
    time.sleep(180)  # Wait for 180 seconds
    os.kill(process.pid, signal.CTRL_BREAK_EVENT)  # Send CTRL_BREAK_EVENT signal to terminate the process group
    process.wait()  # Wait for the process to exit

# Main loop
start_keyspace = int('20000000000000000', 16)  # Starting keyspace value (hex)
end_keyspace = int('20100000000000000', 16)  # Ending keyspace value (hex)
increment = int('100000000000000', 16)  # Increment value (hex)

# Load checkpoint if it exists
checkpoint = load_checkpoint()
if checkpoint is not None:
    start_keyspace, end_keyspace = checkpoint

while end_keyspace <= int('3ffffffffffffffff', 16):  # Continue until the ending keyspace value is reached
    run_bitcrack(hex(start_keyspace), hex(end_keyspace))
    start_keyspace = end_keyspace + 1  # Increment the start keyspace value
    end_keyspace = start_keyspace + increment - 1  # Increment the end keyspace value correctly

    # Save checkpoint
    save_checkpoint(start_keyspace, end_keyspace)

    time.sleep(5)  # Wait for 10 seconds before restarting

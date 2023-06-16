import subprocess
import time
import os
import signal

def run_bitcrack(start_keyspace, end_keyspace):
    command = [
        'BitCrack.exe', '-b', '672', '-t', '256', '-p', '256', '--stride', '100000000',
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

while True:  # Outer loop for continuous execution
    while end_keyspace <= int('3ffffffffffffffff', 16):  # Continue until the ending keyspace value is reached
        run_bitcrack(hex(start_keyspace), hex(end_keyspace))
        start_keyspace = end_keyspace + 1  # Increment the start keyspace value
        end_keyspace = start_keyspace + increment - 1  # Increment the end keyspace value correctly
        time.sleep(10)  # Wait for 10 seconds before restarting

    # Reset keyspace values and restart
    start_keyspace = int('20000000000000000', 16)  # Reset to the beginning keyspace value
    end_keyspace = int('20100000000000000', 16)  # Reset to the ending keyspace value

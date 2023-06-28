# Bitcrack-automation
for Windows puzzle 66 automate incrementing and scanning through the range by automatically incrementing through the puzzle 66<br>
can use any version of bitcrack but for this I used random bitcrack that generates millions of random starting points<br>
Keeping the range scanned small and with millions of starting points increases the chance of finding the private key<br>
<b>Change</b> -b,-t,-p to fit your  card's memory, more memory more starting points and more chance for success<br>
change time.sleep(180)  # Wait for 180 seconds    to adjust the amount of keys scanned before bitcrack killed, restarted, incremented<br>
tested with RTX3060TI 50% power giving 525 million/sec and about 240 billion keys in 180 seconds before restart and incrementing<br> 
time.sleep(10)  # Wait for 10 seconds before restarting is the delay after previous range scan killed.<br> 
python3 run2.py when reaches end of keyspace stops<br>
python3 runloop.py loops back to beginning instead of stopping for another entire random range scan.<br> 
Not tried on Linux or WSL, don't know if kill command will work but you will need to change line <br>
'BitCrack.exe', '-b', '672', '-t', '256', '-p', '256', '--stride', '1', to<br>
'./BitCrack', '-b', '672', '-t', '256', '-p', '256', '--stride', '1', and compile linux version of bitcrack or bitcrack random<br>
non-random version of bitcrack remove -r from code or you get a error. <br>
<b>Random with continue,</b><br>
adjust -b, -t and -p to match your gpu<br>
adjust time.sleep(180)  # Wait for 180 seconds to value of desired run before auto restart with new random keyspace values<br>
delete .pkl file once entire keyspace is scanned to start over<br> 
change increment valye to your desired value default is 100000000000000

If this program helps find your hidden treasures : donations<br>
<b>Bitcoin bc1qus09g0n5jwg79gje76zxqmzt3gpw80dcqspsmm   <br>
Litecoin ltc1q5qtw6fhuqcarv8ysfv7c52gyyfnys3gzlds5s8   </b>
  
 (https://github.com/unclevito2017/Bitcrack-automation/assets/37158637/1e855627-fdf1-4dc3-a5bd-3ee47ef8c3a5)

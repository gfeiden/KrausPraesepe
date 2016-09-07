# Convert the detailed mass track output file from 
# DSEP into a more useable form (remove line breaks).
#
import sys
import fileinput as fi
import numpy as np

files = [f.rstrip('\n') for f in fi.input(sys.argv[1])]

for f in files:
    data = [line for line in fi.input(f)]
    
    head = data[:14] 
    data = data[14:]

    file_out = open(f[:-4] + 'ntrk', 'w')
    print f[:-4] + 'ntrk'
    for line in head:
        file_out.write('# ' + line)

    for i in range(0, len(data) - 6, 6):
        time_step = ''
        for j in range(6):
            time_step += data[i + j].rstrip('\n')
        dtrk = ''.join(time_step)
        dtrk.replace('\\n', '')
        
        file_out.write(dtrk + '\n')
    file_out.close()


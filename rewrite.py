a = 32
b = 4

import time
import os

print(a + b)

with open(__file__, 'r') as f:
    lines = f.read().split('\n')
    val = int(lines[0].split(' = ')[-1])
    new_line = 'a = {}'.format(val+b)
    new_file = '\n'.join([new_line] + lines[1:])

with open(__file__, 'w') as f:
    f.write('\n'.join([new_line] + lines[1:]))

time.sleep(2)
os.system('py {}'.format(__file__))
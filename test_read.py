import time
from astropy.io import ascii

time1 = time.time()
try:
    ascii.read('large_withnewlines', format='ecsv')
except Exception:
    print("Reading failed")
time2 = time.time()
print('With newlines:', time2 - time1)

time3 = time.time()
try:
    ascii.read('large_nonewlines', format='ecsv')
except Exception:
    print("Reading failed")
time4 = time.time()
print('No newlines:  ', time4 - time3)

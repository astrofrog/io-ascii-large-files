with open('large_nonewlines', 'w') as f:
    f.write('a' * 1000000000)

with open('large_withnewlines', 'w') as f:
    f.write(('a' * 100 + '\n') * 10000000)

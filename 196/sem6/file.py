# r - read
# w - write
# a - append, add to the end of the file

f = open('file_to_read', 'r')
lines = list(map(lambda x: x.strip(), f.readlines()))

f.close()

print(lines)

# repr - print with all system symbols
print(repr(lines[0]))
print(repr(lines[0].strip()))

with open('file_to_read', 'r') as f:
    print(f.read())

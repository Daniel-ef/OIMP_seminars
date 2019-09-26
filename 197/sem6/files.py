# r - read
# w - write
f = open('file_to_read', 'r')
lines = f.readlines()

# repr - print string with system symbols
print(repr(lines[0]))
# strip - remove whitespaces, tabs, newlines
print(repr(lines[0].strip()))

# Always close file!
f.close()

# with ... as ... - you don't need to close file.
# File will close if exception will be raised
with open('file_to_read', 'r') as f:
    r = f.read()
    print(r)

import sys

# Get shift value from command line
shift = int(sys.argv[1]) % 26

output = []
count = 0

for line in sys.stdin:
    line = line.upper()
    for ch in line:
        if 'A' <= ch <= 'Z':
            # Shift character
            new_char = chr((ord(ch) - ord('A') + shift) % 26 + ord('A'))
            output.append(new_char)

# Print in blocks of 5 letters, 10 blocks per line
block_count = 0
char_count = 0

for ch in output:
    print(ch, end='')
    char_count += 1

    if char_count == 5:
        print(' ', end='')
        char_count = 0
        block_count += 1

    if block_count == 10:
        print()
        block_count = 0

# Final newline (clean output)
print()
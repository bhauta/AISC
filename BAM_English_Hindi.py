# Bidirectional Associative Memory for English-Hindi word pairs
# Uses fixed-width binary encoding of Unicode character codes.

# Small bilingual training dictionary
pairs = [("DOG", "कुत्ता"), ("CAT", "बिल्ली"), ("SUN", "सूरज")]
english_width = 3 * 8
hindi_width = 5 * 16

def encode_word(word, char_width, max_chars):
    bits = []
    for char in word[:max_chars]:
        value = ord(char)
        for bit in range(char_width - 1, -1, -1):
            bits.append(1 if value & (1 << bit) else 0)
    while len(bits) < char_width * max_chars:
        bits.append(0)
    return bits

def decode_word(bits, char_width, max_chars):
    chars = []
    for i in range(max_chars):
        value = 0
        for j in range(char_width):
            value = value * 2 + bits[i * char_width + j]
        if value != 0:
            chars.append(chr(value))
    return "".join(chars)

# Convert binary patterns to bipolar (-1, +1) and train weight matrix
eng_patterns = []
hin_patterns = []
for english, hindi in pairs:
    eng = encode_word(english, 8, 3)
    hin = encode_word(hindi, 16, 5)
    eng_patterns.append([1 if bit == 1 else -1 for bit in eng])
    hin_patterns.append([1 if bit == 1 else -1 for bit in hin])

weights = [[0 for j in range(hindi_width)] for i in range(english_width)]
for p in range(len(pairs)):
    for i in range(english_width):
        for j in range(hindi_width):
            weights[i][j] += eng_patterns[p][i] * hin_patterns[p][j]

# Forward recall: English -> Hindi
english_test = "DOG"
input_bits = encode_word(english_test, 8, 3)
input_bipolar = [1 if bit == 1 else -1 for bit in input_bits]
output = []
for j in range(hindi_width):
    total = 0
    for i in range(english_width):
        total += input_bipolar[i] * weights[i][j]
    output.append(1 if total >= 0 else -1)
output_binary = [1 if value == 1 else 0 for value in output]
print("English:", english_test)
print("Hindi recall:", decode_word(output_binary, 16, 5))

# Reverse recall: Hindi -> English
hindi_test = "बिल्ली"
hindi_bits = encode_word(hindi_test, 16, 5)
hindi_bipolar = [1 if bit == 1 else -1 for bit in hindi_bits]
reverse = []
for i in range(english_width):
    total = 0
    for j in range(hindi_width):
        total += hindi_bipolar[j] * weights[i][j]
    reverse.append(1 if total >= 0 else -1)
reverse_binary = [1 if value == 1 else 0 for value in reverse]
print("Hindi:", hindi_test)
print("English recall:", decode_word(reverse_binary, 8, 3))

# Theory: BAM stores paired patterns in a weight matrix and recalls one side
# from the other. This tiny dictionary is illustrative; collisions can occur.

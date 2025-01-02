def all_variants(text):
    for length in range(1, len(text) + 1):
        for start_pos in range(0, len(text)):
            if start_pos + length <= len(text):
                yield text[start_pos:start_pos + length]


a = all_variants("abc")

for i in a:
    print(i)

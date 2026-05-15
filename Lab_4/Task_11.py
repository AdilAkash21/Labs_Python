# Caesar Cipher


text = "hello world!"
shift = 3

alphabet = list("abcdefghijklmnopqrstuvwxyz")

result = ""

for ch in text:

    found = False

    for i in range(len(alphabet)):

        if ch == alphabet[i]:

            new_index = (i + shift) % 26

            result += alphabet[new_index]

            found = True
            break

    if not found:
        result += ch

print(result)


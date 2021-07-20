import os, json

signatures = []
unique = []

alpha_num = {'z': 0, 'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8, 'i': 9, 'j': 10, 'k': 11, 'l': 12, 'm': 13, 'n': 14, 'o': 15, 'p': 16, 'q': 17, 'r': 18, 's': 19, 't': 20, 'u': 21, 'v': 22, 'w': 23, 'x': 24, 'y': 25}
# print (dict(zip(alpha_num.values(), alpha_num.keys())))

DATA_FILE = "words_alpha.txt"

f = open(DATA_FILE, "r")
lines = f.readlines()
f.close()

if not os.path.exists("Files"):
    os.mkdir("Files")

os.chdir("Files")

def get_sig(word):
    word = list(word)
    adjusted_signature = [alpha_num[i] for i in word]
    start = adjusted_signature[0]
    common_signature = ("".join([f"-{(26 + (i - start)) % 26}" for i in adjusted_signature]))[1:]
    return [common_signature, start]

# if you want words instead of signatures
# def add_word(file_num, word):
#     with open(f"{file_num}.txt", "a") as f:
#         f.write(word)

def add_signature(file_num, signature_details):
    with open(f"{file_num}.txt", "a") as f:
        f.write(f"{signature_details[0]} - {signature_details[1]}\n")

for word in lines:
    # add_word(len(word.strip()), word)
    signature = get_sig(word.strip())
    add_signature(len(word.strip()), get_sig(word.strip()))
    
    if signature[0] in signatures and signature[0] not in unique:
        unique.append(signature[0])
    elif signature[0] not in signatures:
        signatures.append(signature[0])

with open('Unique_Signatures.json', 'w') as database:
    json.dump(unique, database)



import time, os, re
import pandas as pd

alpha_num = {
    0: "z",
    1: "a",
    2: "b",
    3: "c",
    4: "d",
    5: "e",
    6: "f",
    7: "g",
    8: "h",
    9: "i",
    10: "j", 
    11: "k",
    12: "l",
    13: "m",
    14: "n",
    15: "o",
    16: "p",
    17: "q",
    18: "r",
    19: "s",
    20: "t",
    21: "u",
    22: "v",
    23: "w",
    24: "x",
    25: "y"
}

def get_word(signature, turns):
    index = [(int(i) + turns) % 26 for i in re.findall(r"\d+", signature)]
    word = "".join([alpha_num[i] for i in index])
    return word

def add_transformers(data):
    if not os.path.exists("Transformers"):
        os.mkdir("Transformers")
    os.chdir("Transformers")

    df = pd.DataFrame(data)
    df.to_csv("Caesar_s Wheel Transformers.csv", index = False)
    os.chdir("..")

data = {
    "Signature": [],
    "Turn": [],
    "Word": [],
    "Length": [], 
    "Signature Commonality": []
}

os.chdir("Files")
unique_signatures = pd.read_json("Unique_Signatures.json")[0]

for signature in unique_signatures:
    length = len(re.findall(r"\d+", signature))

    with open(f"{length}.txt") as f:
        text = "".join(f.readlines())

    pattern = re.compile(r"\b%s - (\d+)\b" % signature)
    matches = pattern.finditer(text)

    indexes = [match.group(1) for match in matches]
    commonality = len(indexes)

    for index in indexes:
        index = int(index)
        word = get_word(signature, index)

        # Add to dictionary
        data["Signature"].append(signature)
        data["Turn"].append(index)
        data["Word"].append(word)
        data["Length"].append(length)
        data["Signature Commonality"].append(commonality)

add_transformers(data)


# Would've been nice if I know how to put nested dictionaries in pandas

# Transformations = {
#     "word" : {
#         "Morphs" : ["Word", "Also another word"],
#         "Turns" : [12, 12]
#     },
#     "word1" : {
#         "Morphs" : ["Word", "Also another word"],
#         "Turns" : [12, 12]
#     },
#     "word223" : {
#         "Morphs" : ["Word", "Also another word"],
#         "Turns" : [12, 12]
#     },
#     "word234" : {
#         "Morphs" : ["Word", "Also another word"],
#         "Turns" : [12, 12]
#     }
# }

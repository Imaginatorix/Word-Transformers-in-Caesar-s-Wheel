# Word-Transformers-in-Caesar-s-Wheel
Find word transformers in Caesar's Wheel. 

What are Word Transformers?
- Word transformers are words that, when placed on the Caesar's Wheel and is then encrypted, the encrypted word is still a word in a dictionary.

Words are separated by their lengths for easier look-up, and then based on their signatures, which are the patterns of the words where the first letter is always zero, that have more that one respective word, look it up and place it in a pandas table. Meaning that words with same signatures are co-transformers (they can switch into one another in a Caesar's Wheel).

The code for the length separation is painfully slow and ineffecient though... it needs to be improved, by a lot. The time it takes to finish took hours.

Note to self:
It would also be nice to have it in this fashion.
'''
Transformations = {
    "word" : {
        "Morphs" : ["Word", "Also another word"],
        "Turns" : [12, 12]
    },
    "word1" : {
        "Morphs" : ["Word", "Also another word"],
        "Turns" : [12, 12]
    },
    "word223" : {
        "Morphs" : ["Word", "Also another word"],
        "Turns" : [12, 12]
    },
    "word234" : {
        "Morphs" : ["Word", "Also another word"],
        "Turns" : [12, 12]
    }
}
'''


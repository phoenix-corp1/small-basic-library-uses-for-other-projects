#importing spell checker library
from spellchecker import SpellChecker

spell = SpellChecker()

#finding words misspelled
element= input("THE SENTENCE IS:")
element1 = element.split()
misspelled = spell.unknown(element1)

for word in misspelled:
    print(spell.correction(word))

for word in misspelled:
    print(spell.candidates(word))
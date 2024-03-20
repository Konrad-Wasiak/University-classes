import string
tekst = input("Wpisz proszę jakiś tekst.\n").lower()

punctuation = 0
letters = 0
spaces = 0
quantities = [punctuation, letters, spaces]

letter_frequencies = {}
# lower() - małe i wielkie litery w string.ascii_letters są oddzielnie
# set() - wykluczanie powtórzeń z powodu lower()
# list() konwertowanie z powrotem na listę, żeby mieć sensowną indeksowalność
for letter in list(set(string.ascii_letters.lower())):
    letter_frequencies[letter] = 0

for char in tekst:
    if char in string.punctuation:
        quantities[0] += 1
    if char in string.ascii_letters:
        quantities[1] += 1
    if char == ' ':
        quantities[2] += 1

    for letter, letter_frequency in letter_frequencies.items():
        if char == letter:
            letter_frequency += 1
            letter_frequencies[letter] = letter_frequency

print(
    f'Liczba liter: {quantities[1]}\nLiczba znaków interpunkcyjnych: {quantities[0]}\nLiczba spacji: {quantities[2]}\nLiczba wyrazów: {quantities[2]+2}'
)
print(
    f'-------------------\nWystąpienia poszczególnych liter:'
)
for letter, letter_frequency in letter_frequencies.items():
    print(letter + ': ' + str(letter_frequency))
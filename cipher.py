"""
Some simple ciphers for teaching the kids.
"""

# Global variables
CODEABLE_LETTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def codeable_letters(text: str):
    """
    Generator for codeable letters in the provided text
    """
    pos = 0
    while pos < len(text):
        letter = text[pos].upper()
        if letter in CODEABLE_LETTERS:
            yield letter
        pos += 1


def encode_shift_cipher(message: str, key=0, encode=True):
    """
    Encode the message with the shift cipher
    """
    if not encode:
        key *= -1

    shifted_letters = list(
        chr((ord(letter) - ord("A") + key) % (ord("Z") - ord("A") + 1) + ord("A"))
        for letter in CODEABLE_LETTERS
        )

    return "".join(
        shifted_letters[CODEABLE_LETTERS.find(letter)]
        if letter in CODEABLE_LETTERS
        else letter
        for letter in message.upper()
    )


def encode_book_cipher(message: str, text: str, encode=True):
    """
    Encode the message with a book cipher
    """
    text_letters = codeable_letters(text)

    return "".join(
        encode_shift_cipher(letter, CODEABLE_LETTERS.find(next(text_letters)), encode)
        if letter in CODEABLE_LETTERS
        else letter
        for letter in message.upper()
    )
    

#=== Test code ===#

BOOK_TEXT = """
The problem with using a number as a key is that it's actually very easy
to crack the code.  All that needs to be done is to guess one number and,
since there are only 26 possible keys, that doesn't take long (especially
for a computer). Using a book cipher makes it almost impossible to crack,
because the key changes for every letter.  The only problem is that both
people need to have the same book (or text) and it must remain a secret.
"""

MESSAGE = """
This is a test!
Hello
"""

CODED_MESSAGE = """
MOMH ZG B EIEP!
"""

CODED_MESSAGE = """
MOMH ZG B EIEP!
PXSFG
"""

# Clean up the leading/trailing whitespace
MESSAGE = MESSAGE.strip()
CODED_MESSAGE = CODED_MESSAGE.strip()


# Test encoding
print(encode_book_cipher(MESSAGE, BOOK_TEXT))

# Test decoding
print(encode_book_cipher(CODED_MESSAGE, BOOK_TEXT, False))


# We're done
print("\nDone")

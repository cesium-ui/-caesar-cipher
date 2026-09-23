# Caesar Cipher

A simple command-line Caesar cipher encoder written in Python. Shifts each letter in a word or sentence by a given amount, wrapping around the alphabet, while leaving spaces and punctuation untouched.

## Features

- Shifts letters by any integer amount (including values larger than 26)
- Wraps around the alphabet correctly (e.g. `z` shifted by 1 becomes `a`)
- Preserves spaces, punctuation, and other non-letter characters as-is
- Validates shift input and re-prompts until a valid number is entered

## Usage

Run the script and follow the prompts:

```bash
python caesar_cipher.py
```

Example:

```
Enter a word: hello world
Amount to shift by: 3
khoor zruog
```

## How it works

Each letter's position in the alphabet is calculated using `ord()`, shifted by the given amount, and wrapped using modulo 26 so shifts of any size stay within `a`-`z`. Non-letter characters are printed unchanged.

## Possible improvements

- Add a decode/decrypt mode (negative shift)
- Support uppercase letters without lowercasing the whole input
- Accept the word and shift as command-line arguments instead of prompts

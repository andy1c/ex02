def encode_char(char: str) -> str: 
    """Given a string, return encoded version."""
    lowerChar: str = char.lower()
    ascii: int = ord(lowerChar)
    normalize: int = ascii - ord("a")
    encode_char: int = ((normalize + 1) % 26) + ord("a")
    cipher: str = chr(encode_char)
    return (cipher)


def encode_str(chars: str) -> str:
    """Given strings, return encoded version."""
    encode_first: str = encode_char(chars[0])
    encode_second: str = encode_char(chars[1])
    encode_third: str = encode_char(chars[2])
    encode_fourth: str = encode_char(chars[3])
    return (encode_first + encode_second + encode_third + encode_fourth)


def decode_char(coded_letter: str) -> str:
    """Given a code, return original"""
    letter: str = coded_letter.lower()
    ascii_code: int = ord(letter)
    normalized_code: int = ascii_code - 97
    decoded_code: int = (normalized_code - 1) % 26 + 97
    decoded_character: str = chr(decoded_code)
    return decoded_character


def decode_str(coded_letter: str) -> str:
    """Given mulitple codes, return originals"""
    decode_first: str = decode_char(coded_letter[0])
    decode_second: str = decode_char(coded_letter[1])
    decode_third: str = decode_char(coded_letter[2])
    decode_fourth: str = decode_char(coded_letter[3])
    return (decode_first + decode_second + decode_third + decode_fourth)
    
    





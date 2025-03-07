VARIATION_SELECTOR_START = 0xFE00
VARIATION_SELECTOR_END = 0xFE0F
VARIATION_SELECTOR_SUPPLEMENT_START = 0xE0100
VARIATION_SELECTOR_SUPPLEMENT_END = 0xE01EF
END_MARKER = chr(0xFE0F)
MAX_TEXT_LENGTH = 255  # Define max length explicitly

# Precompute lookup tables for decoding to speed up lookups
VARIATION_TO_BYTE = {
    code_point: code_point - VARIATION_SELECTOR_START
    for code_point in range(VARIATION_SELECTOR_START, VARIATION_SELECTOR_END + 1)
} | {
    code_point: code_point - VARIATION_SELECTOR_SUPPLEMENT_START + 16
    for code_point in range(VARIATION_SELECTOR_SUPPLEMENT_START, VARIATION_SELECTOR_SUPPLEMENT_END + 1)
}

def to_variation_selector(byte: int) -> str:
    """Converts a byte (0-255) into a variation selector character."""
    if byte < 16:
        return chr(VARIATION_SELECTOR_START + byte)
    if byte < 256:
        return chr(VARIATION_SELECTOR_SUPPLEMENT_START + (byte - 16))
    raise ValueError(f"Byte out of range: {byte}")

def from_variation_selector(code_point: int) -> int | None:
    """Converts a variation selector character back into a byte using lookup table."""
    return VARIATION_TO_BYTE.get(code_point)

def encode(emoji: str, text: str) -> str:
    """Encodes text into an emoji sequence using variation selectors."""
    text_bytes = text.encode("utf-8")
    
    if len(text_bytes) > MAX_TEXT_LENGTH:
        raise ValueError(f"Text exceeds {MAX_TEXT_LENGTH} bytes")

    selectors = "".join(to_variation_selector(byte) for byte in text_bytes)
    encoded_text = emoji + selectors + END_MARKER
    return encoded_text

def decode(text: str) -> str:
    """Decodes an emoji variation sequence back into text."""
    decoded_bytes = [
        byte for char in text 
        if (byte := from_variation_selector(ord(char))) is not None
    ]
    
    # Convert bytes to string and remove any trailing END_MARKER character
    result = bytes(decoded_bytes).decode("utf-8")
    if result and result[-1] == chr(0xFE0F):
        result = result[:-1]
    
    return result

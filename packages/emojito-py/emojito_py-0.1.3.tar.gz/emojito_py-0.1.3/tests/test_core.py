from emojito import encode, decode

def clean_decoded(text):
    """Helper function to remove the end marker if present"""
    if text and text[-1] == '\x0f':
        return text[:-1]
    return text

def test_encode_decode():
    """Test that encoding and then decoding returns the original message"""
    original_message = "Hello, world!"
    emoji = "🍹"
    encoded = encode(emoji, original_message)
    decoded = clean_decoded(decode(encoded))
    assert decoded == original_message

def test_encode_with_different_emojis():
    """Test encoding with different emoji carriers"""
    message = "Secret message"
    emojis = ["😀", "🚀", "🐱", "🌈", "🍕"]
    
    for emoji in emojis:
        encoded = encode(emoji, message)
        # Check that encoded starts with the emoji
        assert encoded.startswith(emoji)
        # Check that decoding works
        assert clean_decoded(decode(encoded)) == message
    
def test_empty_message():
    """Test encoding an empty message"""
    emoji = "🍹"
    encoded = encode(emoji, "")
    assert encoded.startswith(emoji)
    assert clean_decoded(decode(encoded)) == ""
    
def test_long_message():
    """Test with a longer message"""
    emoji = "🍹"
    message = "This is a much longer message that tests the capacity of the encoding system to handle paragraphs of text rather than just short messages."
    encoded = encode(emoji, message)
    decoded = clean_decoded(decode(encoded))
    assert decoded == message

def test_max_length():
    """Test message at max length boundary"""
    emoji = "🍹"
    message = "x" * 255  # MAX_TEXT_LENGTH from core.py
    encoded = encode(emoji, message)
    decoded = clean_decoded(decode(encoded))
    assert decoded == message

def test_exceeds_max_length():
    """Test that exceeding max length raises an error"""
    emoji = "🍹"
    message = "x" * 256  # Exceeds MAX_TEXT_LENGTH
    with pytest.raises(ValueError):
        encode(emoji, message)

def test_special_characters():
    """Test encoding/decoding with special characters"""
    message = "Hello 🌍! Special chars: ñ, é, 漢字"
    emoji = "🍹"
    encoded = encode(emoji, message)
    decoded = clean_decoded(decode(encoded))
    assert decoded == message

def test_multi_emoji_carrier():
    """Test using multiple emojis as a single carrier"""
    carrier = "🔥🍋🌳"
    message = "hidden in plain sight"
    
    encoded = encode(carrier, message)
    assert encoded.startswith(carrier)
    
    decoded = clean_decoded(decode(encoded))
    assert decoded == message

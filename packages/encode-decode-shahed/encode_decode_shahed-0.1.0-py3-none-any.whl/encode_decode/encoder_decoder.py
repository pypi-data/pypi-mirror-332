import base64

def encode_text(text: str) -> str:
    """Encodes a string using Base64 encoding."""
    encoded_bytes = base64.b64encode(text.encode("utf-8"))
    return encoded_bytes.decode("utf-8")

def decode_text(encoded_text: str) -> str:
    """Decodes a Base64 encoded string."""
    decoded_bytes = base64.b64decode(encoded_text.encode("utf-8"))
    return decoded_bytes.decode("utf-8")

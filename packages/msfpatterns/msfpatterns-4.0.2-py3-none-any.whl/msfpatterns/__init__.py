import itertools
import string
import struct


def generate_pattern(length: int) -> str:
    """Generate a unique cyclic pattern (like Metasploit's pattern_create)"""
    pattern = "".join(
        "".join(x)
        for x in itertools.product(
            string.ascii_uppercase, string.ascii_lowercase, string.digits
        )
    )
    return (pattern * ((length // len(pattern)) + 1))[:length]


def find_offset(value: str, length: int) -> list[int] | None:
    """Find the offset of a value inside a cyclic pattern."""
    pattern = generate_pattern(length)
    pattern_bytes = pattern.encode()

    if value.startswith("0x"):
        hex_length = len(value) - 2
        hex_packing_map = {4: "<H", 8: "<I", 16: "<Q"}
        if hex_length not in hex_packing_map:
            raise ValueError(
                "Hex value must be exactly 4, 8, or 16 hex digits (2, 4, or 8 bytes)."
            )
        try:
            value_bytes = struct.pack(hex_packing_map[hex_length], int(value, 16))
        except ValueError:
            raise ValueError("Invalid hexadecimal input format.")
    elif len(value) in (2, 4, 8):
        value_bytes = value.encode()
    else:
        raise ValueError(
            "Input must be a 2-character, 4-character, or 8-character string or hexadecimal equivalent."
        )

    offsets = []
    start = 0
    while start < len(pattern_bytes):
        found_at = pattern_bytes.find(value_bytes, start)
        if found_at == -1:
            break
        offsets.append(found_at)
        start = found_at + 1

    return offsets if offsets else None

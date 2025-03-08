"""The Core Functions of "TurboCLI" """
def hexdump(data: bytes, undef: str = ".") -> str:
    """Generate a hex dump of binary data in a hex editor-like format.

    Parameters
    ----------
    data : bytes
        The binary data to be represented in hex dump format.
    undef : str, optional
        The character to use for non-printable bytes in the ASCII representation (default is '.').

    Returns
    -------
    str
        A formatted string displaying:
        - Byte offsets in hexadecimal (leftmost column).
        - Byte values in hexadecimal (middle section).
        - ASCII representation of printable characters (rightmost section).

    Examples
    --------
    >>> data = b'Hello, world!'
    >>> print(hexdump(data))
              00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F  Decoded Text
    00000000  48 65 6C 6C 6F 2C 20 77  6F 72 6C 64 21           Hello, world!

    >>> binary_data = bytes([0x00, 0x01, 0x02, 0x41, 0x42, 0x43, 0x7F, 0x80, 0xFF])
    >>> print(hexdump(binary_data, undef="?"))
              00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F  Decoded Text
    00000000  00 01 02 41 42 43 7F 80  FF                      ???ABC???

    Notes
    -----
    - Non-printable ASCII characters (outside the range 32-126) are replaced by `undef`.
    - Each line shows up to 16 bytes of data.
    - The hex dump format mimics the layout of common hex editors.
    """
    width = 16  # Number of bytes per line
    lines = []

    # Fix: Avoid nested f-strings
    hex_header = " ".join(f"{i:02X}" for i in range(width))
    header = f"{' ' * 10}{hex_header}  Decoded Text"

    lines.append(header)

    for i in range(0, len(data), width):
        chunk = data[i:i + width]
        hex_part = " ".join(f"{b:02X}" for b in chunk)  # Convert bytes to hex
        ascii_part = "".join(chr(b) if 32 <= b <= 126 else undef for b in chunk)  # Convert to ASCII
        lines.append(f"{i:08X}  {hex_part:<47}  {ascii_part}")

    return "\n".join(lines)

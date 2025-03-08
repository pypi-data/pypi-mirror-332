import unittest
from turbocli import hexdump

class TestHexDump(unittest.TestCase):

    def test_hexdump_basic(self):
        data = b'Hello, world!'
        expected_output = """          00 01 02 03 04 05 06 07 08 09 0A 0B 0C 0D 0E 0F  Decoded Text\n00000000  48 65 6C 6C 6F 2C 20 77 6F 72 6C 64 21           Hello, world!"""
        self.assertEqual(hexdump(data), expected_output)

    def test_hexdump_special_chars(self):
        data = bytes([0x00, 0x01, 0x02, 0x41, 0x42, 0x43, 0x7F, 0x80, 0xFF])
        expected_output = """          00 01 02 03 04 05 06 07 08 09 0A 0B 0C 0D 0E 0F  Decoded Text\n00000000  00 01 02 41 42 43 7F 80 FF                       ...ABC..."""
        self.assertEqual(hexdump(data, undef="."), expected_output)

    def test_hexdump_empty(self):
        self.assertEqual(hexdump(b''), "          00 01 02 03 04 05 06 07 08 09 0A 0B 0C 0D 0E 0F  Decoded Text")

    def test_hexdump_custom_undef(self):
        data = b'\x00\xFF\x41\x42\x43'
        expected_output = """          00 01 02 03 04 05 06 07 08 09 0A 0B 0C 0D 0E 0F  Decoded Text\n00000000  00 FF 41 42 43                                   ??ABC"""
        self.assertEqual(hexdump(data, undef="?"), expected_output)

if __name__ == "__main__":
    unittest.main()

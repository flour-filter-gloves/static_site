from block_to_block_type import BlockType, block_to_block_type
import unittest

class test(unittest.TestCase):
    def test_heading(self):
        self.assertEqual(block_to_block_type("### HEADING"), BlockType.HEADING)

    def test_code(self):
        self.assertEqual(block_to_block_type("```CODE```"), BlockType.CODE)

    def test_quote(self):
        
        self.assertEqual(block_to_block_type("""
                                             >HEADING
                                             >SOME AWESOME STUFF.
                                             >EVEN MORE STUFF.
                                             """), BlockType.QUOTE)
    def test_unordered_list(self):
        
        self.assertEqual(block_to_block_type("""
                                             - HEADING
                                             - SOME AWESOME STUFF.
                                             - EVEN MORE STUFF.
                                             """), BlockType.UNORDERED_LIST)
    def test_unordered_list(self):
        
        self.assertEqual(block_to_block_type("""
                                             1. HEADING
                                             2. SOME AWESOME STUFF.
                                             3. EVEN MORE STUFF.
                                             """), BlockType.ORDERED_LIST)
    def test_paragraph(self):
        

        self.assertEqual(block_to_block_type("""
                                              3. HEADING
                                              1. SOME AWESOME STUFF.
                                              EVEN MORE STUFF.
                                             """), BlockType.PARAGRAPH)
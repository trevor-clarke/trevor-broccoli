import unittest
from ttl_parser import TTLParser
from ttl_tokenizer import TokenType

class TestTTLParser(unittest.TestCase):
    def setUp(self):
        self.parser = TTLParser()

    def basic_parse(self):
        tokens = [
            (TokenType.STRING, "Test"),
            (TokenType.OPENER, "("),
            (TokenType.STRING, "title"),
            (TokenType.OPENER, ":"),
            (TokenType.STRING, "hello"),
            (TokenType.CLOSER, ")")
        ]

        tree = self.parser.parse(tokens)

        self.assertEqual(tree.root.name, "root")



if __name__ == "__main__":
    unittest.main()
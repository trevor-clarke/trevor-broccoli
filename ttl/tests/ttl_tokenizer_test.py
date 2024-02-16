import unittest
from ttl_tokenizer import Tokenizer, TOKENS, ALL_TOKENS

class TestTokenizer(unittest.TestCase):
    def test_next_token(self):
        content = '[Hello, World]->{Python: "OpenAI"}'
        tokenizer = Tokenizer(content)

        self.assertEqual(tokenizer.next_token(), ("OPENER", "["))
        self.assertEqual(tokenizer.next_token(), ("STRING", "Hello"))
        self.assertEqual(tokenizer.next_token(), ("COMMA", ","))
        self.assertEqual(tokenizer.next_token(), ("STRING", "World"))
        self.assertEqual(tokenizer.next_token(), ("CLOSER", "]"))
        self.assertEqual(tokenizer.next_token(), ("ARROW", "->"))
        self.assertEqual(tokenizer.next_token(), ("OPENER", "{"))
        self.assertEqual(tokenizer.next_token(), ("STRING", "Python"))
        self.assertEqual(tokenizer.next_token(), ("OPENER", ":"))
        self.assertEqual(tokenizer.next_token(), ("QUOTE", "\""))
        self.assertEqual(tokenizer.next_token(), ("STRING", "OpenAI"))
        self.assertEqual(tokenizer.next_token(), ("QUOTE", "\""))
        self.assertEqual(tokenizer.next_token(), ("CLOSER", "}"))
        self.assertEqual(tokenizer.next_token(), ("EOF", None))

    def test_get_tokens(self):
        content = '[Hello, World]->{Python: "OpenAI"}'
        tokenizer = Tokenizer(content)

        expected_tokens = [
            ("OPENER", "["),
            ("STRING", "Hello"),
            ("COMMA", ","),
            ("STRING", "World"),
            ("CLOSER", "]"),
            ("ARROW", "->"),
            ("OPENER", "{"),
            ("STRING", "Python"),
            ("OPENER", ":"),
            ("QUOTE", "\""),
            ("STRING", "OpenAI"),
            ("QUOTE", "\""),
            ("CLOSER", "}"),
        ]

        self.assertEqual(tokenizer.get_tokens(), expected_tokens)

if __name__ == '__main__':
    unittest.main()
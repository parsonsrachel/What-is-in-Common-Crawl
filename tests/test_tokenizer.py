import unittest
import tiktoken
import sqlite3


class TestTokenizer(unittest.TestCase):

    # Tests that the tokenizer returns the correct number of tokens
    def test_string(self):
        encoding = tiktoken.encoding_for_model('gpt-3.5-turbo')
        text = ('The point of "Secret Santa" is to make Christmas shopping easier and to spread around '
                'the spirit of giving to those who you might not normally have on your Christmas list. It involves '
                'a group of people exchanging names for a secret gift exchange. Consider playing "secret Santa" '
                'at your next holiday get together or learn the instructions for a round of the game you have '
                'already been invited to.')
        token_integers = encoding.encode(text)
        num_tokens = len(token_integers)
        self.assertEqual(num_tokens, 77)

    # Tests that empty string returns zero tokens
    def test_zero(self):
        encoding = tiktoken.encoding_for_model('gpt-3.5-turbo')
        text = ""
        token_integers = encoding.encode(text)
        num_tokens = len(token_integers)
        self.assertEqual(num_tokens, 0)

    # Tests that the correct number of tokens is stored in database for random entry
    def test_database(self):
        con = sqlite3.connect('./data/c4_sample.db')
        cur = con.cursor()

        i = 749
        cur.execute("SELECT content, n_tokens FROM c4_sample WHERE rowid = " + str(i))
        row = cur.fetchone()

        text = row[0]
        encoding = tiktoken.encoding_for_model('gpt-3.5-turbo')
        token_integers = encoding.encode(text)
        num_tokens = len(token_integers)

        self.assertEqual(num_tokens, row[1])


if __name__ == '__main__':
    unittest.main()
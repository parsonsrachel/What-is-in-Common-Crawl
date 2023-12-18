import unittest
import pyplexity
import sqlite3


class TestPerplexity(unittest.TestCase):

    # Tests that correct bigrams-bnc perplexity is returned for string
    def test_string_bnc(self):
        model = pyplexity.PerplexityModel.from_str('bigrams-bnc')
        text = ('The point of "Secret Santa" is to make Christmas shopping easier and to spread around '
                'the spirit of giving to those who you might not normally have on your Christmas list. It involves '
                'a group of people exchanging names for a secret gift exchange. Consider playing "secret Santa" '
                'at your next holiday get together or learn the instructions for a round of the game you have '
                'already been invited to.')
        perpl = model.compute_sentence(text)
        self.assertEqual(perpl, 294.87339827872296)

    # Tests that correct bigrams-cord19 perplexity is returned for string
    def test_string_cord19(self):
        model = pyplexity.PerplexityModel.from_str('bigrams-cord19')
        text = ('The point of "Secret Santa" is to make Christmas shopping easier and to spread around '
                'the spirit of giving to those who you might not normally have on your Christmas list. It involves '
                'a group of people exchanging names for a secret gift exchange. Consider playing "secret Santa" '
                'at your next holiday get together or learn the instructions for a round of the game you have '
                'already been invited to.')
        perpl = model.compute_sentence(text)
        self.assertEqual(perpl, 641.5683858718759)

    # Tests that correct bigrams-bnc perplexity is returned for string repeated 3 times, and that the perplexity
    # doesn't triple compared to the single string
    def test_triplet_bnc(self):
        model = pyplexity.PerplexityModel.from_str('bigrams-bnc')
        text = ('The point of "Secret Santa" is to make Christmas shopping easier and to spread around '
                'the spirit of giving to those who you might not normally have on your Christmas list. It involves '
                'a group of people exchanging names for a secret gift exchange. Consider playing "secret Santa" '
                'at your next holiday get together or learn the instructions for a round of the game you have '
                'already been invited to. ')
        sentence = (text + text + text).strip()
        perpl = model.compute_sentence(sentence)
        self.assertEqual(perpl, 274.9141531676184)

    # Tests that correct perplexity is returned for empty string
    def test_empty(self):
        model = pyplexity.PerplexityModel.from_str('bigrams-bnc')
        text = ""
        perpl = model.compute_sentence(text)
        self.assertEqual(perpl, 995016.4982976777)

    # Tests that the correct perplexities is stored in database for random entry
    def test_database(self):
        con = sqlite3.connect('./data/c4_sample.db')
        cur = con.cursor()

        i = 749
        cur.execute("SELECT content, bigrams_bnc, bigrams_cord19 FROM c4_sample WHERE rowid = " + str(i))
        row = cur.fetchone()

        model_bnc = pyplexity.PerplexityModel.from_str('bigrams-bnc')
        model_cord19= pyplexity.PerplexityModel.from_str('bigrams-cord19')

        text = row[0]
        perpl_bnc = model_bnc.compute_sentence(text)
        perpl_cord19 = model_cord19.compute_sentence(text)

        self.assertEqual(perpl_bnc, row[1])
        self.assertEqual(perpl_cord19, row[2])


if __name__ == '__main__':
    unittest.main()
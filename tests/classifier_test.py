import unittest
from whatsincc import google_cloud_lang


class TestGoogleClassifier(unittest.TestCase):

    def test_too_short(self):
        text = "This text is too short to classify."
        self.assertEqual(google_cloud_lang.classify(text), {})

    def test_category(self):
        text = ("This text is about Sports at UMD. The university of Maryland has different sports teams \
                including Football, Soccer, Baseball and Basketball.")
        classification = next(iter(google_cloud_lang.classify(text)))
        self.assertEqual(classification, "/Sports/College Sports")


if __name__ == '__main__':
    unittest.main()

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

    def test_consistency(self):
        text = ("I the south French countryside is the town of Camargue on the largest river delta in Europe known for \
                its iconic pink flamingoes and salt that has been harvested since the Middle Ages. Complete with \
                paddocks overflowing with statuesque white horses & mean looking black bulls rutting in the dust with \
                rippling muscles bred for bull fighting. \
                Bastille Day is the largest public celebration in France, when its citizens celebrate the \
                anniversary of the storming of the Bastille on 14th July 1789. This was the beginning of the \
                end of the French monarchy, launching the French Revolution.")

        classification = google_cloud_lang.classify(text)
        self.assertEqual(classification, google_cloud_lang.classify(text))


if __name__ == '__main__':
    unittest.main()

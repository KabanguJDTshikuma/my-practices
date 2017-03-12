def reverse_words(s):
    return " ".join([word[::-1] for word in s.split(" ")])


from unittest import TestCase


class TestReverseWords(TestCase):
    def test_reverse_words(self):
        self.assertEquals(reverse_words(s))

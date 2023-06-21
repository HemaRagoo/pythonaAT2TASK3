import unittest
from human import Human
from letter import Letter
from letterbox import Letterbox

class TestHuman(unittest.TestCase):
    def setup(self):
        self.alice = Human("Alice", 19, "Female")
        self.bob = Human("Bob", 18, "Male")

    def test_create_letter(self):
        self.alice.create_letter("Hello, Bob!", self.bob)
        self.assertIsNotNone(self.alice.senders_letter)

    def test_read_letter(self):
        self.alice.create_letter("Hello, Bob!", self.bob)
        self.alice.send_letter(self.bob)
        self.bob.read_letter()
        self.assertTrue(self.bob.letterbox.sent_letter.is_read)

class TestLetter(unittest.TestCase):
            def setup(self):
                self.letter = Letter(self.alice, "Hello!", self.bob)

            def letter_exist(self):
                self.assertIsTrue






if __name__ == '__main__':
                    unittest.main()
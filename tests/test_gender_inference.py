import unittest
from src.gender_inference import infer_gender

class TestGenderInference(unittest.TestCase):
    def test_male(self):
        self.assertEqual(infer_gender("He is a good boy."), "male")
    
    def test_female(self):
        self.assertEqual(infer_gender("She is a talented girl."), "female")
    
    def test_neutral(self):
        self.assertEqual(infer_gender("They are an amazing person."), "neutral")
    
    def test_unknown(self):
        self.assertEqual(infer_gender("The dog runs fast."), "unknown")

if __name__ == "__main__":
    unittest.main()

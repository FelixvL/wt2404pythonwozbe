import unittest
import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import LV_stringcontrol

class MyTestCase(unittest.TestCase):
    input_string = 'voorbeeld'
    minimum = 3
    maximum = 10

    def test_correct_string(self):
        result = LV_stringcontrol.valideer_srange(self.input_string, self.minimum, self.maximum)
        self.assertTrue(result)

    def test_incorrect_min_string(self): #Def 'incorrect' omschrijft de testcase verwachte output
        # Given
        minimum = 10
        # When
        result = LV_stringcontrol.valideer_srange(self.input_string, minimum, self.maximum)
        # Then
        self.assertFalse(result)

    def test_incorrect_max_string(self):
        maximum = 3
        result = LV_stringcontrol.valideer_srange(self.input_string, self.minimum, maximum)
        self.assertFalse(result)

    def test_incorrect_string_short(self):
        print("hier zijn we gekomen")
        input_string = 'hi'
        result = LV_stringcontrol.valideer_srange(input_string, self.minimum, self.maximum)
        self.assertFalse(result)
        self.assertEqual(5,5)

    def test_incorrect_string_long(self):
        input_string = 'hiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii'
        result = LV_stringcontrol.valideer_srange(input_string, self.minimum, self.maximum)
        self.assertFalse(result)

if __name__ == '__main__':
    unittest.main()

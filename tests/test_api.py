import unittest

from assesment.api import app


class StringAPITestCase(unittest.TestCase):

    def setUp(self):
        app.testing = True
        self.app = app.test_client()

    def test_no_string_input(self):
        response = self.app.post('/string/', data=dict())
        self.assertFalse(response.json['is_pangram'])

    def test_empty_string_input(self):
        data = {
            "string_input": ""
        }
        response = self.app.post('/string/', data=data)
        self.assertFalse(response.json['is_pangram'])

    def test_non_pangram(self):
        data = {
            "string_input": "testtest"
        }
        response = self.app.post('/string/', data=data)
        self.assertFalse(response.json['is_pangram'])

    def test_pangram(self):
        data = {
            "string_input": ("Farmer jack realized that big yellow "
                             "quilts were expensive")
        }
        response = self.app.post('/string/', data=data)
        self.assertTrue(response.json['is_pangram'])

    def test_pangram_with_special_characters(self):
        data = {
            "string_input": ("@Farmer#@$% jack&* realized that "
                             "big yellow quilts were expensive()*")
        }
        response = self.app.post('/string/', data=data)
        self.assertTrue(response.json['is_pangram'])

    def test_pangram_with_special_characters_and_numbers(self):
        data = {
            "string_input": "1Quick wafting zephyrs vex bold Jim@#%#234235634"
        }
        response = self.app.post('/string/', data=data)
        self.assertTrue(response.json['is_pangram'])


if __name__ == '__main__':
    unittest.main()

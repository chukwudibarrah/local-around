import unittest
from app import create_app

class FareTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client()

    def test_get_fare(self):
        response = self.client.get('/fare?start=LocationA&end=LocationB')
        self.assertEqual(response.status_code, 200)
        self.assertIn('fare', response.json)

if __name__ == '__main__':
    unittest.main()

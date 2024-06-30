import unittest
from app import create_app

class TimetableTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client()

    def test_get_timetable(self):
        response = self.client.get('/timetable?start=LocationA&end=LocationB')
        self.assertEqual(response.status_code, 200)
        self.assertIn('timetable', response.json[0])

if __name__ == '__main__':
    unittest.main()

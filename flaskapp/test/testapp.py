import unittest
from app.app import app  # Importing the Flask app

class FlaskAppTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        """Set up the test client before running tests"""
        app.testing = True
        cls.client = app.test_client()

    def test_home_page(self):
        """Test if the home page loads correctly"""
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Welcome to Flask Web App", response.data)  # Check content

    def test_404_page(self):
        """Test if a non-existing route returns a 404"""
        response = self.client.get('/invalid-url')
        self.assertEqual(response.status_code, 404)

    def test_static_css(self):
        """Test if the CSS file is accessible"""
        response = self.client.get('/static/css/styles.css')
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()

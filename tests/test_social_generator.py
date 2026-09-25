import unittest
from fastapi.testclient import TestClient
from app.api import app

class TestSocialGenerator(unittest.TestCase):
    def setUp(self):
        self.client = TestClient(app)

    def test_social_package(self):
        payload = {"core_concept": "Multi-Agent Systems", "target_audience": "Tech Executives"}
        res = self.client.post("/generate-social-package", json=payload)
        self.assertEqual(res.status_code, 200)
        data = res.json()
        self.assertEqual(len(data["posts"]), 2)
        self.assertIn("Twitter_X", [p["platform"] for p in data["posts"]])

if __name__ == "__main__":
    unittest.main()

import subprocess
import json
import unittest

class TestMemeAPI(unittest.TestCase):
    base_url = 'http://localhost:8000'

    def test_create_meme(self):
        payload = json.dumps({"title": "Test Meme"})
        result = subprocess.run(
            ['curl', '-X', 'POST', f'{self.base_url}/memes', '-H', 'Content-Type: application/json', '-d', payload],
            capture_output=True, text=True
        )
        self.assertEqual(result.returncode, 0)
        response_json = json.loads(result.stdout)
        self.assertEqual(response_json["title"], "Test Meme")

    def test_read_memes(self):
        result = subprocess.run(
            ['curl', f'{self.base_url}/memes'],
            capture_output=True, text=True
        )
        self.assertEqual(result.returncode, 0)
        response_json = json.loads(result.stdout)
        self.assertIsInstance(response_json, list)

    def test_update_meme(self):
        memes = subprocess.run(['curl', f'{self.base_url}/memes'],capture_output=True, text=True)
        meme_id = json.loads(memes.stdout)[0]["id"]
        payload = json.dumps({"title": "Updated Meme"})
        result = subprocess.run(
            ['curl', '-X', 'PUT', f'{self.base_url}/memes/{meme_id}', '-H', 'Content-Type: application/json', '-d', payload],
            capture_output=True, text=True
        )
        self.assertEqual(result.returncode, 0)
        response_json = json.loads(result.stdout)
        self.assertEqual(response_json["title"], "Updated Meme")

    def test_delete_meme(self):
        memes = subprocess.run(['curl', f'{self.base_url}/memes'],capture_output=True, text=True)
        meme_id = json.loads(memes.stdout)[0]["id"]
        result = subprocess.run(
            ['curl', '-X', 'DELETE', f'{self.base_url}/memes/{meme_id}'],
            capture_output=True, text=True
        )
        self.assertEqual(result.returncode, 0)
        response_json = json.loads(result.stdout)
        memes = subprocess.run(['curl', f'{self.base_url}/memes'],capture_output=True, text=True)
        meme_id = json.loads(memes.stdout)[0]["id"]
        self.assertFalse(response_json["id"] == meme_id)

if __name__ == '__main__':
    unittest.main()

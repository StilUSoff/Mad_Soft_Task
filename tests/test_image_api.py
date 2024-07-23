import subprocess
import json
import unittest
import os

class TestImageAPI(unittest.TestCase):
    base_url = 'http://127.0.0.1:8001'
    api_key = 'hDf6GVg8B0813klvs695HVlksd'

    def test_upload_file(self):
        meme_id = 1
        result = subprocess.run(
            ['curl', '-X', 'POST', f'{self.base_url}/image/{meme_id}?api_key={self.api_key}', '-F', f'file=@{FILEPATH}'],
            capture_output=True, text=True
        )
        self.assertEqual(result.returncode, 0)
        response_json = json.loads(result.stdout)
        self.assertIn('file_url', response_json)

    def test_see_file(self):
        meme_id = 1
        command = [
            'curl', f'{self.base_url}/image/{meme_id}?api_key={self.api_key}'
        ]
        result = subprocess.run(
            command,
            capture_output=True
        )
        self.assertEqual(result.returncode, 0)
        with open('test_image_received.jpg', 'wb') as f:
            f.write(result.stdout)

        self.assertTrue(os.path.getsize('test_image_received.jpg') > 0, "Received image is empty")

        os.remove('test_image_received.jpg')


    def test_update_file(self):
        meme_id = 1
        result = subprocess.run(
            ['curl', '-X', 'PUT', f'{self.base_url}/image/{meme_id}?api_key={self.api_key}', '-F', f'file=@{FILEPATH}'],
            capture_output=True, text=True
        )
        self.assertEqual(result.returncode, 0)
        response_json = json.loads(result.stdout)
        self.assertIn('file_url', response_json)

    def test_delete_file(self):
        meme_id = 1
        result = subprocess.run(
            ['curl', '-X', 'DELETE', f'{self.base_url}/image/{meme_id}?api_key={self.api_key}'],
            capture_output=True, text=True
        )
        self.assertEqual(result.returncode, 0)
        response_json = json.loads(result.stdout)
        self.assertIn('Success!', response_json)



if __name__ == '__main__':
    FILEPATH=input("FILEPATH: ")
    unittest.main()

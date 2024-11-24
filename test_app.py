import unittest
from app import app, db, UserModel

class TestFlaskAPI(unittest.TestCase):
    def setUp(self):
        # Configure the app for testing
        app.config['TESTING'] = True
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test_database.db'
        self.client = app.test_client()

        # Create test database
        with app.app_context():
            db.create_all()

    def tearDown(self):
        # Drop test database
        with app.app_context():
            db.drop_all()

    def test_get_users_empty(self):
        # Test GET /greet/ when no users exist
        response = self.client.get('/greet/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, [])

    def test_post_user(self):
        # Test POST /greet/ to add a user
        response = self.client.post('/greet/', json={"message": "Hello", "name": "John"})
        self.assertEqual(response.status_code, 201)
        self.assertEqual(len(response.json), 1)
        self.assertEqual(response.json[0]["name"], "John")
        self.assertEqual(response.json[0]["message"], "Hello")

    def test_get_user_by_id(self):
        # Add a user and test GET /greet/<id>
        self.client.post('/greet/', json={"message": "Hello", "name": "John"})
        response = self.client.get('/greet/1')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json["name"], "John")
        self.assertEqual(response.json["message"], "Hello")

    def test_patch_user(self):
        # Add a user, update them, and verify
        self.client.post('/greet/', json={"message": "Hello", "name": "John"})
        response = self.client.patch('/greet/1', json={"message": "Hi", "name": "John Updated"})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json["name"], "John Updated")
        self.assertEqual(response.json["message"], "Hi")

    def test_delete_user(self):
        # Add a user, delete them, and verify
        self.client.post('/greet/', json={"message": "Hello", "name": "John"})
        response = self.client.delete('/greet/1')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json), 0)

    def test_get_user_not_found(self):
        # Test GET /greet/<id> for non-existent user
        response = self.client.get('/greet/1')
        self.assertEqual(response.status_code, 404)
        self.assertIn("User not found", response.json["message"])

if __name__ == '__main__':
    unittest.main()

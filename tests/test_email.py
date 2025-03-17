import unittest
from src.original_pr import is_valid_email

class TestEmailValidation(unittest.TestCase):
    def test_valid_emails(self):
        self.assertTrue(is_valid_email("test@example.com"))
        self.assertTrue(is_valid_email("user.name+tag@sub.domain.com"))
    
    def test_invalid_emails(self):
        self.assertFalse(is_valid_email("invalid-email"))
        self.assertFalse(is_valid_email("test@.com"))
        self.assertFalse(is_valid_email("@example.com"))
        self.assertFalse(is_valid_email("test..email@example.com"))  # Multiple dots
        self.assertFalse(is_valid_email("test@"))  # Missing domain
        self.assertFalse(is_valid_email("@example.com"))  # Missing local part
        self.assertFalse(is_valid_email("user@com"))  # Invalid domain format

if __name__ == "__main__":
    unittest.main()

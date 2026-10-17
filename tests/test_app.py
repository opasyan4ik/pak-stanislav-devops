import os
import unittest
from unittest.mock import patch

from app.main import student_details, student_message, version_message


class StudentAppTests(unittest.TestCase):
    def test_default_information(self):
        with patch.dict(os.environ, {}, clear=True):
            details = student_details()
        self.assertEqual(details["STUDENT_SURNAME"], "Pak")
        self.assertEqual(details["STUDENT_ID"], "37845")

    def test_environment_overrides(self):
        with patch.dict(os.environ, {"STUDENT_NAME": "Example"}):
            message = student_message()
        self.assertIn("Name: Example", message)

    def test_version_endpoint_value_is_stable(self):
        self.assertEqual(version_message(), "pak-stanislav-devops 1.0\n")


if __name__ == "__main__":
    unittest.main()

import unittest
from SpartaUniversity import Modules
from SpartaUniversity import Batches


class TestSparta(unittest.TestCase):

    def test_module(self):
        module_name = "Not a Sparta module"
        test = Modules(module_name, 3)
        self.assertFalse(test.is_sparta_module())

    def test_name(self):
        student_name = "123456"
        test = Batches("Python", "24th Feb")
        self.assertFalse(test.add_student(student_name))


if __name__ == "__main__":
    unittest.main()

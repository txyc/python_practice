import unittest

class TestCheck01(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("所有用例执行前执行一次")

    @classmethod
    def tearDownClass(cls):
        print("所有用例执行后执行一次")

    def setUp(self) -> None:
        print("每个用例执行前执行一次")

    def tearDown(self) -> None:
        print("每个用例执行后执行一次")

    def test_md01(self):
        print("测试方法001_01")

    def test_md02(self):
        print("测试方法001_02")

if __name__ == "__main__":
    unittest.main(verbosity=2)

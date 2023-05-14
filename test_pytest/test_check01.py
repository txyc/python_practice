import pytest

class Test_Check():
    def setup_class(self):
        print("在所有用例执行前执行\n")

    def teardown_class(self):
        print("在所有用例执行后执行\n")

    def setup(self):
        print("在每个用例执行前执行\n")

    def teardown(self):
        print("在每个用例执行后执行\n")

    def test_check1(self):
        print('hello world')
        assert 1 == 1

    def test_check2(self):
        print('hello world')
        assert 2 == 2

    def test_check3(self):
        print('hello world')
        assert 3 == 1

    def test_check4(self):
        print('hello world')
        assert 14 >= 12

if __name__ == "__main__":
    pytest.main(["-vs"])
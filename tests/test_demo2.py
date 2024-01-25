'''import pytest

@pytest.mark.usefixtures("setup")
class TestExample():

    def test_demo1(self, setup):
        print(setup)
        print("I will execute from the test function")

    @pytest.mark.filterwarnings
    def test_demo2(self, setup):
        print("I will execute from the test function")
        print(setup[0])
        print(setup[1])

    def test_demo3(self, setup):
        print("I will execute from the test function")
        print(setup[0])
        print(setup[1])

    def test_demo4(s
        elf, setup):
        print("I will execute from the test function")
        print(setup[0])
        print(setup[1])'''

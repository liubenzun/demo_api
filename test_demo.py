class TestClass:

    def setup_class(self):
        print("class预处理")

    def test_one(self):
        print("执行一条测试用例")
        x = "this"
        assert "h" in x

    def test_two(self):
        print("执行2条测试用例")
        x = 1
        assert x > 5

    def teardown(self):
        print("teardown")

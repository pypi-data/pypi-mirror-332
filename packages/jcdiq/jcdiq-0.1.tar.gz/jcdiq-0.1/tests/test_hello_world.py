import unittest
from io import StringIO
import sys
from jcdiq.hello_world import say


class TestSayFunction(unittest.TestCase):
    def setUp(self):
        # 重定向标准输出以捕获打印输出
        self.held, sys.stdout = sys.stdout, StringIO()

    def tearDown(self):
        # 恢复标准输出
        sys.stdout = self.held

    def test_say_PrintsHelloWorld(self):
        say()
        output = sys.stdout.getvalue().strip()
        self.assertEqual(output, "hello world!")


if __name__ == '__main__':
    unittest.main()

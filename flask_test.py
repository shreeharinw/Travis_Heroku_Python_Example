import unittest
import hello_world_flask

class TestStringMethods(unittest.TestCase):

    def testHelloWorld(self):
        self.assertEqual(hello_world_flask.hello_world("FOO"), 'Hello, World!FOO')
    
if __name__ == '__main__':
    unittest.main()
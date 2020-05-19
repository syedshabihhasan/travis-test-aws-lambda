from unittest import TestCase
from mytestlambda import myfunction_handler


class TestMyTestLambda(TestCase):

    def test_mylambda(self):
        value = myfunction_handler(None, None)
        self.assertDictEqual(value, {'statusCode': 200, 'body': 'This is a successful message'})

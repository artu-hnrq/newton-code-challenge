import unittest

def suite():
    return unittest.TestLoader().discover('test', pattern='*.py')

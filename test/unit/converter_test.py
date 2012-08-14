import os
import sys
if sys.version_info < (2, 7):
    import unittest2 as unittest
else:
    import unittest

pkg_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
sys.path.insert(0, pkg_path)
import mcider.converter as converter
import mcider.util as util

test_path = os.path.join(pkg_path, 'test')

class ConverterTest(unittest.TestCase):

    def setUp(self):
        self.html = util.fs_reader(os.path.join(test_path, 'fixtures', 'slide.md'))
        self.slide = converter.Slide(self.html, 'io2012')

    def test_set_theme(self):
        self.assertEqual(self.slide.theme, 'io2012')

    def test_get_slide(self):
        self.assertIsNotNone(self.slide._get_slide())
        #print self.slide._get_slide().encode('utf-8')

if __name__ == '__main__':
    unittest.main()

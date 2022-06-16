import unittest
from flatex import parse_args

class TestParse(unittest.TestCase):
    def test_verbose(self):
        args = parse_args(['-v', 'test.txt'])
        self.assertTrue(args.verbose)

        args = parse_args(['test.txt'])
        self.assertFalse(args.verbose)

    def test_quiet(self):
        args = parse_args(['-q', 'test.txt'])
        self.assertTrue(args.quiet)

        args = parse_args(['test.txt'])
        self.assertFalse(args.quiet)

    def test_bib(self):
        args = parse_args(['-b', 'test.txt'])
        self.assertTrue(args.b)

        args = parse_args(['test.txt'])
        self.assertFalse(args.b)




if __name__ == '__main__':
    unittest.main()
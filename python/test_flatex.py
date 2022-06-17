import unittest
from flatex import get_included_file_name, parse_args


class TestParse(unittest.TestCase):
    def test_verbose(self):
        args = parse_args(["-v", "test.txt"])
        self.assertTrue(args.verbose)

        args = parse_args(["test.txt"])
        self.assertFalse(args.verbose)

    def test_quiet(self):
        args = parse_args(["-q", "test.txt"])
        self.assertTrue(args.quiet)

        args = parse_args(["test.txt"])
        self.assertFalse(args.quiet)

    def test_bib(self):
        args = parse_args(["-b", "test.txt"])
        self.assertTrue(args.b)

        args = parse_args(["test.txt"])
        self.assertFalse(args.b)


class TestIncludedFileName(unittest.TestCase):
    def test_simple_case(self):
        res = get_included_file_name(r"\input{file}")
        self.assertEqual("file.tex", res)

        res = get_included_file_name(r"    \input{file}")
        self.assertEqual("file.tex", res)

        res = get_included_file_name(r"    \input{file} %comment")
        self.assertEqual("file.tex", res)


    def test_error_case(self):
        res = get_included_file_name(r"file")
        self.assertEqual("", res)



if __name__ == "__main__":
    unittest.main()

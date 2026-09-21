import os
import subprocess
import sys
import unittest

from acronymMaker import makeAcronym

repoRoot = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
scriptPath = os.path.join(repoRoot, "acronymMaker.py")


class TestAcronymMaker(unittest.TestCase):
	def test_multi_word_input_yields_initials(self):
		self.assertEqual(makeAcronym("Hello World Foo"), "HWF")

	def test_case_of_each_initial_is_preserved(self):
		# "(Case Sensitive)" is the advertised behavior: no upper-casing.
		self.assertEqual(makeAcronym("hello World foo"), "hWf")

	def test_single_word_yields_its_first_character(self):
		self.assertEqual(makeAcronym("Hello"), "H")

	def test_empty_input_yields_empty_acronym(self):
		self.assertEqual(makeAcronym(""), "")

	def test_consecutive_spaces_do_not_raise(self):
		# split(" ") yields an empty field between the spaces; ""[:1] is "".
		self.assertEqual(makeAcronym("a  b"), "ab")

	def test_tab_is_not_treated_as_a_separator(self):
		# Characterizes the current split(" ") behavior tracked by #4.
		self.assertEqual(makeAcronym("a\tb"), "a")

	def test_end_to_end_prompts_prints_acronym_and_exits_cleanly(self):
		# Two newlines feed both input() calls; timeout guards against a hang.
		result = subprocess.run(
			[sys.executable, scriptPath],
			input="Hello World Foo\n\n",
			capture_output=True,
			text=True,
			timeout=10,
		)
		self.assertEqual(result.returncode, 0)
		self.assertEqual(
			result.stdout,
			"Enter what you want to make into an acronym: "
			"Your new acronym is HWF\n"
			"Press 'Enter' to exit the program.",
		)


if __name__ == "__main__":
	unittest.main()

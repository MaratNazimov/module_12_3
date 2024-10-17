import suite_12_3 as m1
import unittest


tests = unittest.TestSuite()

tests.addTest(unittest.TestLoader().loadTestsFromTestCase(m1.RunnerTest))
tests.addTest(unittest.TestLoader().loadTestsFromTestCase(m1.TournamentTest))

tests_run = unittest.TextTestRunner(verbosity=2)
tests_run.run(tests)


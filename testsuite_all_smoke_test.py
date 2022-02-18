import unittest

from losthatsmoketests import LostHatSmokeTests
from lost_hat_tests import LostHatFrontPageTests
from main import Mainautodemo

def smoke_sanity_test():
    test_smoke_sanity = unittest.TestSuite()
    test_smoke_sanity.addTest(unittest.makeSuite(LostHatSmokeTests))
    test_smoke_sanity.addTest(unittest.makeSuite(LostHatFrontPageTests))
    test_smoke_sanity.addTest(unittest.makeSuite(Mainautodemo))
    return test_smoke_sanity

runner = unittest.TextTestRunner(verbosity=2)
runner.run(smoke_sanity_test())

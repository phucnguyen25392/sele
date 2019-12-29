import unittest
import sys
import lib.HTMLTestRunner as HTMLTestRunner
import tests.logintc as logintc
import tests.tokentc as tokentc
import tests.usertc as usertc
import tests.companytc as companytc
import tests.tagtc as tagtc
import tests.campagintc as campagintc
import tests.notificationtc as notificationtc
# setting
from config.setting import *


#----------------------------------------------------------------------
class Test_HTMLTestRunner(unittest.TestCase):

    def test_main(self):
        # Run HTMLTestRunner. Verify the HTML report.
 
        # suite of TestCases
        self.suite = unittest.TestSuite()
        self.suite.addTests([
            unittest.defaultTestLoader.loadTestsFromTestCase(campagintc.Campaign),
            unittest.defaultTestLoader.loadTestsFromTestCase(tagtc.Tag),
            ])

        # Invoke TestRunner
        #buf = StringIO.StringIO()
        #runner = unittest.TextTestRunner(buf)       #DEBUG: this is the unittest baseline
        fp = file( root_dir + '\my_report.html', 'wb')
        runner = HTMLTestRunner.HTMLTestRunner(
                    stream=fp,
                    title='<Realmax Test>',
                    description='This demonstrates the report output by HTMLTestRunner.'
                    )
        runner.run(self.suite)

if __name__ == "__main__":
    if len(sys.argv) > 1:
        argv = sys.argv
    else:
        argv=['test_HTMLTestRunner.py', 'Test_HTMLTestRunner']
    try:
        unittest.main(argv=argv)
    except:
        print "ok"
    
import unittest
import StringIO
import sys
import lib.HTMLTestRunner as HTMLTestRunner
import pageobject.realmaxpage as realmaxpage

from selenium import webdriver

# class PythonOrgSearch(unittest.TestCase):
#     """A sample test class to show how page object works"""

#     def setUp(self):
#         self.driver = webdriver.Chrome('D:\sele\chromedriver.exe')
#         self.driver.get("http://www.python.org")

#     def test_search_in_python_org(self):
#         """
#         Tests python.org search feature. Searches for the word "pycon" then verified that some results show up.
#         Note that it does not look for any particular text in search results page. This test verifies that
#         the results were not empty.
#         """
#         #Load the main page. In this case the home page of Python.org.
#         main_page = page.MainPage(self.driver)
#         #Checks if the word "Python" is in title
#         assert main_page.is_title_matches(), "python.org title doesn't match."
#         #Sets the text of search textbox to "pycon"
#         main_page.search_text_element = "pycon"
#         main_page.click_go_button()
#         search_results_page = page.SearchResultsPage(self.driver)
#         #Verifies that the results page is not empty
#         assert search_results_page.is_results_found(), "No results found."

#     def tearDown(self):
#         self.driver.close()

class RealMax(unittest.TestCase):
      
    def setUp(self):
        self.driver = webdriver.Chrome('D:\sele\chromedriver.exe')
        self.driver.get("https://www.realmax.ga")

    def test_login_realmax(self):
        
        login_page = realmaxpage.LoginPage(self.driver)
        login_page.login('admin@realmax.com', 'abc123')
        login_page.logout()

    def tearDown(self):
        self.driver.close()

# ----------------------------------------------------------------------

def safe_unicode(obj, *args):
    """ return the unicode representation of obj """
    try:
        return unicode(obj, *args)
    except UnicodeDecodeError:
        # obj is byte string
        ascii_text = str(obj).encode('string_escape')
        return unicode(ascii_text)

def safe_str(obj):
    """ return the byte string representation of obj """
    try:
        return str(obj)
    except UnicodeEncodeError:
        # obj is unicode
        return unicode(obj).encode('unicode_escape')

class Test_HTMLTestRunner(unittest.TestCase):

    def test0(self):
        self.suite = unittest.TestSuite()
        buf = StringIO.StringIO()
        runner = HTMLTestRunner.HTMLTestRunner(buf)
        runner.run(self.suite)
        # didn't blow up? ok.
        self.assert_('</html>' in buf.getvalue())

    def test_main(self):
        # Run HTMLTestRunner. Verify the HTML report.

        # suite of TestCases
        self.suite = unittest.TestSuite()
        self.suite.addTests([
            unittest.defaultTestLoader.loadTestsFromTestCase(RealMax),
            ])

        # Invoke TestRunner
        buf = StringIO.StringIO()
        #runner = unittest.TextTestRunner(buf)       #DEBUG: this is the unittest baseline
        fp = file('my_report.html', 'wb')
        runner = HTMLTestRunner.HTMLTestRunner(
                    stream=fp,
                    title='<Demo Test>',
                    description='This demonstrates the report output by HTMLTestRunner.'
                    )
        runner.run(self.suite)

        # Define the expected output sequence. This is imperfect but should
        # give a good sense of the well being of the test.
        EXPECTED = u"""
Demo Test

>RealMax:
>test_login_realmax
>pass

</html>
"""
        # check out the output
        byte_output = buf.getvalue()
        # output the main test output for debugging & demo
        print byte_output
        # HTMLTestRunner pumps UTF-8 output
        output = byte_output.decode('utf-8')
        self._checkoutput(output,EXPECTED)


    def _checkoutput(self,output,EXPECTED):
        i = 0
        for lineno, p in enumerate(EXPECTED.splitlines()):
            if not p:
                continue
            j = output.find(p,i)
            if j < 0:
                self.fail(safe_str('Pattern not found lineno %s: "%s"' % (lineno+1,p)))
            i = j + len(p)


if __name__ == "__main__":
    if len(sys.argv) > 1:
        argv = sys.argv
    else:
        argv=['test_HTMLTestRunner.py', 'Test_HTMLTestRunner']
    unittest.main(argv=argv)
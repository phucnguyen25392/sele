import platform
###############################
##  Define global variables ###
###############################

#realmax_stag_url = 'https://realmax.ga'
#realmax_pro_url = 'http://134.209.101.113'
realmax_url = 'https://app.realcrm.vn'
gb_access_token = 'r7k6ywzxsv75svruybasue4s'
gb_refesh_token = 'zz222pp58uf7z6xvgvuqkxd4'
gb_admin = 'phucnguyen25392+seleadmin@gmail.com'
gb_admin_pass = 'Test@123'
gb_user = 'phucnguyen25392+seleuser@gmail.com'
gb_user_pass = 'Test@123'
##### Define Driver

if platform.system() == 'Darwin':
    root_dir = '/Users/mac/workspace/sele'
    gb_report_path = '/Users/mac/workspace/sele/my_report.html'
    gb_chromedriverlocation = root_dir + '/chrome_driver_mac/chromedriver'
elif platform.system() == 'Windows':
    root_dir = 'C:\Jenkins\workspace\sele_test\sele'
    gb_report_path = 'C:\Jenkins\workspace\sele_test\sele\my_report.html'
    gb_chromedriverlocation = root_dir + '\chrome_driver_win\chromedriver.exe'

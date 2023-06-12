import pytest
import os

def test_excute():
    report_dir = os.sep.join([os.path.dirname(__file__), "reports"])
    if not os.path.exists(report_dir):
        os.mkdir(report_dir)
    report_html = os.sep.join([report_dir,"report.html"])
    allure_dir = os.sep.join([report_dir,"allure_files"])
    excute_case = os.sep.join([os.path.dirname(__file__),"test_check01.py"])
    command_line = ["-vs", excute_case, "--html={:s}".format(report_html), "--alluredir={:s}".format(allure_dir)]
    pytest.main(command_line)

if __name__ == "__main__":
    test_excute()
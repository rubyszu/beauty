# -*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import pytest
import time
from core.entry import runStage
from core.resolve_stage import getStage

def pytest_collect_file(parent, path):
    if path.ext == ".yaml" and path.basename.startswith("test"):
        return YamlFile(path, parent)

def add_parser_options(parser, with_defaults=True):
    """Add argparse options

    This is shared between the CLI and pytest (for now)
    """
    parser(
        "--p",
        help="no cache",
        default='no:cacheprovider',
        required=False
    )

    # --html=./report_html.html
    # stamp = time.strftime('%Y%m%d%H%M%S',time.localtime(time.time()))
    # html_path = "./report/report_{}.html".format(stamp)

    # parser(
    #     "--html",
    #     help="traceback",
    #     default=html_path,
    #     required=False
    # )

    parser(
        "--env",
        help="api running environment",
        choices=['production','development'],
        default='production',
        required=False
    )
    parser(
        "--product",
        help="Which product api belong to",
        default="project",
        required=False
    )
    parser(
        "--branch",
        help="api running branch",
        default="v1",
        required=False
    )

def pytest_addoption(parser):
    """Add an option to pass in a global config file for tavern
    """
    add_parser_options(parser.addoption, with_defaults=False)

@pytest.mark.hookwrapper
def pytest_runtest_makereport(item, call):
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])
    if report.when == 'call':
        status_code = item.summary.response.status_code
        request = item.summary.stage.stage.request
        response = item.summary.response.json()
        extra.append(pytest_html.extras.json(status_code, status_code))
        extra.append(pytest_html.extras.json(request, "request"))
        extra.append(pytest_html.extras.json(response, "response"))
        report.extra = extra

class YamlFile(pytest.File):
    def collect(self):
        # get command line arguments
        cli_args = {}
        cli_args_list = ["env", "product", "branch"]
        for i in cli_args_list:
            cli_args.update({i: self.config.getoption(i)})
        
        #test_name
        stage = getStage(str(self.fspath))
        test_name = stage.test_name

        yield YamlItem(test_name, self, cli_args, stage)

class YamlItem(pytest.Item):
    def __init__(self, name, parent, cli_args, stage):
        self.cli_args = cli_args
        self.stage = stage
        super(YamlItem, self).__init__(name, parent)


    def repr_failure(self, excinfo):
        
        # called when self.runtest() raises an exception.
        self.summary = excinfo._excinfo[1]
        return super(YamlItem, self).repr_failure(excinfo)

    def reportinfo(self):
        return self.fspath, 0, "{s.fspath}::{s.name:s}".format(s=self)

    def runtest(self):
        runStage(self.stage, self.cli_args)

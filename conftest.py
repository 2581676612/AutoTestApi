import pytest

from py._xmlgen import html

_driver = None


def pytest_configure(config):
    # Environment配置
    # config._metadata.pop('JAVA_HOME')
    config._metadata.pop('Packages')
    # config._metadata.pop('Platform')
    config._metadata.pop('Plugins')
    # config._metadata.pop('Python')


@pytest.mark.optionalhook
def pytest_html_results_summary(prefix):
    prefix.extend([html.p(f'测试人员：测试')])


@pytest.mark.hookwrapper
def pytest_runtest_makereport(item):
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    report.description = str(item.function.__doc__)


@pytest.mark.optionalhook
def pytest_html_results_table_header(cells):
    cells.insert(1, html.th('Description'))
    cells.pop()


@pytest.mark.optionalhook
def pytest_html_results_table_row(report, cells):
    cells.insert(1, html.td(report.description))
    cells.pop()

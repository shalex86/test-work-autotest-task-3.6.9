import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
	parser.addoption('--language', action='store', default=None,
					 help="Choose language: ru, es, fr etc")


@pytest.fixture(scope="function")
def browser(request):
	user_language = request.config.getoption("language")
	if user_language:
		options = Options()
		options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
		browser = webdriver.Chrome(options=options)
		print("\nstart browser Chrome for test (+ options)..")
	else:
		raise pytest.UsageError("--language should by example: ru, es..")
	yield browser
	print("\nquit browser..")
	browser.quit()
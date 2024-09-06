import pytest
from selenium import webdriver
import time
from Assets.styles import style, block


def pytest_configure(config):
    print("\n" + "=" * 50)
    print("AXE AUTOMATION TEST".center(50))
    print("=" * 50)

    if not block:
        block_name = input("\nEnter block name (e.g., '2021 Pant, Tapered..':\n").strip()
        block.append(block_name)

    if not style:
        style_name = input("Enter style (e.g., 'BLANK'): ").strip()
        style.append(style_name)

    print("\n" + "=" * 50)
    print("Configuration Completed Successfully".center(50))
    print("=" * 50)


def pytest_addoption(parser):
    parser.addoption(
        "--browser", action="store", default="chrome", help="my option: type1 or type2"
    )

@pytest.fixture(scope="session")
def setup(request):
    browser_named = request.config.getoption("browser")

    if browser_named == "chrome":
        driver = webdriver.Chrome()
    elif browser_named == "safari":
        driver = webdriver.Safari()
    else:
        raise ValueError(f"Unsupported browser: {browser_named}")

    driver.get("https://axe-customizer-stg.qstrike.net/")
    driver.maximize_window()
    request.session.driver = driver
    yield driver
    time.sleep(3)
    driver.quit()


@pytest.fixture(scope="session")
def URL():
    return "https://axe-customizer-stg.qstrike.net/"


@pytest.fixture(scope="class", autouse=True)
def setup_class(request, setup, URL):
    request.cls.driver = setup
    request.cls.url_name = URL


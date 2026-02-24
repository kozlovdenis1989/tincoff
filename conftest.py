import pytest


@pytest.fixture(scope="session")
def browser_type_launch_args(browser_type_launch_args):
    return {
        **browser_type_launch_args,
        "args": ["--disable-blink-features=AutomationControlled"],
        "headless": False,  # Чтобы всегда видеть браузер
    }


# Настраиваем параметры КОНТЕКСТА (экран, язык)
@pytest.fixture(scope="session")
def browser_context_args(browser_context_args):
    return {
        **browser_context_args,
        "viewport": {"width": 1920, "height": 1080},
        "locale": "ru-RU",
    }

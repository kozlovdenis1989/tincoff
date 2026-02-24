import pytest
import os

@pytest.fixture(scope="session")
def browser_type_launch_args(browser_type_launch_args):
    # Проверяем, запущены ли мы в GitHub Actions
    is_ci = os.getenv("CI") == "true"
    
    args = [
        "--disable-blink-features=AutomationControlled",
    ]
    
    # В CI обязательно нужны эти два флага
    if is_ci:
        args.extend(["--no-sandbox", "--disable-dev-shm-usage"])

    return {
        **browser_type_launch_args,
        "args": args,
        # Если в CI — headless всегда True, если локально — False
        "headless": False if not is_ci else True,
    }
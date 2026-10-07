"""Gera evidências visuais para falhas inesperadas do Pytest."""

from datetime import datetime
from pathlib import Path
import re

import pytest


EVIDENCES_DIR = Path("evidencias")


def _safe_file_name(text):
    """Converte o nome do teste em um nome seguro de arquivo."""
    return re.sub(r"[^a-zA-Z0-9_-]+", "_", text).strip("_")


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """Salva imagem e descrição quando um teste falha na execução."""
    outcome = yield
    report = outcome.get_result()

    # Falhas de coleta/encerramento não mostram a tela do aplicativo.
    if report.when != "call" or not report.failed:
        return

    test_instance = getattr(item, "instance", None)
    driver = getattr(test_instance, "driver", None)

    if driver is None:
        return

    EVIDENCES_DIR.mkdir(exist_ok=True)
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    test_name = _safe_file_name(item.nodeid)
    base_name = f"{timestamp}_{test_name}"
    screenshot_path = EVIDENCES_DIR / f"{base_name}.png"
    report_path = EVIDENCES_DIR / f"{base_name}.txt"

    # A captura é feita antes do teardown para registrar o estado da página.
    try:
        driver.save_screenshot(str(screenshot_path))
    except Exception as error:
        screenshot_path = None
        screenshot_error = f"Não foi possível salvar a captura: {error}"
    else:
        screenshot_error = ""

    report_path.write_text(
        "EVIDÊNCIA DE FALHA DE TESTE\n"
        f"Data e hora: {timestamp}\n"
        f"Teste: {item.nodeid}\n"
        f"URL: {driver.current_url}\n"
        f"Print: {screenshot_path.name if screenshot_path else 'não gerado'}\n\n"
        "O que aconteceu:\n"
        f"{report.longreprtext}\n\n"
        f"{screenshot_error}\n",
        encoding="utf-8",
    )

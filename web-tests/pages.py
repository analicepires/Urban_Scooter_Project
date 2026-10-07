from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class UrbanScooterPage:
    """Métodos e localizadores da primeira etapa do pedido."""

    ORDER_BUTTON = (
        By.XPATH,
        "//button[normalize-space()='Fazer pedido' and not(@disabled)]",
    )
    ACCEPT_COOKIES_BUTTON = (
        By.XPATH,
        "//button[contains(translate(normalize-space(.), "
        "'ACEITARCOOKIES', 'aceitarcookies'), 'aceitar') "
        "or contains(@aria-label, 'Accept cookies')]",
    )

    FIRST_NAME_FIELD = (By.CSS_SELECTOR, "input[placeholder='* Nome']")
    LAST_NAME_FIELD = (By.CSS_SELECTOR, "input[placeholder='* Sobrenome']")
    ADDRESS_FIELD = (
        By.CSS_SELECTOR,
        "input[placeholder='* Endereço: para onde levar a scooter']",
    )
    METRO_FIELD = (By.CSS_SELECTOR, "input[placeholder='* Estação de metrô']")
    PHONE_FIELD = (
        By.CSS_SELECTOR,
        "input[placeholder='* Telefone: o entregador ligará para este número']",
    )
    NEXT_BUTTON = (By.XPATH, "//button[normalize-space()='Avançar']")
    RENTAL_TITLE = (By.XPATH, "//*[normalize-space()='Locação']")

    FIRST_NAME_ERROR = (
        By.XPATH,
        "//input[@placeholder='* Nome']/following-sibling::div[contains(@class, 'ErrorMessage')]",
    )
    LAST_NAME_ERROR = (
        By.XPATH,
        "//input[@placeholder='* Sobrenome']/following-sibling::div[contains(@class, 'ErrorMessage')]",
    )
    PHONE_ERROR = (
        By.XPATH,
        "//input[@placeholder='* Telefone: o entregador ligará para este número']"
        "/following-sibling::div[contains(@class, 'ErrorMessage')]",
    )

    def __init__(self, driver):
        self.driver = driver
        # O servidor de testes pode demorar alguns segundos para carregar.
        self.wait = WebDriverWait(driver, 20)

    def open(self, url):
        self.driver.get(url)

    def accept_cookies_if_visible(self):
        """Aguarda brevemente o aviso de cookies e o aceita quando aparecer."""
        try:
            button = WebDriverWait(self.driver, 5).until(
                EC.element_to_be_clickable(self.ACCEPT_COOKIES_BUTTON)
            )
            self.driver.execute_script("arguments[0].click();", button)
        except TimeoutException:
            # O aviso já foi aceito em uma execução anterior ou não foi exibido.
            pass

    def open_order_form(self):
        self.accept_cookies_if_visible()
        order_button = self.wait.until(
            EC.element_to_be_clickable(self.ORDER_BUTTON)
        )
        self.driver.execute_script(
            "arguments[0].scrollIntoView({block: 'center'});", order_button
        )
        self.driver.execute_script("arguments[0].click();", order_button)
        self.wait.until(EC.visibility_of_element_located(self.FIRST_NAME_FIELD))

    def fill_field(self, locator, value):
        field = self.wait.until(EC.element_to_be_clickable(locator))
        field.clear()
        field.send_keys(value)

    def select_metro_station(self, station_value):
        self.wait.until(EC.element_to_be_clickable(self.METRO_FIELD)).click()
        station = (By.CSS_SELECTOR, f".select-search__select button[value='{station_value}']")
        self.wait.until(EC.element_to_be_clickable(station)).click()

    def fill_customer_form(self, first_name, last_name, address, phone, station_value):
        self.fill_field(self.FIRST_NAME_FIELD, first_name)
        self.fill_field(self.LAST_NAME_FIELD, last_name)
        self.fill_field(self.ADDRESS_FIELD, address)
        self.select_metro_station(station_value)
        self.fill_field(self.PHONE_FIELD, phone)

    def click_next(self):
        self.accept_cookies_if_visible()
        self.wait.until(EC.element_to_be_clickable(self.NEXT_BUTTON)).click()

    def is_rental_form_displayed(self):
        return self.wait.until(EC.visibility_of_element_located(self.RENTAL_TITLE)).is_displayed()

    def get_error_text(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator)).text

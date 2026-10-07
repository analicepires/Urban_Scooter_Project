import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

import data
from pages import UrbanScooterPage


class TestUrbanScooter:
    @classmethod
    def setup_class(cls):
        # A resolução solicitada na tarefa é 1280x720.
        options = Options()
        options.add_argument("--window-size=1280,720")
        cls.driver = webdriver.Chrome(options=options)
        cls.page = UrbanScooterPage(cls.driver)

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()

    def setup_method(self):
        # Cada caso começa em uma página limpa para não depender do anterior.
        self.page.open(data.URBAN_SCOOTER_URL)
        self.page.accept_cookies_if_visible()
        self.page.open_order_form()

    def fill_valid_form(self, first_name=data.VALID_FIRST_NAME,
                        last_name=data.VALID_LAST_NAME,
                        phone=data.VALID_PHONE):
        self.page.fill_customer_form(
            first_name,
            last_name,
            data.VALID_ADDRESS,
            phone,
            data.METRO_STATION_VALUE,
        )

    @pytest.mark.parametrize(
        "case_id, first_name",
        [
            ("CT-01", "Li"),
            ("CT-02", "Maria"),
            ("CT-03", "Ana-Maria"),
        ],
    )
    def test_valid_first_name(self, case_id, first_name):
        self.fill_valid_form(first_name=first_name)
        self.page.click_next()
        assert self.page.is_rental_form_displayed(), case_id

    @pytest.mark.parametrize(
        "case_id, first_name",
        [
            ("CT-04", "A"),
            ("CT-05", "Abcdefghijklmnop"),
            ("CT-06", "Maria123"),
            ("CT-07", ""),
        ],
    )
    def test_invalid_first_name(self, case_id, first_name):
        self.fill_valid_form(first_name=first_name)
        self.page.click_next()
        assert self.page.get_error_text(self.page.FIRST_NAME_ERROR) == "Insira um nome válido", case_id

    def test_valid_last_name(self):
        self.fill_valid_form(last_name="Li")
        self.page.click_next()
        assert self.page.is_rental_form_displayed(), "CT-08"

    @pytest.mark.parametrize(
        "case_id, last_name",
        [
            ("CT-09", ""),
            ("CT-10", "S"),
            ("CT-11", "Silva123"),
        ],
    )
    def test_invalid_last_name(self, case_id, last_name):
        self.fill_valid_form(last_name=last_name)
        self.page.click_next()
        assert self.page.get_error_text(self.page.LAST_NAME_ERROR) == "Insira um nome válido", case_id

    @pytest.mark.parametrize(
        "case_id, phone",
        [
            ("CT-12", "11987654321"),
            ("CT-13", "5511987654321"),
            ("CT-14", "+11987654321"),
        ],
    )
    def test_valid_phone(self, case_id, phone):
        self.fill_valid_form(phone=phone)
        self.page.click_next()
        assert self.page.is_rental_form_displayed(), case_id

    @pytest.mark.parametrize(
        "case_id, phone",
        [
            ("CT-15", ""),
            ("CT-16", "1198765432"),
            ("CT-17", "55119876543210"),
            ("CT-18", "11987abc321"),
            ("CT-19", "11 98765-4321"),
            ("CT-20", "11+987654321"),
        ],
    )
    def test_invalid_phone(self, case_id, phone):
        self.fill_valid_form(phone=phone)
        self.page.click_next()
        assert self.page.get_error_text(self.page.PHONE_ERROR) == "Insira um número válido", case_id

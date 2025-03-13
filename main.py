import data
import urban_routes_page
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestUrbanRoutes:

    driver = None

    @classmethod
    def setup_class(cls):
        # no lo modifiques, ya que necesitamos un registro adicional habilitado para recuperar el código de confirmación del teléfono
        options = Options ()
        options.set_capability("goog:loggingPrefs", {'performance': 'ALL'})
        cls.driver = webdriver.Chrome(service=Service(), options=options)

    def test_set_route(self): #Prueba para introducir una dirección
        self.driver.get(data.urban_routes_url)
        routes_page = urban_routes_page.UrbanRoutesPage(self.driver)
        address_from = data.address_from
        address_to = data.address_to
        routes_page.set_route(address_from, address_to)
        routes_page.click_on_button_taxi()
        assert routes_page.get_from() == address_from
        assert routes_page.get_to() == address_to

    def test_select_comfort_rate (self): #Prueba para seleccionar la tárifa comfort
        self.test_set_route()
        routes_page = urban_routes_page.UrbanRoutesPage(self.driver)
        routes_page.click_on_button_taxi()
        routes_page.click_on_button_comfort()
        # Esperar a que aparezca la imagen que indica que la tarifa Comfort fue seleccionada
        comfort_icon = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//img[@alt='Comfort']"))
        )

        assert comfort_icon is not None, "Error: No se encontró la imagen que confirma la selección de Comfort."

    def test_set_phone_number(self): #Prueba para agregar número de teléfono
        self.test_select_comfort_rate()
        routes_page = urban_routes_page.UrbanRoutesPage(self.driver)
        routes_page.click_phone_number_field()
        routes_page.set_phone_number_popup_window()
        routes_page.click_button_next_phone_number_popup_window()
        routes_page.click_code_field()
        routes_page.enter_code_field()
        routes_page.click_button_confirm()
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(routes_page.phone_number_field)
        )

        button_confirm = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(routes_page.button_confirm)
        )
        assert button_confirm.is_enabled(), "El botón Confirmar no está habilitado"

    def test_set_select_payment_method(self): #Prueba para agregar una tarjeta
        self.test_select_comfort_rate()
        routes_page = urban_routes_page.UrbanRoutesPage(self.driver)
        routes_page.click_on_payment_method_field()
        routes_page.click_on_button_add_card()
        routes_page.click_on_number_card_field()
        routes_page.add_number_card()
        routes_page.click_on_code_card_field()
        routes_page.enter_code_card(routes_page.code_card_field)
        routes_page.click_on_button_add_popup_window()
        routes_page.click_on_button_close_add_payment_window()
        assert routes_page.card_is_added()

    def test_message_to_driver(self):  #Prueba para insertar mensaje al conductor
        self.test_select_comfort_rate()
        routes_page = urban_routes_page.UrbanRoutesPage(self.driver)
        routes_page.click_on_message_to_driver_field()
        routes_page.write_message_to_driver_field()
        written_message = routes_page.get_message_value()
        assert written_message == data.message_for_driver, f"Se esperaba: {data.message_for_driver}, pero se obtuvo: {written_message}"


    def test_order_tissues_and_blanket(self): #Prueba para seleccionar manta y pañuelos
        self.test_select_comfort_rate()
        routes_page = urban_routes_page.UrbanRoutesPage(self.driver)
        routes_page.click_on_switch_button_tissue_blanket()
        assert routes_page.get_switch_button_tissue_blanket(), "El botón switch de manta y pañuelos no esta activado"

    def test_order_2_ice_cream(self): #Prueba para agregar 2 helados
        self.test_select_comfort_rate()
        routes_page = urban_routes_page.UrbanRoutesPage(self.driver)
        routes_page.click_on_button_ice_cream()
        assert routes_page.get_ice_cream_counter_value() == 2

    def test_request_taxi(self): #Prueba para pedir un taxi
        self.test_set_route()
        routes_page = urban_routes_page.UrbanRoutesPage(self.driver)
        routes_page.get_button_request_taxi()
        routes_page.click_on_button_request_taxi()
        assert routes_page.get_sucess_request_taxi_popup_window() is not None



    @classmethod
    def teardown_class(cls):
        cls.driver.quit()

import data
import urban_routes_page
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options


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
        assert routes_page.get_from() == address_from
        assert routes_page.get_to() == address_to

    def test_select_comfort_rate (self): #Prueba para seleccionar la tárifa comfort
        self.test_set_route()
        routes_page = urban_routes_page.UrbanRoutesPage(self.driver)
        routes_page.click_on_button_taxi()
        routes_page.click_on_button_comfort()

    def test_set_phone_number (self): #Prueba para agregar número de teléfono
        self.test_select_comfort_rate()
        routes_page = urban_routes_page.UrbanRoutesPage(self.driver)
        routes_page.click_phone_number_field()
        routes_page.set_phone_number_popup_window()
        routes_page.click_button_next_phone_number_popup_window()
        routes_page.click_code_field()
        routes_page.enter_code_field()
        routes_page.click_button_confirm()

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

    def test_message_to_driver(self):  #Prueba para insertar mensaje al conductor
        self.test_select_comfort_rate()
        routes_page = urban_routes_page.UrbanRoutesPage(self.driver)
        routes_page.click_on_message_to_driver_field()
        routes_page.write_message_to_driver_field()
        assert routes_page.get_message_to_driver_field().get_property('value') == data.message_for_driver

    def test_order_tissues_and_blanket(self): #Prueba para seleccionar manta y pañuelos
        self.test_select_comfort_rate()
        routes_page = urban_routes_page.UrbanRoutesPage(self.driver)
        routes_page.click_on_switch_button_tissue_blanket()

    def test_order_2_ice_cream(self): #Prueba para agregar 2 helados
        self.test_select_comfort_rate()
        routes_page = urban_routes_page.UrbanRoutesPage(self.driver)
        routes_page.click_on_button_ice_cream()

    def test_request_taxi(self): #Prueba para pedir un taxi
        self.test_select_comfort_rate()
        self.test_set_phone_number()
        self.test_set_select_payment_method()
        routes_page = urban_routes_page.UrbanRoutesPage(self.driver)
        routes_page.get_button_request_taxi()
        routes_page.click_on_button_request_taxi()


    @classmethod
    def teardown_class(cls):
        cls.driver.quit()

import data
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import helpers


class UrbanRoutesPage:
    from_field = (By.ID, 'from')
    to_field = (By.ID, 'to')
    button_taxi = (By.CSS_SELECTOR, '.button.round')
    button_comfort = (By.XPATH, "//div[@class='tcard-title'][text()='Comfort']")
    phone_number_field = (By.XPATH, "//div[contains(text(), 'Número de teléfono')]")
    phone_number_popup_window = (By.XPATH, "//input[@id='phone']")
    button_next_phone_number_popup_window = (By.CSS_SELECTOR, ".button.full")
    code_field = (By.XPATH, "//label[contains(text(), 'Introduce el código')]")
    button_confirm = (By.XPATH, "//button[text()='Confirmar']")
    payment_method_field = (By.CLASS_NAME, "pp-text")
    button_add_card = (By.XPATH, "//div[@class='pp-title' and contains(text(), 'Agregar tarjeta')]")
    number_card_field = (By.ID, 'number')
    code_card_field = (By.XPATH, "//input[@placeholder='12']")
    button_add_in_popup_window = (By.XPATH, "//button[@type='submit' and contains(text(), 'Agregar')]")
    button_close_add_payment_window = (By.XPATH, "(//button[@class= 'close-button section-close'])[3]")
    popup_window_add_card = (By.CLASS_NAME, "card-wrapper")
    message_to_driver_field = (By.ID, 'comment')
    driver_message_label = (By.XPATH, "//label[@for='comment']")
    switch_button_tissues_blanket = (By.CLASS_NAME, "switch")
    button_ice_cream = (By.CLASS_NAME, "counter-plus")
    ice_cream_counter = (By.CLASS_NAME, "counter-value")
    button_request_taxi = (By.CLASS_NAME, "smart-button-wrapper")
    sucess_request_taxi = (By.CLASS_NAME, "order-header-title")


    def __init__(self, driver):
        self.driver = driver
        self.driver.implicitly_wait(10)

    def set_from(self, from_address): #Codigo para rellenar el campo "Desde"
        self.driver.find_element(*self.from_field).send_keys(from_address)

    def set_to(self, to_address): #Codigo para rellenar el campo "Hasta"
        self.driver.find_element(*self.to_field).send_keys(to_address)

    def get_from(self): #Codigo para encontrar el campo "Desde"
        return self.driver.find_element(*self.from_field).get_property('value')

    def get_to(self): #Codigo para encontrar el campo "Hasta"
        return self.driver.find_element(*self.to_field).get_property('value')

    def set_route (self, from_address, to_address): #Código para colocar la ruta en los campos "Desde" y "Hasta"
        self.set_from(from_address)
        self.set_to(to_address)

    def get_request_button_taxi (self): #Codigo para obtener el botón "Pedir un taxi"
        return WebDriverWait (self.driver, 10).until(
            EC.element_to_be_clickable(self.button_taxi)
        )

    def click_on_button_taxi (self): #Codigo para dar click en el botón "Pedir un taxi"
        self.get_request_button_taxi().click()

    def get_button_comfort (self): #Codigo para obtener el botón "Comfort"
        return WebDriverWait (self.driver, 10).until(
            EC.element_to_be_clickable(self.button_comfort)
        )

    def click_on_button_comfort (self): #Codigo para dar click al botón comfort
        self.get_button_comfort().click()

    def get_phone_number_field (self): #Código para obtener el campo de insertar número
        return WebDriverWait (self.driver, 20).until(
            EC.element_to_be_clickable(self.phone_number_field)
        )

    def click_phone_number_field (self): #Código para dar click al campo de insertar número
        self.get_phone_number_field().click()

    def set_phone_number_popup_window (self): #Código para ingresar el número en la ventana de "Insertar número"
        WebDriverWait(self.driver,10).until(
            EC.visibility_of_element_located(self.phone_number_popup_window)
        )
        WebDriverWait(self.driver,10).until(
            EC.element_to_be_clickable(self.phone_number_popup_window)
        ).send_keys(data.phone_number)

    def click_button_next_phone_number_popup_window (self): #Código para dar click al botón "Siguiente" del formulario ingresar número
        WebDriverWait (self.driver,10).until(
            EC.element_to_be_clickable(self.button_next_phone_number_popup_window)
        ).click()

    def get_code_field (self): #Código para obtener el campo "Código"
        return self.driver.find_element(*self.code_field)

    def click_code_field (self): #Código para dar click al campo código
        WebDriverWait(self.driver,10).until(
            EC.element_to_be_clickable(self.code_field)
        ).click()

    def enter_code_field(self):
        code = helpers.retrieve_phone_code(self.driver)
        code_field_element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.code_field)
        )
        self.driver.execute_script("arguments[0].value = arguments[1];", code_field_element,
                                   code)  # Ingresar el código usando JavaScript

    def click_button_confirm(
            self):  # Código para dar click al botón confirmar del formulario "Insertar número de teléfono"
        self.driver.find_element(*self.button_confirm).click()

    def get_payment_method_field(self):  # Código para obtener el campo "Metodo de pago"
        return self.driver.find_element(*self.payment_method_field)

    def click_on_payment_method_field(self):  # Código para dar click al campo de "Metodo de pago"
        self.driver.find_element(*self.payment_method_field).click()

    def click_on_button_add_card(self):  # Código para dar click en el botón de "Agregar tarjeta"
        self.driver.find_element(*self.button_add_card).click()

    def click_on_number_card_field(self):  # Código para dar click al campo para agregar el número de tarjeta
        self.driver.find_element(*self.number_card_field).click()

    def add_number_card(self):  # Código para añadir el número de tarjeta
        self.driver.find_element(*self.number_card_field).send_keys(data.card_number)

    def get_code_card_field(self):  # Código para obtener el campo código de tarjeta
        return self.driver.find_element(*self.code_card_field)

    def click_on_code_card_field(self):  # Código para dar click al campo Código
        WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable(self.code_card_field)
        ).click()

    def enter_code_card(self, code_card_field):  # Código para agregar el código de tarjeta
        WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable(self.code_card_field)
        ).send_keys(data.card_code)

    def get_button_add_popup_window(self):  # Código para obtener el botón "Agregar" del formulario para agregar tarjeta
        return self.driver.find_element(*self.button_add_in_popup_window)

    def click_on_button_add_popup_window(self):  # Código para dar click al botón "Agregar" del formulario para agregar tarjeta
        WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable(self.popup_window_add_card)
        ).click()

        WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable(self.button_add_in_popup_window)
        ).click()

    def card_is_added(self):
        payment_method_text_xpath = "//div[@class='pp-value-text' and text()='Tarjeta']"
        return WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, payment_method_text_xpath))
        )

    def get_button_close_add_payment_window(self):  # Código para obtener el botón "Cerrar" de la ventana para agregar el metodo de pago
        return self.driver.find_element(*self.button_close_add_payment_window)

    def click_on_button_close_add_payment_window(self):
        WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable(self.button_close_add_payment_window)
        ).click()

    def get_message_to_driver_field(self):  # Código para obtener el campo "Mensaje para el conductor"
        return WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.message_to_driver_field)
        )

    def get_driver_message_label(self): #Código para obtener el campo en la parte interactuable ya que se bloquea por el input
        return WebDriverWait(self.driver,10).until(
            EC.element_to_be_clickable(self.driver_message_label)
        )

    def click_on_message_to_driver_field(self): # Código para dar click en el campo "Mensaje al conductor"
        self.get_driver_message_label().click()

    def write_message_to_driver_field(self): #Escribir mensaje al conductor
        self.get_message_to_driver_field().send_keys(data.message_for_driver)

    def get_message_value(self): #Obtener el valor del campo de texto después de escribir el mensaje
        message_field = self.get_message_to_driver_field()
        return message_field.get_attribute("value")

    def get_switch_button_tissue_blanket(self): #Obtener el botón "Mantas y pañuelos"
        return WebDriverWait(self.driver,20).until(
            EC.element_to_be_clickable(self.switch_button_tissues_blanket)
        )

    def click_on_switch_button_tissue_blanket(self): #Dar click en el botón "Manta y pañuelos"
        self.get_switch_button_tissue_blanket().click()

    def get_button_ice_cream(self): #Obtener el botón "+" para agregar helados
        return WebDriverWait(self.driver,20).until(
            EC.visibility_of_element_located(self.button_ice_cream)
        )

    def get_ice_cream_counter(self): #Obtener el contador de helado
        return WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located(self.ice_cream_counter)
        )

    def get_ice_cream_counter_value(self): #Obtener el contenido del contador de helados
        counter_element = self.get_ice_cream_counter()
        counter_text = counter_element.text
        # Convertir el texto (que es un número) a entero
        return int(counter_text)

    def click_on_button_ice_cream(self): #Dar 2 clicks en el botón "+" para pedir 2 helados
        ice_cream = self.get_button_ice_cream()
        ice_cream.click() #Primer click para agregar 1 helado
        ice_cream.click() #Segundo click para agregar 2 helados

    def get_button_request_taxi(self): #Obtener el botón para reservar un taxi
        return WebDriverWait(self.driver,10).until(
            EC.element_to_be_clickable(self.button_request_taxi)
        )

    def click_on_button_request_taxi(self): #Dar click en el botón "Reservar un taxi"
        self.get_button_request_taxi().click()

    def get_sucess_request_taxi_popup_window(self): #Ventana de pedido de taxi
        return WebDriverWait(self.driver,20).until(
            EC.visibility_of_element_located(self.sucess_request_taxi)
        )


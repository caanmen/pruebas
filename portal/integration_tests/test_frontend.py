from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import unittest

class NewsIntegrationTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.get("http://127.0.0.1:5500")  # URL del frontend servido por Live Server
        cls.wait = WebDriverWait(cls.driver, 20)  # Espera explícita de hasta 10 segundos

    def test_news_displayed_and_link(self):
        # Espera hasta que el contenedor de noticias esté presente
        news_container = self.wait.until(EC.presence_of_element_located((By.ID, "newsContainer")))
        self.assertIsNotNone(news_container, "Error: Contenedor de noticias no encontrado.")

        # Verifica que haya al menos una noticia
        news_cards = news_container.find_elements(By.CLASS_NAME, "news-card")
        self.assertGreater(len(news_cards), 0, "Error: No se encontraron noticias en el contenedor.")

        # Verificar que el enlace "Leer más" redirige correctamente a noticia.html
        read_more_button = news_cards[0].find_element(By.CLASS_NAME, "read-more-button")
        read_more_button.click()

        # Espera hasta que se cargue la página de noticia
        self.wait.until(EC.title_contains("Noticia Detallada"))
        self.assertIn("Noticia Detallada", self.driver.title, "Error: No se redirigió a la página de detalle de noticia.")

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__ == "__main__":
    unittest.main()

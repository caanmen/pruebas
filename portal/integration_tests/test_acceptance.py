from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import unittest

class AcceptanceTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.get("http://127.0.0.1:5500/frontend/index.html")  # URL de la página principal
        cls.wait = WebDriverWait(cls.driver, 20)  # Espera explícita de hasta 20 segundos

    def test_news_section_display(self):
        # Verifica que el contenedor de noticias esté visible
        news_container = self.wait.until(EC.presence_of_element_located((By.ID, "newsContainer")))
        self.assertIsNotNone(news_container, "No se encontró el contenedor de noticias.")

        # Verifica que al menos una noticia esté presente
        news_cards = news_container.find_elements(By.CLASS_NAME, "news-card")
        self.assertGreater(len(news_cards), 0, "No se encontraron noticias en la sección de noticias.")

        # Hacer clic en "Leer más" para ver detalles
        read_more_button = news_cards[0].find_element(By.CLASS_NAME, "read-more-button")
        read_more_button.click()

        # Verificar que se redirige a la página de detalle de la noticia
        self.wait.until(EC.title_contains("Noticia Detallada"))
        self.assertIn("Noticia Detallada", self.driver.title, "La página de detalle de noticia no se cargó correctamente.")

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__ == "__main__":
    unittest.main()

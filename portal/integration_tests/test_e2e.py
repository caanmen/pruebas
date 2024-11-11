from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import unittest

class EndToEndTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.get("http://127.0.0.1:5500/frontend/index.html")  # Apunta a la raíz del servidor
        cls.wait = WebDriverWait(cls.driver, 20)  # Espera explícita de hasta 20 segundos

        # Imprime el título actual para verificar la carga correcta de la página principal
        print("Título de la página principal:", cls.driver.title)  

    def test_navigate_to_news_detail(self):
        # Paso 1: Verificar que estamos en la página principal
        self.assertIn("Centro Cultural Popular Victor Jara", self.driver.title, "No se cargó la página principal correctamente.")

        # Paso 2: Hacer clic en el enlace "Noticia" en el menú de navegación
        noticia_link = self.wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Noticia")))
        noticia_link.click()

        # Paso 3: Esperar hasta que la página de noticias se cargue
        self.wait.until(EC.title_contains("Noticia Detallada"))
        self.assertIn("Noticia Detallada", self.driver.title, "La página de detalle de noticia no se cargó correctamente.")

        # Paso 4: Verificar que el contenido esperado de la noticia esté presente
        detail_section = self.wait.until(EC.presence_of_element_located((By.ID, "detalle-noticia")))
        heading = detail_section.find_element(By.TAG_NAME, "h2").text
        content = detail_section.find_element(By.TAG_NAME, "p").text
        self.assertEqual(heading, "¿Por qué hay crisis en las manifestaciones?", "El encabezado de la noticia no es el esperado.")
        self.assertIn("El pasado jueves 25 de julio la policía disparó", content, "El contenido de la noticia no es el esperado.")

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__ == "__main__":
    unittest.main()

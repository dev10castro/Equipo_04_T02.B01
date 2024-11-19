import pytest
from PySide6.QtWidgets import QApplication
from Componentes_Personalizado import Button_Search, Search_Bar
from PySide6.QtCore import Qt

@pytest.fixture(scope="session")  # La aplicación existirá durante toda la sesión de pytest
def app():
    """Fixture para inicializar la aplicación Qt."""
    app = QApplication.instance()  # Verifica si ya existe una instancia de QApplication
    if not app:  # Si no existe, crea una nueva
        app = QApplication([])
    return app

@pytest.fixture
def button_search(app):
    """Fixture para inicializar Button_Search."""
    return Button_Search(icon="utils/icons/search-512.png")

@pytest.fixture
def search_bar(app):
    """Fixture para inicializar Search_Bar."""
    return Search_Bar()

### Pruebas para Button_Search ###

def test_button_search_default_text(button_search):
    """Verificar que el texto por defecto sea 'Buscar'."""
    assert button_search.text() == "Buscar"

def test_button_search_signal_emission(qtbot, button_search):
    """Verificar que la señal `signal_presionado` se emita correctamente al presionar."""
    with qtbot.wait_signal(button_search.signal_presionado, timeout=1000):
        qtbot.mouseClick(button_search, Qt.LeftButton)

def test_button_search_text_update(button_search):
    """Verificar que se pueda actualizar dinámicamente el texto del botón."""
    button_search.setText("Nuevo Texto")
    assert button_search.text() == "Nuevo Texto", "El texto del botón no se actualizó correctamente."

### Pruebas para Search_Bar ###

def test_search_bar_default_text(search_bar):
    """Verificar que el texto predeterminado en la barra de búsqueda está vacío."""
    assert search_bar.text() == ""

def test_search_bar_text_update(search_bar, qtbot):
    """Probar si el texto ingresado en la barra de búsqueda se actualiza correctamente."""
    qtbot.keyClicks(search_bar, "Hola Mundo")
    assert search_bar.text() == "Hola Mundo"

def test_search_bar_stylesheet(search_bar):
    """Verificar que el estilo CSS aplicado a la barra de búsqueda es el correcto."""
    expected_stylesheet = "border: 2px solid #f2784b;border-radius:5px;"
    assert search_bar.styleSheet() == expected_stylesheet, "El estilo CSS no coincide con el esperado."

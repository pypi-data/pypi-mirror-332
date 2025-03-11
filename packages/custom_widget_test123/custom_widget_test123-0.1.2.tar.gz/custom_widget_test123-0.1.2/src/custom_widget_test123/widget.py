import anywidget
import traitlets

from pathlib import Path

CURRENT_DIR = Path(__file__).parent
JS_PATH = CURRENT_DIR / "static" / "script.js"
CSS_PATH = CURRENT_DIR / "static" / "styles.css"

class CustomWidget(anywidget.AnyWidget):
    _esm = JS_PATH
    _css = CSS_PATH
    value = traitlets.Int(0).tag(sync=True)


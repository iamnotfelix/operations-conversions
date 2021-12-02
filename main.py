from ui.ui import UI
from validation.validation import Validation
from services.conversions import Conversions
from services.operations import Operations

conversions = Conversions()
operations = Operations()
validator = Validation()
ui = UI(conversions, operations, validator)

ui.start()
from ui.ui import UI
from validation.validation import Validation
from services.conversions import Conversions
from services.operations import Operations

operations = Operations()
conversions = Conversions(operations)
validator = Validation()
ui = UI(conversions, operations, validator)

ui.start()

# IMPORTANT: CHANGE VALIDATIONS SO IT FITS THE PROBLEM STATEMENT
#            - FOR BASES
#            - DIVISION BY 0
#            - ETC. 
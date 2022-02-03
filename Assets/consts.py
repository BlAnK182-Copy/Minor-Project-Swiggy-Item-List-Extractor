import os
from datetime import datetime

FILENAME= datetime.now().strftime("MENU%H%M%S%d%m%Y")
MAX_LINE_LIMIT = 150
DATABASE_NAME = "Restaurant Items"
FILE_DIR_NAME = "Files"
OUTER_FOLDER = __file__.rstrip("Assets\\"+os.path.basename(__file__))
FILE_STORAGE = OUTER_FOLDER + "\\" + FILE_DIR_NAME + "\\"

#GUI Constants
BG_IMAGE_PATH = __file__.rstrip(os.path.basename(__file__)) + "\\Images\\bgImage1.png"
BUTTON_IMAGE_PATH = __file__.rstrip(os.path.basename(__file__)) + "\\Images\\SubmitButton.png"
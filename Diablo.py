# The baseline of this program is to acknowledge the basics of Python programming
# along with importing multiple libraries to showcase module import, such as
# pandas and numpy. Also, I just really enjoyed Diablo IV. So there's that.

# ------ BLUEPRINT -------
# The idea of this program is to import an Excel file with existing Diablo characters
# These characters include their gender, level, class, and what world tier they are in
# The user will also be asked if they would like to enter in their own characters as well
# and be added to the list of data that has been provided
# After creating their character, maybe a machine learning model can be developed in order
# to predict the user's next character? (may differ base on the amount of characters that
# the user inputs)

import pyinputplus as pyip
import pandas as pd

# import Excel file with other characters
def read_file():
    diablo_data = pd.read_excel('file.xlxs')
    for row in range(0, diablo_data.max_row):
        for col in diablo_data.iter_cols(1, diablo_data.max_column):
            print(col[row].value)

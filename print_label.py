
import os
import sys
from PIL import Image
import base64
import io
import time

curr_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(curr_dir))

import dymo_sdk as dsdk

file = "Sample_Label.dymo"
#Loads label
label = dsdk.DymoLabel(filepath = file)
#Displays loaded label
image_data = base64.b64decode(label.get_preview_label())
image_buffer = io.BytesIO(image_data)
image = Image.open(image_buffer)
image.show()

#Change the existing text
addr_object = label.get_label_object("TextObject0")
addr_object.update_data("Hello World")
#Displays updated preview
image_data = base64.b64decode(label.get_preview_label())
image_buffer = io.BytesIO(image_data)
image = Image.open(image_buffer)
image.show()

#gets printers
printers = dsdk.get_printers()
selected_printer = None

#selects first connected printer
for p in printers:
    print(p.name)
    if p.is_connected:
        selected_printer = p

#prints

selected_printer.print_label(label)

# Created by: Khoa Le
# Created on September 12 2017
# Created for ICS3U
# This program is the "Hello, World!", but with GUI

import ui

def hello_world_touch_up_inside(sender):
	view['hello_world_label'].text = ("Hello, World!")

view = ui.load_view()
view.present('sheet')

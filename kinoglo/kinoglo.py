import gi, os

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk


class TreeViewFilterWindow:
    def __init__(self):
        super().__init__(title="Kinoglo")
        self.set_border_width(10)

root = "/home/anderson"
for files in os.listdir(root):
    if os.path.isdir(os.path.join(root,files)):
            print("Directory :", files)


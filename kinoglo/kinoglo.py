import gi, os

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk


class TreeViewFilterWindow(Gtk.Window):
    def __init__(self):
        super().__init__(title="Kinoglo")
        self.set_border_width(10)
        
        # Setting up the self.grind in which the elements are to be positioned
        self.grid = Gtk.Grid()
        self.grid.set_row_homogeneous(True)
        self.add(self.grid)

        # Creating the ListStore model 
        self.movie_liststore = Gtk.ListStore(str, int)
        self.root = "/home/anderson/Videos"
        self.dir_list = []
        # Checks all the files in self.root to determine if they are directories,
        # if they are, appends them 
        for dirs in os.listdir(self.root):
            # Makes an absolute path out of every directory in self.root
            abs_path = os.path.join(self.root,dirs)
            if os.path.isdir(os.path.join(abs_path)):
                self.dir_list.append((dirs, os.path.getsize(abs_path)))
        self.current_filter = None 
        self.directory_liststore = Gtk.ListStore(str, int)

win = TreeViewFilterWindow()
print(win.dir_list)
#root = "/home/anderson"
#for dirs in os.listdir(root):
#    abs_path = os.path.join(root,dirs)
#    if os.path.isdir(abs_path):
#        print(f"Directory :{dirs} {os.path.getsize(abs_path)}")

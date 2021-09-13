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
        self.grid.set_column_homogeneous(True)
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
        print(self.dir_list)
        for movie_dir in self.dir_list:
            self.movie_liststore.append(list(movie_dir))
        self.current_filter = None 
        
        # Creating the filter, feeding it with the ListStore model 
        self.movie_filter = self.movie_liststore.filter_new()
        # setting the filter function
        self.movie_filter.set_visible_func(self.movie_filter_func)

        # creating the treview, making it use the filter as a model and 
        # adding the columns (the filter is passed as an argument to treeview)

        self.treeview = Gtk.TreeView(model=self.movie_filter)
        for i, column_title in enumerate(
                ["Title", "Size"]
        ):
            renderer = Gtk.CellRendererText()
            column = Gtk.TreeViewColumn(column_title, renderer, text=i)
            self.treeview.append_column(column)
       
        self.buttons = list()
        for prog_language in ["Java", "C", "C++", "Python", "None"]:
            button = Gtk.Button(label=prog_language)
            self.buttons.append(button)
            button.connect("clicked", self.on_selection_button_clicked)
        
        # setting up the layout, putting the treeview in a scroll window and the buttons in a row
        # There's something about the presence of the buttons in the tutorial
        # that makes the treeview size properly
        
        self.scrollable_treelist = Gtk.ScrolledWindow()
        self.scrollable_treelist.set_vexpand(True)
        self.grid.attach(self.scrollable_treelist, 0, 0, 8, 10)
        self.grid.attach_next_to(
        self.buttons[0], self.scrollable_treelist, Gtk.PositionType.BOTTOM, 1, 1)

        for i, button in enumerate(self.buttons[1:]):
            self.grid.attach_next_to(
                button, self.buttons[i], Gtk.PositionType.RIGHT, 1, 1)
        self.scrollable_treelist.add(self.treeview)
        
        # Add menubar
        self.menubar = Gtk.MenuBar()
        self.menubar.set_hexpand(True)
        self.menubar.set_vexpand(True)

        self.menu_file = Gtk.MenuItem('File')
        self.menubar.append(self.menu_file)
        
        self.grid.attach_next_to(self.menubar, self.scrollable_treelist, Gtk.PositionType.TOP, 1, 1)
        #menu_preferences = self.submenu(menubar, 'Preferences')
        #menu_filter = self.add_submenu(menubar, 'Filter')

        self.show_all()

    def movie_filter_func(self, model, iter, data):
        return True


    def on_selection_button_clicked(self, widget):
        pass

win = TreeViewFilterWindow()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()

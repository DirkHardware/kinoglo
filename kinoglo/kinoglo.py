import gi
import os
import json
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

movie_attributes = ["Title", "Director", "Year", "Country", "Genre", "Directory", "Size"]

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
        self.movie_liststore = Gtk.ListStore(str, str, int, str, str, str, int)
        self.root = "/home/anderson/Videos"
        self.dir_list = []
        # Checks all the files in self.root to determine if they are directories,
        # if they are, appends them 
        
        for dirs in os.listdir(self.root):
            # Makes an absolute path out of every directory in self.root
            abs_path = os.path.join(self.root,dirs)
            if os.path.isdir(os.path.join(abs_path)):
                info_list = list()
                f = open('{}/data.json'.format(abs_path))
                data = json.load(f)
                for i in data['movie_details'][0].items():
                    if i[0] == "year":
                        info_list.append(int(i[1]))
                    else:
                        info_list.append(i[1])
                info_list.append(dirs) 
                info_list.append(os.path.getsize(abs_path))
                info_tup = tuple(info_list)
                self.dir_list.append(info_tup)
                # self.dir_list.append((dirs, os.path.getsize(abs_path)))
        for movie_dir in self.dir_list:
            self.movie_liststore.append(list(movie_dir))
        self.current_filter = None 
        
        # We create a treevie with movie_liststore. It can't be a filter or else
        # it can't be sorted.

        self.treeview = Gtk.TreeView(model=self.movie_liststore)
        self.treeview.connect("button_press_event", self.mouse_click_event)
        
        for i, column_title in enumerate(
                #["Title", "Director", "Year", "Country", "Genre", "Directory", "Size"]
                movie_attributes
        ):
            renderer = Gtk.CellRendererText()
            column = Gtk.TreeViewColumn(column_title, renderer, text=i)
            column.set_sort_column_id(i)
            self.treeview.append_column(column)
       
        self.buttons = list()
        
        for attribute in movie_attributes:
        #for prog_language in ["Title", "Director", "Year", "Country", "Genre", "Size"]:
            button = Gtk.Button(label=attribute)
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
        
        self.show_all()
    

    def movie_filter_func(self, model, iter, data):
        return True


    def on_selection_button_clicked(self):
        pass
    
    def mouse_click_event(self, lv, event):
        if event.button == 3:
            pthinfo = self.treeview.get_path_at_pos(event.x, event.y)
            if pthinfo != None:
                path,col,cellx,celly = pthinfo 
                self.treeview.grab_focus()
                self.treeview.set_cursor(path,col,0)

            selection = self.treeview.get_selection()
            (model, iter) = selection.get_selected()
            print(model[iter][0])


win = TreeViewFilterWindow()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()

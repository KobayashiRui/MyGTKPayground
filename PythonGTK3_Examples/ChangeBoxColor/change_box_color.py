import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, Gdk

def load_style():
    screen = Gdk.Screen.get_default()
    provider = Gtk.CssProvider()
    provider.load_from_path("./style.css")
    Gtk.StyleContext.add_provider_for_screen(screen, provider, Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION)

class MyWindow(Gtk.Window):
    def __init__(self):
        super().__init__(title="Hello World")
        self.box = Gtk.Box(spacing=6)
        self.box.get_style_context().add_class('red-background')

        self.add(self.box)

        self.hbox = Gtk.HBox(spacing=6)
        self.box.pack_start(self.hbox, True, True, 0)
        
        self.button1 = Gtk.Button(label="Hello")
        self.button1.set_size_request(50, 50)
        self.button1.connect("clicked", self.on_button1_clicked)
        self.button1.get_style_context().add_class('yellow-background')
        #self.box.pack_start(self.button1, True, True, 0)
        self.hbox.pack_start(self.button1, False, False, 0)

        self.button2 = Gtk.Button(label="Goodbye")
        self.button2.set_size_request(50, 50)
        self.button2.connect("clicked", self.on_button2_clicked)
        self.button2.get_style_context().add_class('yellow-background')
        #self.box.pack_start(self.button2, True, True, 0)
        self.hbox.pack_start(self.button2, False, False, 0)


        self.set_default_size(800, 480)
        

    def on_button1_clicked(self, widget):
        print("Hello World")

    def on_button2_clicked(self, widget):
        print("Hello World2")

load_style()
win = MyWindow()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()
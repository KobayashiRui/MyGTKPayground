import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk


class MyWindow(Gtk.Window):
    def __init__(self):
        super().__init__(title="Hello World")
        self.box = Gtk.Box(spacing=6)
        self.add(self.box)

        self.button1 = Gtk.Button(label="Hello")
        self.button1.connect("clicked", self.on_button1_clicked)
        self.box.pack_start(self.button1, True, True, 0)

        self.button2 = Gtk.Button(label="Goodbye")
        self.button2.connect("clicked", self.on_button2_clicked)
        self.box.pack_start(self.button2, True, True, 0)

        self.button3 = Gtk.Button(label="Goodbye2")
        self.button3.connect("clicked", self.on_button2_clicked)
        self.box.pack_start(self.button3, True, True, 0)
        

    def on_button1_clicked(self, widget):
        print("Hello World")

    def on_button2_clicked(self, widget):
        print("Hello World2")

win = MyWindow()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()

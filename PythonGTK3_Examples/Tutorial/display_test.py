import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

win = Gtk.Window()
screen = win.get_screen()
print("Screen:", screen)
#print("Screen Index: " , screen.get_number())
disp = screen.get_display()
print("Disp:", disp)
print("Disp Name:", disp.get_name())

print("Monitor Num:", disp.get_n_monitors())
#print("Screen Num:", disp.get_n_screens())

win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()
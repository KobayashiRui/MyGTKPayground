import gi
import sys

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, Gdk

#print(sys.argv)
Gdk.init(sys.argv)
#disp =Gdk.get_default()
#print(Gdk.get_display_arg_name())

disp_path = "/private/tmp/com.apple.launchd.LLRNjaoLx1/org.xquartz:0"

disp_manager = Gdk.DisplayManager.get()
print(disp_manager.get_default_display())
print(disp_manager.list_displays())
disp = Gdk.Display()
disp = disp.open(disp_path)
print(disp.get_name())
#screen = disp.get_default_screen()

#screen = win.get_screen()
#screen.get_default()
#print("Screen:", screen)
#new_disp_name = screen.make_display_name()
#print("new disp name")
##print("Screen Index: " , screen.get_number())
#disp = screen.get_display()
#print("Disp:", disp)
#print("Disp Name:", disp.get_name())
#
#print("Monitor Num:", disp.get_n_monitors())
#print("Screen Num:", disp.get_n_screens())

#win.set_screen(screen)
#win.connect("destroy", Gtk.main_quit)
#win.show_all()
#Gtk.main()
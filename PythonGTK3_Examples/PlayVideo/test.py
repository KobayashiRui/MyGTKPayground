import gi
gi.require_version("Gtk", "3.0")
gi.require_version("Gst", "1.0")
from gi.repository import Gtk, Gst

import os, sys

Gst.init(None)
Gst.init_check(None)


class PlayerWidget(Gtk.Box):
    """ This is the gtksink widget """
    def __init__(self, parent):
        super().__init__()
        self.parent = parent
        self.player = Gst.ElementFactory.make("playbin")

        self.connect('realize', self.on_realize)

    def on_realize(self, widget):
        playerFactory = self.player.get_factory()

        gtksink = playerFactory.make('gtksink')
        self.player.set_property("video-sink", gtksink)
        print(gtksink)

        self.pack_start(gtksink.props.widget, True, True, 0)
        gtksink.props.widget.show()


class VideoDialog(Gtk.Dialog):
    def __init__(self, parent, filename):
        Gtk.Dialog.__init__(self, "VideoDialog", parent, 0,
                            (Gtk.STOCK_CANCEL, Gtk.ResponseType.CANCEL,
                             Gtk.STOCK_OK, Gtk.ResponseType.OK))
        self.filename = filename
        self.__setupUi()

    def __setupUi(self):
        self.set_default_size(800, 400)

        self.playerWidget = PlayerWidget(parent=self)
        self.playerWidget.set_size_request(800, 450)

        self.player = self.playerWidget.player
        self.player.set_property("uri", self.filename)

        self.btnPlay = Gtk.Button(label="Play")
        self.btnPlay.connect("clicked", self.on_btnPlay_clicked)

        self.hboxBtn01 = Gtk.Box()
        self.hboxBtn01.add(self.btnPlay)

        self.vbox_intern = self.get_content_area()
        self.vbox_intern.add(self.playerWidget)
        self.vbox_intern.add(self.hboxBtn01)

        self.show_all()

    def on_btnPlay_clicked(self, widget):
        playerState = self.player.get_state(Gst.SECOND).state
        if playerState <= Gst.State.PAUSED:
            self.player.set_state(Gst.State.PLAYING)
            self.btnPlay.set_label("Pause")
        elif playerState is Gst.State.PLAYING:
            self.player.set_state(Gst.State.PAUSED)
            self.btnPlay.set_label("Play")


class MainWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="Open VideoDialog")

        self.filename = "https://www.freedesktop.org/software/gstreamer-sdk" + \
                                        "/data/media/sintel_trailer-480p.webm"
        self.set_border_width(40)
        self.set_default_size(200, 110)
        button = Gtk.Button(label="Don't push the button!")
        button.connect("clicked", self.on_button_clicked)
        self.add(button)

    def on_button_clicked(self, widget):
        videoDialog = VideoDialog(self, self.filename)
        videoDialog.set_transient_for(self)
        videoDialog.set_modal(True)

        if Gtk.ResponseType.OK == videoDialog.run():
            print("Response: OK")
        else:
            print("Response: Cancel")

        videoDialog.player.set_state(Gst.State.NULL)
        videoDialog.destroy()

win = MainWindow()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()
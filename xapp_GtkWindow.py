"""
This is a basic example on how to create a XAppGtkWindow using code

As per upstream documentation, this allow to create a derivative of the native Gtk window,
however, it provides some additional capabilities such as:

* Ability to set an icon name or icon file path for the window manager to make use of, 
rather than relying on a desktop file or fixed-size window- backed icon that Gtk 
normally generates (in this case you can use either a Gtk standard icon, a named icon
that must exists within the icon-theme, or a fixed named icon in a given path)

* Ability to send progress info to the window manager, in the form of an integer, 
0-100, which can then be used to display this progress in some manner in a task 
manager or window list. The window manager must support the NET_WM_XAPP_PROGRESS hint.
(Consider this as a copy of progress bar-like option shown in Windows 7 onwards)

* Ability to signal a 'pulsing' progress state, of potentially indeterminate value, 
in the form of a boolean, which can be passed on to a window list. The window manager 
must support the NET_WM_XAPP_PROGRESS_PULSE hint


"""

import gi
gi.require_version('Gtk','3.0')
gi.require_version('XApp','1.0')
from gi.repository import Gtk, XApp

class xApplication(Gtk.Application):
    def __init__(self):
        self.window = XApp.GtkWindow()
        self.window.set_title("XApp GtkWindow")
        self.window.set_icon_name("application-certificate-symbolic")
        #self.window.set_default_size(300, 300) #Optional parameter, window size
        self.window.connect("delete-event", lambda w, e: Gtk.main_quit())
        self.window.present()

        Gtk.main()

if __name__ == "__main__":
    app = xApplication()
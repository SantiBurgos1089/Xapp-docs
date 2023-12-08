"""
This is a basic example on how to create a XAppStatusIcon using code

As per upstream documentation, this allow to create a StatusIcon using XApp libraries
instead of using Gtk libraries directly, this means that, instead of making Gtk to render
directly, we use the native panel of the Desktop Environment to render that icon

When we use an XappStatusIcon, the information about the icon is passed over to the
panel applet via DBus, which allows it for more control depending on the methods used

The name of the variables can be named any way you like, as long as you
follow a standard convention and can be capable to be readable for anyone
but you, remember that someone else might need to check the code and consistency
is key

The icon name must exist within either the entire Gtk standard or the icon theme
you are using!!! It is highly recommended to use the Gtk generic icon names, else
you will end up with a blank icon

"""

import gi
gi.require_version('Gtk','3.0')
gi.require_version('XApp','1.0')
from gi.repository import Gtk, XApp

tray = XApp.StatusIcon()
tray.set_icon_name("dialog-information-symbolic") 
tray.set_tooltip_text("This my first XAppStatusIcon application")

Gtk.main()
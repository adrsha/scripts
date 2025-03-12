#!/usr/bin/env python3
from gi.repository import GLib
import dbus
import dbus.service
from dbus.mainloop.glib import DBusGMainLoop
import subprocess

class NotificationDaemon(dbus.service.Object):
    def __init__(self):
        bus_name = dbus.service.BusName('org.freedesktop.Notifications', dbus.SessionBus())
        dbus.service.Object.__init__(self, bus_name, '/org/freedesktop/Notifications')

    @dbus.service.method('org.freedesktop.Notifications', in_signature='susssasa{sv}i', out_signature='u')
    def Notify(self, app_name, replaces_id, app_icon, summary, body, actions, hints, expire_timeout):
        subprocess.run(['hyprctl', 'notify', '1', "rgb(0C1418)", "fontsize:19 "+ body])
        return 0

    @dbus.service.method('org.freedesktop.Notifications', in_signature='', out_signature='ssss')
    def GetServerInformation(self):
        return ("hypr-notify", "hypr", "1.0", "1.2")

    @dbus.service.method('org.freedesktop.Notifications', in_signature='', out_signature='as')
    def GetCapabilities(self):
        return ["body"]

DBusGMainLoop(set_as_default=True)
loop = GLib.MainLoop()
NotificationDaemon()
loop.run()

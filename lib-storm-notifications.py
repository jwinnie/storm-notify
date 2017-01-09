
import dbus
import dbus.service
import dbus.mainloop.glib
from gi.repository import GObject

class handler:
    def __init__(self, function, name):

        # Initialize DBus
        dbus.mainloop.glib.DBusGMainLoop(set_as_default=True)
		bus_name = dbus.service.BusName(name, dbus.SessionBus())
		dbus.service.Object.__init__(self, bus_name, "/" + name.replace(".", "/"))
        
        # Subscribe to storm.notification-daemon     
        bus = dbus.SessionBus()
        session = bus.get_object("us.stormdesign.notification-daemon", "/us/stormdesign/notification-daemon")
        method = session.get_dbus_method("subscribe", "us.stormdesign.notification-daemon.subscribe")
        method(bus_name)

        # GObject MainLoop
        self._loop = GObject.MainLoop()
   		self._loop.run()

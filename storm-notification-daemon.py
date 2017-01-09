
import dbus
import dbus.service
import dbus.mainloop.glib
from gi.repository import GObject

class Daemon(dbus.service.Object):

    # Start the daemon
    def start(self):

        self._subscribers = []

        # Initialize DBus
        dbus.mainloop.glib.DBusGMainLoop(set_as_default=True)
		bus_name = dbus.service.BusName("us.stormdesign.notification-daemon", dbus.SessionBus())
		dbus.service.Object.__init__(self, bus_name, "/us/stormdesign/notification-daemon")
        
        # GObject MainLoop
        self._loop = GObject.MainLoop()
		print("storm.notification-daemon: Service started")
		self._loop.run()
		print("storm.notification-daemon: Service stopped")

    @dbus.service.method('us.stormdesign.notification-daemon.subscribe')
    def subscribe(self, bus_name):
        self._subscribers.append(bus_name)

    @dbus.service.method('us.stormdesign.notification-daemon.notify')
    def notify(self, title, body):
        # Use DBus to call notification_handler function of handler
        bus = dbus.SessionBus()
        for id in self._subscribers:
            session = bus.get_object(id, "/" + id.replace(".", "/"))
            method = session.get_dbus_method('notification_handler', id+'.notification_handler')
            method(title, body)

if __name__ == "__main__":
    daemon = Daemon()
    daemon.start()

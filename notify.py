
class Notification (object):
	def __init__(self, title, body, image, click_action):
		self.title = title
		self.body = body
		self.image = image
		self.click_action = click_action

class Daemon (object):
	def __init__(self):
		self.notifications = []
		self.callbacks = []
	def notify(self, notification):
		self.notifications.append(notification)
		for callback in self.callbacks:
			callback(notification)
	def wait_for_notification(self, callback):
		self.callbacks.append(callback)

local_daemon = Daemon()
def notification_handler(notification):
	print(notification.title)
	print(notification.body)
local_daemon.wait_for_notification(notification_handler)
while True:
	title = raw_input("title: ")
	body = raw_input("body: ")
	local_daemon.notify(Notification(title, body, "", ""))

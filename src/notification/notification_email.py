from notification.notification import Notification

class NotificationEmail(Notification):
    def send_notification(self, client_name, message):
        print(f"Send email for {client_name.name}: {message}")
from src.notification.notification import Notification

class NotificationSMS(Notification):
    def send_notification(self, client_name, message):
        print(f"Send SMS for {client_name.name}: {message}")
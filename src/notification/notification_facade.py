from src.notification.notification_email import NotificationEmail
from src.notification.notification_sms import NotificationSMS

class NotificationFacade:
    def __init__(self):
        self.notifications = [NotificationSMS(), NotificationEmail()]

    def send_notifications(self, client_name, message):
        for notification in self.notifications:
            notification.send_notification(client_name, message)
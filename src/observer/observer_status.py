class ObserverStatus:
    def __init__(self, notifications):
        self.notifications = notifications
    
    def update_status(self, order):
        message = f"Order updated, status: {order.status}"
        self.notifications.send_notifications(order.client_name, message)
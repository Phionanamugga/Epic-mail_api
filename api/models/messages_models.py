messages = []
sender_id = 1
received = []
receiver_id = 1
senders = []


class Message:
    def __init__(self, message_id, subject, message, created_on, status):
        self.message_id = message_id
        self.subject = subject
        self.message = message
        self.created_on = created_on
        self.status = status

    def get_details(self):
        return {
            "message_id": self.message_id,
            "subject": self.subject,  
            "message": self.message,
            "created_on": self.created_on,
            }


class Received(Message):
    def __init__(self, message_id, subject, message, 
                 created_on, status, received_id, sender_id):
        super().__init__(self, message_id, subject, message, 
                         created_on, status)
        self.message_id = received_id
        self.sender_id = sender_id
        sender_id += 1

    def get_received_message_details(self):
        details = dict()
        details["id"] = self.message_id
        details.update(super().get_details())
        return details


def get_all_received_messages(messages):
        for received_message in messages:
            result = received_message.get_received_message_details
            if received_message.received_id == received_id:
                return result
            else:
                return {"message": "you have not received any messages yet"}


def get_all_unread_received_messages(messages):
        for received_message in messages:
            data = request.get_json()
            data["status"] = "unread"
            record = received_message.get_received_message_details
            if received_message.status == data["status"]:
                return record
            else:
                return {"message": "you have not sent any message yet"}


class Sent(Message):
    def __init__(self, message_id, subject, message, 
                 created_on, status, receiver_id):
        super().__init__(self, message_id, subject, message, 
                         created_on, status)
        self.receiver_id = receiver_id
        receiver_id += 1

    def get_sent_message_details(self):
        details = dict()
        details["id"] = self.message_id
        details.update(super().get_details())
        return details


def get_all_sent_messages(messages):
        for sent_message in messages:
            data = request.get_json()
            data["status"] = "sent"
            result = sent_message.get_sent_message_details
            if sent_message.status == data["status"]:
                return result
            else:
                return {"message": "you have not received any messages yet"}
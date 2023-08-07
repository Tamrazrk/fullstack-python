class Phone:
    def __init__(self, phone_number):
        """creates new instalce of Phone with phone number and empty history"""
        self.phone_number = phone_number
        self.call_history = []
        self.messages = []

    def call(self, other_phone):
        """print calling record and save record to history"""
        call_record = f"{self.phone_number} called to {other_phone.phone_number}"
        self.call_history.append(call_record)  # save record to current phone
        other_phone.call_history.append(call_record)  # save record to other phone
        print(call_record)  # print call record

    def show_call_history(self):
        """print whole call history"""
        print("call history:")
        for record in self.call_history:
            print(record)

    def send_message(self, other_phone, content):
        """send content to other_phone as message and save the record to messages"""
        message_record = {
            "to": other_phone.phone_number,
            "from": self.phone_number,
            "content": content,
        }
        self.messages.append(message_record)
        other_phone.messages.append(message_record)

    def show_outgoing_messages(self):
        messages = filter(
            lambda record: record["from"] == self.phone_number, self.messages
        )
        print("outgoing messages:")
        for message in messages:
            print(message)

    def show_incoming_messages(self):
        messages = filter(
            lambda record: record["to"] == self.phone_number, self.messages
        )
        print("incoming messages:")
        for message in messages:
            print(message)

    def show_messages_from(self, other_phone):
        messages = filter(
            lambda record: record["from"] == other_phone.phone_number, self.messages
        )
        print(f"showing messages from {other_phone.phone_number}:")
        for message in messages:
            print(message)


# Example usage
phone1 = Phone("123-456-7890")
phone2 = Phone("987-654-3210")

phone1.call(phone2)
phone2.call(phone1)

phone1.show_call_history()
phone2.show_call_history()

phone1.send_message(phone2, "Hello, how are you?")
phone2.send_message(phone1, "Hi, I'm good! How about you?")
phone1.send_message(phone2, "Me too :)")

phone1.show_incoming_messages()
phone1.show_outgoing_messages()

phone2.show_messages_from(phone1)

# Интерфейс реализации
class MessageSender:
    def send(self, message: str):
        pass

# Конкретная реализация для отправки сообщений через Email
class EmailSender(MessageSender):
    def send(self, message: str):
        return f"Отправка email сообщения: {message}"

# Конкретная реализация для отправки сообщений через SMS
class SMSSender(MessageSender):
    def send(self, message: str):
        return f"Отправка SMS сообщения: {message}"

# Абстракция
class Message:
    def __init__(self, sender: MessageSender):
        self._sender = sender  # Хранит реализацию отправки сообщения

    def send_message(self, message: str):
        return self._sender.send(message)  # Делегирует отправку реализации


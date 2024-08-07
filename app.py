import PyQt6
from PyQt6.QtWidgets import QApplication, QMainWindow, QTextEdit, QLineEdit, QPushButton
import sys
class ChatbotWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Chatbot")
        self.setMinimumSize(700,500)

        self.chat_area = QTextEdit(self)
        self.input_field = QLineEdit(self)
        self.button = QPushButton("Send", self)
        self.show()

class ChatBot:
    pass

app = QApplication(sys.argv)
window = ChatbotWindow()
sys.exit(app.exec())

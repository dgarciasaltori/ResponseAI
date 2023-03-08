import sys
import openai
import time
from PyQt5.QtWidgets import (
    QApplication,
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QTextEdit,
    QPushButton,
)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QTextCursor
from halo import Halo

openai.api_key = "API-KEY"

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("OpenAI Question Answering")

        # Create widgets
        self.answer_label = QLabel("Resposta:")
        self.answer_output = QTextEdit()
        self.question_label = QLabel("Pergunta:")
        self.question_input = QLineEdit()
        self.answer_output.setReadOnly(True)
        self.answer_output.setLineWrapMode(QTextEdit.WidgetWidth)
        self.answer_output.setPlaceholderText(
            "As respostas serão exibidas aqui."
        )
        self.ask_button = QPushButton("Perguntar")
        self.ask_button.clicked.connect(self.get_answer)

        # Create layouts
        input_layout = QHBoxLayout()
        input_layout.addWidget(self.question_label)
        input_layout.addWidget(self.question_input)

        output_layout = QHBoxLayout()
        output_layout.addWidget(self.answer_label)
        output_layout.addWidget(self.answer_output)

        main_layout = QVBoxLayout()
        main_layout.addLayout(output_layout)
        main_layout.addLayout(input_layout)
        main_layout.addWidget(self.ask_button)

        # Set main layout
        self.setLayout(main_layout)

    def get_answer(self):
        question = self.question_input.text().strip()
        if not question:
            return

        context_question = question + " e mais alguma informação relevante"
        prompt = (f"Q: {context_question}\nA:")

        with Halo(text="Gerando resposta", spinner="dots"):
            response = openai.Completion.create(
                model="text-davinci-003",
                prompt=prompt,
                temperature=0,
                max_tokens=1024,
                top_p=1,
                frequency_penalty=0,
                presence_penalty=0,
                stop=["\n"],
            )

        answer = response.choices[0].text.strip()

        # Append answer to output
        self.answer_output.moveCursor(QTextCursor.End)
        self.answer_output.insertPlainText("> ")
        self.write_slowly(self.answer_output, answer)
        self.answer_output.insertPlainText("\n")

        # Clear input
        self.question_input.clear()

    def write_slowly(self, widget, text, delay=0.03):
        for char in text:
            widget.insertPlainText(char)
            widget.repaint()
            QApplication.processEvents()
            QApplication.processEvents()
            widget.moveCursor(QTextCursor.End)
            time.sleep(delay)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

"""
==========================================
StudentOS
Version 0.1.0
Developer: AK74

StudentOS is a lightweight operating system for SMART-CALC
designed for a handheld student device packed with useful
features and a seemless experience

Goals:
-Fast
-Simple
-Realible
-Keyboard-first
-Offline Device

Main Apps:
- Home
- Scientific Calculator
- Graphing Calculator
- Notes
- Formula Library
- Planner
- Flashcards
- Timer
- Settings
===========================================
"""

import sys

from PySide6.QtCore import Qt, QTimer
from PySide6.QtGui import QKeyEvent
from PySide6.QtWidgets import (
    QApplication,
    QWidget,
    QHBoxLayout,
    QVBoxLayout,
    QLabel,
    QPushButton,
    QListWidget,
    QStackedWidget,
)
from datetime import datetime

class BootScreen(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Booting StudentOS...")
        self.resize(600, 400)

        layout = QVBoxLayout(self)

        logo = QLabel("StudentOS")
        logo.setAlignment(Qt.AlignCenter)

        logo.setStyleSheet("""
            font-size: 40px;
            font-weight: bold;
        """)

        loading = QLabel("Starting SMART-CALCULATOR...")
        loading.setAlignment(Qt.AlignCenter)

        layout.addStretch()
        layout.addWidget(logo)
        layout.addWidget(loading)
        layout.addStretch()

        QTimer.singleShot(2000, self.start_os)

    def start_os(self):
        self.main = StudentOS()
        self.main.show()
        self.close()

class StudentOS(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("StudentOS")
        self.resize(600, 400)
        self.setStyleSheet("""
        QWidget {
    background: #1f1f1f;
    color: white;
    font-size: 14px;
}

QListWidget {
    background: #2a2a2a;
    border: none;
}

QListWidget::item {
    padding: 14px;
    margin: 3px;
}

QListWidget::item:selected {
    background: #3d6df2;
    border-radius: 8px;
}
        """)

        self.setup_ui()

    def setup_ui(self):
        main_layout = QVBoxLayout(self)
        top_bar = QWidget()
        top_bar.setFixedHeight(45)

        top_layout = QHBoxLayout(top_bar)

        title = QLabel("StudentOS")
        device = QLabel("SMART-CALC")
        version = QLabel("v0.1")

        self.clock = QLabel()

        self.update_clock()

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_clock)
        self.timer.start(1000)

        top_layout.addWidget(title)
        top_layout.addStretch()
        top_layout.addWidget(device)
        top_layout.addSpacing(20)
        top_layout.addWidget(self.clock)
        top_layout.addSpacing(20)
        top_layout.addWidget(version)

        self.sidebar = QListWidget()
        self.sidebar.setFixedWidth(200)

        apps = [
        "🏠 Home",
        "🧮 Scientific Calculator",
        "📈 Graphing Calculator",
        "📝 Notes",
        "📚 Formula Library",
        "📅 Planner",
        "⚙ Settings",
]

        self.sidebar.addItems(apps)

        self.pages = QStackedWidget()

        self.pages.addWidget(self.home_page())
        self.pages.addWidget(self.placeholder_page("Scientific Calculator"))
        self.pages.addWidget(self.placeholder_page("Graphing Calculator"))
        self.pages.addWidget(self.placeholder_page("Notes"))
        self.pages.addWidget(self.placeholder_page("Formula Library"))
        self.pages.addWidget(self.placeholder_page("Planner"))
        self.pages.addWidget(self.placeholder_page("Settings"))

        self.sidebar.currentRowChanged.connect(
                self.pages.setCurrentIndex
            )

        self.sidebar.setCurrentRow(0)

        content_layout = QHBoxLayout()

        content_layout.addWidget(self.sidebar)
        content_layout.addWidget(self.pages)

        main_layout.addWidget(top_bar)
        main_layout.addLayout(content_layout)

    def home_page(self):
        page = QWidget()

        layout = QVBoxLayout(page)

        title = QLabel("StudentOS")
        title.setAlignment(Qt.AlignCenter)
        title.setStyleSheet("""
                font-size: 34px;
                font-weight: bold;
""")
        welcome = QLabel("Welcome Back!")
        welcome.setAlignment(Qt.AlignCenter)
        welcome.setStyleSheet("""
        font-size:20px;
        """)

        apps = QLabel(""" 
        Quick Access

        🧮 Scientific Calculator
        📈 Graphing Calculator
        📝 Notes
        📚 Formula Library
        📅 Planner            

""")
        apps.setAlignment(Qt.AlignCenter)
        apps.setStyleSheet("""
            font-size: 18px;
        """)

        system = QLabel(
            """
            System Status

            Version 0.1.0
            Device: SMART-CALCULATOR
            STATUS: READY
            """
        )

        system.setAlignment(Qt.AlignCenter)

        layout.addStretch()
        layout.addWidget(title)
        layout.addWidget(welcome)
        layout.addSpacing(30)
        layout.addWidget(apps)
        layout.addSpacing(30)
        layout.addWidget(system)
        layout.addStretch()

        return page

    def placeholder_page(self, name):
            page = QWidget()

            layout = QVBoxLayout(page)

            title = QLabel(name)
            title.setAlignment(Qt.AlignCenter)
            title.setStyleSheet("""
            font-size:28px;
            font-weight:bold;
                """)

            info = QLabel("Coming Soon...")
            info.setAlignment(Qt.AlignCenter)

            layout.addStretch()
            layout.addWidget(title)
            layout.addWidget(info)
            layout.addStretch()

            return page

    def update_clock(self):
        current_time = datetime.now().strftime("%H:%M:%S")
        self.clock.setText(current_time)

    def keyPressEvent(self, event):
        key = event.key()

        if key == Qt.Key_Down:
            current = self.sidebar.currentRow()
            if current < self.sidebar.count() -1:
                self.sidebar.setCurrentRow(current + 1)

        elif key == Qt.Key_Up:
            current = self.sidebar.currentRow()
            if current > 0:
                self.sidebar.setCurrentRow(current -1)

        elif key == Qt.Key_Return:
            self.pages.setCurrentIndex(
                self.sidebar.currentRow()
            )

app = QApplication(sys.argv)

boot = BootScreen()
boot.show()

sys.exit(app.exec())
                
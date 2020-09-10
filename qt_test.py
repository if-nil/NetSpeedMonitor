from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QHBoxLayout
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt, QThread
import sys, psutil, time

class MainWindow(QWidget):
    def __init__(self):
        super(MainWindow, self).__init__()
        layout = QHBoxLayout(self)
        self.setLayout(layout)

        self.mem_label = QLabel('网速')
        self.net_label = QLabel('内存')

        layout.addWidget(self.mem_label)
        layout.addWidget(self.net_label)

        layout.setSpacing(0)

        self.mem_label.setMinimumSize(50, 25)
        self.mem_label.setAlignment(Qt.AlignCenter)

        
        self.net_label.setMinimumSize(85, 25)
        # 文本居中显示
        self.net_label.setAlignment(Qt.AlignCenter)

        font = QFont("黑体", 9)
        self.mem_label.setFont(font)
        self.net_label.setFont(font)

        self.mem_label.setText("0%")
        self.net_label.setText("0K/s")

        self.setWindowOpacity(1)
        
        from qss_example import example
        # 这里修改颜色
        self.mem_label.setStyleSheet(example("lightgrey").mem_lable)
        self.net_label.setStyleSheet(example("9cf").net_lable)

        self.setWindowFlags(Qt.FramelessWindowHint | Qt.Tool | Qt.WindowStaysOnTopHint)
        # 窗体背景透明
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setAutoFillBackground(False)
        self.__x_offset = 0
        self.__y_offset = 0
    def mousePressEvent(self, event):
        self.__x_offset = event.globalX() - self.pos().x()
        self.__y_offset = event.globalY() - self.pos().y()
    def mouseMoveEvent(self, event):
        self.move(event.globalX() - self.__x_offset, event.globalY() - self.__y_offset)

class SystemInfoThread(QThread):
    def __init__(self, window):
        super(SystemInfoThread, self).__init__()
        self.__win = window
    
    def run(self):
        old_net_speed = psutil.net_io_counters().bytes_recv
        while True:
            new_net_speed = psutil.net_io_counters().bytes_recv
            time.sleep(1)
            if new_net_speed - old_net_speed > 1024*1024:
                self.__win.net_label.setText("%.2fM/s" % ((new_net_speed - old_net_speed) / 1024 / 1024))
            else:
                self.__win.net_label.setText("%.2fK/s" % ((new_net_speed - old_net_speed) / 1024))
            self.__win.mem_label.setText(str(int(psutil.virtual_memory().used * 100 / psutil.virtual_memory().total)) + '%')
            old_net_speed = new_net_speed

if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys_info_thread = SystemInfoThread(win)
    sys_info_thread.start()
    sys.exit(app.exec())
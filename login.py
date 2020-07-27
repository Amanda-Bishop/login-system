# Import statements
from PyQt5.QtWidgets import * 
from PyQt5.QtGui import *
import sys, re
  
# Main class  
class Window(QMainWindow):
    # Initialization function
    def __init__(self): 
        super().__init__()
        self.title = 'Login System'
        self.x, self.y, self.w, self.h = 400, 300, 500, 300
        self.validEmail = False
        self.validPass = False
        self.initUI()                                               # Calls the UI initialization function

    # UI initialization function
    def initUI(self):
        # Sets the window dimensions and title
        self.setWindowTitle(self.title) 
        self.setGeometry(self.x, self.y, self.w, self.h)

        # Creates the text on the screen
        self.l1 = QLabel('Login', self) 
        self.l1.move(230, 10)
        self.l1.resize(40,30)

        self.l2 = QLabel('Email Address:', self) 
        self.l2.move(110, 50)

        self.l3 = QLabel('Password', self) 
        self.l3.move(110, 150)

        self.email = QLabel('Invalid email. The email must contain a username, domain, and extension. The username cannot contain special characters other than "-,.,_". The extension can only be 1-3 characters in length', self) 
        self.email.setGeometry(50, 25, 400, 200)
        self.email.setWordWrap(True)
        self.email.hide()                                           # Hides the error message

        self.pw = QLabel('Invalid password. The email must contain an uppercase letter, a lowercase letter, a number, and a special character. It must be 6-16 characters in length', self) 
        self.pw.setGeometry(50, 120, 400, 200)
        self.pw.setWordWrap(True)
        self.pw.hide()                                              # Hides the error message

        # Creates the submit button
        self.b1 = QPushButton('Submit', self)
        self.b1.move(210,250)
        self.b1.clicked.connect(self.onClick)                       # Connects the button to the onClick function
        self.b1.resize(80,30)

        # Creates the input boxes
        self.t1 = QLineEdit(self)
        self.t1.move(110, 75)
        self.t1.resize(280,20)

        self.t2 = QLineEdit(self)
        self.t2.move(110, 175)
        self.t2.resize(280,20)
        self.t2.setEchoMode(QLineEdit.Password)

        # Shows the window
        self.show()
        
    def onClick(self):
        # Calls the checkEmail and checkPass functions by taking the text in the input boxes
        self.validEmail = self.checkEmail(self.t1.text())
        self.validPass = self.checkPass(self.t2.text())
        # Displays the error messages if needed
        if not self.validEmail: 
            self.email.show()
        else:
            self.email.hide()
        if not self.validPass:
            self.pw.show()
        else:
            self.pw.hide()

    def checkEmail(self, txt):
        # Function to check if the email is valid
        email = txt.split('@')
        user = re.split('[-._]', email[0])
        try:
            domain = email[1].split('.')
        except:
            domain = None
        return len(email) == 2 and email[0][0].isalpha() and len(domain) == 2 and domain[0].isalpha() and domain[1].isalpha() and len(domain[1]) > 0 and len(domain[1]) < 4

    def checkPass(self, txt):
        # Function to check if the password is valid
        if len(txt) > 5 and len(txt) < 17 and re.search("[a-z]", txt) and re.search("[A-Z]", txt) and re.search("[0-9]", txt) and re.search("[!@#$%^&*]", txt):
            return True
        else:
            return False
            

# Runs the code  
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    sys.exit(app.exec())                                            # Quits the program


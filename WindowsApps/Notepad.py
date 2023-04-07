from pywinauto import Application
import datetime


class Notepad:
    __app = Application
    __last_saved_file_name = 'test' + datetime.datetime.now().strftime("%H%M%S%f")

    def __init__(self, application):
        self.__app = application
        self.dialog = self.__app.Dialog

    def create_new_file(self):
        self.dialog.menu_select("File->New")

    def save_file(self):
        self.dialog.menu_select("File->Save As")
        self.dialog.child_window(auto_id='1001', control_type="Edit").type_keys(self.__last_saved_file_name)
        self.dialog.Button15.click()
        return self.__last_saved_file_name

    def type_text(self, text):
        self.dialog.Edit.type_keys(text)

    def exit(self):
        self.dialog.menu_select("File->Exit")

    def open_file(self, file_path):
        self.dialog.menu_select('File->Open...')
        self.dialog.child_window(auto_id='1148', control_type="Edit").type_keys(file_path)
        self.dialog.Button14.click()

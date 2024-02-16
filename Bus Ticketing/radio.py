from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivymd.app import MDApp
from kivymd.uix.pickers import MDDatePicker

class MainWindow(Screen):
    pass
class LoginWindow(Screen):
    pass
class SignupWindow(Screen):
    pass
class TicketBuyWindow(Screen):
    pass
class ChooseBusWindow(Screen):
    pass
class WindowManager(ScreenManager):
    pass

class Bus(MDApp):

    def build(self):
        self.theme_cls.theme_style = "Light"
        self.theme_cls.primary_palette = "Purple"
        kv = Builder.load_file('bus.kv')
        return kv
    
    #Login validation
    def logger(self,username,passwd):
        login_window = MDApp.get_running_app().root.get_screen('login')
        signup_window = MDApp.get_running_app().root.get_screen('signup')
        if(username==signup_window.ids.sign_user.text and passwd==signup_window.ids.sign_password.text):
            self.root.current = 'buy_ticket'
        else:
            login_window.ids.welcome_label.text = f'Wrong Username and Password'
    

    #Date picker
    def on_save(self,instace, value, date_range):
        tickets = MDApp.get_running_app().root.get_screen('buy_ticket')
        tickets.ids.date.text = str(value)
    def show_date_picker(self):
        date_dialog = MDDatePicker()
        date_dialog.bind(on_save = self.on_save)
        date_dialog.open()

Bus().run()
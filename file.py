from kivy.app import App

from kivy.uix.screenmanager import Screen, ScreenManager


class Gerenciador(ScreenManager):
    pass

class BoasVindas(Screen):
    pass

class Login(Screen):
    def logar(self, usuario, senha):
        print("usuario={0}, senha={1}".format(usuario, senha))

class Resultado(Screen):
    pass

class LoginApp(App):

    def build(self):
       return Gerenciador()

LoginApp().run()
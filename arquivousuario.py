from kivy.app import App
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.lang.builder import Builder
from kivy.uix.checkbox import CheckBox
from random import randint
import json
from kivy.core.window import Window

Window.softinput_mode = 'below_target'

Builder.load_string('''

<ScreenManager>:
    
    BoasVindas:
        name:'boasvindas'
        BoxLayout:
            orientation:'vertical'
            BoxLayout:
                Label:
                    text:'Faça o seu Login ou crie uma nova conta'
            BoxLayout:
                padding:30
                spacing:30
                orientation:'vertical'
                BoxLayout:
                    spacing:30    
                    Button:
                        id:loginBtn
                        text:'Login'
                        on_release:root.current='login'
                    Button:
                        text:'Criar nova conta'
                        on_release:root.current='criar_conta'
                BoxLayout:
                    spacing:30
                    Button:
                        text:'Mostrar Usuário'
                        id:mostrar
                        on_release:root.current='mostrar'
                        
                    Button:
                        text:'Sair'
                        on_release:exit()
                
    Mostrar:
        name:'mostrar'
        mostrar:id_lbl_mostrar
        BoxLayout:
            spacing:30
            padding:40
            orientation:'vertical'
            BoxLayout:
                TextInput:
                    id:identidade
                    multiline: False
                    size_hint_y:0.2
                Button:
                    id:ok
                    text:'Ok'
                    size_hint_y:0.2
                    on_release:root.ids.identidade.text=''
                    on_release:root.display(identidade.text)
                    #on_release:root.current = 'resultpesq'
            BoxLayout:
                size_hint_y:0.2
                Button:
                    text:'Voltar'
                    on_release:root.current = 'boasvindas'
                    on_release:root.ids.identidade.text=''
            BoxLayout:    
                Label:
                    id: id_lbl_mostrar
                    text:''
    
    Resultado_pesquisa:
        name:'resultadopesq'
        BoxLayout:
            orientation:'vertical'
            BoxLayout:
                Label:
                    text:'Nome'
                Label:
                    id:nome_usr
                    text:'separar o nome do usuario'
            BoxLayout:
                Label:
                    text:'Sobrenome'
                Label:
                    id:sobrenome_usr
                    text:'separar o sobrenome do usuario no dicionario'
            BoxLayout:
                Label: 
                    text:'Sexo'
                Label:
                    id:sexo_usr
                    text:'puxar o sexo do checkbox no kivy'
            BoxLayout:
                Label:
                    text:'Data de nascimento'
                Label:
                    id:nascimento_usr
                    text:'separar a data de nascimento do usuario'
                          
    
    Login:
        name:"login"
        BoxLayout:
            
            size_hint_y:0.5
            orientation:"vertical"
            padding:40
            spacing:20
            TextInput:
                id:usuario
                size_hint_x:0.5
                hint_text:'Usuário'
                multiline: False
                write_tab: False
            TextInput:
                size_hint_x:0.5
                id:senha
                hint_text:'Senha'
                multiline: False
                write_tab: False
                password: True
            Button:
                id:btn
                size_hint_x:0.5
                text:'Ok'
                on_press:self.parent.parent.logar(usuario.text, senha.text)
                on_release:root.current='boasvindas'
                on_release:root.ids.senha.text = ''
                on_release:root.ids.usuario.text = ''
                
            
            Button:
                size_hint_x:0.5
                id:'voltar'
                text:'Voltar'
                on_release:root.current='boasvindas'
                on_release:root.ids.senha.text = ''
                on_release:root.ids.usuario.text = ''
        
    Criar_conta:
        name:'criar_conta'
        BoxLayout:
            padding:30
            spacing:20
            orientation:'vertical'
            BoxLayout:
                Label:
                    text:'Nome'
                TextInput:
                    id:nome
                    hint_text:"Nome"
                    multiline: False
                    write_tab: False
            BoxLayout:
                Label:
                    text:'Sobrenome'
                TextInput:
                    id:sobrenome
                    hint_text:"Sobrenome"
                    multiline: False
                    write_tab: False
            BoxLayout:
                Label:
                    text:'Data de nascimento'
                TextInput:
                    id:dia
                    multiline: False
                    hint_text: "Dia"
                    write_tab: False
                TextInput:
                    id:mes
                    multiline: False
                    hint_text: "Mês"
                    write_tab: False
                TextInput:
                    id:ano
                    hint_text:"Ano"
                    multiline: False
                    write_tab: False
            BoxLayout:
                Label:
                    text:'Sexo'
                Label:
                    text:'Masculino'
                CheckBox:
                    id:masc
                    text:'Masculino'
                    group:'sex'
                    on_active:self.parent.parent.parent.ids.sex.text = ("Masculino")
                Label:
                    text:'Feminino'
                CheckBox:
                    id:fem
                    value:"Feminino"
                    text:'Feminino'
                    group:'sex'
                    on_active:self.parent.parent.parent.ids.sex.text = ("Feminino")
                    
            BoxLayout:
                Label:
                    text:'O sexo escolhido foi'
                Label:
                    text:''
                    id:sex
            BoxLayout:
                Label:
                    text:'Nome de usuário'
                TextInput:
                    id:cadastro_usuario
                    hint_text:'Usuario'
                    multiline: False
                    write_tab: False
                    
            BoxLayout:
            
                Label:
                    text:'Senha'
                    
                TextInput:
                    id:cadastro_senha
                    hint_text:'Senha'
                    multiline: False
                    write_tab: False
                    password: True
                            
            Button:
                text:'Voltar'
                on_release:root.current = 'boasvindas'
                on_release:self.parent.parent.ids.nome.text=''
                on_release:self.parent.parent.ids.sobrenome.text=''
                on_release:self.parent.parent.ids.dia.text=''
                on_release:self.parent.parent.ids.mes.text=''
                on_release:self.parent.parent.ids.ano.text=''
                on_release:self.parent.parent.ids.sex.text=''
                    
            Button:
                text:'Cadastrar usuário'
                on_release:self.parent.parent.ids.nome.text=''
                on_release:self.parent.parent.ids.sobrenome.text=''  
                on_release:self.parent.parent.ids.dia.text=''  
                on_release:self.parent.parent.ids.mes.text=''  
                on_release:self.parent.parent.ids.ano.text=''
                on_release:self.parent.parent.ids.sex.text=''
                on_release:self.parent.parent.ids.cadastro_senha.text=''
                on_release:self.parent.parent.ids.cadastro_usuario.text=''
                on_release:self.parent.parent.cadastros(nome.text, sobrenome.text, sex.text, dia.text, mes.text, ano.text, cadastro_usuario.text, cadastro_senha.text)       
''')

from random import randint
ident = randint(10000, 99999)
dicionario1 = {}
a = {ident: {}}
cadastro_usuariod = {ident: {}}
cadastro_senhad = {ident: {}}
logado = True
usuario = ''
senha = ''
class BoasVindas(Screen):
    def status(self,state):
        logado = state
        if logado == True:
            self.ids.login_btn.text = 'Logout'
        else:
            self.ids.login_btn.text = 'Login'
        print(logado)

class Login(Screen):
    def logar(self, usuario, senha):
        identificador = ''
        with open("usuario.json", "r") as f:
            usr = json.load(f)
            for keys, values in usr.items():
                if values == usuario:
                    identificador = keys

        with open("senhas.json", "r") as fi:
            senhas = json.load(fi)
            for keys, values in senhas.items():
                if keys == identificador and values == senha:
                    print('YESSSSSSSSSSSSSS')
                    return True


class Criar_conta(Screen):


    def cadastros(self, nome, sobrenome, sexo, nas_dia, nas_mes, nas_ano, cadastro_usuario, cadastro_senha):

        with open("usuario.json", "r") as uf:
            u = json.load(uf)

        with open("usuario.json", "w") as fu:
            cadastro_usuariod[ident] = cadastro_usuario
            u.update(cadastro_usuariod)
            json.dump(u, fu, indent=4)

        with open("senhas.json", "r") as us:
            sen = json.load(us)

        with open("senhas.json", "w") as se:
            cadastro_senhad[ident] = cadastro_senha
            sen.update(cadastro_senhad)
            json.dump(sen, se, indent=4)


        with open('teste.json', 'r') as f:
            b = json.load(f)
            print(a)

        with open('teste.json', 'w') as f:
            dicionario1["Nome"] = nome
            dicionario1["Sobrenome"] = sobrenome
            dicionario1["Data de nascimento"] = f'{nas_dia}/{nas_mes}/{nas_ano}'
            dicionario1["Sexo"] = sexo
            a[ident] = dicionario1
            b.update(a)
            json.dump(b, f, indent=4)
            return a

class Resultado(Screen):
    pass





class Mostrar(Screen):

    def display(self, identidade):
        if identidade == "":
            with open("teste.json", "r") as f:
                g = json.load(f)
                print(json.dumps(g, indent=4, sort_keys=True))

            print(str(g))
        try:
            with open('teste.json', 'r') as f:
                c = json.load(f)
                d = str(identidade)
                self.ids.id_lbl_mostrar.text = str(c[d]["Nome"] + " " + c[d]["Sobrenome"] + '\n' + c[d]["Data de nascimento"] + '\n' + c[d]["Sexo"])
        except KeyError:
            pass

class Resultado_pesquisa(Screen):
    pass


sm = ScreenManager()
sm.add_widget(BoasVindas(name='boasvindas'))
sm.add_widget(Login(name='login'))
sm.add_widget(Criar_conta(name='criar_conta'))
sm.add_widget(Mostrar(name='mostrar'))
sm.add_widget(Resultado_pesquisa(name = 'resultpesq'))


class TesteLogin(App):

    def build(self):
        return sm

TesteLogin().run()

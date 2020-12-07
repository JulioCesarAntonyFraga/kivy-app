from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.uix.screenmanager import Screen,ScreenManager
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton
from kivy.storage.jsonstore import JsonStore
from kivymd.uix.picker import MDDatePicker
from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout
from kivymd.theming import ThemableBehavior
from kivymd.uix.card import MDCardSwipe
from kivymd.uix.list import IRightBodyTouch
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.expansionpanel import MDExpansionPanel, MDExpansionPanelThreeLine
from kivymd import images_path
from kivy.uix.widget import Widget
from kivymd.uix.list import OneLineListItem, MDList, TwoLineListItem, ThreeLineListItem, ThreeLineIconListItem
from kivymd.uix.list import OneLineIconListItem, IconLeftWidget
from kivy.uix.scrollview import ScrollView
from kivy.clock import Clock


############IMPORT ARQUIVOS LOCAIS############



##################TELAS APP####################
class WelcomeScreen(Screen):
    pass
class UsernameScreen(Screen):
    pass
class DOB(Screen):
    pass

class Screen1(Screen):      #####CHECKLISTS######
    pass
class Screen2(Screen):      #####MINHAS CHECKLISTS#####
    pass
class Screen3(Screen):     #####CHECKLIST SELECIONADA#####
    pass

class Screen5(Screen):
    pass

class CreateCheckList(ThreeLineIconListItem):
    pass

class ChecklistName(Screen):     #####NOME CHECKLIST#####
    pass

class ChecklistItem1(Screen):     #####ITEM 1 NOVA LV#####
    pass

class ChecklistItem2(Screen):     #####ITEM 1 NOVA LV#####
    pass

class ChecklistItem3(Screen):     #####ITEM 1 NOVA LV#####
    pass

class ChecklistItem4(Screen):     #####ITEM 1 NOVA LV#####
    pass

class ChecklistItem5(Screen):     #####ITEM 1 NOVA LV#####
    pass

class ChecklistItem6(Screen):     #####ITEM 1 NOVA LV#####
    pass

class ChecklistItem7(Screen):     #####ITEM 1 NOVA LV#####
    pass
class ChecklistItem8(Screen):     #####ITEM 1 NOVA LV#####
    pass
class ChecklistItem9(Screen):     #####ITEM 1 NOVA LV#####
    pass


#######INTEGRANDO TELAS NO GERENCIADOR DE SCREEN########
sm = ScreenManager()
sm.add_widget(WelcomeScreen(name = 'welcomescreen'))
sm.add_widget(UsernameScreen(name = 'usernamescreen'))
sm.add_widget(DOB(name = 'dob'))
sm.add_widget(Screen1(name = 'screen1'))
sm.add_widget(Screen2(name = 'screen2'))
sm.add_widget(Screen3(name = 'screen3'))

sm.add_widget(Screen5(name = 'screen5'))
sm.add_widget(ChecklistName(name = 'checklistName'))
sm.add_widget(ChecklistItem1(name = 'checklistItem1'))
sm.add_widget(ChecklistItem2(name = 'checklistItem2'))
sm.add_widget(ChecklistItem3(name = 'checklistItem3'))
sm.add_widget(ChecklistItem4(name = 'checklistItem4'))
sm.add_widget(ChecklistItem5(name = 'checklistItem5'))
sm.add_widget(ChecklistItem6(name = 'checklistItem6'))
sm.add_widget(ChecklistItem7(name = 'checklistItem7'))
sm.add_widget(ChecklistItem8(name = 'checklistItem8'))
sm.add_widget(ChecklistItem9(name = 'checklistItem9'))


############MAQUINARIO APP########################
class PawareApp(MDApp):

    def get_date(self, date):
        '''
        :type date: <class 'datetime.date'>
        '''

    def show_date_picker(self):
        date_dialog = MDDatePicker(callback=self.get_date)
        date_dialog.open()

    def build(self):
        self.strng = Builder.load_file('conteudos.kv') #####CARREGANDO KV DAS TELA####
        return self.strng
    

    ###############DETALHES DO PERFIL ##############
    try:
        store = JsonStore("userProfile.json")
        nome_perfil = store.get('UserInfo')['name']
        email_perfil = store.get('UserInfo')['email']
    except:
        nome_perfil = "Usuário desconhecido"
        email_perfil = "Email não cadastrado"
        


    #####INICIO DO APP CARREGANDO PERFIL E CADASTRO####
    def on_start(self):                   
        self.store = JsonStore("userProfile.json")
        try:
            if self.store.get('UserInfo')['name'] != "":
                #self.load_checklists_screen_main()
                self.load_checklists_my_checklists()
                self.strng.get_screen('screen1').manager.current = 'screen1'
                
        except KeyError:
            self.strng.get_screen('welcomescreen').manager.current = 'welcomescreen'   

    #########PREENCHIMENTO NOME OBRIGATORIO FUNCAO############
    def check_username(self):
        self.username_text = self.strng.get_screen('usernamescreen').ids.username_text_fied.text
        username_check_false = True
        try:
            int(self.username_text)
        except:
            username_check_false = False
        if username_check_false or self.username_text.split() == []:
                cancel_btn_username_dialogue = MDFlatButton(text='OK',on_release = self.close_username_dialogue)
                self.dialog = MDDialog(title = 'Nome inválido',text = "Por favor preencha um nome válido",size_hint = (0.7,0.2),buttons = [cancel_btn_username_dialogue])
                self.dialog.open()

        else:
            self.strng.get_screen('usernamescreen').ids.disabled_button.disabled = False

    #################BLOCO DE AVISO NOME INVALIDO##################
    def close_username_dialogue(self,obj):
        self.dialog.dismiss()
        
    
    def get_email(self):
        self.email_text = self.strng.get_screen('dob').ids.email_text_fied.text
        username_check_false = True
        try:
            int(self.username_text)
        except:
            username_check_false = False
        if username_check_false or self.email_text.split() == []:
                cancel_btn_username_dialogue = MDFlatButton(text='OK',on_release = self.close_username_dialogue)
                self.dialog = MDDialog(title = 'Email inválido',text = "Por favor preencha um email válido",size_hint = (0.7,0.2),buttons = [cancel_btn_username_dialogue])
                self.dialog.open()

        else:
            self.strng.get_screen('dob').ids.disabled_button.disabled = False

        ###############SALVANDO EM UM ARQUIVO OS DADOS LOGIN#################
        self.store.put('UserInfo',name = self.username_text, email = self.email_text)
        
        
 
    ############CARREGANDO E CRIANDO CHECKLIST DO BANCO DE DADOS####################
   
     

    def load_checklists_my_checklists(self):
        ######BUSCANDO NO BANCO AS CHECKLIST############
        checklists_data = ('APR 02', 'Gabriel', '11/03/2020')
        list_name = checklists_data[0]
        criado_por = checklists_data[1]
        criado_em = checklists_data[2]

        ########ADCIONANDO WIDGET CHECKLIST###########
        for i in range(6):
            my_check_list = ThreeLineIconListItem(
            text=list_name,
            secondary_text='Responsável: ' + criado_por,
            tertiary_text='Data de emissão: ' + criado_em, on_release=self.change_screen)
            my_check_list.add_widget(IconLeftWidget(icon='check-box-outline'))
            self.strng.get_screen('screen2').ids.my_checklists.add_widget(my_check_list)

    ##########DELETA CHECKLIST NA TELA SCREEN1######################
    def remove_checklist (self, ThreeLineIconListItem):
        self.strng.get_screen('screen2').ids.my_checklists.remove_widget(ThreeLineIconListItem)
        self.strng.get_screen('screen2').ids.my_checklists.clear_widgets()
      
        

    ############AO SELECIONAR UMA CHECKLIST MUDANDO DE TELA##########
    def change_screen(self, ThreeLineIconListItem):
        self.strng.get_screen('screen3').manager.current = 'screen3'

    ###############MUDANDO A TELA PARA INICIAR A VERIFICACAO###########
    def start_checklist(self):
        self.strng.get_screen('screen5').manager.current = 'screen5'
       
    class ContentNavigationDrawer(BoxLayout):  #######PERFIL########
        pass

    class DrawerList(ThemableBehavior, MDList): ######lISTAS DE AÇÕES DO PERFIL######
        pass

    


PawareApp().run()
import pymongo
from kivymd.uix.snackbar import Snackbar
from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.uix.screenmanager import Screen, ScreenManager
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton, MDRaisedButton, MDFloatingActionButton
from kivy.storage.jsonstore import JsonStore
from kivymd.uix.picker import MDDatePicker
from datetime import date
from kivymd.utils import asynckivy
from kivy.uix.boxlayout import BoxLayout
from kivymd.theming import ThemableBehavior
from kivymd.uix.card import MDCardSwipe
from kivymd.uix.textfield import MDTextField
from kivymd.uix.list import IRightBodyTouch
from kivymd.uix.list import StringProperty, TwoLineAvatarIconListItem
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.expansionpanel import MDExpansionPanel, MDExpansionPanelThreeLine, MDExpansionPanelOneLine
from kivymd import images_path
from kivy.uix.widget import Widget
from kivymd.uix.list import OneLineListItem, MDList, TwoLineListItem, ThreeLineListItem, ThreeLineIconListItem
from kivymd.uix.list import OneLineIconListItem, IconLeftWidget
from kivy.uix.scrollview import ScrollView
from kivy.clock import Clock
from bson import ObjectId
from datetime import date
from kivy.animation import Animation



class Content(BoxLayout):
    pass


##################TELAS APP####################
class WelcomeScreen(Screen):
    pass


class UsernameScreen(Screen):
    pass


class DOB(Screen):
    pass


class Profile(Screen):  #####PERFIL#####
    pass


class Screen1(Screen):  #####CHECKLISTS######
    pass


class Screen2(Screen):  #####MINHAS CHECKLISTS#####
    pass


class Screen3(Screen):  #####CHECKLIST SELECIONADA#####
    pass


class Screen5(Screen):
    pass


class CreateCheckList(ThreeLineIconListItem):
    pass


class ChecklistName(Screen):  #####NOME CHECKLIST#####
    pass


class ChecklistItem1(Screen):  #####ITEM 1 NOVA LV#####
    pass


class ChecklistItem2(Screen):  #####ITEM 1 NOVA LV#####
    pass


class ChecklistItem3(Screen):  #####ITEM 1 NOVA LV#####
    pass


class ChecklistItem4(Screen):  #####ITEM 1 NOVA LV#####
    pass


class ChecklistItem5(Screen):  #####ITEM 1 NOVA LV#####
    pass


class ChecklistItem6(Screen):  #####ITEM 1 NOVA LV#####
    pass


class ChecklistItem7(Screen):  #####ITEM 1 NOVA LV#####
    pass


class ChecklistItem8(Screen):  #####ITEM 1 NOVA LV#####
    pass


class ChecklistItem9(Screen):  #####ITEM 1 NOVA LV#####
    pass


class CustomItem(TwoLineAvatarIconListItem):
    icon = StringProperty('')

#######INTEGRANDO TELAS NO GERENCIADOR DE SCREEN########
sm = ScreenManager()
sm.add_widget(WelcomeScreen(name='welcomescreen'))
sm.add_widget(UsernameScreen(name='usernamescreen'))
sm.add_widget(DOB(name='dob'))
sm.add_widget(Profile(name='profile'))
sm.add_widget(Screen1(name='screen1'))
sm.add_widget(Screen2(name='screen2'))
sm.add_widget(Screen3(name='screen3'))
sm.add_widget(Screen5(name='screen5'))
sm.add_widget(ChecklistName(name='checklistName'))
sm.add_widget(ChecklistItem1(name='checklistItem1'))
sm.add_widget(ChecklistItem2(name='checklistItem2'))
sm.add_widget(ChecklistItem3(name='checklistItem3'))
sm.add_widget(ChecklistItem4(name='checklistItem4'))
sm.add_widget(ChecklistItem5(name='checklistItem5'))
sm.add_widget(ChecklistItem6(name='checklistItem6'))
sm.add_widget(ChecklistItem7(name='checklistItem7'))
sm.add_widget(ChecklistItem8(name='checklistItem8'))
sm.add_widget(ChecklistItem9(name='checklistItem9'))


############MAQUINARIO APP########################
class PawareApp(MDApp):
    panel_is_open = False

    try:
        name_perfil_toolbar = "Desconhecido"
        email_perfil_toolbar = "Desconhecido"
    except:
        pass


    def panel_open(self, *args):
        self.panel_is_open = True

    def panel_close(self, *args):
        self.panel_is_open = False

    def delete_item(self, item):
        self.panel.content.remove_widget(item)
        self.panel.height -= item.height
        for index, val in enumerate(self.panel.content.children[::-1]):
            val.secondary_text = str(index + 1)



    def update(self):
        async def update():
            await asynckivy.sleep(1)
            try:
                self.store = JsonStore("userProfile.json")
                nome = self.store.get('UserInfo')['name']
                email = self.store.get('UserInfo')['email']

                self.strng.get_screen('profile').ids.profile_name_input.text = nome
                self.strng.get_screen('profile').ids.profile_email_input.text = email

            except Exception as erro:
                print(erro)

        asynckivy.start(update())

    def set_refresh(self):
        async def set_refresh():
            await asynckivy.sleep(1)
            try:
                self.store = JsonStore("userProfile.json")
                nome = self.store.get('UserInfo')['name']
                email = self.store.get('UserInfo')['email']

                await asynckivy.sleep(1)
                self.strng.get_screen('profile').ids.name_perfil_toolbar.text = nome
                self.strng.get_screen('profile').ids.email_perfil_toolbar.text = email

                self.strng.get_screen('screen1').ids.name_perfil_toolbar.text = nome
                self.strng.get_screen('screen1').ids.email_perfil_toolbar.text = email

                self.strng.get_screen('screen2').ids.name_perfil_toolbar.text = nome
                self.strng.get_screen('screen2').ids.email_perfil_toolbar.text = email

                self.strng.get_screen('screen3').ids.name_perfil_toolbar.text = nome
                self.strng.get_screen('screen3').ids.email_perfil_toolbar.text = email

                self.strng.get_screen('screen5').ids.name_perfil_toolbar.text = nome
                self.strng.get_screen('screen5').ids.email_perfil_toolbar.text = email

                self.strng.get_screen('checklistName').ids.name_perfil_toolbar.text = nome
                self.strng.get_screen('checklistName').ids.email_perfil_toolbar.text = email

                self.strng.get_screen('profile').ids.profile_name_input.text = nome
                self.strng.get_screen('profile').ids.profile_email_input.text = email

            except Exception as erro:
                print(erro)

        asynckivy.start(set_refresh())

    def update_profile(self):
        name = self.strng.get_screen('profile').ids.profile_name_input.text
        email = self.strng.get_screen('profile').ids.profile_email_input.text
        self.store.put('UserInfo', name=name, email=email)
        self.set_refresh()

        #######################CARREGAMENTO E CONTRUCAO AO INICIAR O APP##############

    def build(self):
        self.strng = Builder.load_file('conteudos.kv')
        return self.strng

    #############FUNCAO AO INICIAR O APP ELE VAI CARREGAR ISSO ANTES DE MOSTRAR TELA#################
    def on_start(self):

        self.load_checklist()
        self.set_refresh()
        self.update()      
        self.store = JsonStore("userProfile.json")
        try:
            if self.store.get('UserInfo')['name'] != "":
                print(self.store.get('UserInfo')['name'])
                self.strng.get_screen('screen1').manager.current = 'screen1'
            else:
                print(self.store.get('UserInfo')['name'])
                self.strng.get_screen('welcomescreen').manager.current = 'welcomescreen'
        except:
            self.strng.get_screen('welcomescreen').manager.current = 'welcomescreen'

    def clear_items_inputs(self):
        if self.strng.get_screen('checklistItem1').ids.radio_item1_c.active or self.strng.get_screen(
                'checklistItem1').ids.radio_item1_na.active:
            self.strng.get_screen('checklistItem1').ids.acao_item1.text = ''
            self.strng.get_screen('checklistItem1').ids.responsavel_item1.text = ''
            self.strng.get_screen('checklistItem1').ids.prazo_item1.text = ''

        if self.strng.get_screen('checklistItem2').ids.radio_item2_c.active or self.strng.get_screen(
                'checklistItem2').ids.radio_item2_na.active:
            self.strng.get_screen('checklistItem2').ids.acao_item2.text = ''
            self.strng.get_screen('checklistItem2').ids.responsavel_item2.text = ''
            self.strng.get_screen('checklistItem2').ids.prazo_item2.text = ''

        if self.strng.get_screen('checklistItem3').ids.radio_item3_c.active or self.strng.get_screen(
                'checklistItem3').ids.radio_item3_na.active:
            self.strng.get_screen('checklistItem3').ids.acao_item3.text = ''
            self.strng.get_screen('checklistItem3').ids.responsavel_item3.text = ''
            self.strng.get_screen('checklistItem3').ids.prazo_item3.text = ''

        if self.strng.get_screen('checklistItem4').ids.radio_item4_c.active or self.strng.get_screen(
                'checklistItem4').ids.radio_item4_na.active:
            self.strng.get_screen('checklistItem4').ids.acao_item4.text = ''
            self.strng.get_screen('checklistItem4').ids.responsavel_item4.text = ''
            self.strng.get_screen('checklistItem4').ids.prazo_item4.text = ''

        if self.strng.get_screen('checklistItem5').ids.radio_item5_c.active or self.strng.get_screen(
                'checklistItem5').ids.radio_item5_na.active:
            self.strng.get_screen('checklistItem5').ids.acao_item5.text = ''
            self.strng.get_screen('checklistItem5').ids.responsavel_item5.text = ''
            self.strng.get_screen('checklistItem5').ids.prazo_item5.text = ''

        if self.strng.get_screen('checklistItem6').ids.radio_item6_c.active or self.strng.get_screen(
                'checklistItem6').ids.radio_item6_na.active:
            self.strng.get_screen('checklistItem6').ids.acao_item6.text = ''
            self.strng.get_screen('checklistItem6').ids.responsavel_item6.text = ''
            self.strng.get_screen('checklistItem6').ids.prazo_item6.text = ''

    class ContentNavigationDrawer(BoxLayout):  #######PERFIL########
        pass

    class DrawerList(ThemableBehavior, MDList):  ######lISTAS DE AÇÕES DO PERFIL######
        pass

    def check_lv_name_and_description(self):
        print(self.strng.get_screen('checklistName').ids.name_text_field_lv.text)
        print(self.strng.get_screen('checklistName').ids.descricao_text_field_lv.text)
        if self.strng.get_screen('checklistName').ids.name_text_field_lv.text != '' and self.strng.get_screen(
                'checklistName').ids.descricao_text_field_lv.text != '':
            self.strng.get_screen('checklistName').ids.lv_name_button.disabled = False

        else:
            self.strng.get_screen('checklistName').ids.lv_name_button.disabled = True

    def add_new_lv(self):
        conformes = 0
        nao_conformes = 0
        nao_aplicaveis = 0
        myclient = pymongo.MongoClient(
            "mongodb+srv://julio:senha@cluster0.pn3vb.mongodb.net/kivyapp?retryWrites=true&w=majority")
        db = myclient["kivyapp"]
        col_lv = db["lvs"]

        today = str(date.today())

        self.store = JsonStore("userProfile.json")
        nome = self.store.get('UserInfo')['name']
        email = self.store.get('UserInfo')['email']

        lv_name = self.strng.get_screen(f'checklistName').ids.name_text_field_lv.text
        lv_descricao = self.strng.get_screen(f'checklistName').ids.descricao_text_field_lv.text

        item1_acao = self.strng.get_screen(f'checklistItem1').ids.acao_item1.text
        item1_responsavel = self.strng.get_screen(f'checklistItem1').ids.responsavel_item1.text
        item1_prazo = self.strng.get_screen(f'checklistItem1').ids.prazo_item1.text

        item2_acao = self.strng.get_screen(f'checklistItem2').ids.acao_item2.text
        item2_responsavel = self.strng.get_screen(f'checklistItem2').ids.responsavel_item2.text
        item2_prazo = self.strng.get_screen(f'checklistItem2').ids.prazo_item2.text

        item3_acao = self.strng.get_screen(f'checklistItem3').ids.acao_item3.text
        item3_responsavel = self.strng.get_screen(f'checklistItem3').ids.responsavel_item3.text
        item3_prazo = self.strng.get_screen(f'checklistItem3').ids.prazo_item3.text

        item4_acao = self.strng.get_screen(f'checklistItem4').ids.acao_item4.text
        item4_responsavel = self.strng.get_screen(f'checklistItem4').ids.responsavel_item4.text
        item4_prazo = self.strng.get_screen(f'checklistItem4').ids.prazo_item4.text

        item5_acao = self.strng.get_screen(f'checklistItem5').ids.acao_item5.text
        item5_responsavel = self.strng.get_screen(f'checklistItem5').ids.responsavel_item5.text
        item5_prazo = self.strng.get_screen(f'checklistItem5').ids.prazo_item5.text

        item6_acao = self.strng.get_screen(f'checklistItem6').ids.acao_item6.text
        item6_responsavel = self.strng.get_screen(f'checklistItem6').ids.responsavel_item6.text
        item6_prazo = self.strng.get_screen(f'checklistItem6').ids.prazo_item6.text

        item7_acao = self.strng.get_screen(f'checklistItem7').ids.acao_item7.text
        item7_responsavel = self.strng.get_screen(f'checklistItem7').ids.responsavel_item7.text
        item7_prazo = self.strng.get_screen(f'checklistItem7').ids.prazo_item7.text

        item8_acao = self.strng.get_screen(f'checklistItem8').ids.acao_item8.text
        item8_responsavel = self.strng.get_screen(f'checklistItem8').ids.responsavel_item8.text
        item8_prazo = self.strng.get_screen(f'checklistItem8').ids.prazo_item8.text

        item9_acao = self.strng.get_screen(f'checklistItem9').ids.acao_item9.text
        item9_responsavel = self.strng.get_screen(f'checklistItem9').ids.responsavel_item9.text
        item9_prazo = self.strng.get_screen(f'checklistItem9').ids.prazo_item9.text

        item1_resultado = ''
        item2_resultado = ''
        item3_resultado = ''
        item4_resultado = ''
        item5_resultado = ''
        item6_resultado = ''
        item7_resultado = ''
        item8_resultado = ''
        item9_resultado = ''

        #################conformes#################
        if self.strng.get_screen('checklistItem1').ids.radio_item1_c.active == True:
            item1_resultado = 'Conforme'
            conformes += 1

        if self.strng.get_screen('checklistItem2').ids.radio_item2_c.active == True:
            item2_resultado = 'Conforme'
            conformes += 1

        if self.strng.get_screen('checklistItem3').ids.radio_item3_c.active == True:
            item3_resultado = 'Conforme'
            conformes += 1

        if self.strng.get_screen('checklistItem4').ids.radio_item4_c.active == True:
            item4_resultado = 'Conforme'
            conformes += 1

        if self.strng.get_screen('checklistItem5').ids.radio_item5_c.active == True:
            item5_resultado = 'Conforme'
            conformes += 1

        if self.strng.get_screen('checklistItem6').ids.radio_item6_c.active == True:
            item6_resultado = 'Conforme'
            conformes += 1

        if self.strng.get_screen('checklistItem7').ids.radio_item7_c.active == True:
            item7_resultado = 'Conforme'
            conformes += 1

        if self.strng.get_screen('checklistItem8').ids.radio_item8_c.active == True:
            item8_resultado = 'Conforme'
            conformes += 1

        if self.strng.get_screen('checklistItem9').ids.radio_item9_c.active == True:
            item9_resultado = 'Conforme'
            conformes += 1

        #################Não conformes#################
        if self.strng.get_screen('checklistItem1').ids.radio_item1_nc.active == True:
            item1_resultado = 'Não conforme'
            nao_conformes += 1

        if self.strng.get_screen('checklistItem2').ids.radio_item2_nc.active == True:
            item2_resultado = 'Não conforme'
            nao_conformes += 1

        if self.strng.get_screen('checklistItem3').ids.radio_item3_nc.active == True:
            item3_resultado = 'Não conforme'
            nao_conformes += 1

        if self.strng.get_screen('checklistItem4').ids.radio_item4_nc.active == True:
            item4_resultado = 'Não conforme'
            nao_conformes += 1

        if self.strng.get_screen('checklistItem5').ids.radio_item5_nc.active == True:
            item5_resultado = 'Não conforme'
            nao_conformes += 1

        if self.strng.get_screen('checklistItem6').ids.radio_item6_nc.active == True:
            item6_resultado = 'Não conforme'
            nao_conformes += 1

        if self.strng.get_screen('checklistItem7').ids.radio_item7_nc.active == True:
            item7_resultado = 'Não conforme'
            nao_conformes += 1

        if self.strng.get_screen('checklistItem8').ids.radio_item8_nc.active == True:
            item8_resultado = 'Não conforme'
            nao_conformes += 1

        if self.strng.get_screen('checklistItem9').ids.radio_item9_nc.active == True:
            item9_resultado = 'Não conforme'
            nao_conformes += 1

        #################Não aplicáveis#################
        if self.strng.get_screen('checklistItem1').ids.radio_item1_na.active == True:
            item1_resultado = 'Não aplicável'
            nao_aplicaveis += 1

        if self.strng.get_screen('checklistItem2').ids.radio_item2_na.active == True:
            item2_resultado = 'Não aplicável'
            nao_aplicaveis += 1

        if self.strng.get_screen('checklistItem3').ids.radio_item3_na.active == True:
            item3_resultado = 'Não aplicável'
            nao_aplicaveis += 1

        if self.strng.get_screen('checklistItem4').ids.radio_item4_na.active == True:
            item4_resultado = 'Não aplicável'
            nao_aplicaveis += 1

        if self.strng.get_screen('checklistItem5').ids.radio_item5_na.active == True:
            item5_resultado = 'Não aplicável'
            nao_aplicaveis += 1

        if self.strng.get_screen('checklistItem6').ids.radio_item6_na.active == True:
            item6_resultado = 'Não aplicável'
            nao_aplicaveis += 1

        if self.strng.get_screen('checklistItem7').ids.radio_item7_na.active == True:
            item7_resultado = 'Não aplicável'
            nao_aplicaveis += 1

        if self.strng.get_screen('checklistItem8').ids.radio_item8_na.active == True:
            item8_resultado = 'Não aplicável'
            nao_aplicaveis += 1

        if self.strng.get_screen('checklistItem9').ids.radio_item9_na.active == True:
            item9_resultado = 'Não aplicável'
            nao_aplicaveis += 1

        porcentagem_conformes = conformes * 100 / 9

        status_lv = ''

        if porcentagem_conformes < 100:
            status_lv = 'Pendente'

        else:
            status_lv = 'Concluído'

        lv = {
            "nome_lv": lv_name,
            "descricao_lv": lv_descricao,
            "nome_usuario": nome,
            "email_usuario": email,
            "Data_emissao": today.replace('-', '/'),
            "porcentagem_c": round(porcentagem_conformes, 2),
            "quantidade_nc": nao_conformes,
            "quantidade_na": nao_aplicaveis,
            "lv_status": status_lv,

            "item1_nome": "Os locais adjacentes das caixas estão limpos e organizados?",
            "item1_resultado": item1_resultado,
            "item1_acao": item1_acao,
            "item1_prazo": item1_prazo,
            "item1_responsavel": item1_responsavel,

            "item2_nome": "As caixas estão com acúmulo excessivo de gordura?",
            "item2_resultado": item2_resultado,
            "item2_acao": item2_acao,
            "item2_prazo": item2_prazo,
            "item2_responsavel": item2_responsavel,

            "item3_nome": "As caixas de gordura estão obstruídas?",
            "item3_resultado": item3_resultado,
            "item3_acao": item3_acao,
            "item3_prazo": item3_prazo,
            "item3_responsavel": item3_responsavel,

            "item4_nome": "Há evidências de transbordo?",
            "item4_resultado": item4_resultado,
            "item4_acao": item4_acao,
            "item4_prazo": item4_prazo,
            "item4_responsavel": item4_responsavel,

            "item5_nome": "Há evidência de odores?",
            "item5_resultado": item5_resultado,
            "item5_acao": item5_acao,
            "item5_prazo": item5_prazo,
            "item5_responsavel": item5_responsavel,

            "item6_nome": "Há detritos de alimentos, sobras de embalagens, entre outros?",
            "item6_resultado": item6_resultado,
            "item6_acao": item6_acao,
            "item6_prazo": item6_prazo,
            "item6_responsavel": item6_responsavel,

            "item7_nome": "Há telas (grade) de retenção nas áreas internas do refeitório cin objetivo de reter sobras de alimentos?",
            "item7_resultado": item7_resultado,
            "item7_acao": item7_acao,
            "item7_prazo": item7_prazo,
            "item7_responsavel": item7_responsavel,

            "item8_nome": "As tampas das caixas estão encaixadas de acordo com a construção?",
            "item8_resultado": item8_resultado,
            "item8_acao": item8_acao,
            "item8_prazo": item8_prazo,
            "item8_responsavel": item8_responsavel,

            "item9_nome": "O efluente está sendo direcionado para a Estação de tratamento de Efluente - ETE?",
            "item9_resultado": item9_resultado,
            "item9_acao": item9_acao,
            "item9_prazo": item9_prazo,
            "item9_responsavel": item9_responsavel,

        }

        insert = col_lv.insert_one(lv)

    ##################CONFIRMAÇAO DE SAIDA APP################
    dialog = None

    def show_alert_dialog(self):
        if not self.dialog:
            self.dialog = MDDialog(

                text="Você deseja mesmo sair ?",
                buttons=[
                    MDFlatButton(
                        text="Sim", text_color=self.theme_cls.primary_color, on_release=self.close_username_dialogue
                    ),
                    MDFlatButton(
                        text="Não", text_color=self.theme_cls.primary_color, on_release=self.close_username_dialogue_app
                    ),
                ],
            )
        self.dialog.open()

    def show_alert_checklist_exit_operation(self):
        if not self.dialog:
            self.dialog = MDDialog(

                text="Você deseja mesmo cancelar a verificação ?",
                buttons=[
                    MDFlatButton(
                        text="Sim", text_color=self.theme_cls.primary_color, on_release=self.close_username_dialogue1
                    ),
                    MDFlatButton(
                        text="Não", text_color=self.theme_cls.primary_color, on_release=self.close_username_dialogue
                    ),
                ],
            )
        self.dialog.open()

        ####################TELE DE REALMENTE QUER CONFIRMAR EXCLUIR CHECKLIST######################

    def show_alert__delete_dialog(self):
        if not self.dialog:
            self.dialog = MDDialog(
                text="Você deseja mesmo excluir ?",
                buttons=[
                    MDFlatButton(
                        text="Sim", text_color=self.theme_cls.primary_color,
                        on_release=self.close_username_dialogue_excluir
                    ),
                    MDFlatButton(
                        text="Não", text_color=self.theme_cls.primary_color, on_release=self.close_username_dialogue
                    ),
                ],
            )
        self.dialog.open()
        #################BLOCO DE AVISO NOME INVALIDO FECHANDO##################

    def close_username_dialogue1(self, obj):
        self.change_screen_to_checklists()
        self.dialog.dismiss()

    def close_username_dialogue(self, obj):
        self.change_screen_to_checklistname()
        self.dialog.dismiss()

    #############FUNCAO PARA BLOCO DE AVISO PARA SAIR DO APP################
    def close_username_dialogue_app(self, obj):
        quit()

    #####################BLOCO DE AVISO ECLUIR CHECKLIST FECHANDO##############
    def close_username_dialogue_excluir(self, obj):
        self.dialog.dismiss()
        self.remove_checklist()
        self.change_screen_to_checklists()

    #################REMOVE WIDGET CHECKLIST##################
    def remove_checklist(self):
        try:
            myclient = pymongo.MongoClient(
                "mongodb+srv://julio:senha@cluster0.pn3vb.mongodb.net/kivyapp?retryWrites=true&w=majority")
            db = myclient["kivyapp"]
            col_lv = db["lvs"]

            col_lv = col_lv.delete_one(
                {
                    "_id": ObjectId("id do bagulho")
                }
            )
        except Exception as erro:
            print(erro)

    ############MUDANDO A TELA PARA CHECKLIST INFORMAÇOES##########
    def change_screen(self, ThreeLineIconListItem):
        self.strng.get_screen('screen3').manager.current = 'screen3'

    ###############MUDANDO A TELA PARA O MENU DAS CHECKLISTS###########
    def change_screen_to_checklists(self):
        self.strng.get_screen('screen1').manager.current = 'screen1'

    def change_screen_to_checklistname(self):
        self.strng.get_screen('checklistName').manager.current = 'checklistName'

    ####################MUDANDO A TELA PARA A TELA INICIAR UM NOVA VERIFICAÇAO#############
    def start_checklist(self):
        self.strng.get_screen('checklistName').manager.current = 'checklistName'

    ##################FUNCAO PARA JANELHINHA DE DATA#########################
    def get_date(self, date):
        '''
        :type date: <class 'datetime.date'>
        '''

    ##################FUNCAO PARA JANELHINHA DE DATA#########################
    def show_date_picker(self):
        date_dialog = MDDatePicker(callback=self.get_date)
        date_dialog.open()

    #########FUNCAO RECARREGAR OS DELETALHES DO PEFIL APOS MUDANÇA##############

    ###############CARREGANDO OS VALORES DA CHECKLIST##############
    try:
        myclient = pymongo.MongoClient(
            "mongodb+srv://julio:senha@cluster0.pn3vb.mongodb.net/kivyapp?retryWrites=true&w=majority")
        db = myclient["kivyapp"]
        col_lv = db["lvs"]

        for item in col_lv.find({}, {"_id": 0}):
            list_name = item["nome_lv"]
            descricao_lv = item["descricao_lv"]
            criado_por = item["nome_usuario"]
            email_usuario = item["email_usuario"]
            criado_em = item["Data_emissao"]
            porcentagem_c = item["porcentagem_c"]
            quantidade_nc = item["quantidade_nc"]
            quantidade_na = item["quantidade_na"]
            status = item["lv_status"]

            item1_resultaldo = item['item1_resultado']
            acao = item['item1_acao']
            reponsavel_relizar = item['item1_responsavel']
            prazo = item['item1_prazo']

            item2_resultaldo = item['item2_resultado']
            item2_acao = item['item2_acao']
            item2_responsavel = item['item2_responsavel']
            item2_prazo = item['item2_prazo']

            item3_resultaldo = item['item3_resultado']
            item3_acao = item['item3_acao']
            item3_responsavel = item['item3_responsavel']
            item3_prazo = item['item3_prazo']

            item4_resultaldo = item['item4_resultado']
            item4_acao = item['item4_acao']
            item4_responsavel = item['item4_responsavel']
            item4_prazo = item['item4_prazo']

            item5_resultaldo = item['item5_resultado']
            item5_acao = item['item5_acao']
            item5_responsavel = item['item5_responsavel']
            item5_prazo = item['item5_prazo']

            item6_resultaldo = item['item6_resultado']
            item6_acao = item['item6_acao']
            item6_responsavel = item['item6_responsavel']
            item6_prazo = item['item6_prazo']

            item7_resultaldo = item['item7_resultado']
            item7_acao = item['item7_acao']
            item7_responsavel = item['item7_responsavel']
            item7_prazo = item['item7_prazo']

            item8_resultaldo = item['item8_resultado']
            item8_acao = item['item8_acao']
            item8_responsavel = item['item8_responsavel']
            item8_prazo = item['item8_prazo']

            item9_resultaldo = item['item9_resultado']
            item9_acao = item['item9_acao']
            item9_responsavel = item['item9_responsavel']
            item9_prazo = item['item9_prazo']
    except:
        pass

    #########PREENCHIMENTOD DO NOME NA TELA DE LOGIN OBRIGATORIO FUNCAO############
    def check_username(self):
        self.username_text = self.strng.get_screen('usernamescreen').ids.username_text_fied.text
        username_check_false = True
        try:
            int(self.username_text)
        except:
            username_check_false = False
        if username_check_false or self.username_text.split() == []:
            cancel_btn_username_dialogue = MDFlatButton(text='OK', on_release=self.close_username_dialogue)
            self.dialog = MDDialog(title='Nome inválido', text="Por favor preencha um nome válido",
                                   size_hint=(0.7, 0.2), buttons=[cancel_btn_username_dialogue])
            self.dialog.open()
        else:
            self.strng.get_screen('usernamescreen').ids.disabled_button.disabled = False

    ####################PREENCHIMENTO DO EMAIL TELA DE LOGIN OBRIGATORIO###################
    def get_email(self):
        self.email_text = self.strng.get_screen('dob').ids.email_text_fied.text
        username_check_false = True
        try:
            int(self.username_text)
        except:
            username_check_false = False
        if username_check_false or self.email_text.split() == []:
            cancel_btn_username_dialogue = MDFlatButton(text='OK', on_release=self.close_username_dialogue)
            self.dialog = MDDialog(title='Email inválido', text="Por favor preencha um email válido",
                                   size_hint=(0.7, 0.2), buttons=[cancel_btn_username_dialogue])
            self.dialog.open()
        else:
            name = self.strng.get_screen('usernamescreen').ids.username_text_fied.text
            email = self.strng.get_screen('dob').ids.email_text_fied.text
            self.store.put('UserInfo', name=name, email=email)
            self.strng.get_screen('dob').ids.disabled_button2.disabled = False
            self.set_refresh()
            self.update()

    ####################FUNCAO DE BLOQUEI DOS BOTAO CASO NAO SEJA SELECIONADO AS OPCOES DA VERIFICAÇAO############
    def enable_items_inputs(self):
        ##Item 1
        if self.strng.get_screen('checklistItem1').ids.radio_item1_nc.active == True:
            self.strng.get_screen(f'checklistItem1').ids.acao_item1.disabled = False
            self.strng.get_screen(f'checklistItem1').ids.responsavel_item1.disabled = False
            self.strng.get_screen(f'checklistItem1').ids.prazo_item1.disabled = False

        else:
            self.strng.get_screen(f'checklistItem1').ids.acao_item1.disabled = True
            self.strng.get_screen(f'checklistItem1').ids.responsavel_item1.disabled = True
            self.strng.get_screen(f'checklistItem1').ids.prazo_item1.disabled = True

        ##Item 2
        if self.strng.get_screen('checklistItem2').ids.radio_item2_nc.active == True:
            self.strng.get_screen(f'checklistItem2').ids.acao_item2.disabled = False
            self.strng.get_screen(f'checklistItem2').ids.responsavel_item2.disabled = False
            self.strng.get_screen(f'checklistItem2').ids.prazo_item2.disabled = False

        else:
            self.strng.get_screen(f'checklistItem2').ids.acao_item2.disabled = True
            self.strng.get_screen(f'checklistItem2').ids.responsavel_item2.disabled = True
            self.strng.get_screen(f'checklistItem2').ids.prazo_item2.disabled = True

        ##Item 3
        if self.strng.get_screen('checklistItem3').ids.radio_item3_nc.active == True:
            self.strng.get_screen(f'checklistItem3').ids.acao_item3.disabled = False
            self.strng.get_screen(f'checklistItem3').ids.responsavel_item3.disabled = False
            self.strng.get_screen(f'checklistItem3').ids.prazo_item3.disabled = False

        else:
            self.strng.get_screen(f'checklistItem3').ids.acao_item3.disabled = True
            self.strng.get_screen(f'checklistItem3').ids.responsavel_item3.disabled = True
            self.strng.get_screen(f'checklistItem3').ids.prazo_item3.disabled = True

        ##Item 4
        if self.strng.get_screen('checklistItem4').ids.radio_item4_nc.active == True:
            self.strng.get_screen(f'checklistItem4').ids.acao_item4.disabled = False
            self.strng.get_screen(f'checklistItem4').ids.responsavel_item4.disabled = False
            self.strng.get_screen(f'checklistItem4').ids.prazo_item4.disabled = False

        else:
            self.strng.get_screen(f'checklistItem4').ids.acao_item4.disabled = True
            self.strng.get_screen(f'checklistItem4').ids.responsavel_item4.disabled = True
            self.strng.get_screen(f'checklistItem4').ids.prazo_item4.disabled = True

        ##Item 5
        if self.strng.get_screen('checklistItem5').ids.radio_item5_nc.active == True:
            self.strng.get_screen(f'checklistItem5').ids.acao_item5.disabled = False
            self.strng.get_screen(f'checklistItem5').ids.responsavel_item5.disabled = False
            self.strng.get_screen(f'checklistItem5').ids.prazo_item5.disabled = False

        else:
            self.strng.get_screen(f'checklistItem5').ids.acao_item5.disabled = True
            self.strng.get_screen(f'checklistItem5').ids.responsavel_item5.disabled = True
            self.strng.get_screen(f'checklistItem5').ids.prazo_item5.disabled = True

        ##Item 6
        if self.strng.get_screen('checklistItem6').ids.radio_item6_nc.active == True:
            self.strng.get_screen(f'checklistItem6').ids.acao_item6.disabled = False
            self.strng.get_screen(f'checklistItem6').ids.responsavel_item6.disabled = False
            self.strng.get_screen(f'checklistItem6').ids.prazo_item6.disabled = False

        else:
            self.strng.get_screen(f'checklistItem6').ids.acao_item6.disabled = True
            self.strng.get_screen(f'checklistItem6').ids.responsavel_item6.disabled = True
            self.strng.get_screen(f'checklistItem6').ids.prazo_item6.disabled = True

        ##Item 7
        if self.strng.get_screen('checklistItem7').ids.radio_item7_nc.active == True:
            self.strng.get_screen(f'checklistItem7').ids.acao_item7.disabled = False
            self.strng.get_screen(f'checklistItem7').ids.responsavel_item7.disabled = False
            self.strng.get_screen(f'checklistItem7').ids.prazo_item7.disabled = False

        else:
            self.strng.get_screen(f'checklistItem7').ids.acao_item7.disabled = True
            self.strng.get_screen(f'checklistItem7').ids.responsavel_item7.disabled = True
            self.strng.get_screen(f'checklistItem7').ids.prazo_item7.disabled = True

        ##Item 8
        if self.strng.get_screen('checklistItem8').ids.radio_item8_nc.active == True:
            self.strng.get_screen(f'checklistItem8').ids.acao_item8.disabled = False
            self.strng.get_screen(f'checklistItem8').ids.responsavel_item8.disabled = False
            self.strng.get_screen(f'checklistItem8').ids.prazo_item8.disabled = False

        else:
            self.strng.get_screen(f'checklistItem8').ids.acao_item8.disabled = True
            self.strng.get_screen(f'checklistItem8').ids.responsavel_item8.disabled = True
            self.strng.get_screen(f'checklistItem8').ids.prazo_item8.disabled = True

        ##Item 9
        if self.strng.get_screen('checklistItem9').ids.radio_item9_nc.active == True:
            self.strng.get_screen(f'checklistItem9').ids.acao_item9.disabled = False
            self.strng.get_screen(f'checklistItem9').ids.responsavel_item9.disabled = False
            self.strng.get_screen(f'checklistItem9').ids.prazo_item9.disabled = False

        else:
            self.strng.get_screen(f'checklistItem9').ids.acao_item9.disabled = True
            self.strng.get_screen(f'checklistItem9').ids.responsavel_item9.disabled = True
            self.strng.get_screen(f'checklistItem9').ids.prazo_item9.disabled = True

    def callback(self, nome):
        print(nome)


    def disable_nextButton(self):
        self.strng.get_screen(f'checklistItem1').ids.next_button1.disabled = True
        self.strng.get_screen(f'checklistItem2').ids.next_button2.disabled = True
        self.strng.get_screen(f'checklistItem3').ids.next_button3.disabled = True
        self.strng.get_screen(f'checklistItem4').ids.next_button4.disabled = True
        self.strng.get_screen(f'checklistItem5').ids.next_button5.disabled = True
        self.strng.get_screen(f'checklistItem6').ids.next_button6.disabled = True
        self.strng.get_screen(f'checklistItem7').ids.next_button7.disabled = True
        self.strng.get_screen(f'checklistItem8').ids.next_button8.disabled = True
        self.strng.get_screen(f'checklistItem9').ids.next_button9.disabled = True

    ####################FUNCAO PARA LIBERAR OS BOTAO CASO SEJA SELECIONADO AS OPCOES DA VERIFICAÇAO############

    def check_lv_items(self):

        # Item 1
        if self.strng.get_screen('checklistItem1').ids.radio_item1_nc.active == True and self.strng.get_screen(
                f'checklistItem1').ids.acao_item1.text.split() != [] and self.strng.get_screen(
            f'checklistItem1').ids.responsavel_item1.text.split() != [] and self.strng.get_screen(
            f'checklistItem1').ids.prazo_item1.text.split() != [] or self.strng.get_screen(
            f'checklistItem1').ids.radio_item1_c.active == True or self.strng.get_screen(
            f'checklistItem1').ids.radio_item1_na.active == True:
            self.strng.get_screen(f'checklistItem1').ids.next_button1.disabled = False

        # Item 2
        if self.strng.get_screen('checklistItem2').ids.radio_item2_nc.active == True and self.strng.get_screen(
                f'checklistItem2').ids.acao_item2.text.split() != [] and self.strng.get_screen(
            f'checklistItem2').ids.responsavel_item2.text.split() != [] and self.strng.get_screen(
            f'checklistItem2').ids.prazo_item2.text.split() != [] or self.strng.get_screen(
            f'checklistItem2').ids.radio_item2_c.active == True or self.strng.get_screen(
            f'checklistItem2').ids.radio_item2_na.active == True:
            self.strng.get_screen(f'checklistItem2').ids.next_button2.disabled = False

        # Item 3
        if self.strng.get_screen('checklistItem3').ids.radio_item3_nc.active == True and self.strng.get_screen(
                f'checklistItem3').ids.acao_item3.text.split() != [] and self.strng.get_screen(
            f'checklistItem3').ids.responsavel_item3.text.split() != [] and self.strng.get_screen(
            f'checklistItem3').ids.prazo_item3.text.split() != [] or self.strng.get_screen(
            f'checklistItem3').ids.radio_item3_c.active == True or self.strng.get_screen(
            f'checklistItem3').ids.radio_item3_na.active == True:
            self.strng.get_screen(f'checklistItem3').ids.next_button3.disabled = False

        # Item 4
        if self.strng.get_screen('checklistItem4').ids.radio_item4_nc.active == True and self.strng.get_screen(
                f'checklistItem4').ids.acao_item4.text.split() != [] and self.strng.get_screen(
            f'checklistItem4').ids.responsavel_item4.text.split() != [] and self.strng.get_screen(
            f'checklistItem4').ids.prazo_item4.text.split() != [] or self.strng.get_screen(
            f'checklistItem4').ids.radio_item4_c.active == True or self.strng.get_screen(
            f'checklistItem4').ids.radio_item4_na.active == True:
            self.strng.get_screen(f'checklistItem4').ids.next_button4.disabled = False

        # Item 5
        if self.strng.get_screen('checklistItem5').ids.radio_item5_nc.active == True and self.strng.get_screen(
                f'checklistItem5').ids.acao_item5.text.split() != [] and self.strng.get_screen(
            f'checklistItem5').ids.responsavel_item5.text.split() != [] and self.strng.get_screen(
            f'checklistItem5').ids.prazo_item5.text.split() != [] or self.strng.get_screen(
            f'checklistItem5').ids.radio_item5_c.active == True or self.strng.get_screen(
            f'checklistItem5').ids.radio_item5_na.active == True:
            self.strng.get_screen(f'checklistItem5').ids.next_button5.disabled = False

        # Item 6
        if self.strng.get_screen('checklistItem6').ids.radio_item6_nc.active == True and self.strng.get_screen(
                f'checklistItem6').ids.acao_item6.text.split() != [] and self.strng.get_screen(
            f'checklistItem6').ids.responsavel_item6.text.split() != [] and self.strng.get_screen(
            f'checklistItem6').ids.prazo_item6.text.split() != [] or self.strng.get_screen(
            f'checklistItem6').ids.radio_item6_c.active == True or self.strng.get_screen(
            f'checklistItem6').ids.radio_item6_na.active == True:
            self.strng.get_screen(f'checklistItem6').ids.next_button6.disabled = False

        # Item 7
        if self.strng.get_screen('checklistItem7').ids.radio_item7_nc.active == True and self.strng.get_screen(
                f'checklistItem7').ids.acao_item7.text.split() != [] and self.strng.get_screen(
            f'checklistItem7').ids.responsavel_item7.text.split() != [] and self.strng.get_screen(
            f'checklistItem7').ids.prazo_item7.text.split() != [] or self.strng.get_screen(
            f'checklistItem7').ids.radio_item7_c.active == True or self.strng.get_screen(
            f'checklistItem7').ids.radio_item7_na.active == True:
            self.strng.get_screen(f'checklistItem7').ids.next_button7.disabled = False

        # Item 8
        if self.strng.get_screen('checklistItem8').ids.radio_item8_nc.active == True and self.strng.get_screen(
                f'checklistItem8').ids.acao_item8.text.split() != [] and self.strng.get_screen(
            f'checklistItem8').ids.responsavel_item8.text.split() != [] and self.strng.get_screen(
            f'checklistItem8').ids.prazo_item8.text.split() != [] or self.strng.get_screen(
            f'checklistItem8').ids.radio_item8_c.active == True or self.strng.get_screen(
            f'checklistItem8').ids.radio_item8_na.active == True:
            self.strng.get_screen(f'checklistItem8').ids.next_button8.disabled = False

        # Item 9
        if self.strng.get_screen('checklistItem9').ids.radio_item9_nc.active == True and self.strng.get_screen(
                f'checklistItem9').ids.acao_item9.text.split() != [] and self.strng.get_screen(
            f'checklistItem9').ids.responsavel_item9.text.split() != [] and self.strng.get_screen(
            f'checklistItem9').ids.prazo_item9.text.split() != [] or self.strng.get_screen(
            f'checklistItem9').ids.radio_item9_c.active == True or self.strng.get_screen(
            f'checklistItem9').ids.radio_item9_na.active == True:
            self.strng.get_screen(f'checklistItem9').ids.next_button9.disabled = False

    ###################BLOQUEIO DOS BOTAO PARA EDITAR CHCKLIST#########################
    def enable_checklist_inputs(self):
        if self.strng.get_screen('screen3').ids.profile_name_input.disabled == True:

            self.strng.get_screen('screen3').ids.profile_name_input.disabled = False

            self.strng.get_screen('screen3').ids.profile_data_input.disabled = False

            self.strng.get_screen('screen3').ids.profile_responsavel_input.disabled = False

            self.strng.get_screen('screen3').ids.profile_acao_input.disabled = False

            self.strng.get_screen('screen3').ids.profile_responsavel_realizar_input.disabled = False

            self.strng.get_screen('screen3').ids.profile_prazo_input.disabled = False

            self.strng.get_screen('screen3').ids.profile_status_input.disabled = False

            self.strng.get_screen('screen3').ids.save_checklist_button.disabled = False

            self.strng.get_screen('screen3').ids.delete_checklist_button.disabled = False

        else:
            self.strng.get_screen('screen3').ids.profile_name_input.disabled = True

            self.strng.get_screen('screen3').ids.profile_data_input.disabled = True

            self.strng.get_screen('screen3').ids.profile_responsavel_input.disabled = True

            self.strng.get_screen('screen3').ids.profile_acao_input.disabled = True

            self.strng.get_screen('screen3').ids.profile_responsavel_realizar_input.disabled = True

            self.strng.get_screen('screen3').ids.profile_prazo_input.disabled = True

            self.strng.get_screen('screen3').ids.profile_status_input.disabled = True

            self.strng.get_screen('screen3').ids.save_checklist_button.disabled = True

            self.strng.get_screen('screen3').ids.delete_checklist_button.disabled = True

    #######################BLOQUEIO DOS BOTAO PARA EDITAR PERFIL################
    def enable_profile_inputs(self):

        if self.strng.get_screen('profile').ids.profile_email_input.disabled == True:

            self.strng.get_screen('profile').ids.profile_email_input.disabled = False

            self.strng.get_screen('profile').ids.profile_name_input.disabled = False

            self.strng.get_screen('profile').ids.save_profile_button.disabled = False
        else:
            self.strng.get_screen('profile').ids.profile_email_input.disabled = True

            self.strng.get_screen('profile').ids.profile_name_input.disabled = True

            self.strng.get_screen('profile').ids.save_profile_button.disabled = True

    def load_checklist(self):
        myclient = pymongo.MongoClient("mongodb+srv://julio:senha@cluster0.pn3vb.mongodb.net/kivyapp?retryWrites=true&w=majority")
        db = myclient["kivyapp"]
        col_lv = db["lvs"]

        try:

            for item in col_lv.find():
                list_name = item["nome_lv"]
                descricao_lv = item["descricao_lv"]
                criado_por = item["nome_usuario"]
                email_usuario = item["email_usuario"]
                criado_em = item["Data_emissao"]
                porcentagem_c = item["porcentagem_c"]
                quantidade_nc = item["quantidade_nc"]
                quantidade_na = item["quantidade_na"]
                status = item["lv_status"]



                #####NOMES DOS ITENS#####
                item1_nome = item['item1_nome']
                item2_nome = item['item2_nome']
                item3_nome = item['item3_nome']
                item4_nome = item['item4_nome']
                item5_nome = item['item5_nome']
                item6_nome = item['item6_nome']
                item7_nome = item['item7_nome']
                item8_nome = item['item8_nome']
                item9_nome = item['item9_nome']


                item1_resultaldo = item['item1_resultado']
                item1_acao = item['item1_acao']
                item1_responsavel = item['item1_responsavel']
                item1_prazo = item['item1_prazo']

                item2_resultaldo = item['item2_resultado']
                item2_acao = item['item2_acao']
                item2_responsavel = item['item2_responsavel']
                item2_prazo = item['item2_prazo']

                item3_resultaldo = item['item3_resultado']
                item3_acao = item['item3_acao']
                item3_responsavel = item['item3_responsavel']
                item3_prazo = item['item3_prazo']

                item4_resultaldo = item['item4_resultado']
                item4_acao = item['item4_acao']
                item4_responsavel = item['item4_responsavel']
                item4_prazo = item['item4_prazo']

                item5_resultaldo = item['item5_resultado']
                item5_acao = item['item5_acao']
                item5_responsavel = item['item5_responsavel']
                item5_prazo = item['item5_prazo']

                item6_resultaldo = item['item6_resultado']
                item6_acao = item['item6_acao']
                item6_responsavel = item['item6_responsavel']
                item6_prazo = item['item6_prazo']

                item7_resultaldo = item['item7_resultado']
                item7_acao = item['item7_acao']
                item7_responsavel = item['item7_responsavel']
                item7_prazo = item['item7_prazo']

                item8_resultaldo = item['item8_resultado']
                item8_acao = item['item8_acao']
                item8_responsavel = item['item8_responsavel']
                item8_prazo = item['item8_prazo']

                item9_resultaldo = item['item9_resultado']
                item9_acao = item['item9_acao']
                item9_responsavel = item['item9_responsavel']
                item9_prazo = item['item9_prazo']


                self.panel = MDExpansionPanel(
                    icon=f"kivymd.png",
                    content=Content(),
                    panel_cls=MDExpansionPanelThreeLine(
                        text=list_name,
                        secondary_text=criado_por,
                        tertiary_text=criado_em + descricao_lv,
                    )
                )

                self.strng.get_screen('screen1').ids.box.add_widget(self.panel)
                self.panel.bind(on_open=self.panel_open, on_close=self.panel_close)

                self.panel.content.add_widget(
                    MDTextField(text=criado_em, pos_hint={'center_x': 0.5, 'center_y': 0.05}, size_hint=(0.98, 0.1),
                                hint_text='Data de emissão.', icon_right='calendar'))
                self.panel.content.add_widget(
                    MDTextField(text=str(porcentagem_c), pos_hint={'center_x': 0.5, 'center_y': 0.05},
                                size_hint=(0.98, 0.1), hint_text='Porcentagens de conformes !', icon_right='percent'))

                if status == 'Pendente':

                    self.panel.content.add_widget(
                        MDTextField(text=status, pos_hint={'center_x': 0.5, 'center_y': 0.05}, size_hint=(0.98, 0.1),
                                    hint_text='Status da checklist.', icon_right='alert'))
                else:
                    self.panel.content.add_widget(
                        MDTextField(text=status, pos_hint={'center_x': 0.5, 'center_y': 0.05}, size_hint=(0.98, 0.1),
                                    hint_text='Status da checklist.', icon_right='check-all'))


                ########################

                if item1_resultaldo == 'Conforme':

                    self.panel.content.add_widget(
                        MDTextField(text=item1_resultaldo, pos_hint={'center_x': 0.5, 'center_y': 0.05},
                                    size_hint=(0.98, 0.1), hint_text='Status da checklist.', icon_right='check'))

                if item1_resultaldo == 'Não aplicável':
                    self.panel.content.add_widget(
                        MDTextField(text=item1_resultaldo, pos_hint={'center_x': 0.5, 'center_y': 0.05},
                                    size_hint=(0.98, 0.1), hint_text='Status da checklist.', icon_right='close'))

                ########################



                if item1_resultaldo == 'Não conforme':

                    self.panel.content.add_widget(
                        MDTextField(text=item1_resultaldo, pos_hint={'center_x': 0.5, 'center_y': 0.05},
                                    size_hint=(0.98, 0.1), hint_text='Status da checklist.', icon_right='alert'))

                    self.panel.content.add_widget(
                        MDTextField(text=item1_acao, pos_hint={'center_x': 0.5, 'center_y': 0.05}, size_hint=(0.98, 0.1),
                                    hint_text='Data de emissão.', icon_right='alert'))
                    self.panel.content.add_widget(
                        MDTextField(text=item1_prazo, pos_hint={'center_x': 0.5, 'center_y': 0.05}, size_hint=(0.98, 0.1),
                                    hint_text='Data de emissão.', icon_right='alert'))




                ########################

                if item2_resultaldo == 'Conforme':
                    self.panel.content.add_widget(
                        MDTextField(text=item2_resultaldo, pos_hint={'center_x': 0.5, 'center_y': 0.05},
                                    size_hint=(0.98, 0.1), hint_text='Status da checklist.', icon_right='check'))

                if item2_resultaldo == 'Não aplicável':
                    self.panel.content.add_widget(
                        MDTextField(text=item2_resultaldo, pos_hint={'center_x': 0.5, 'center_y': 0.05},
                                    size_hint=(0.98, 0.1), hint_text='Status da checklist.', icon_right='close'))

                ########################





                if item2_resultaldo == 'Não conforme':

                    self.panel.content.add_widget(
                        MDTextField(text=item2_resultaldo, pos_hint={'center_x': 0.5, 'center_y': 0.05},
                                    size_hint=(0.98, 0.1), hint_text='Status da checklist.', icon_right='alert'))

                    self.panel.content.add_widget(
                        MDTextField(text=item2_acao, pos_hint={'center_x': 0.5, 'center_y': 0.05}, size_hint=(0.98, 0.1),
                                    hint_text='Data de emissão.', icon_right='alert'))
                    self.panel.content.add_widget(
                        MDTextField(text=item2_prazo, pos_hint={'center_x': 0.5, 'center_y': 0.05}, size_hint=(0.98, 0.1),
                                    hint_text='Data de emissão.', icon_right='alert'))



                ########################

                if item3_resultaldo == 'Conforme':
                    self.panel.content.add_widget(
                        MDTextField(text=item3_resultaldo, pos_hint={'center_x': 0.5, 'center_y': 0.05},
                                    size_hint=(0.98, 0.1), hint_text='Status da checklist.', icon_right='check'))

                if item3_resultaldo == 'Não aplicável':
                    self.panel.content.add_widget(
                        MDTextField(text=item3_resultaldo, pos_hint={'center_x': 0.5, 'center_y': 0.05},
                                    size_hint=(0.98, 0.1), hint_text='Status da checklist.', icon_right='close'))

                ########################



                if item3_resultaldo == 'Não conforme':

                    self.panel.content.add_widget(
                        MDTextField(text=item3_resultaldo, pos_hint={'center_x': 0.5, 'center_y': 0.05},
                                    size_hint=(0.98, 0.1), hint_text='Status da checklist.', icon_right='alert'))

                    self.panel.content.add_widget(
                        MDTextField(text=item3_acao, pos_hint={'center_x': 0.5, 'center_y': 0.05}, size_hint=(0.98, 0.1),
                                    hint_text='Data de emissão.', icon_right='alert'))
                    self.panel.content.add_widget(
                        MDTextField(text=item3_prazo, pos_hint={'center_x': 0.5, 'center_y': 0.05}, size_hint=(0.98, 0.1),
                                    hint_text='Data de emissão.', icon_right='alert'))


                ########################

                if item4_resultaldo == 'Conforme':
                    self.panel.content.add_widget(
                        MDTextField(text=item4_resultaldo, pos_hint={'center_x': 0.5, 'center_y': 0.05},
                                    size_hint=(0.98, 0.1), hint_text='Status da checklist.', icon_right='check'))

                if item4_resultaldo == 'Não aplicável':
                    self.panel.content.add_widget(
                        MDTextField(text=item4_resultaldo, pos_hint={'center_x': 0.5, 'center_y': 0.05},
                                    size_hint=(0.98, 0.1), hint_text='Status da checklist.', icon_right='close'))

                ########################

                if item4_resultaldo == 'Não conforme':

                    self.panel.content.add_widget(
                        MDTextField(text=item4_resultaldo, pos_hint={'center_x': 0.5, 'center_y': 0.05},
                                    size_hint=(0.98, 0.1), hint_text='Status da checklist.', icon_right='alert'))

                    self.panel.content.add_widget(
                        MDTextField(text=item4_acao, pos_hint={'center_x': 0.5, 'center_y': 0.05}, size_hint=(0.98, 0.1),
                                    hint_text='Data de emissão.', icon_right='alert'))

                    self.panel.content.add_widget(
                        MDTextField(text=item4_prazo, pos_hint={'center_x': 0.5, 'center_y': 0.05}, size_hint=(0.98, 0.1),
                                    hint_text='Data de emissão.', icon_right='alert'))



                ########################

                if item5_resultaldo == 'Conforme':
                    self.panel.content.add_widget(
                        MDTextField(text=item5_resultaldo, pos_hint={'center_x': 0.5, 'center_y': 0.05},
                                    size_hint=(0.98, 0.1), hint_text='Status da checklist.', icon_right='check'))

                if item5_resultaldo == 'Não aplicável':
                    self.panel.content.add_widget(
                        MDTextField(text=item5_resultaldo, pos_hint={'center_x': 0.5, 'center_y': 0.05},
                                    size_hint=(0.98, 0.1), hint_text='Status da checklist.', icon_right='close'))


                ########################


                if item5_resultaldo == 'Não conforme':

                    self.panel.content.add_widget(
                        MDTextField(text=item5_resultaldo, pos_hint={'center_x': 0.5, 'center_y': 0.05},
                                    size_hint=(0.98, 0.1), hint_text='Status da checklist.', icon_right='alert'))

                    self.panel.content.add_widget(
                        MDTextField(text=item5_acao, pos_hint={'center_x': 0.5, 'center_y': 0.05}, size_hint=(0.98, 0.1),
                                    hint_text='Data de emissão.', icon_right='alert'))

                    self.panel.content.add_widget(
                        MDTextField(text=item5_prazo, pos_hint={'center_x': 0.5, 'center_y': 0.05}, size_hint=(0.98, 0.1),
                                    hint_text='Data de emissão.', icon_right='alert'))



                ########################

                if item6_resultaldo == 'Conforme':
                    self.panel.content.add_widget(
                        MDTextField(text=item6_resultaldo, pos_hint={'center_x': 0.5, 'center_y': 0.05},
                                    size_hint=(0.98, 0.1), hint_text='Status da checklist.', icon_right='check'))

                if item6_resultaldo == 'Não aplicável':
                    self.panel.content.add_widget(
                        MDTextField(text=item6_resultaldo, pos_hint={'center_x': 0.5, 'center_y': 0.05},
                                    size_hint=(0.98, 0.1), hint_text='Status da checklist.', icon_right='close'))

                ########################



                if item6_resultaldo == 'Não conforme':

                    self.panel.content.add_widget(
                        MDTextField(text=item6_resultaldo, pos_hint={'center_x': 0.5, 'center_y': 0.05},
                                    size_hint=(0.98, 0.1), hint_text='Status da checklist.', icon_right='alert'))

                    self.panel.content.add_widget(
                        MDTextField(text=item6_acao, pos_hint={'center_x': 0.5, 'center_y': 0.05}, size_hint=(0.98, 0.1),
                                    hint_text='Data de emissão.', icon_right='alert'))
                    self.panel.content.add_widget(
                        MDTextField(text=item6_prazo, pos_hint={'center_x': 0.5, 'center_y': 0.05}, size_hint=(0.98, 0.1),
                                    hint_text='Data de emissão.', icon_right='alert'))




                ########################

                if item7_resultaldo == 'Conforme':
                    self.panel.content.add_widget(
                        MDTextField(text=item7_resultaldo, pos_hint={'center_x': 0.5, 'center_y': 0.05},
                                    size_hint=(0.98, 0.1), hint_text='Status da checklist.', icon_right='check'))

                if item7_resultaldo == 'Não aplicável':
                    self.panel.content.add_widget(
                        MDTextField(text=item7_resultaldo, pos_hint={'center_x': 0.5, 'center_y': 0.05},
                                    size_hint=(0.98, 0.1), hint_text='Status da checklist.', icon_right='close'))

                ########################




                if item7_resultaldo == 'Não conforme':

                    self.panel.content.add_widget(
                        MDTextField(text=item7_resultaldo, pos_hint={'center_x': 0.5, 'center_y': 0.05},
                                    size_hint=(0.98, 0.1), hint_text='Status da checklist.', icon_right='alert'))

                    self.panel.content.add_widget(
                        MDTextField(text=item7_acao, pos_hint={'center_x': 0.5, 'center_y': 0.05}, size_hint=(0.98, 0.1),
                                    hint_text='Data de emissão.', icon_right='alert'))

                    self.panel.content.add_widget(
                        MDTextField(text=item7_prazo, pos_hint={'center_x': 0.5, 'center_y': 0.05}, size_hint=(0.98, 0.1),
                                    hint_text='Data de emissão.', icon_right='alert'))



                ########################

                if item8_resultaldo == 'Conforme':
                    self.panel.content.add_widget(
                        MDTextField(text=item8_resultaldo, pos_hint={'center_x': 0.5, 'center_y': 0.05},
                                    size_hint=(0.98, 0.1), hint_text='Status da checklist.', icon_right='check'))

                if item8_resultaldo == 'Não aplicável':
                    self.panel.content.add_widget(
                        MDTextField(text=item8_resultaldo, pos_hint={'center_x': 0.5, 'center_y': 0.05},
                                    size_hint=(0.98, 0.1), hint_text='Status da checklist.', icon_right='close'))

                ########################



                if item8_resultaldo == 'Não conforme':

                    self.panel.content.add_widget(
                        MDTextField(text=item8_resultaldo, pos_hint={'center_x': 0.5, 'center_y': 0.05},
                                    size_hint=(0.98, 0.1), hint_text='Status da checklist.', icon_right='alert'))

                    self.panel.content.add_widget(
                        MDTextField(text=item8_acao, pos_hint={'center_x': 0.5, 'center_y': 0.05}, size_hint=(0.98, 0.1),
                                    hint_text='Data de emissão.', icon_right='alert'))
                    self.panel.content.add_widget(
                        MDTextField(text=item8_prazo, pos_hint={'center_x': 0.5, 'center_y': 0.05}, size_hint=(0.98, 0.1),
                                    hint_text='Data de emissão.', icon_right='alert'))



                ########################

                if item9_resultaldo == 'Conforme':
                    self.panel.content.add_widget(
                        MDTextField(text=item9_resultaldo, pos_hint={'center_x': 0.5, 'center_y': 0.05},
                                    size_hint=(0.98, 0.1), hint_text='Status da checklist.', icon_right='check'))

                if item9_resultaldo == 'Não aplicável':
                    self.panel.content.add_widget(
                        MDTextField(text=item9_resultaldo, pos_hint={'center_x': 0.5, 'center_y': 0.05},
                                    size_hint=(0.98, 0.1), hint_text='Status da checklist.', icon_right='close'))

                ########################


                if item9_resultaldo == 'Não conforme':

                    self.panel.content.add_widget(
                        MDTextField(text=item9_resultaldo, pos_hint={'center_x': 0.5, 'center_y': 0.05},
                                    size_hint=(0.98, 0.1), hint_text='Status da checklist.', icon_right='alert'))

                    self.panel.content.add_widget(
                        MDTextField(text=item9_acao, pos_hint={'center_x': 0.5, 'center_y': 0.05}, size_hint=(0.98, 0.1),
                                    hint_text='Data de emissão.', icon_right='alert'))
                    self.panel.content.add_widget(
                        MDTextField(text=item9_prazo, pos_hint={'center_x': 0.5, 'center_y': 0.05}, size_hint=(0.98, 0.1),
                                    hint_text='Data de emissão.', icon_right='alert'))

        except:
            pass

PawareApp().run()
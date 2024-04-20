from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.core.clipboard import Clipboard
from kivy.config import ConfigParser
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.base import EventLoop
from kivy.uix.scrollview import ScrollView
from kivy.core.window import Window
import ast

main_menu = BoxLayout(orientation='horizontal')
button_main = GridLayout(cols=2, size_hint = [1, 0.9], size_hint_y=None)
list_main = GridLayout(cols=5, size_hint = [1, 0.9])
settings_main = GridLayout(cols=2, size_hint_y = None)
menu_end = GridLayout(cols=2, size_hint = [1, 0.1], padding = [10])
root = ScrollView()
root2 = ScrollView()

#numberlist = config.get('General', 'user_data')

#numberlist = ast.literal_eval(self.config.get('General', 'user_data'))

class class_leader(App):

	def build_config(self, config):
		config.adddefaultsection('General')
		config.setdefault('General', 'user_data', [ 
		["Федорович", "@shishkin666", "[Не пришел]"], ] )
		config.setdefault('General', 'list', [  ] )
		config.setdefault('General', 'hascome', 0 )

	def hook_keyboard(self, window, key, *largs):
		if key == 27:

			self.btn_press_end(None)

			return True 

	def build(self):

		self.exitmenu = 5

		self.numberlist = ast.literal_eval(self.config.get('General', 'user_data'))
		self.hascome = ast.literal_eval(self.config.get('General', 'hascome'))

		EventLoop.window.bind(on_keyboard=self.hook_keyboard)

		main_menu.add_widget(Button(
			text = "Отмеченные",
			font_size = 30, 
			on_press = self.menu_marked,
			background_color = [0, 0, 1, 1],
			#size_hint =  [.5, .5]
		))

		main_menu.add_widget(Button(
			text = "Записки",
			font_size = 30, 
			on_press = self.menu_list,
			background_color = [0, 0, 1, 1],
			#size_hint =  [.5, .5]
		))

		main_menu.add_widget(Button(
			text = "Настройки",
			font_size = 30, 
			on_press = self.menu_settings,
			background_color = [0, 0, 1, 1],
			#size_hint =  [.5, .5]
		))

		return main_menu

	def menu_marked(self, instance):
		main_menu.clear_widgets()
		button_main.bind(minimum_height=button_main.setter('height'))
		#asd = BoxLayout(orientation='vertical')
		#main_menu = asd
		self.exitmenu = 2
		main_menu.orientation = "vertical"
		for index, x in enumerate(self.numberlist):
			if x[2] == "[Пришел]":
				color_button = [0, 1, 0, 1]
			elif x[2] == "[Перезачёт]":
				color_button = [1, 0, 1, 1]
			elif x[2] == "[Опоздал]":
				color_button = [0, 0, 1, 1]
			elif x[2] == "[Заболел]":
				color_button = [0, 1, 1, 1]
			else:
				color_button = [1, 0, 0, 1]

			button_main.add_widget(Button(
				text = str(index + 1) + ". " + x[0] + " " + x[2],
				font_size = 30, 
				on_press = self.btn_press,
				background_color = color_button,
				#size_hint =  [.5, .5],
				size_hint = [1, 0.9], 
				size_hint_y=None,
				height=Window.size[1]/16.5
			))

		#global lbl
		self.lbl = Label(text="Всего: "+ str(len(self.numberlist)) + " Пришло: " + str(self.hascome),font_size = 30, size_hint_y=None, height=Window.size[1]/16.5 ) 
		
		button_main.add_widget( self.lbl )

		menu_reset_copy = GridLayout(cols=3, size_hint = [1, 0.1], padding = [10])

		menu_reset_copy.add_widget( Button(
			text = "Скопировать", 
			font_size = 30, 
			on_press = lambda x: Clipboard.copy("Список тех кто опоздал/не пришел:\n" + tabletext(self.numberlist) + "Всего: "+ str(len(self.numberlist)) + " Пришло: " + str(self.hascome)), 
			background_color = [0, 0, 1, 1], 
			size_hint = [.1, .1],
			pos_hint = {"center_x": 0.5, "center_y": 0.5},
			) )

		menu_reset_copy.add_widget( Button(
			text = "Сбросить", 
			font_size = 30, 
			on_press = self.btn_press_reset, 
			background_color = [0, 0, 1, 1], 
			size_hint = [.1, .1],
			pos_hint = {"center_x": 0.5, "center_y": 0.5},
			) )

		menu_reset_copy.add_widget( Button(

			text = "Назад", 
			font_size = 30, 
			on_press = self.btn_press_end, 
			background_color = [0, 0, 1, 1], 
			size_hint = [.1, .1],
			pos_hint = {"center_x": 0.5, "center_y": 0.5},
			) )

		root.add_widget( button_main )

		main_menu.add_widget( root )
		main_menu.add_widget( menu_reset_copy )


	def btn_press_end(self, instance):
		main_menu.clear_widgets()
		button_main.clear_widgets()
		list_main.clear_widgets()
		settings_main.clear_widgets()
		root.clear_widgets()
		root2.clear_widgets()

		if self.exitmenu == 2:

			self.exitmenu = 5

			main_menu.orientation = "horizontal"

			main_menu.add_widget(Button(
				text = "Отмеченные",
				font_size = 30, 
				on_press = self.menu_marked,
				background_color = [0, 0, 1, 1],
				#size_hint =  [.5, .5]
			))

			main_menu.add_widget(Button(
				text = "Записки",
				font_size = 30, 
				on_press = self.menu_list,
				background_color = [0, 0, 1, 1],
				#size_hint =  [.5, .5]
			))

			main_menu.add_widget(Button(
				text = "Настройки",
				font_size = 30, 
				on_press = self.menu_settings,
				background_color = [0, 0, 1, 1],
				#size_hint =  [.5, .5]
			))
		elif self.exitmenu == 3:
			self.exitmenu = 2
			
			main_menu.orientation = "vertical"

			self.main_list = ast.literal_eval(self.config.get('General', 'list'))
			for x in self.main_list:
				list_main.add_widget(Button(
					text = x[0],
					font_size = 30,
					on_press = self.btn_press_list,
					background_color = [1, 0, 0, 1],
					#size_hint =  [.5, .5]
				))

			menu_end = GridLayout(cols=2, size_hint = [1, 0.1], padding = [10])

			menu_end.add_widget(Button(
					text = "Добавить",
					font_size = 30, 
					on_press = self.btn_press_add,
					background_color = [0, 0, 1, 1],
					#size_hint =  [.5, .5]
				))

			menu_end.add_widget(Button(
					text = "Назад",
					font_size = 30, 
					on_press = self.btn_press_end,
					background_color = [0, 0, 1, 1],
					#size_hint =  [.5, .5]
				))

			main_menu.add_widget( list_main )
			main_menu.add_widget( menu_end )
		elif self.exitmenu == 4:
			self.exitmenu = 2

			main_menu.clear_widgets()
			main_menu.orientation = "vertical"
			settings_main.bind(minimum_height=settings_main.setter('height'))
			for x in range(0, len(self.numberlist)):
				settings_main.add_widget(Button(
					text = str(x + 1) + ". " + self.numberlist[x][0],
					font_size = 25,
					on_press = self.btn_press_settings,
					background_color = [1, 0, 0, 1],
					#size_hint =  [.5, .5]
					size_hint_y=None,
					height=Window.size[1]/16.5
				))

			menu_end = GridLayout(cols=2, size_hint = [1, 0.1], padding = [10])

			menu_end.add_widget(Button(
				text = "Добавить",
				font_size = 30, 
				on_press = self.btn_press_add_settings,
				background_color = [0, 0, 1, 1],
				#size_hint =  [.5, .5]
			))

			menu_end.add_widget(Button(
				text = "Назад",
				font_size = 30, 
				on_press = self.btn_press_end,
				background_color = [0, 0, 1, 1],
					#size_hint =  [.5, .5]
				))

			root2.add_widget(settings_main)

			main_menu.add_widget( root2 )
			main_menu.add_widget( menu_end )
		else:
			App.stop(self)

	def btn_press_reset(self, instance):
		for x in self.numberlist:
			x[2] = "[Не пришел]"

		self.hascome = 0

		App.get_running_app().config.set('General', 'user_data', self.numberlist)
		App.get_running_app().config.write()

		App.get_running_app().config.set('General', 'hascome', self.hascome)
		App.get_running_app().config.write()

		button_main.clear_widgets()
		for index, x in enumerate(self.numberlist):

			button_main.add_widget(Button(
				text = str(index + 1) + ". " + x[0] + " " + x[2],
				font_size = 30,
				on_press = self.btn_press,
				background_color = [1, 0, 0, 1],
				#size_hint =  [.5, .5]
				size_hint_y=None, 
				height=Window.size[1]/16.5
			))


		self.lbl = Label(text="Всего: "+ str(len(self.numberlist)) + " Пришло: " + str(self.hascome),font_size = 30, size_hint_y=None, height=Window.size[1]/16.5 ) 

		button_main.add_widget( self.lbl  )

	def btn_press(self, instance):
		idbutton = int(instance.text.split(".")[0]) - 1
		if instance.background_color == [0, 1, 0, 1]:
			instance.background_color = [1, 0, 0, 1]
			self.numberlist[idbutton][2] = "[Не пришел]"
			self.hascome -= 1
		elif instance.background_color == [1, 0, 0, 1]:
			instance.background_color = [0, 1, 1, 1]
			self.numberlist[idbutton][2] = "[Заболел]"
		elif instance.background_color == [0, 1, 1, 1]:
			instance.background_color = [1, 0, 1, 1]
			self.numberlist[idbutton][2] = "[Перезачёт]"
		elif instance.background_color == [1, 0, 1, 1]:
			instance.background_color = [0, 0, 1, 1]
			self.numberlist[idbutton][2] = "[Опоздал]"
			self.hascome += 1
		else:
			instance.background_color = [0, 1, 0, 1]
			self.numberlist[idbutton][2] = "[Пришел]"

		self.lbl.text = "Всего: "+ str(len(self.numberlist)) + " Пришло: " + str(self.hascome)
		App.get_running_app().config.set('General', 'user_data', self.numberlist)
		App.get_running_app().config.write()
		App.get_running_app().config.set('General', 'hascome', self.hascome)
		App.get_running_app().config.write()
		instance.text = str(idbutton + 1) + ". " + self.numberlist[idbutton][0] + " " + self.numberlist[idbutton][2]

	def menu_list(self, instance):
		self.exitmenu = 2
		main_menu.clear_widgets()
		main_menu.orientation = "vertical"
		self.main_list = ast.literal_eval(self.config.get('General', 'list'))
		for x in self.main_list:
			list_main.add_widget(Button(
					text = x[0],
					font_size = 30, 
					on_press = self.btn_press_list,
					background_color = [1, 0, 0, 1],
					#size_hint =  [.5, .5]
				))

		menu_end = GridLayout(cols=2, size_hint = [1, 0.1], padding = [10])

		menu_end.add_widget(Button(
					text = "Добавить",
					font_size = 30, 
					on_press = self.btn_press_add,
					background_color = [0, 0, 1, 1],
					#size_hint =  [.5, .5]
				))

		menu_end.add_widget(Button(
					text = "Назад",
					font_size = 30, 
					on_press = self.btn_press_end,
					background_color = [0, 0, 1, 1],
					#size_hint =  [.5, .5]
				))

		main_menu.add_widget( list_main )
		main_menu.add_widget( menu_end )

	def btn_press_add(self, instance):
		if gettable2("Записка " + str(len(self.main_list) + 1), self.main_list) == None:
			name = "Записка " + str(len(self.main_list) + 1)
		else:
			name = "Записка " + str(len(self.main_list) + 1) + "_copy"

		self.main_list.append([name, "Текст\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n"])  # что такое гавно код? не слышал?
		list_main.add_widget(Button(
				text = name,
				font_size = 30,
				on_press = self.btn_press_list,
				background_color = [1, 0, 0, 1],
					#size_hint =  [.5, .5]
			))
		App.get_running_app().config.set('General', 'list', self.main_list)
		App.get_running_app().config.write()

	def btn_press_list(self, instance):
		self.exitmenu = 3
		main_menu.clear_widgets()
		#global settingslist
		self.settingslist = gettable2(instance.text, self.main_list)
		Input = TextInput(text=self.main_list[self.settingslist][1], size_hint =  [1, .8])
		Input2 = TextInput(text=self.main_list[self.settingslist][0], size_hint =  [1, .2])
		#Input = TextInput(text="self.main_list[gettable(instance.text, self.main_list)][1]")
		Input.bind(text=self.save_text_list)
		Input2.bind(text=self.save_text_list2)
		main_menu.add_widget( Input2 )
		main_menu.add_widget( Input )
		#main_menu.add_widget( Label(text=instance.text,font_size = 30 ) )

		menu_end_save_copy = GridLayout(cols=3, size_hint = [1, 0.1], padding = [10])
		menu_end_save_copy.add_widget(Button(
					text = "Скопировать",
					font_size = 30,
					on_press = lambda x: Clipboard.copy(self.main_list[self.settingslist][1]),
					background_color = [0, 0, 1, 1],
					#size_hint =  [.5, .5]
				))
		menu_end_save_copy.add_widget(Button(
					text = "Удалить",
					font_size = 30, 
					on_press = self.btn_press_dell,
					background_color = [0, 0, 1, 1],
					#size_hint =  [.5, .5]
				))
		menu_end_save_copy.add_widget(Button(
					text = "Назад",
					font_size = 30, 
					on_press = self.btn_press_end,
					background_color = [0, 0, 1, 1],
					#size_hint =  [.5, .5]
				))
		main_menu.add_widget( menu_end_save_copy )


	def btn_press_dell(self, instance):
		self.main_list.pop(self.settingslist)
		App.get_running_app().config.set('General', 'list', self.main_list)
		App.get_running_app().config.write()
		self.btn_press_end(None)

	def save_text_list(self, instance, value):
		self.main_list[self.settingslist][1] = value
		App.get_running_app().config.set('General', 'list', self.main_list)
		App.get_running_app().config.write()

	def save_text_list2(self, instance, value):
		#print(gettable2(value, self.main_list))
		if gettable2(value, self.main_list) == None:
			self.main_list[self.settingslist][0] = value
			App.get_running_app().config.set('General', 'list', self.main_list)
			App.get_running_app().config.write()

	def menu_settings(self, instance):
		main_menu.clear_widgets()
		menu_end.clear_widgets()
		self.exitmenu = 2
		main_menu.orientation = "vertical"
		settings_main.bind(minimum_height=settings_main.setter('height'))
		for x in range(0, len(self.numberlist)):
			settings_main.add_widget(Button(
					text = str(x + 1) + ". " + self.numberlist[x][0],
					font_size = 25,
					on_press = self.btn_press_settings,
					background_color = [1, 0, 0, 1],
					#size_hint =  [.5, .5]
					size_hint = [1, 0.1], 
					size_hint_y = None,
					height=Window.size[1]/16.5
				))

		menu_end.add_widget(Button(
				text = "Добавить",
				font_size = 30, 
				on_press = self.btn_press_add_settings,
				background_color = [0, 0, 1, 1],
				#size_hint =  [.5, .5]
			))

		menu_end.add_widget(Button(
				text = "Назад",
				font_size = 30, 
				on_press = self.btn_press_end,
				background_color = [0, 0, 1, 1],
					#size_hint =  [.5, .5]
			))

		root2.add_widget(settings_main)

		main_menu.add_widget( root2 )
		main_menu.add_widget( menu_end )
		#main_menu.add_widget( menu_end )

	def btn_press_add_settings(self, instance):
		self.numberlist.append(["Пусто", "id", "[Не пришел]"])
		settings_main.add_widget(Button(
				text = str(len(self.numberlist)) + ". " + "Пусто",
				font_size = 25,
				on_press = self.btn_press_settings,
				background_color = [1, 0, 0, 1],
				size_hint = [1, 0.9], 
				size_hint_y=None,
				height=Window.size[1]/16.5
			))
		App.get_running_app().config.set('General', 'user_data', self.numberlist)
		App.get_running_app().config.write()

	def btn_press_settings(self, instance):
		self.idbutton = int(instance.text.split(".")[0]) - 1
		
		self.exitmenu = 4
		main_menu.clear_widgets()
		menu_end.clear_widgets()
		
		Input = TextInput(text=self.numberlist[self.idbutton][1], size_hint =  [1, .2], multiline=False)
		Input2 = TextInput(text=self.numberlist[self.idbutton][0], size_hint =  [1, .2], multiline=False)
		#Input = TextInput(text="self.main_list[gettable(instance.text, self.main_list)][1]")
		Input.bind(text=self.save_text_list3)
		Input2.bind(text=self.save_text_list4)

		menu_end.add_widget(Button(
				text = "Удалить",
				font_size = 30, 
				on_press = self.btn_press_dell_settings,
				background_color = [0, 0, 1, 1],
				#size_hint =  [.5, .5]
			))

		menu_end.add_widget(Button(
				text = "Назад",
				font_size = 30, 
				on_press = self.btn_press_end,
				background_color = [0, 0, 1, 1],
					#size_hint =  [.5, .5]
			))
		
		main_menu.add_widget( Input2 )
		main_menu.add_widget( Input )
		main_menu.add_widget( menu_end )

	def save_text_list3(self, instance, value):
		self.numberlist[self.idbutton][1] = value
		App.get_running_app().config.set('General', 'user_data', self.numberlist)
		App.get_running_app().config.write()

	def save_text_list4(self, instance, value):
		self.numberlist[self.idbutton][0] = value
		App.get_running_app().config.set('General', 'user_data', self.numberlist)
		App.get_running_app().config.write()

	def btn_press_dell_settings(self, instance):
		self.numberlist.pop(self.idbutton)
		App.get_running_app().config.set('General', 'user_data', self.numberlist)
		App.get_running_app().config.write()
		self.btn_press_end(None)

def tabletext(tabl):

	text = ""
	for texttabl in tabl: # 29
		if not texttabl[2] == "[Пришел]":
			text = text + texttabl[1] + " " + texttabl[0] + " " + texttabl[2] + "\n"

	return text

def gettable(text, table):
	#print(list(range(idmax(table))))
	for x in range(len(table)):
		if table[x][0] in text:
			return x

def gettable2(text, table):
	#print(list(range(idmax(table))))
	for x in range(len(table)):
		if table[x][0] == text:
			return x

# idmax = len
def idmax(tabl):
    number3 = 0
    for number in tabl:
        number3 += 1

    return number3

def arrived(tabl):
	number1 = 0
	for text in tabl:
		if text[2] == "[Пришел]" or text[2] == "[Опоздал]" or text[2] == "[Перезачёт]":
			number1 += 1

	return number1

if __name__ == "__main__":
	class_leader().run()

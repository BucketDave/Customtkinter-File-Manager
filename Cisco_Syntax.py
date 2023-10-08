import customtkinter as ctk

import Cisco_Syntax_MiddleMan

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")


import customtkinter as ctk

import Cisco_Syntax_MiddleMan

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")


class App(ctk.CTk):
	def __init__(self, title, size):
		# main setup
		super().__init__()
		self.title(title)
		self.geometry(f'{size[0]}x{size[1]}')
		self.minsize(size[0],size[1])  
		
		# layout
		self.grid_columnconfigure((0,1), weight=0) 
		self.grid_columnconfigure(1, weight=1)
		self.grid_rowconfigure((0,1), weight=1) 

		# widgets
		self.menu = Menu(self)
		self.submenu = SubMenu(self)
		self.menu.grid(row=0, column=0, rowspan=2, sticky="nsw")
        
        
		# run 
		self.mainloop()


class Menu(ctk.CTkFrame):
	def __init__(self, parent):
		super().__init__(parent)
		self.configure(width=250)
		self.configure(corner_radius=0)

		self.columnconfigure(0, weight=1)

		# Elements
		self.after_idle(self.Menu)
		self.onemenu = False
		self.maindir = Cisco_Syntax_MiddleMan.Host_dir_list()
    
	def Menu(self):
		if self.onemenu == False:
			for i in range(len(self.maindir)):
					self.rowconfigure(i, weight=0)

			buttondict = []

			for number, name in enumerate(self.maindir):
				a = (f"mainbutton{number} = Button(parent=self, name='{name}', corner=0, command= lambda: Button.Main_Click(name='{name}'))")
				buttondict.append(a)
				
			for number, command in enumerate(buttondict):
				print(command, number)
				exec(command)
				exec(f"mainbutton{number}.grid(row={number}, sticky='w')")

			self.onemenu = True
		else:
			pass

class SubMenu(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)
        print(f"SM {dir}")
        global ssubmenu
        ssubmenu = self
        ssubmenu.configure(width=140)

    def subbuttons(dir: list):
        SubMenu.SubMenuVis(hidden=True)
        SubMenu.SubMenuVis(hidden=False)

        for i in range(len(dir)):
            ssubmenu.rowconfigure(i, weight=0)

        subbuttondict = []

        for number, name in enumerate(dir):
            a = (f"button{number} = Button(parent=ssubmenu, name='{name}', corner=0, command= lambda: Button.SubButtonClick('{name}'))")
            subbuttondict.append(a)
            
        for number, command in enumerate(subbuttondict):
            print(command, number)
            exec(command)
            exec(f"button{number}.grid(row={number}, sticky='ew')")
    
    def SubMenuVis(hidden: bool):
        if hidden == True:
            for but in ssubmenu.winfo_children():
                but.destroy()
                
        elif hidden == False:
            ssubmenu.grid(row=0, column=1, rowspan=9, sticky="nsw", padx=(5,0))

class Button(ctk.CTkButton):
        def __init__(self, parent, name: str, corner: int, command: callable):
            super().__init__(parent)

            self.configure(text=name)
            self.configure(corner_radius= corner)
            self.configure(command=command)
            
        def Main_Click(name):
            str_name = str(name)
            n_name = str_name.replace("{", "")
            nn_name = n_name.replace("}", "")
            nnn_name = nn_name.replace("'", "")
            print(nnn_name)
            path = Cisco_Syntax_MiddleMan.MainButton_Dir(name=name)
            list = Cisco_Syntax_MiddleMan.GetDir_List(path)
            if name == False:
                pass
            else:
                SubMenu.subbuttons(dir = list)
                pass

        def SubButtonClick(name):
            
            str_name = str(name)
            n_name = str_name.replace("{", "")
            nn_name = n_name.replace("}", "")
            nnn_name = nn_name.replace("'", "")
                
            print(nnn_name)


if __name__ == "__main__":
    App('Cisco Syntax', (1400,800))

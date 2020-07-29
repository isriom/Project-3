from tkinter import *  # libraries imported :GUI


class Window:
	def __init__(self):
		self.window = Tk()
		self.window.title("3C")
		self.screen = Canvas(self.window, width=700, height=600, bg="White")
		self.bill_image = PhotoImage(file="Plantillas menu\Bill.png")
		self.screen.pack()

class Menu:
	# images = {"logo_3C": PhotoImage(file="Plantillas menu/3clogo.png"),
	#           "main_menu_image": PhotoImage(file="Plantillas menu\dibujo.png")}

	def __init__(self, user):
		self.window = Window()
		self.menu_window = self.window.window
		self.menu_screen = self.window.screen
		self.user = user
		self.menu()

	def menu(self):
		main_menu_image = PhotoImage(file="Plantillas menu\dibujo.png")
		logo_3C = PhotoImage(file="Plantillas menu/3clogo.png")
		bill_image = PhotoImage(file="Plantillas menu\Bill.png")
		self.menu_screen.create_image(350, 300, image=main_menu_image)
		self.menu_screen.create_image(238, 73, image=logo_3C)
		# make_bill
		make_bill_button = Button(self.menu_screen, text="Make Bill", bg="#FBC281", height=4, width=21,
		                          command=lambda: (self.make_bill(bill_image))).place(x=535, y=29)

		# search_bill
		search_bill_button = Button(self.menu_screen, text="Search Bill", bg="#FBC281", height=4, width=21,
		                            command=lambda: (self.search_bill())).place(x=535, y=115)

		# delete_bill
		delete_bill_button = Button(self.menu_screen, text="Delete Bill", bg="#FBC281", height=4, width=21,
		                            command=lambda: (self.delete_bill())).place(x=535, y=197)
		# generate_report
		generate_report_button = Button(self.menu_screen, text="Generate Report", bg="#FBC281", height=4, width=21,
		                                command=lambda: (self.generate_report())).place(x=535, y=279)
		# add_services
		add_services_button = Button(self.menu_screen, text="Add Services", bg="#FBC281", height=4, width=21,
		                             command=lambda: (self.add_services())).place(x=535, y=361)
		# update_services
		upd_services_button = Button(self.menu_screen, text="Update Services", bg="#FBC281", height=4, width=21,
		                             command=lambda: (self.upd_services())).place(x=535, y=444)
		# generate_pdf
		generate_pdf_button = Button(self.menu_screen, text="Generate pdf", bg="#FBC281", height=4, width=21,
		                             command=lambda: (self.generate_pdf())).place(x=535, y=526)
		self.menu_window.mainloop()

	def make_bill(self, bill):
		sub_window = Window()
		sub_window.screen.create_image(350, 300, image=sub_window.bill_image)
		sub_window.window.mainloop()

	def search_bill(self):
		sub_window = Window()
		make_bill_text = Label(sub_window.screen, text="search_bill", bg="White", anchor=S).pack()
		sub_window.window.mainloop()

	def delete_bill(self):
		sub_window = Window()
		make_bill_text = Label(sub_window.screen, text="delete_bill", bg="White", anchor=S).pack()
		sub_window.window.mainloop()

	def generate_report(self):
		sub_window = Window()
		make_bill_text = Label(sub_window.screen, text="generate_report", bg="White", anchor=S).pack()
		sub_window.window.mainloop()

	def add_services(self):
		sub_window = Window()
		make_bill_text = Label(sub_window.screen, text="add_services", bg="White", anchor=S).pack()
		sub_window.window.mainloop()

	def upd_services(self):
		sub_window = Window()
		make_bill_text = Label(sub_window.screen, text="update_services", bg="White", anchor=S).pack()
		sub_window.window.mainloop()

	def generate_pdf(self):
		sub_window = Window()
		make_bill_text = Label(sub_window.screen, text="generate_pdf", bg="White", anchor=S).pack()
		sub_window.window.mainloop()


main_window = Menu(None)

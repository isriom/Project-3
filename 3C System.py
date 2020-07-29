from tkinter import *  # libraries imported :GUI


class Window:
	screen = Tk()
	screen.title("3C")
	sub_screen = Tk()
	sub_screen.title("3C")
	logo_3C = PhotoImage(file="Plantillas menu/3clogo.png")

	def __init__(self, user):
		self.user = user
		self.menu()

	def menu(self):
		main_menu = Canvas(self.screen, width=700, height=600, bg="White")
		main_menu.pack()
		main_menu_image = PhotoImage(file="Plantillas menu\dibujo.png")
		main_menu.create_image(350, 300, image=main_menu_image)
		main_menu.create_image(238, 73, image=self.logo_3C)
		# make_bill
		make_bill_button = Button(main_menu, text="Make Bill", bg="#FBC281", height=4, width=21,
		                          command=lambda: (self.make_bill())).place(x=535, y=29)

		# search_bill
		search_bill_button = Button(main_menu, text="Search Bill", bg="#FBC281", height=4, width=21,
		                            command=lambda: (self.search_bill())).place(x=535, y=115)

		# delete_bill
		delete_bill_button = Button(main_menu, text="Delete Bill", bg="#FBC281", height=4, width=21,
		                            command=lambda: (self.delete_bill())).place(x=535, y=197)
		# generate_report
		generate_report_button = Button(main_menu, text="Generate Report", bg="#FBC281", height=4, width=21,
		                                command=lambda: (self.generate_report())).place(x=535, y=279)
		# add_services
		add_services_button = Button(main_menu, text="Add Services", bg="#FBC281", height=4, width=21,
		                             command=lambda: (self.add_services())).place(x=535, y=361)
		# update_services
		upd_services_button = Button(main_menu, text="Update Services", bg="#FBC281", height=4, width=21,
		                             command=lambda: (self.upd_services())).place(x=535,  y=444)
		# generate_pdf
		generate_pdf_button = Button(main_menu, text="Generate pdf", bg="#FBC281", height=4, width=21,
		                             command=lambda: (self.generate_pdf())).place(x=535,  y=526)
		self.screen.mainloop()

	def make_bill(self):
		sub_menu = Canvas(self.sub_screen, width=700, height=600, bg="White")
		sub_menu.pack()
		make_bill_text = Label(sub_menu, text="BILL", bg="White", anchor=S).pack()
		self.screen.mainloop()

	def search_bill(self):
		sub_menu = Canvas(self.sub_screen, width=700, height=600, bg="White")
		sub_menu.pack()
		make_bill_text = Label(sub_menu, text="search_bill", bg="White", anchor=S).pack()
		self.screen.mainloop()

	def delete_bill(self):
		sub_menu = Canvas(self.sub_screen, width=700, height=600, bg="White")
		sub_menu.pack()
		make_bill_text = Label(sub_menu, text="delete_bill", bg="White", anchor=S).pack()
		self.screen.mainloop()

	def generate_report(self):
		sub_menu = Canvas(self.sub_screen, width=700, height=600, bg="White")
		sub_menu.pack()
		make_bill_text = Label(sub_menu, text="generate_report", bg="White", anchor=S).pack()
		self.screen.mainloop()

	def add_services(self):
		sub_menu = Canvas(self.sub_screen, width=700, height=600, bg="White")
		sub_menu.pack()
		make_bill_text = Label(sub_menu, text="add_services", bg="White", anchor=S).pack()
		self.screen.mainloop()

	def upd_services(self):
		sub_menu = Canvas(self.sub_screen, width=700, height=600, bg="White")
		sub_menu.pack()
		make_bill_text = Label(sub_menu, text="update_services", bg="White", anchor=S).pack()
		self.screen.mainloop()

	def generate_pdf(self):
		sub_menu = Canvas(self.sub_screen, width=700, height=600, bg="White")
		sub_menu.pack()
		make_bill_text = Label(sub_menu, text="generate_pdf", bg="White", anchor=S).pack()
		self.screen.mainloop()


main_window = Window(None)

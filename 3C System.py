from tkinter import *  # libraries imported :GUI


def top_level():
	global main_window
	window = Toplevel()
	window.title("3C")
	sub_menu_canva = Canvas(window, width=700, height=600, bg="White")
	sub_menu_canva.pack()
	return window, sub_menu_canva


class Menu:
	window = Tk()
	window.title("3C")
	menu_canva = Canvas(window, width=700, height=600, bg="White")
	menu_canva.pack()

	# screen.create_image(238, 73, image=logo_3C)
	def __init__(self, user):
		self.user = user
		self.menu()

	def menu(self):
		main_menu_image = PhotoImage(file="Plantillas menu\dibujo.png")
		logo_3C = PhotoImage(file="Plantillas menu/3clogo.png")
		self.menu_canva.create_image(350, 300, image=main_menu_image)
		self.menu_canva.create_image(238, 73, image=logo_3C)
		# make_bill
		make_bill_button = Button(self.menu_canva, text="Make Bill", bg="#FBC281", height=4, width=21,
		                          command=lambda: (self.make_bill())).place(x=535, y=29)

		# search_bill
		search_bill_button = Button(self.menu_canva, text="Search Bill", bg="#FBC281", height=4, width=21,
		                            command=lambda: (self.search_bill())).place(x=535, y=115)

		# delete_bill
		delete_bill_button = Button(self.menu_canva, text="Delete Bill", bg="#FBC281", height=4, width=21,
		                            command=lambda: (self.delete_bill())).place(x=535, y=197)
		# generate_report
		generate_report_button = Button(self.menu_canva, text="Generate Report", bg="#FBC281", height=4, width=21,
		                                command=lambda: (self.generate_report())).place(x=535, y=279)
		# add_services
		add_services_button = Button(self.menu_canva, text="Add Services", bg="#FBC281", height=4, width=21,
		                             command=lambda: (self.add_services())).place(x=535, y=361)
		# update_services
		upd_services_button = Button(self.menu_canva, text="Update Services", bg="#FBC281", height=4, width=21,
		                             command=lambda: (self.upd_services())).place(x=535, y=444)
		# generate_pdf
		generate_pdf_button = Button(self.menu_canva, text="Generate pdf", bg="#FBC281", height=4, width=21,
		                             command=lambda: (self.generate_pdf())).place(x=535, y=526)
		self.window.mainloop()

	def make_bill(self):
		sub_window, sub_canva = top_level()
		sub_window.bill_image = PhotoImage(file="Plantillas menu/Bill.png")
		sub_canva.create_image(350, 300, image=sub_window.bill_image)

	def search_bill(self):
		sub_window, sub_canva = top_level()
		make_bill_text = Label(sub_canva, text="search_bill", bg="White", anchor=S).pack()


	def delete_bill(self):
		sub_window, sub_canva = top_level()
		make_bill_text = Label(sub_canva, text="delete_bill", bg="White", anchor=S).pack()


	def generate_report(self):
		sub_window, sub_canva = top_level()
		make_bill_text = Label(sub_canva, text="generate_report", bg="White", anchor=S).pack()


	def add_services(self):
		sub_window, sub_canva = top_level()
		make_bill_text = Label(sub_canva, text="add_services", bg="White", anchor=S).pack()


	def upd_services(self):
		sub_window, sub_canva = top_level()
		make_bill_text = Label(sub_canva, text="update_services", bg="White", anchor=S).pack()


	def generate_pdf(self):
		sub_window, sub_canva = top_level()
		make_bill_text = Label(sub_canva, text="generate_pdf", bg="White", anchor=S).pack()



main_window = Menu(None)

from tkinter import *  # libraries imported :GUI


class Window:
	screen = Tk()
	screen.geometry("700x600")
	screen.title("3C")
	user = None

	def __init__(self):
		# while self.user is None:
		# 	Call (face recognit algoritm).
		# 	pass
		self.menu()

	def menu(self):
		main_menu = Canvas(self.screen, width=700, height=600, bg="DarkGrey")
		main_menu.pack()
		# make_bill
		make_bill_text = Label(main_menu, text="Make_bill", bg="DarkGrey", anchor=S).pack()
		make_bill_button = Button(main_menu, text="     ",
		                          command=lambda: (self.screen.quit(), main_menu.destroy(), self.make_bill())).pack()

		# search_bill
		search_bill_text = Label(main_menu, text="search_bill", bg="DarkGrey", anchor=W).pack()
		search_bill_button = Button(main_menu, text="   ",
		                            command=lambda: (
			                            self.screen.quit(), main_menu.destroy(), self.search_bill())).pack()

		# delete_bill
		delete_bill_text = Label(main_menu, text="delete_bill", bg="DarkGrey", anchor=W).pack()
		delete_bill_button = Button(main_menu, text="   ",
		                            command=lambda: (
			                            self.screen.quit(), main_menu.destroy(), self.delete_bill())).pack()
		# generate_report
		generate_report_text = Label(main_menu, text="generate_report", bg="DarkGrey", anchor=W).pack()
		generate_report_button = Button(main_menu, text="   ",
		                                command=lambda: (
			                                self.screen.quit(), main_menu.destroy(), self.generate_report())).pack()
		# add_services
		add_services_text = Label(main_menu, text="add_services", bg="DarkGrey", anchor=W).pack()
		add_services_button = Button(main_menu, text="  ",
		                             command=lambda: (
			                             self.screen.quit(), main_menu.destroy(), self.add_services())).pack()
		# update_services
		upd_services_text = Label(main_menu, text="upd_services", bg="DarkGrey", anchor=W).pack()
		upd_services_button = Button(main_menu, text="  ",
		                             command=lambda: (
			                             self.screen.quit(), main_menu.destroy(), self.upd_services())).pack()
		# generate_pdf
		generate_pdf_text = Label(main_menu, text="generate_pdf", bg="DarkGrey", anchor=W).pack()
		generate_pdf_button = Button(main_menu, text="  ",
		                             command=lambda: (
			                             self.screen.quit(), main_menu.destroy(), self.generate_pdf())).pack()
		self.screen.mainloop()

	def make_bill(self):
		main_menu = Canvas(self.screen, width=700, height=600, bg="White")
		main_menu.pack()
		make_bill_text = Label(main_menu, text="BILL", bg="White", anchor=S).pack()
		self.screen.mainloop()

	def search_bill(self):
		main_menu = Canvas(self.screen, width=700, height=600, bg="White")
		main_menu.pack()
		make_bill_text = Label(main_menu, text="search_bill", bg="White", anchor=S).pack()
		self.screen.mainloop()

	def delete_bill(self):
		main_menu = Canvas(self.screen, width=700, height=600, bg="White")
		main_menu.pack()
		make_bill_text = Label(main_menu, text="delete_bill", bg="White", anchor=S).pack()
		self.screen.mainloop()

	def generate_report(self):
		main_menu = Canvas(self.screen, width=700, height=600, bg="White")
		main_menu.pack()
		make_bill_text = Label(main_menu, text="generate_report", bg="White", anchor=S).pack()
		self.screen.mainloop()

	def add_services(self):
		main_menu = Canvas(self.screen, width=700, height=600, bg="White")
		main_menu.pack()
		make_bill_text = Label(main_menu, text="add_services", bg="White", anchor=S).pack()
		self.screen.mainloop()

	def upd_services(self):
		main_menu = Canvas(self.screen, width=700, height=600, bg="White")
		main_menu.pack()
		make_bill_text = Label(main_menu, text="update_services", bg="White", anchor=S).pack()
		self.screen.mainloop()

	def generate_pdf(self):
		main_menu = Canvas(self.screen, width=700, height=600, bg="White")
		main_menu.pack()
		make_bill_text = Label(main_menu, text="generate_pdf", bg="White", anchor=S).pack()
		self.screen.mainloop()


main_window = Window()

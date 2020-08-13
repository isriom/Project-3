from tkinter import *  # libraries imported :GUI
from tkinter import ttk  # libraries imported :GUI
from typing import Iterable
from fpdf import FPDF
import face_recognition
import numpy as np
import cv2
import os
from PIL import ImageTk, Image
import datetime
import webbrowser


class Services:

	def __init__(self, name, price):
		self.name = name
		self.price = price
		service_list.append(self)

	def add_service(self):
		file = open(r"clients/" + self.name + ".txt", "x")
		service = "" + self.name + "\n" + self.price
		file.write(service)


class Client:
	def __init__(self, data, name, email):
		self.email = email
		self.name = name
		self.data = data
		self.bill = []
		clients_list.append(self)

	def update_bills(self):
		file = open("clients/" + str(self.data), "r")
		for bill in file.read().splitlines()[3:]:
			if (bill + ".pdf") in os.listdir("invoices/"):
				self.bill.append(bill)

	def add_client(self):
		file = open(r"clients/" + self.data + ".txt", "x")
		client = "" + self.name + "\n" + self.data + "\n" + self.email + ""
		file.write(client)


class Menu:
	"""
	The main menu Class
	"""
	window = Tk()
	window.title("3C")
	menu_canva = Canvas(window, width=700, height=600, bg="White")
	menu_canva.pack()
	logo_3C = PhotoImage(file="Plantillas menu/3clogo.png")

	# screen.create_image(238, 73, image=logo_3C)

	def __init__(self, user):
		"""
		Call the creation of the menu GUI and load the user
		:param user: name of the user
		"""
		self.user = user
		self.menu()

	def menu(self):
		main_menu_image = PhotoImage(file="Plantillas menu\dibujo.png")
		user_image = Image.open("user_database/" + self.user)
		user_image = user_image.resize((436, 435), Image.ANTIALIAS)
		user_photo = ImageTk.PhotoImage(user_image)
		self.menu_canva.create_image(350, 300, image=main_menu_image)
		self.menu_canva.create_image(238, 73, image=self.logo_3C)
		self.menu_canva.create_image(237, 382, image=user_photo)
		# make_bill
		Button(self.menu_canva, text="Make Bill", bg="#FBC281", height=4, width=21,
		       command=lambda: (Bill(self))).place(x=535, y=29)
		# search_bill
		Button(self.menu_canva, text="Search Bill", bg="#FBC281", height=4, width=21,
		       command=lambda: (BillSearch(self))).place(x=535, y=115)
		# delete_bill
		Button(self.menu_canva, text="Delete Bill", bg="#FBC281", height=4, width=21,
		       command=lambda: (BillSearch(self))).place(x=535, y=197)
		# generate_report
		Button(self.menu_canva, text="Generate Report", bg="#FBC281", height=4, width=21,
		       command=lambda: (BillSearch(self))).place(x=535, y=279)
		# add_services
		Button(self.menu_canva, text="Add Services", bg="#FBC281", height=4, width=21,
		       command=lambda: (self.add_services())).place(x=535, y=361)
		# update_services
		Button(self.menu_canva, text="Register", bg="#FBC281", height=4, width=21,
		       command=lambda: (Register(self, user))).place(x=535, y=444)
		# generate_pdf
		Button(self.menu_canva, text="Generate pdf", bg="#FBC281", height=4, width=21,
		       command=lambda: (BillSearch(self))).place(x=535, y=526)
		self.window.mainloop()

	def add_services(self):
		sub_window, sub_canva = top_level()
		make_bill_text = Label(
			sub_canva, text="add_services", bg="White", anchor=S).pack()

	def upd_services(self):
		sub_window, sub_canva = top_level()
		make_bill_text = Label(
			sub_canva, text="update_services", bg="White", anchor=S).pack()


class Bill:
	"""
	Class that determine the GUI and algorithms to create a bill and add a new client
	"""
	def __init__(self, main):
		"""
		call the GUI and load all the available clients
		:param main: root tkinter object
		"""
		load_clients()
		load_services()
		self.main = main
		self.sub_window, self.sub_canva = top_level()
		self.services_view = ttk.Treeview(self.sub_canva, selectmode='browse', height=6, show="tree")
		self.client_id = StringVar()
		self.client_id.set("EM" + str(len(os.listdir("clients/")) + 1))
		self.client_name = StringVar()
		self.client_email = StringVar()
		self.bil_number = IntVar()
		self.bil_number.set(number_bill())
		self.date = datetime.date.today()
		self.due_date = ""
		self.services_data = []
		self.services = StringVar()
		self.services.set("Service")
		self.quantity = IntVar()
		self.total = IntVar()
		self.price = IntVar()
		self.sub_total = IntVar()
		self.taxes = IntVar()
		self.total_with_taxes = IntVar()
		self.make_bill()

	def make_bill(self):
		sub_window, sub_canva = self.sub_window, self.sub_canva
		sub_window.bill_image = PhotoImage(file="Plantillas menu/Bill.png")
		sub_canva.create_image(350, 300, image=sub_window.bill_image)
		sub_canva.create_image(350, 73, image=self.main.logo_3C)
		bill_time = datetime.timedelta(days=2)
		self.due_date = self.date + bill_time

		# tree
		services_view = self.services_view

		services_view["columns"] = ("quantity", "sub total")
		services_view.column("#0", width=255)  # services
		services_view.column("quantity", width=160)
		services_view.column("sub total", width=105)
		services_view["displaycolumns"] = ("quantity", "sub total")
		services_view.place(x=18, y=427)
		scroll = create_scroll(sub_canva, services_view, "vertical", x=549, y=428)

		# combobox´s
		customer_data = ttk.Combobox(sub_canva, state="normal", width=30, textvariable=self.client_id)
		customer_data["values"] = clients_list
		customer_data.place(x=208, y=178, height=22)

		customer_name = ttk.Combobox(sub_canva, state="normal", width=30, textvariable=self.client_name)
		customer_name["values"] = clients_names
		customer_name.place(x=208, y=208, height=22)

		service = ttk.Combobox(sub_canva, state="normal", width=33, text="Service", textvariable=self.services)
		service["values"] = service_list
		service.place(x=20, y=338, height=32)

		# labels

		bill_number = Label(sub_canva, width=12, bg="MistyRose2", textvariable=self.bil_number)
		bill_number.place(x=538, y=178, height=22)

		date = Label(sub_canva, width=12, bg="MistyRose2", text=self.date)
		date.place(x=538, y=208, height=22)

		due_date = Label(sub_canva, width=12, bg="MistyRose2", text=self.due_date)
		due_date.place(x=538, y=238, height=22)

		price = Label(sub_canva, width=13, bg="chartreuse3", textvariable=self.price)
		price.place(x=398, y=338, height=32)

		sub_total = Label(sub_canva, width=12, bg="chartreuse3", textvariable=self.sub_total)
		sub_total.place(x=508, y=338, height=32)

		amount = Label(sub_canva, width=12, bg="HotPink3", textvariable=self.total)
		amount.place(x=578, y=428, height=33)

		tax = Label(sub_canva, width=12, bg="HotPink3", textvariable=self.taxes)
		tax.place(x=578, y=508, height=33)

		total = Label(sub_canva, width=12, bg="HotPink3", textvariable=self.total_with_taxes)
		total.place(x=578, y=548, height=33)

		# entry
		quantity_entry = Entry(sub_canva, textvariable=self.quantity, width=23)
		quantity_entry.place(x=249, y=339, height=32)

		customer_email = Entry(sub_canva, textvariable=self.client_email, width=33)
		customer_email.place(x=208, y=238, height=22)

		# buttons
		delete_services_button = Button(sub_canva, text="X", bg="seashell3", height=1, width=5,
		                                command=lambda: (self.clear_bill_services())).place(x=618, y=298)

		add_services_button = Button(sub_canva, text="!", bg="seashell3", height=1, width=5,
		                             command=(lambda: self.call_add_button())).place(
			x=618, y=338)

		add_bill = Button(sub_canva, text="Accept", bg="#FBC281", height=1, width=15,
		                  command=lambda: (self.add_client(services_view))).place(x=33, y=563)

		delete_bill = Button(sub_canva, text="Delete", bg="#FBC281", height=1, width=15,
		                     command=lambda: self.sub_window.destroy()).place(x=188, y=563)

		# events
		customer_data.bind("<<ComboboxSelected>>", lambda event: self.found_client())
		customer_name.bind("<<ComboboxSelected>>", lambda event: self.found_client())
		service.bind("<<ComboboxSelected>>", lambda event: self.upd_temp_bill())
		services_view.bind('<ButtonRelease-1>', self.select_item)
		quantity_entry.bind("<Key>", lambda event: self.upd_temp_bill())

	def clear_bill_services(self):
		try:
			service = self.services_view.selection()[0]
			amount = self.services_view.item(service)["values"][1]
			self.total.set(self.total.get() - int(amount))
			self.taxes.set(self.total.get() * 0.13)
			self.total_with_taxes.set(self.total.get() + self.taxes.get())
			self.services_view.delete(service)
		finally:
			self.services.set("")
			self.quantity.set(0)

	def add_client(self, tree):
		if self.client_id.get() in clients_list:
			# Create a txt
			bill = "Client" + "\n" + self.client_id.get() + ":" + self.client_name.get() + "\n" + "Dates" + "\n" + str(
				self.date) + ":" + str(
				self.due_date) + "\n" + "Services            Quantity        Total" + "\n"
			services = 0
			for line in tree.get_children():
				bill = bill + str(tree.item(line)["text"])
				for value in tree.item(line)['values']:
					bill = bill + " " + str(value)
				bill = bill + "\n"
			file = open(r"bills/" + str(self.bil_number.get()) + ".txt", "x")
			file.write(bill + "total" + "\n" + str(self.total_with_taxes.get()))
			file.close()

			# Create a pdf using the txt as template
			# put a header
			pdf_bill = FPDF('P', 'mm', 'A4')
			pdf_bill.add_page()
			pdf_bill.set_font("times", "B", 30)
			pdf_bill.image("Plantillas menu/3clogo.png", 10, 8, 70)
			pdf_bill.cell(80)
			pdf_bill.cell(70, 10, ("Bill:  " + str(self.bil_number.get()) + "°"), 1, 1, 'C')
			pdf_bill.ln(10)
			# put the data
			pdf_bill.set_font("helvetica", size=12)
			for line in bill.split("\n"):
				pdf_bill.cell(600, 3, str(line), 0, 1)
				pdf_bill.ln()
			pdf_bill.cell(600, 3, "total:" + str(self.total.get()), 0, 1)
			pdf_bill.output("invoices/" + str(self.bil_number.get()) + ".pdf", 'F')
			file = open(r"clients/" + str(self.client_id.get()) + ".txt", "a")
			file.write("\n" + str(self.bil_number.get()))

		else:
			new_client = self.client_id.get()
			client_name = self.client_name.get()
			client_email = self.client_email.get()
			new_client = Client(new_client, client_name, client_email)
			new_client.add_client()
			self.add_client(tree)

	def tree_insert(self, tree):
		tree.insert('', 'end', text=self.services.get(), values=(
			self.quantity.get(), self.quantity.get() * service_price[service_list.index(self.services.get())]))
		self.total.set(self.total.get() + self.sub_total.get())
		self.taxes.set(self.total.get() * 0.13)
		self.total_with_taxes.set(self.total.get() + self.taxes.get())
		"""need to get the price of the services"""
		return

	def found_client(self):
		global clients_list, clients_names
		if self.client_id.get() in clients_list:
			indice = clients_list.index(self.client_id.get())
			self.client_email.set(clients_emails[indice])
			self.client_name.set(clients_names[indice])
		if self.client_name.get() in clients_names:
			indice = clients_names.index(self.client_name.get())
			self.client_email.set(clients_emails[indice])
			self.client_id.set(clients_list[indice])

	def upd_temp_bill(self):
		self.price.set(service_price[service_list.index(self.services.get())])
		
		self.sub_total.set(self.price.get() * self.quantity.get())

	def select_item(self, event):
		service = self.services_view.item(self.services_view.focus())
		#if service not in service_list:
		#	self.service_list.append(service)
		self.services.set(service["text"])
		self.quantity.set(service["values"][0])

	def call_add_button(self):
		self.upd_temp_bill()
		self.tree_insert(self.services_view)


class BillSearch:
	"""
	Class that determine the GUI and algoritm to search bills and generate reports
	"""

	def __init__(self, main):
		"""
		call the GUI and load all the available bills
		:param main: root tkinter object
		"""
		self.main = main
		self.sub_window, self.sub_canva = top_level()
		self.services_view = ttk.Treeview(self.sub_canva, selectmode='browse', height=10, show="tree")

		self.min_day = IntVar()
		self.min_day.set(1)
		self.min_month = IntVar()
		self.min_month.set(1)
		self.min_year = IntVar()
		self.min_year.set(1970)

		self.max_day = IntVar()
		self.max_day.set(28)
		self.max_month = IntVar()
		self.max_month.set(12)
		self.max_year = IntVar()
		self.max_year.set(9999)

		self.max_date = datetime.date(self.max_year.get(), self.max_month.get(), self.max_day.get())
		self.min_date = datetime.date(self.min_year.get(), self.min_month.get(), self.min_day.get())

		self.total = IntVar()

		self.search_bill()

	def search_bill(self):
		sub_window, sub_canva = self.sub_window, self.sub_canva
		sub_window.bill_search_image = PhotoImage(file="Plantillas menu/Bill search.png")
		sub_canva.create_image(350, 300, image=sub_window.bill_search_image)
		sub_canva.create_image(350, 73, image=self.main.logo_3C)

		# tree
		self.services_view["columns"] = ("Client", "Dates", "total bill")
		self.services_view.column("#0", width=70)  # services
		self.services_view.column("Client", width=170)
		self.services_view.column("Dates", width=170)
		self.services_view.column("total bill", width=110)
		self.services_view.place(x=18, y=346)
		scroll = create_scroll(sub_canva, self.services_view, "vertical", x=548, y=348)
		self.tree_insert()

		# combobox´s
		min_day = ttk.Combobox(sub_canva, state="normal", width=6, text="day", textvariable=self.min_day)
		min_day["values"] = data_range(30)
		min_day.place(x=70, y=229, height=30)

		min_month = ttk.Combobox(sub_canva, state="normal", width=6, text="month", textvariable=self.min_month)
		min_month["values"] = data_range(12)
		min_month.place(x=132, y=229, height=30)

		min_year = ttk.Combobox(sub_canva, state="normal", width=6, text="year", textvariable=self.min_year)
		min_year["values"] = data_range(datetime.date.today().year, 1970)
		min_year.place(x=195, y=229, height=30)

		max_day = ttk.Combobox(sub_canva, state="normal", width=6, text="day", textvariable=self.max_day)
		max_day["values"] = data_range(30)
		max_day.place(x=443, y=229, height=30)

		max_month = ttk.Combobox(sub_canva, state="normal", width=6, text="month", textvariable=self.max_month)
		max_month["values"] = data_range(12)
		max_month.place(x=505, y=229, height=30)

		max_year = ttk.Combobox(sub_canva, state="normal", width=6, text="year", textvariable=self.max_year)
		max_year["values"] = data_range(datetime.date.today().year + 1, 1970)
		max_year.place(x=568, y=229, height=30)

		# labels

		total = Label(sub_canva, width=14, bg="HotPink3", textvariable=self.total)
		total.place(x=438, y=548, height=33)

		# buttons

		report_button = Button(sub_canva, text="Report", bg="seashell3", height=1, width=8,
		                       command=(lambda: self.make_report())).place(x=592, y=331)

		pdf_bill = Button(sub_canva, text="!", bg="seashell3", height=1, width=8,
		                  command=lambda: self.item_pdf()).place(x=592, y=402)

		delete_bill = Button(sub_canva, text="X", bg="seashell3", height=1, width=8,
		                     command=lambda: self.delete_bill()).place(x=592, y=472)

		# events
		min_year.bind("<<ComboboxSelected>>", lambda event: self.days_sort())
		min_month.bind("<<ComboboxSelected>>", lambda event: self.days_sort())
		min_day.bind("<<ComboboxSelected>>", lambda event: self.days_sort())
		max_year.bind("<<ComboboxSelected>>", lambda event: self.days_sort())
		max_month.bind("<<ComboboxSelected>>", lambda event: self.days_sort())
		max_day.bind("<<ComboboxSelected>>", lambda event: self.days_sort())

	def tree_insert(self, arg=False):
		if arg:
			self.total.set(0)
			for item in self.services_view.get_children():
				self.services_view.delete(item)
		list = []
		for bills in os.listdir("invoices/"):
			# load available bills id
			indice = bills.find(".pdf")
			list.append(bills[:indice])

		for bill in list:

			# load bill data
			file = open("bills/" + bill + ".txt", "r")
			file = file.read().splitlines()
			date = file[3]
			date = date.split(":")[0]
			date = date.split("-")
			date = datetime.date(int(date[0]), int(date[1]), int(date[2]))
			# check if the bill satisfy the date condition
			if self.max_date > date > self.min_date:
				self.services_view.insert('', 'end', text=bill, values=(
					file[1], file[3], file[-1]))
				self.total.set(self.total.get() + int(file[-1]))

		return

	def days_sort(self):
		self.max_date = datetime.date(self.max_year.get(), self.max_month.get(), self.max_day.get())
		self.min_date = datetime.date(self.min_year.get(), self.min_month.get(), self.min_day.get())
		self.tree_insert(True)
		pass

	def item_pdf(self):
		item = self.services_view.item(self.services_view.focus())
		os.startfile(os.getcwd() + "/invoices/" + item["text"] + ".pdf")

	def delete_bill(self):
		item = self.services_view.item(self.services_view.focus())

		os.remove(os.getcwd() + "/invoices/" + item["text"] + ".pdf")
		self.tree_insert(True)

	def make_report(self):
		# Create a pdf using the txt as template
		# put a header
		pdf_bill = FPDF('P', 'mm', 'A4')
		pdf_bill.add_page()
		pdf_bill.set_font("times", "B", 30)
		pdf_bill.image("Plantillas menu/3clogo.png", 10, 8, 70)
		pdf_bill.cell(80)
		pdf_bill.cell(70, 10, ("Report"), 1, 1, 'C')
		pdf_bill.ln(10)

		# put the data
		pdf_bill.set_font("helvetica", size=12)
		pdf_bill.cell(20, 10, ("Bill"), 1, 0)
		pdf_bill.cell(2)
		pdf_bill.cell(70, 10, ("Client"), 1, 0)
		pdf_bill.cell(2)
		pdf_bill.cell(70, 10, ("Sub total"), 1, 1)

		for bills in os.listdir("bills/"):
			# load bill data
			file = open("bills/" + bills, "r")
			file = file.read().splitlines()
			date = file[3]
			date = date.split(":")[0]
			date = date.split("-")
			date = datetime.date(int(date[0]), int(date[1]), int(date[2]))
			# check if the bill satisfy the date condition

			if self.max_date > date > self.min_date:
				pdf_bill.cell(20, 10, (bills.split(".")[0]), 1, 0, "C")
				pdf_bill.cell(2)
				pdf_bill.cell(70, 10, (file[1]), 1, 0)
				pdf_bill.cell(2)
				pdf_bill.cell(70, 10, (file[-1]), 1, 0)
				pdf_bill.ln()
				self.total.set(self.total.get() + int(file[-1]))

		pdf_bill.ln(3)
		pdf_bill.cell(95)
		pdf_bill.cell(15, 10, ("taxes"), 1, 0, "C")
		pdf_bill.cell(40, 10, (str(self.total.get() * 0.13)), 1, 1)
		pdf_bill.cell(95)
		pdf_bill.cell(15, 10, ("Total"), 1, 0, "C")
		pdf_bill.cell(40, 10, (str(self.total.get())), 1, 0)

		pdf_bill.output("reports/report.pdf", 'F')
		os.startfile(os.getcwd() + "/reports/report.pdf")


def create_scroll(canvas, object, orientation, x=0, y=0):
	"""
	Auto create a scroll that adapt to the parent object
	:param canvas: canvas to insert the scroll
	:param object: parent objecto of the scroll
	:param orientation: "vertical" or "horizontal"
	:param x: position to place the scroll
	:param y: position to place the scroll
	:return: scroll widget
	"""
	if orientation == "vertical":
		orientation = "vertical"
	else:
		orientation = "horizontal"
	scroll = ttk.Scrollbar(canvas, orient=orientation, command=object.yview)
	scroll.place(x=x, y=y, height=object["height"] * 18.65)
	return scroll


def load_clients():
	"""
	load all the clients id, clients names and clients emails in the globals variable
	:return: None
	"""
	global clients_list, clients_names, clients_emails
	list = []
	list2 = []
	list3 = []
	for client in os.listdir("clients/"):
		# load client id
		indice = client.find(".txt")
		list.append(client[:indice])
		# load client names
		file = open("clients/" + client, "r")
		file = file.read().splitlines()
		list2.append(file[0])
		# load clients emails
		list3.append(file[2])
	# save in memory the clients data
	clients_list = list
	clients_names = list2
	clients_emails = list3


def data_range(max: int, min: int = 0):
	"""
	create a inverse list to easiest the input
	:param max: The top limit of the range
	:param min: The bottom limit og the range, by default is 0
	:return: a list start form the top of the range and end in the bottom
	"""
	if max == min:
		return []
	return [max] + data_range(max - 1, min)


def load_services():
	"""
	load in the global variables all the services than can use the bill
	:return: None
	"""
	global service_list, service_price
	list = []
	list2 = []
	for services in os.listdir("services/"):
		file = open(r"services/" + services, "r")
		file = file.read().splitlines()
		list.append(file[0])
		list2.append(int(file[1]))
	service_list = list
	service_price = list2


def number_bill():
	"""
	generate a number for the bill
	:return: number bill autoo generated
	"""
	number: int = 0
	bills = os.listdir("bills/")
	for number in bills:
		indice = number.find(".txt")
		number = number[:indice]
		number = int(number)
	return number + 1


def load_users():
	"""
	search for all the user name in the data base and create his face encodings
	:return: None
	"""
	for user in os.listdir("user_database"):
		image = face_recognition.load_image_file(r"user_database/" + user)
		face_encoding = face_recognition.face_encodings(
			image, num_jitters=1)[0]
		faces.append(face_encoding)
		users.append(user)


def login_image():
	"""
	Create a img to compare with the database
	:return: None
	"""
	cam = cv2.VideoCapture(0)

	cv2.namedWindow("FaceCapture")

	while True:
		ret, frame = cam.read()
		if not ret:
			print("failed to grab frame")
			break
		cv2.imshow("test", frame)

		k = cv2.waitKey(1)
		if k % 256 == 32:  # Space pressed
			user_face = "user_0.png"
			file = cv2.imwrite(r"user_database/" + user_face, frame)
			print("User_0 written!")
			print("Closing...")
			break

	cam.release()
	cv2.destroyAllWindows()


def login():
	"""
	Check all the images in the database and compare with the img form login image
	:return: a tuple that indicate if user is in the database and user
	"""
	# ---------------------------------------------------------------------------------
	# This sentences will load and encode the image and face of the person trying to login
	image_of_user = face_recognition.load_image_file(
		"user_database/user_0.png")
	user_face_encoding = face_recognition.face_encodings(image_of_user)[0]
	# ---------------------------------------------------------------------------------

	results = False
	if True in face_recognition.compare_faces(faces, user_face_encoding, 0.469):
		print(face_recognition.compare_faces(faces, user_face_encoding, 0.469))

		results = True
	# ---------------------------------------------------------------------------------
	# Print the results
	if results:
		print("Welcome!")
		return True, face_recognition.compare_faces(faces, user_face_encoding, 0.469).index(True)
	else:
		print("You are not in our database! Please create your profile or get in contact with support")
		return Register()

class Register:

	def __init__(self, main, user):

		self.user = user
		self.main = main
		self.sub_window, self.sub_canva = top_level()
		self.services_view = ttk.Treeview(self.sub_canva, selectmode='browse', height=10, show="tree")
		self.face_registration()

	def face_registration(self):
		main_menu_image = PhotoImage(file="Plantillas menu\Add_user.png")
		user_image = Image.open("user_database/" + self.user)
		user_image = user_image.resize((436, 435), Image.ANTIALIAS)
		user_photo = ImageTk.PhotoImage(user_image)
		self.sub_canva.create_image(350, 300, image=main_menu_image)
		self.sub_canva.create_image(238, 73, image=self.logo_3C)
		self.menu_canva.create_image(237, 382, image=user_photo)
		name_entry = textBox.get()
		self.name_entry.pack()
		
		






		self.window.mainloop()


def top_level():
	"""
	:return: a tuple with a topelevel quith title and size defined and they canvas
	"""
	global main_window
	window = Toplevel()
	window.title("3C")
	sub_menu_canva = Canvas(window, width=700, height=600, bg="White")
	sub_menu_canva.pack()
	return window, sub_menu_canva


faces = []
users = []
clients_list = []
clients_names = []
clients_emails = []
service_list = []
service_price = []

load_clients()
load_users()
load_services()
login_image()
sucefull_login, user = login()
if sucefull_login:
	main_window = Menu(users[user])
#else:
#	face_registration()

os.remove("user_database/user_0.png")

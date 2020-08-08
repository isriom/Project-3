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


class Client:
	def __init__(self, data, name, email):
		self.email = email
		self.name = name
		self.data = data
		self.bill = []
		clients_list.append(self)

	def update_bills(self):  # placeholder for clients bill
		pass

	def add_client(self):
		file = open(r"clients/" + self.data + ".txt", "x")
		print("newclient")
		client = "" + self.name + "\n" + self.data + "\n" + self.email + ""
		print(client)
		file.write(client)


class Menu:
	window = Tk()
	window.title("3C")
	menu_canva = Canvas(window, width=700, height=600, bg="White")
	menu_canva.pack()
	logo_3C = PhotoImage(file="Plantillas menu/3clogo.png")

	# screen.create_image(238, 73, image=logo_3C)

	def __init__(self, user):
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
		make_bill_button = Button(self.menu_canva, text="Make Bill", bg="#FBC281", height=4, width=21,
		                          command=lambda: (Bill(self))).place(x=535, y=29)

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

	def update_price_bill(self, quantity, service):
		pass

	def search_bill(self):
		sub_window, sub_canva = top_level()
		make_bill_text = Label(
			sub_canva, text="search_bill", bg="White", anchor=S).pack()

	def delete_bill(self):
		sub_window, sub_canva = top_level()
		make_bill_text = Label(
			sub_canva, text="delete_bill", bg="White", anchor=S).pack()

	def generate_report(self):
		sub_window, sub_canva = top_level()
		make_bill_text = Label(
			sub_canva, text="generate_report", bg="White", anchor=S).pack()

	def add_services(self):
		sub_window, sub_canva = top_level()
		make_bill_text = Label(
			sub_canva, text="add_services", bg="White", anchor=S).pack()

	def upd_services(self):
		sub_window, sub_canva = top_level()
		make_bill_text = Label(
			sub_canva, text="update_services", bg="White", anchor=S).pack()

	def generate_pdf(self):
		sub_window, sub_canva = top_level()
		make_bill_text = Label(
			sub_canva, text="generate_pdf", bg="White", anchor=S).pack()


class Bill:

	def __init__(self, main, arg=0):
		load_clients()
		self.main = main
		self.client_id = StringVar()
		self.client_name = StringVar()
		self.client_email = StringVar()
		self.bil_number = IntVar()
		self.bil_number.set(number_bill())
		self.date = "%/%/%"
		self.due_date = ""
		self.services_data = []
		self.services = StringVar()
		self.quantity = IntVar()
		self.total = IntVar()
		if arg == 0:
			self.make_bill()
		elif arg == 1:
			pass

	def make_bill(self):
		sub_window, sub_canva = top_level()
		sub_window.bill_image = PhotoImage(file="Plantillas menu/Bill.png")
		sub_canva.create_image(350, 300, image=sub_window.bill_image)
		sub_canva.create_image(350, 73, image=self.main.logo_3C)
		self.date = datetime.date.today()
		bill_time = datetime.timedelta(days=2)
		self.due_date = self.date + bill_time

		# tree
		services_view = ttk.Treeview(sub_canva, selectmode='browse', height=6, show="tree")
		ttk.Style().configure("Treeview", background="SpringGreen3",
		                      foreground="SpringGreen2")
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

		service = ttk.Combobox(sub_canva, state="normal", width=33, textvariable=self.services)
		service["values"] = ("Almendro", "Pablo")
		service.place(x=20, y=338, height=32)

		# labels

		bill_number = Label(sub_canva, width=12, bg="MistyRose2", textvariable=self.bil_number)
		bill_number.place(x=538, y=178, height=22)

		date = Label(sub_canva, width=12, bg="MistyRose2", text=self.date)
		date.place(x=538, y=208, height=22)

		due_date = Label(sub_canva, width=12, bg="MistyRose2", text=self.due_date)
		due_date.place(x=538, y=238, height=22)

		price = Label(sub_canva, width=13, bg="chartreuse3", textvariable="asd")
		price.place(x=398, y=338, height=32)

		sub_total = Label(sub_canva, width=12, bg="chartreuse3", text="price*quantity")
		sub_total.place(x=508, y=338, height=32)

		amount = Label(sub_canva, width=12, bg="HotPink3", text="sum all amounts")
		amount.place(x=578, y=428, height=33)

		tax = Label(sub_canva, width=12, bg="HotPink3", text="13%*amount")
		tax.place(x=578, y=508, height=33)

		total = Label(sub_canva, width=12, bg="HotPink3", textvariable=self.total)
		total.place(x=578, y=548, height=33)
		print("asdda")

		# entry
		quantity_entry = Entry(sub_canva, textvariable=self.quantity, width=23)
		quantity_entry.place(x=249, y=339, height=32)

		customer_email = Entry(sub_canva, textvariable=self.client_email, width=33)
		customer_email.place(x=208, y=238, height=22)

		# buttons
		add_services_button = Button(sub_canva, text="X", bg="seashell3", height=1, width=5,
		                             command=lambda: (self.update_bill_services())).place(x=618, y=298)

		delete_services_button = Button(sub_canva, text="!", bg="seashell3", height=1, width=5,
		                                command=lambda: (self.tree_insert(services_view) and self.clear_bill_services())).place(
			x=618, y=338)

		add_bill = Button(sub_canva, text="Accept", bg="#FBC281", height=1, width=15,
		                  command=lambda: (self.add_client(services_view))).place(x=33, y=563)

		delete_bill = Button(sub_canva, text="Delete", bg="#FBC281", height=1, width=15,
		                     command=lambda: (self.clear_bill_services())).place(x=188, y=563)

		# events
		customer_data.bind("<<ComboboxSelected>>", lambda event: self.found_client())
		customer_name.bind("<<ComboboxSelected>>", lambda event: self.found_client())

	def update_bill_services(self):
		pass

	def update_client_list(self):
		pass

	def clear_bill_services(self):
		self.services.set("")
		self.quantity.set(0)
		pass

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
			print(["as", bill])
			file.write(bill)
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
			pdf_bill.cell(600, 3, "total:"+str(self.total.get()), 0, 1)
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
		tree.insert('', 'end', text=self.services.get(), values=(self.quantity.get(), "subtotal"))
		self.total.set(self.total.get()+ self.quantity.get() * 1)
		"""need to get the price of the services"""
		return

	def found_client(self, ):
		global clients_list, clients_names
		if self.client_id.get() in clients_list:
			indice = clients_list.index(self.client_id.get())
			self.client_email.set(clients_emails[indice])
			self.client_name.set(clients_names[indice])
		if self.client_name.get() in clients_names:
			indice = clients_names.index(self.client_name.get())
			self.client_email.set(clients_emails[indice])
			self.client_id.set(clients_list[indice])
		print([self.client_email.get(), self.client_name.get(), self.client_id.get()])


# quantity_entry.bind("<Return>", self.update_price_bill()) reserved event to input quantity


def create_scroll(canvas, object, orientation, x=0, y=0):
	if orientation == "vertical":
		orientation = "vertical"
	else:
		orientation = "horizontal"
	scroll = ttk.Scrollbar(canvas, orient=orientation, command=object.yview)
	scroll.place(x=x, y=y, height=object["height"] * 18.55)
	return scroll


def load_clients():
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
	print([list, list2, list3])


def number_bill():
	number = 0
	bills = os.listdir("invoices/")
	for number in bills:
		indice = number.find(".pdf")
		number = number[:indice]
		number = int(number)
	return number + 1


def load_users():
	for user in os.listdir("user_database"):
		print(user)
		image = face_recognition.load_image_file(r"user_database/" + user)
		face_encoding = face_recognition.face_encodings(
			image, num_jitters=1)[0]
		print(face_encoding)
		faces.append(face_encoding)
		users.append(user)
	print(faces)


def login_image():
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
		return False, -1


def top_level():
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
load_clients()
load_users()
login_image()
sucefull_login, user = login()
if sucefull_login:
	main_window = Menu(users[user])
os.remove("user_database/user_0.png")

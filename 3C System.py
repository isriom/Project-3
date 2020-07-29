from tkinter import *  # libraries imported :GUI
import face_recognition
import numpy as np
import cv2

cam = cv2.VideoCapture(0)

cv2.namedWindow("FaceCapture")

img_counter = 0

while True:
    ret, frame = cam.read()
    if not ret:
        print("failed to grab frame")
        break
    cv2.imshow("test", frame)

    k = cv2.waitKey(1)
    if k%256 == 27:  # ESC pressed
        
        print("Escape hit, closing...")
        break

    elif k%256 == 32: # SPACE pressed
        
        user_face = "user_0.png"
        cv2.imwrite(r"user_database/"+user_face, frame)
        print("User_0 written!")

cam.release()
cv2.destroyAllWindows()
#---------------------------------------------------------------------------------
#Copy paste this sentence to add more users to the data base
#User image must be in user_database folder to follow the format
image_of_brandon = face_recognition.load_image_file(r"user_database\Brandon Reyes.jpg")
brandon_face_encoding = face_recognition.face_encodings(image_of_brandon)[0]
#---------------------------------------------------------------------------------

#---------------------------------------------------------------------------------
image_of_lena = face_recognition.load_image_file(r"user_database\lena.jpg")
lena_face_encoding = face_recognition.face_encodings(image_of_lena)[0]
#---------------------------------------------------------------------------------

#---------------------------------------------------------------------------------
#Make an array to save the registered user database
registered_users_encodings = [
	brandon_face_encoding,
	lena_face_encoding
]
#--------------------------------------------------------------------------------

#---------------------------------------------------------------------------------
#Make an array to save the data of users//May use the same form to save the user information 
registered_users_names = [
	"Brandon",
	"Lena"
]
#---------------------------------------------------------------------------------



#---------------------------------------------------------------------------------
#This sentences will load and encode the image and face of the person trying to login
image_of_user = face_recognition.load_image_file(r"user_database\user_0.png")
user_face_encoding = face_recognition.face_encodings(image_of_user)[0]
#---------------------------------------------------------------------------------
#Compare the face encoding of the user with the ones of the database
results = face_recognition.compare_faces(
    [brandon_face_encoding], user_face_encoding)
#---------------------------------------------------------------------------------

#---------------------------------------------------------------------------------
#Print the results
if results[0]:
    print("Welcome!")
else:
    print("You are not in our database! Please create your profile or get in contact with support")
#---------------------------------------------------------------------------------



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

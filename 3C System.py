from tkinter import *  # libraries imported :GUI
import face_recognition
import numpy as np
import cv2
import os
from PIL import ImageTk,Image

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
        user_image = Image.open("user_database/"+self.user)
        user_image = user_image.resize((436, 435), Image.ANTIALIAS)
        user_photo = ImageTk.PhotoImage(user_image)
        self.menu_canva.create_image(350, 300, image=main_menu_image)
        self.menu_canva.create_image(238, 73, image=logo_3C)
        self.menu_canva.create_image(237, 382, image=user_photo)
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


def load_users():
    for user in os.listdir("user_database"):
        print(user)
        image = face_recognition.load_image_file(r"user_database/"+user)
        face_encoding = face_recognition.face_encodings(
            image, num_jitters=1)[0]
        print(face_encoding)
        faces.append(face_encoding)
        users.append(user)
    print(faces)


def login_image():
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
        if k % 256 == 27:  # ESC pressed

            print("Escape hit, closing...")
            break

        elif k % 256 == 32:  # SPACE pressed

            user_face = "user_0.png"
            cv2.imwrite("user_database/"+user_face, frame)
            print("User_0 written!")

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
    if True in face_recognition.compare_faces(faces, user_face_encoding, 0.459):
        print(face_recognition.compare_faces(faces, user_face_encoding, 0.459))

        results = True
    # ---------------------------------------------------------------------------------
    # Print the results
    if results:
        print("Welcome!")
        return True,face_recognition.compare_faces(faces, user_face_encoding, 0.459).index(True)
    else:
        print("You are not in our database! Please create your profile or get in contact with support")
        return False
    # ---------------------------------------------------------------------------------


def top_level():
    global main_window
    window = Toplevel()
    window.title("3C")
    sub_menu_canva = Canvas(window, width=700, height=600, bg="White")
    sub_menu_canva.pack()
    return window, sub_menu_canva


faces = []
users = []
load_users()
login_image()
sucefull_login,user=login()
if sucefull_login:
    main_window = Menu(users[user])
os.remove("user_database/user_0.png")

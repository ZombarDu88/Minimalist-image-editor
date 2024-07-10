#coding:utf-8
import os, tkinter, PIL, webbrowser
from tkinter import ttk, filedialog, messagebox
from PIL import Image

class popus:
    pass

    def messagebox_err(arg1, arg2):
        messagebox.showerror(arg1, arg2)

class change_widgets:
    pass

    def xy_entry_disable():

        if base_res_box.instate(["selected"]) == True:
            x_scale_input.state(["disabled"])
            y_scale_input.state(["disabled"])

        else:
            x_scale_input.state(["!disabled"])
            y_scale_input.state(["!disabled"])

    def rotate_entry_enable():

        if rotate_check_box.instate(["selected"]) == True:
            rotate_entry.state(["!disabled"])
            rotate_entry.state(["!disabled"])

        else:
            rotate_entry.state(["disabled"])
            rotate_entry.state(["disabled"])

class images_changer:
    pass

    def open_images():

        global file_selected
        file_selected = filedialog.askopenfilenames(parent=script ,title="Choose a file")

    def display_images_resolution(self, res_file="Resolution_info.txt"):

        nfiles: int = 1

        try:
            if os.path.isfile(res_file):

                if len(file_selected) > 0:

                    with open(res_file, "r+", encoding="utf-8") as resolution_images:

                        resolution_images.truncate()

                        for Images in file_selected:
                            with Image.open(Images) as selected_images:
                                resolution_images.write("({}) -> {} = {}x{}\n\n".format(nfiles, os.path.basename(Images), selected_images.width, selected_images.height))
                                nfiles += 1

                    with open(res_file, "r", encoding="utf-8") as resolution_images:
                        res_lignes = resolution_images.read()

                    messagebox.showinfo("Image(s) resolution", res_lignes)

                else:
                    popus.messagebox_err("Error !", "You have not selected a file(s) !")

            else:

                if len(file_selected) > 0:

                    with open(res_file, "w", encoding="utf-8") as resolution_images:


                        for Images in file_selected:
                            with Image.open(Images) as selected_images:
                                resolution_images.write("({}) -> {} = {}x{}\n\n".format(nfiles, os.path.basename(Images), selected_images.width, selected_images.height))
                                nfiles += 1

                    with open(res_file, "r", encoding="utf-8") as resolution_images:
                        res_lignes = resolution_images.read()

                    messagebox.showinfo("Image(s) resolution", res_lignes)

                else:
                    popus.messagebox_err("Error !", "You have not selected a file(s) !")

        except NameError:
            popus.messagebox_err("Error !", "You have not selected a file(s) !")

    def change_images():

        try:
            if len(file_selected) > 0:

                for images in file_selected:

                    with Image.open(images) as original_image:

                        if base_res_box.instate(["selected"]) and black_check_box.instate(["selected"]) and rotate_check_box.instate(["selected"]) == True:

                            if int(rotate_entry.get()) > 360:
                                webbrowser.open("https://previews.123rf.com/images/blankstock/blankstock1510/blankstock151001563/46331197-angle-45-360-degrés-cercle-icônes-géométrie-mathématiques-signe-symboles-pleine-rotation-complète.jpg")
                                messagebox.showwarning("Warning !", "360 is the max value for a rotate")

                            new_image = original_image.convert("L").rotate(int(rotate_entry.get()))
                            new_image.save("Output_images/{} {}° dark{}".format(os.path.splitext(os.path.basename(images))[0], rotate_entry.get(),
                                           os.path.splitext(os.path.basename(images))[1]))

                        elif base_res_box.instate(["selected"]) and black_check_box.instate(["selected"]) == True:
                            new_image = original_image.convert("L")
                            new_image.save("Output_images/{} dark{}".format(os.path.splitext(os.path.basename(images))[0],
                                       os.path.splitext(os.path.basename(images))[1]))

                        elif base_res_box.instate(["selected"]) and rotate_check_box.instate(["selected"]) == True:

                            if int(rotate_entry.get()) > 360:
                                webbrowser.open("https://previews.123rf.com/images/blankstock/blankstock1510/blankstock151001563/46331197-angle-45-360-degrés-cercle-icônes-géométrie-mathématiques-signe-symboles-pleine-rotation-complète.jpg")
                                messagebox.showwarning("Warning !", "360 is the max value for a rotate")

                            new_image = original_image.rotate(int(rotate_entry.get()))
                            new_image.save("Output_images/{} {}° base{}".format(os.path.splitext(os.path.basename(images))[0], rotate_entry.get(),
                                           os.path.splitext(os.path.basename(images))[1]))

                        elif rotate_check_box.instate(["selected"]) and black_check_box.instate(["selected"]) == True:

                            if int(rotate_entry.get()) > 360:
                                webbrowser.open("https://previews.123rf.com/images/blankstock/blankstock1510/blankstock151001563/46331197-angle-45-360-degrés-cercle-icônes-géométrie-mathématiques-signe-symboles-pleine-rotation-complète.jpg")
                                messagebox.showwarning("Warning !", "360 is the max value for a rotate")

                            new_image = original_image.rotate(int(rotate_entry.get())).resize((int(x_scale_input.get()),int(y_scale_input.get()))).convert("L")
                            new_image.save("Output_images/{} ({}x{}) {}° dark{}".format(os.path.splitext(os.path.basename(images))[0], x_scale_input.get(), 
                                           y_scale_input.get(), rotate_entry.get(),os.path.splitext(os.path.basename(images))[1]))

                        elif base_res_box.instate(["selected"]) == True:
                            original_image.save("Output_images/{} base{}".format(os.path.splitext(os.path.basename(images))[0],
                                                os.path.splitext(os.path.basename(images))[1]))

                        elif black_check_box.instate(["selected"]) == True:
                            new_image = original_image.convert("L").resize((int(x_scale_input.get()),int(y_scale_input.get())))
                            new_image.save("Output_images/{} ({}x{}) dark{}".format(os.path.splitext(os.path.basename(images))[0],
                                           x_scale_input.get(), y_scale_input.get(), os.path.splitext(os.path.basename(images))[1]))

                        elif rotate_check_box.instate(["selected"]) == True:

                            if int(rotate_entry.get()) > 360:
                                webbrowser.open("https://previews.123rf.com/images/blankstock/blankstock1510/blankstock151001563/46331197-angle-45-360-degrés-cercle-icônes-géométrie-mathématiques-signe-symboles-pleine-rotation-complète.jpg")
                                messagebox.showwarning("Warning !", "360 is the max value for a rotate")

                            new_image = original_image.rotate(int(rotate_entry.get())).resize((int(x_scale_input.get()),int(y_scale_input.get())))
                            new_image.save("Output_images/{} ({}x{}) {}°{}".format(os.path.splitext(os.path.basename(images))[0], x_scale_input.get(), 
                                           y_scale_input.get(), rotate_entry.get(),os.path.splitext(os.path.basename(images))[1]))

                        else:
                            new_image = original_image.resize((int(x_scale_input.get()),int(y_scale_input.get())))
                            new_image.save("Output_images/{} ({}x{}){}".format(os.path.splitext(os.path.basename(images))[0],
                                           x_scale_input.get(), y_scale_input.get(), os.path.splitext(os.path.basename(images))[1]))

                messagebox.showinfo("Sucess =D", "The {} file(s) have been saved in Ouput_image folder".format(len(file_selected)))

            else:
                messagebox.showerror("Error !", "You have not selected a file(s) !")

        except NameError:
            messagebox.showerror("Error !", "You have not selected a file(s) !")

        except ValueError:
            messagebox.showerror("Error !", "Please enter a valid numbers !")

        except PIL.UnidentifiedImageError:
            messagebox.showwarning("Warning !", "Program only support: PNG, JPEG, PPM, GIF, TIFF, and BMP format !")

        except FileNotFoundError:
            os.mkdir("Output_images")
            images_changer.change_images()

    def clear_images():

        try:
            nfiles = os.listdir("Output_images")

        except FileNotFoundError:
            os.mkdir("Output_images")
            images_changer.clear_images()

        if len(nfiles) > 0:
            for files in nfiles:
                os.remove(os.path.join("Output_images/", files))
            messagebox.showinfo("Sucess =D","The ({}) file(s) in Ouput_image have been deleted.".format(len(nfiles)))

        else:
            messagebox.showwarning("Warning !", "No file(s) !")

class program:
    pass

    def quitting_program():

        """Quitting main program"""

        quit_program = messagebox.askquestion("Quit...", "Are you sure ?")

        if quit_program == "yes":
            script.destroy()

script = tkinter.Tk()

#s = ttk.Style()
#s.configure("Big.TButton")

script.title("v1.0")
script.resizable(False, False)

label_welcome = ttk.Label(text="Images utility")
label_welcome.grid(row=0, column=1)

label_space = ttk.Label(text="")
label_space.grid(row=1, column=0)

open_button = ttk.Button(text="Open files", width=15, command=images_changer.open_images)
open_button.grid(row=2, column=1)

Display_res = ttk.Button(text="Display res", width=15, command=images_changer().display_images_resolution)
Display_res.grid(row=3, column=1)

label_space2 = ttk.Label(text="")
label_space2.grid(row=4, column=0)

base_res_box = ttk.Checkbutton(text="Initial resolution (x:y)", command=change_widgets.xy_entry_disable)
base_res_box.state(["!alternate", "selected"])
base_res_box.grid(row=5, column=0)

black_check_box = ttk.Checkbutton(text="Turn black")
black_check_box.state(["!alternate"])
black_check_box.grid(row=5, column=1)

rotate_check_box = ttk.Checkbutton(text="Rotate (°) :", command=change_widgets.rotate_entry_enable)
rotate_check_box.state(["!alternate"])
rotate_check_box.grid(row=5, column=2)

rotate_entry = ttk.Entry(width=5)
rotate_entry.insert(0, "X")
rotate_entry.state(["disabled"])
rotate_entry.grid(row=5, column=3)

label_space2 = ttk.Label(text="")
label_space2.grid(row=7, column=0)

label_x = ttk.Label(text="width x:")
label_x.grid(row=8, column=0)

x_scale_input = ttk.Entry(width=10)
x_scale_input.insert(0, "X")
x_scale_input.state(["disabled"])
x_scale_input.grid(row=8, column=1)

label_y = ttk.Label(text="height y:")
label_y.grid(row=9, column=0)

y_scale_input = ttk.Entry(width=10)
y_scale_input.insert(0, "Y")
y_scale_input.state(["disabled"])
y_scale_input.grid(row=9, column=1)

label_space3 = ttk.Label(text="")
label_space3.grid(row=10, column=0)

resize_button = ttk.Button(text="Save", width=15, command=images_changer.change_images)
resize_button.grid(row=11, column=1)

del_button = ttk.Button(text="Delete files", width=15, command=images_changer.clear_images)
del_button.grid(row=12, column=1)

script.protocol("WM_DELETE_WINDOW", program.quitting_program)
script.mainloop()
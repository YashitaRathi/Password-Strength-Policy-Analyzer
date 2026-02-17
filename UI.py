# from tkinter import *
# from tkinter import messagebox
# from password_checker import checkPassword

# root = Tk()
# root.title("Password Strength Checker")
# root.geometry("800x600")
# root.configure(bg="#f0f0f0")

# first_page = Frame(root, bg="#f0f0f0")
# first_page.pack(fill="both", expand=True, pady=40)
# second_page = Frame(root, bg="#f0f0f0")
# second_page.pack_forget()


# def create_popup(title, message):
#     popup = Toplevel()
#     popup.title(title)

#     popup.geometry("600x200")
#     label = Label(popup, text=message, wraplength=400,
#                   justify="center", font=("Helvetica", 16))
#     label.pack(pady=20)
#     button = Button(popup, text="Understand", command=popup.destroy,
#                     font=("Helvetica", 14), bg="#4CAF50", fg="white", width=20, height=2)
#     button.pack(pady=10)


# def check_password():
#     password = e1.get()
#     result = checkPassword(password)
#     message = f"Password Strength: {result} \nReason: \nExplanation: "
#     create_popup("Password Strength Result", message)
#     print("Password entered:", password)


# def switch_to_second_page():
#     first_page.pack_forget()
#     second_page.pack(fill="both", expand=True)


# def switch_to_first_page():
#     second_page.pack_forget()
#     first_page.pack(fill="both", expand=True)


# def check_org_password():
#     org_password = e2.get()
#     print("Password entered:", org_password)


# r = Label(first_page, text="Welcome to Password Strength Checker",
#           font=("Helvetica", 24))
# r.pack(pady=10)

# r2 = Label(first_page, text="You can check the strength of your password here.\n And analyze your password policies. \n And get suggestions to improve them.",
#            font=("Helvetica", 18), wraplength=600, justify="center")
# r2.pack(pady=10)

# li = Label(first_page, text="Please enter your password below:",
#            font=("Helvetica", 18))
# li.pack(pady=5)

# e1 = Entry(first_page, width=30, font=("Helvetica", 18))
# e1.pack(pady=5)

# button = Button(first_page, text="Check Strength", font=(
#     "Helvetica", 14), bg="#4CAF50", fg="white", width=15, height=2, command=check_password)
# button.pack(pady=20)

# button1 = Button(first_page, text="Check Password Policies", font=(
#     "Helvetica", 14), bg="#4C59AF", fg="white", width=25, height=2, command=switch_to_second_page)
# button1.pack(pady=20)


# r3 = Label(second_page, text="Welcome to Password Strength Checker",
#            font=("Helvetica", 16))
# r3.pack(pady=10)

# r4 = Label(second_page, text="You can check the strength of your password here. And analyze your password policies. And get suggestions to improve them.",
#            font=("Helvetica", 12))
# r4.pack(pady=10)

# li0 = Label(second_page, text="Please enter your password below:",
#             font=("Helvetica", 12))
# li0.pack(pady=5)

# e2 = Entry(second_page, width=30)
# e2.pack(pady=5)

# button2 = Button(second_page, text="Check Strength", font=(
#     "Helvetica", 12), bg="#4CAF50", fg="white", width=15, height=2, command=check_password)
# button2.pack(pady=20)

# button3 = Button(second_page, text="Check Password Policies", font=(
#     "Helvetica", 12), bg="#4C59AF", fg="white", width=15, height=2, )
# button3.pack(pady=20)

# button4 = Button(second_page, text="Back", font=(
#     "Helvetica", 12), bg="#4CAF50", fg="white", width=15, height=2, command=switch_to_first_page)
# button4.pack(pady=20)

# root.mainloop()


# # button - “Password Strength Checker” and“Policy Analyzer”
# # Calls functions from password_checker.py & policy_analyzer.py

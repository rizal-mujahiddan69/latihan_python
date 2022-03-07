import tkinter as tk
perkenalan = \
"""Aplikasi ini dibuat untuk memudahkan dari pdf ke docs maupun sebaliknya
"""

class menu_dasar:
    def __init__(self):
        window= tk.Tk(className="Konversiku")
        window.minsize(500,100)
        # window.configure(bg='#000000')

        app_width = 500
        app_height = 100

        screen_width = window.winfo_screenwidth()
        screen_height = window.winfo_screenheight()

        x = int((screen_width / 2) - (app_width / 2))
        y = int((screen_height / 2) - (app_height / 2))

        window.geometry("+{}+{}".format(x,y))

        judul = tk.Label(window,text="Konversi pdf2docs and docx2pdf",font=("papyrus",20),fg="black")
        greeting = tk.Label(window,text=perkenalan,fg="black")
        pdf_ke_docx = tk.Button(window,text="pdf ke docx",width=10,height=2,fg="white",bg="#0d63fd",command=self.create_window)
        docx_ke_pdf = tk.Button(window,text="docx ke pdf",width=10,height=2,fg="white",bg="#0d63fd",command=self.create_window)

        judul.pack(side="top")
        greeting.pack(side="top")
        pdf_ke_docx.pack(side="right",padx=100,pady=10,expand=True)
        docx_ke_pdf.pack(side="left",padx=100,pady=10,expand=True)
        window.mainloop()
    def create_window(self):
        new_window = tk.Tk()
        self.window.destroy()

main_menu = menu_dasar()
print(dir(main_menu))
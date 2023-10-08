import tkinter
import tkinter as tk
import smtplib

class MailApp:
    def __init__(self, master):
        self.master = master
        master.title("Mail Application")
        tkinter.Tk.config(master, background="#fcf3ca")
        self.from_label = tk.Label(master, text="From (Gmail) : ", background="#fcf3ca")
        self.from_label.grid(row=0, column=0, sticky="w", padx=5)
        self.from_entry = tk.Entry(master, width=35)
        self.from_entry.grid(row=0, column=1, sticky="w", pady=10)
        self.pass_label = tk.Label(master, text="App Password (16 Characters) : ", background="#fcf3ca")
        self.pass_label.grid(row=1, column=0, sticky="w", padx=5)
        self.pass_entry = tk.Entry(master, width=35, show="●")
        self.pass_entry.grid(row=1, column=1, sticky="w", pady=10)
        self.to_label = tk.Label(master, text="To : ", background="#fcf3ca")
        self.to_label.grid(row=2, column=0, sticky="w", padx=5)
        self.to_entry = tk.Entry(master, width=35)
        self.to_entry.grid(row=2, column=1, sticky="w", pady=10)
        self.subject_label = tk.Label(master, text="Subject : ", background="#fcf3ca")
        self.subject_label.grid(row=3, column=0, sticky="w", padx=5)
        self.subject_entry = tk.Entry(master, width=35)
        self.subject_entry.grid(row=3, column=1, sticky="w", pady=10)
        self.body_label = tk.Label(master, text="Body : ", background="#fcf3ca")
        self.body_label.grid(row=4, column=0, sticky="w", padx=5)
        self.body_text = tk.Text(master, height=5, width=28)
        self.body_text.grid(row=4, column=1, sticky="w", pady=20)
        self.send_button = tk.Button(master, text="Send", command=self.send_mail, width=16, background="#fc036b", foreground="White", font=8)
        self.send_button.grid(row=5, column=0, columnspan=3, sticky="w", padx=200)

    def send_mail(self):
        from_address = self.from_entry.get()
        app_password = self.pass_entry.get()
        to_address = self.to_entry.get()
        subject = self.subject_entry.get()
        body = self.body_text.get("1.0", tk.END)
        smtp_server = "smtp.gmail.com"
        smtp_port = 587
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(from_address, app_password)
        message = f"Subject: {subject}\n\n{body}"
        server.sendmail(from_address, to_address, message)
        server.quit()
        self.master.destroy()

root = tk.Tk()
mail_app = MailApp(root)
root.geometry("550x350")
root.mainloop()

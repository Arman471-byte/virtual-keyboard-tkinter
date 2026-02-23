# Virtual Keyboard

import os
from tkinter import * # type: ignore
from tkinter import filedialog

class VirtualKeyboard:

    def __init__(self, root):
        self.root = root
        self.root.title("Virtual Keyboard")
        self.root.geometry("1200x600")
        self.root.config(bg="black")

        # Safe icon loading (optional)
        try:
            icon_path = os.path.join(os.getcwd(), "LOGO.png")
            icon = PhotoImage(file=icon_path)
            self.root.iconphoto(True, icon)
        except:
            pass

        # Keyboard layouts
        self.upper_keys = [
            list("QWERTYUIOP"),
            list("ASDFGHJKL"),
            list("ZXCVBNM")
        ]

        self.lower_keys = [
            list("qwertyuiop"),
            list("asdfghjkl"),
            list("zxcvbnm")
        ]

        self.text = ""
        self.display_var = StringVar()
        self.caps_on = False
        self.shift_on = False

        # Display label
        self.label = Label(
            root,
            textvariable=self.display_var,
            bg="grey",
            fg="white",
            font=("Arial", 24),
            width=40,
            height=2
        )
        self.label.pack(pady=10)

        # Keyboard frame
        self.keyboard_frame = Frame(root, bg="black")
        self.keyboard_frame.pack()

        self.build_keyboard()

    # ------------------------
    # Keyboard Logic
    # ------------------------

    def build_keyboard(self):
        # Clear previous buttons
        for widget in self.keyboard_frame.winfo_children():
            widget.destroy()

        layout = self.lower_keys

        for row in layout:
            row_frame = Frame(self.keyboard_frame, bg="black")
            row_frame.pack()

            for key in row:
                Button(
                    row_frame,
                    text=key,
                    width=5,
                    height=2,
                    font=("Arial", 14),
                    command=lambda k=key: self.insert_text(k)
                ).pack(side="left", padx=3, pady=3)

        # Bottom controls
        control_frame = Frame(self.root, bg="black")
        control_frame.pack(pady=10)

        Button(control_frame, text="CapsLock", width=10, height=2,
               font=("Arial", 14), command=self.toggle_caps).pack(side="left", padx=5)

        Button(control_frame, text="Backspace", width=10, height=2,
               font=("Arial", 14), command=self.backspace).pack(side="left", padx=5)

        Button(control_frame, text="Clear", width=10, height=2,
               font=("Arial", 14), command=self.clear).pack(side="left", padx=5)

        Button(control_frame, text="Save", width=10, height=2,
               font=("Arial", 14), command=self.save_file).pack(side="left", padx=5)

        Button(self.root, text="Space", width=60, height=2,
               font=("Arial", 14),
               command=lambda: self.insert_text(" ")
               ).pack(pady=5)
        
        Button(control_frame, text="Shift", width=10, height=2,
               font=("Arial", 14), command=self.toggle_shift).pack(side="left", padx=5)


    def caps_build(self):
        for widget in self.keyboard_frame.winfo_children():
            widget.destroy()

        if self.caps_on or self.shift_on:
            layout = self.upper_keys
        else:
            layout = self.lower_keys

        for row in layout:
            row_frame = Frame(self.keyboard_frame, bg="black")
            row_frame.pack()

            for key in row:
                Button(
                    row_frame,
                    text=key,
                    width=5,
                    height=2,
                    font=("Arial", 14),
                    command=lambda k=key: self.insert_text(k)
                ).pack(side="left", padx=3, pady=3)

    # ------------------------
    # Functional Methods
    # ------------------------

    def insert_text(self, char):
        self.text += char
        self.display_var.set(self.text)
        # If shift was active, turn it off after one key
        if self.shift_on:
            self.shift_on = False
            self.caps_build()

    def backspace(self):
        self.text = self.text[:-1]
        self.display_var.set(self.text)

    def clear(self):
        self.text = ""
        self.display_var.set(self.text)

    def toggle_caps(self):
        self.caps_on = not self.caps_on
        self.caps_build()

    def toggle_shift(self):
        if not self.caps_on:
            self.shift_on = True
            self.caps_build()

    def save_file(self):
        file = filedialog.asksaveasfile(
            defaultextension=".txt",
            filetypes=[
                ("Text file", "*.txt"),
                ("Python file", "*.py"),
                ("HTML file", "*.html"),
                ("All files", "*.*")
            ]
        )

        if file:
            file.write(self.text)
            file.close()


# ------------------------
# Run App
# ------------------------

root = Tk()
app = VirtualKeyboard(root)
root.mainloop()

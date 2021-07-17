import tkinter as tk
from functools import partial

import qrcode


def password_input(root):
    password_label = tk.Label(root, text="Password").grid(row=1, column=0)
    password = tk.StringVar()
    password_entry = tk.Entry(root, textvariable=password, show="*").grid(
        row=1, column=1
    )

    return password


def ssid_input(root):
    ssid_label = tk.Label(root, text="Network Name").grid(row=0, column=0)
    ssid = tk.StringVar()
    ssid_entry = tk.Entry(root, textvariable=ssid).grid(row=0, column=1)
    return ssid


def make_qrcode(ssid, password):
    ssid = ssid.get()
    password = password.get()
    qr_str = f"WIFI:S:{ssid};T:WPA;P:{password};;"
    img = qrcode.make(qr_str)
    img.save(f"{ssid}_QR.png")


def main():
    # Create Tkinter GUI
    root = tk.Tk()
    root.geometry("250x100")
    root.title("Wifi QR Code")

    # SSID input creation
    ssid = ssid_input(root)
    # Password input creation
    password = password_input(root)

    # Generate button
    generate = partial(make_qrcode, ssid, password)
    create = tk.Button(root, text="Generate", command=generate).grid(row=4, column=0)
    # Run Tkinter loop
    root.mainloop()


if __name__ == "__main__":
    main()

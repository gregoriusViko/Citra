from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"D:\KULIAH SANATA DHARMA\SEMESTER 5\PEMROSESAN CITRA\UAS\Citra\assets")
from tkinter import filedialog
import tkinter as tk
from PIL import Image, ImageTk
window = Tk()

window.geometry("950x750")
window.configure(bg = "#FFFFFF")


def LOGIN():
    def relative_to_assets(path: str) -> Path: return ASSETS_PATH / Path("frame0")/Path(path)
    
    canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 750,
    width = 950,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
    )

    canvas.place(x = 0, y = 0)
    canvas.create_rectangle(
        475.0,
        0.0,
        950.0,
        750.0,
        fill="#3B79D8",
        outline="")

    canvas.create_text(
        495.0,
        99.0,
        anchor="nw",
        text="Pemrosesan Citra",
        fill="#FFF6E9",
        font=("Inter Bold", 50 * -1)
    )

    canvas.create_text(
        495.0,
        240.0,
        anchor="nw",
        text="Deteksi dan\nKlasifikasi Penyakit\npada Daun Padi\nMenggunakan CNN",
        fill="#FFF6E9",
        font=("Inter Bold", 40 * -1),
        justify="center"
    )

    button_image_1 = PhotoImage(
        file=relative_to_assets("button_1.png"))
    button_1 = Button(
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=Page2,
        relief="flat"
        
    )
    button_1.place(
        x=630.0,
        y=550.0,
        width=166.0,
        height=56.0
    )

    image_image_1 = PhotoImage(
        file=relative_to_assets("image_1.png"))
    image_1 = canvas.create_image(
        227.0,
        375.0,
        image=image_image_1
    )
    window.resizable(False, False)
    window.mainloop()
    
def Page2():
    global img_tk
    def relative_to_assets(path: str) -> Path: return ASSETS_PATH / Path("frame1")/Path(path)
    
    def uploadImage():
        file_path = filedialog.askopenfilename(
        title="Pilih File JPG",  # Judul dialog
        filetypes=[("Image Files", "*.jpg")]  # Filter hanya file .jpg
        )

        # Menampilkan path file yang dipilih
        if file_path:
            print("File yang dipilih:", file_path)
            img = Image.open(file_path)
            img_tk = ImageTk.PhotoImage(img)
            canvasAsli.create_image(300,300,image=img_tk)
            canvasAsli.img_tk = img_tk
        else:
            print("Tidak ada file yang dipilih.")
    
    canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 750,
    width = 950,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
    )

    canvas.place(x = 0, y = 0)
    canvas.create_rectangle(
        0.0,
        0.0,
        950.0,
        750.0,
        fill="#3B79D8",
        outline="")

    canvas.create_rectangle(
        65.0,
        86.0,
        215.0,
        236.0,
        fill="#F1F5FF",
        outline="")

    canvas.create_rectangle(
        65.0,
        312.0,
        215.0,
        462.0,
        fill="#F1F5FF",
        outline="")

    canvas.create_rectangle(
        259.0,
        312.0,
        409.0,
        462.0,
        fill="#F1F5FF",
        outline="")

    canvas.create_rectangle(
        453.0,
        312.0,
        603.0,
        462.0,
        fill="#F1F5FF",
        outline="")

    canvas.create_rectangle(
        65.0,
        543.0,
        215.0,
        693.0,
        fill="#F1F5FF",
        outline="")

    canvas.create_rectangle(
        259.0,
        543.0,
        409.0,
        693.0,
        fill="#F1F5FF",
        outline="")

    canvas.create_rectangle(
        453.0,
        543.0,
        603.0,
        693.0,
        fill="#F1F5FF",
        outline="")

    canvas.create_text(
        69.0,
        57.0,
        anchor="nw",
        text="CITRA ASLI",
        fill="#FFFFFF",
        font=("Inter Bold", 24 * -1)
    )

    canvas.create_text(
        69.0,
        293.0,
        anchor="nw",
        text="Image Clipping",
        fill="#FFFFFF",
        font=("Inter Bold", 16 * -1)
    )

    canvas.create_text(
        282.0,
        293.0,
        anchor="nw",
        text="Grayscale",
        fill="#FFFFFF",
        font=("Inter Bold", 16 * -1)
    )

    canvas.create_text(
        447.0,
        293.0,
        anchor="nw",
        text="Image Smoothing",
        fill="#FFFFFF",
        font=("Inter Bold", 16 * -1)
    )

    canvas.create_text(
        262.0,
        524.0,
        anchor="nw",
        text="Edge Detection",
        fill="#FFFFFF",
        font=("Inter Bold", 16 * -1)
    )

    canvas.create_text(
        31.0,
        524.0,
        anchor="nw",
        text="Threshold segmentation",
        fill="#FFFFFF",
        font=("Inter Bold", 16 * -1)
    )

    canvas.create_text(
        437.0,
        524.0,
        anchor="nw",
        text="Hasil Preprocessing ",
        fill="#FFFFFF",
        font=("Inter Bold", 16 * -1)
    )

    canvas.create_rectangle(
        646.0,
        0.0,
        666.0,
        750.0,
        fill="#D9D9D9",
        outline="")
    # BUTTON UPLOAD
    button_image_1 = PhotoImage(
        file=relative_to_assets("button_1.png"))
    button_1 = Button(
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        # command=lambda: print("button_1 clicked"),
        command=uploadImage,
        relief="flat"
    )
    button_1.place(
        x=256.0,
        y=149.0,
        width=129.0,
        height=39.0
    )
    # BUTTON PROCESS
    button_image_2 = PhotoImage(
        file=relative_to_assets("button_2.png"))
    button_2 = Button(
        image=button_image_2,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("button_2 clicked"),
        relief="flat"
    )
    button_2.place(
        x=256.0,
        y=197.0,
        width=129.0,
        height=39.0
    )
    # BUTTON KELUAR
    button_image_3 = PhotoImage(
        file=relative_to_assets("button_3.png"))
    button_3 = Button(
        image=button_image_3,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("button_3 clicked"),
        relief="flat"
    )
    button_3.place(
        x=743.0,
        y=472.0,
        width=129.0,
        height=39.0
    )

    canvas.create_text(
        684.0,
        57.0,
        anchor="nw",
        text="Hasil Klasifikasi\ndengan CNN",
        fill="#FFFFFF",
        justify="center",
        font=("Inter Bold", 32 * -1)
    )

    canvas.create_rectangle(
        711.0,
        178.0,
        905.0,
        407.0,
        fill="#FFFFFF",
        outline="")
    window.resizable(False, False)
    window.mainloop()
    
LOGIN()
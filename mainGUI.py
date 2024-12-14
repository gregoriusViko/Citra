from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = Path(__file__).parent/'assets'
from tkinter import filedialog, Label, Toplevel
import tkinter as tk
from PIL import Image, ImageTk
window = Tk()

window.geometry("950x750")
window.configure(bg = "#FFFFFF")
window.title("Preprocessing dan klasifikasi Citra dengan CNN")
window.resizable(False, False)


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
            global img_original
            print("File yang dipilih:", file_path)
            img_original = Image.open(file_path)
            img_resized = img_original.resize((400,400), Image.LANCZOS)
            photoAsli = ImageTk.PhotoImage(img_resized)
            
            gbrAsli_label.config(image=photoAsli)
            gbrAsli_label.image= photoAsli
            gbrAsli_label.bind("<Button-1>", lambda e: show_original_image())

        else:
            print("Tidak ada file yang dipilih.")
    
    def show_original_image():
        # Membuat jendela baru untuk menampilkan gambar asli
        top = Toplevel()
        top.title("Citra Ukuran Asli")
        global img_original
        photoAsli = ImageTk.PhotoImage(img_original)
        
        # Menampilkan gambar asli di jendela baru
        img_label = tk.Label(top, image=photoAsli)
        img_label.image = photoAsli  # Referensi agar gambar tidak terhapus oleh garbage collector
        img_label.pack()
    
    # function tombol proses
    def Process():
        
        ## kotak grayscale
        # photoGray = ImageTk.PhotoImage(img_grayscale)
        # grey_label.config(image=photograyscale)
        grey_label.config(text="image=photograyscale")
        # grey_label.image= photoGray
        grey_label.bind("<Button-2>", lambda e: show_grayscale_image())
        
        ## kotak smoothing
        # photoSmooth = ImageTk.PhotoImage(img_smoothing)
        # smoothing_label.config(image=photoSmooth)
        smoothing_label.config(text="image=photoSmooth")
        # smoothing_label.image= photoSmooth
        smoothing_label.bind("<Button-3>", lambda e: show_smotthing_image())
        
        ## kotak threshold
        # photoThreshold = ImageTk.PhotoImage(photoThreshold)
        # threshold_label.config(image=photoThreshold)
        threshold_label.config(text="image=photoThreshold")
        # threshold_label.image= photoThreshold
        threshold_label.bind("<Button-4>", lambda e: show_threshold_image())
        
        ## kotak edgeDetect
        # photoEdge = ImageTk.PhotoImage(photoEdge)
        # edgeDetec_label.config(image=photoThreshold)
        edgeDetec_label.config(text="image=photoEdge")
        # edgeDetec_label.image= photoEdge
        edgeDetec_label.bind("<Button-5>", lambda e: show_EdgeDetec_image())
        
         ## kotak hasil preprocessing
        # photoFinal = ImageTk.PhotoImage(photoFinal)
        # edgeDetec_label.config(image=photoFinal)
        hasilPreproc_label.config(text="image=photoHasil")
        # edgeDetec_label.image= photoFinal
        hasilPreproc_label.bind("<Button-6>", lambda e: show_Hasil_image())
    
    
    def show_grayscale_image():
        # Membuat jendela baru untuk menampilkan gambar asli
        top = Toplevel()
        top.title("Hasil Image Grayscale")
        global photograyscale
        photoGrayscale = ImageTk.PhotoImage(photograyscale)
        
        # Menampilkan gambar asli di jendela baru
        img_label = tk.Label(top, image=photoGrayscale)
        img_label.image = photoGrayscale  # Referensi agar gambar tidak terhapus oleh garbage collector
        img_label.pack()
        
    def show_smotthing_image():
        # Membuat jendela baru untuk menampilkan gambar asli
        top = Toplevel()
        top.title("Hasil Image Smoothing")
        global photosmoothing
        photoSmoothing = ImageTk.PhotoImage(photosmoothing)
        
        # Menampilkan gambar asli di jendela baru
        img_label = tk.Label(top, image=photoSmoothing)
        img_label.image = photoSmoothing  # Referensi agar gambar tidak terhapus oleh garbage collector
        img_label.pack()
    
    def show_threshold_image():
        # Membuat jendela baru untuk menampilkan gambar asli
        top = Toplevel()
        top.title("Hasil Threshold Segmentation")
        global Threshold
        photoThreshold = ImageTk.PhotoImage(Threshold)
        
        # Menampilkan gambar asli di jendela baru
        img_label = tk.Label(top, image=photoThreshold)
        img_label.image = photoThreshold  # Referensi agar gambar tidak terhapus oleh garbage collector
        img_label.pack()
        
    def show_EdgeDetec_image():
        # Membuat jendela baru untuk menampilkan gambar asli
        top = Toplevel()
        top.title("Hasil Edge Detection")
        global edgedetection
        photoEdge = ImageTk.PhotoImage(edgedetection)
        
        # Menampilkan gambar asli di jendela baru
        img_label = tk.Label(top, image=photoEdge)
        img_label.image = photoEdge  # Referensi agar gambar tidak terhapus oleh garbage collector
        img_label.pack()
    
    def show_Hasil_image():
        # Membuat jendela baru untuk menampilkan gambar asli
        top = Toplevel()
        top.title("Hasil Preprocessing")
        global hasilPreproc
        photoFinal = ImageTk.PhotoImage(hasilPreproc)
        
        # Menampilkan gambar asli di jendela baru
        img_label = tk.Label(top, image=photoFinal)
        img_label.image = photoFinal  # Referensi agar gambar tidak terhapus oleh garbage collector
        img_label.pack()
        
    def klasifikasi():
        
        pass

    canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 750,
    width = 950,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
    )
    # BACKGROUND WINDOW
    canvas.place(x = 0, y = 0)
    canvas.create_rectangle(
        0.0,
        0.0,
        950.0,
        750.0,
        fill="#3B79D8",
        outline="")

    # citra asli
    canvas.create_text(
        69.0,
        57.0,
        anchor="nw",
        text="CITRA ASLI",
        fill="#FFFFFF",
        font=("Inter Bold", 24 * -1)
    )
    
    gbrAsli_label = Label(window, text="Klik untuk melihat \n gambar ukuran asli")
    gbrAsli_label.pack(pady=10)
    gbrAsli_label.place(x=65, y=86, width=150, height=150)
    
    
    # Image greyscale
    canvas.create_text(
        180.0,
        293.0,
        anchor="nw",
        text="Grayscale",
        fill="#FFFFFF",
        font=("Inter Bold", 16 * -1)
    )

    grey_label = Label(window, text="Klik untuk melihat \n hasil greyscale")
    grey_label.pack(pady=10)
    grey_label.place(x=146, y=312, width=150, height=150)
    
    
    # Image smoothing
    canvas.create_text(
        355.0,
        293.0,
        anchor="nw",
        text="Image Smoothing",
        fill="#FFFFFF",
        font=("Inter Bold", 16 * -1)
    )
    
    smoothing_label = Label(window, text="Klik untuk melihat \n hasil smoothing")
    smoothing_label.pack(pady=10)
    smoothing_label.place(x=340, y=312, width=150, height=150)
    
    # Threshold Segmentation
    canvas.create_text(
        50.0,
        524.0,
        anchor="nw",
        text="Threshold segmentation",
        fill="#FFFFFF",
        font=("Inter Bold", 16 * -1)
    )
   
    threshold_label = Label(window, text="Klik untuk melihat \n hasil threshold segmentatiton")
    threshold_label.pack(pady=10)
    threshold_label.place(x=65, y=543, width=150, height=150)
    
    
    # Edge Detection
    canvas.create_text(
        278.0,
        524.0,
        anchor="nw",
        text="Edge Detection",
        fill="#FFFFFF",
        font=("Inter Bold", 16 * -1)
    )
    
    edgeDetec_label = Label(window, text="Klik untuk melihat \n hasil edge detection")
    edgeDetec_label.pack(pady=10)
    edgeDetec_label.place(x=259, y=543, width=150, height=150)
    
    # Hasil preprocessing
    canvas.create_text(
        460.0,
        524.0,
        anchor="nw",
        text="Hasil Preprocessing ",
        fill="#FFFFFF",
        font=("Inter Bold", 16 * -1)
    )

    hasilPreproc_label = Label(window, text="Klik untuk melihat \n hasil citra preprocessing")
    hasilPreproc_label.pack(pady=10)
    hasilPreproc_label.place(x=453, y=543, width=150, height=150)
    

    canvas.create_text(
        69.0,
        709.0,
        anchor="nw",
        text="Keterangan: Tekan gambar pada kotak untuk melihat citra tersebut",
        fill="#FFFFFF",
        justify="center",
        font=("Inter Bold", 14 * -1)
    )
    
    
    # Pembatas
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
        command=Process,
        relief="flat"
    )
    button_2.place(
        x=256.0,
        y=197.0,
        width=129.0,
        height=39.0
    )
    
     # BUTTON KELUAR
    button_image_4 = PhotoImage(
        file=relative_to_assets("button_4.png"))
    button_4 = Button(
        image=button_image_4,
        borderwidth=0,
        highlightthickness=0,
        command=klasifikasi,
        relief="flat"
    )
    button_4.place(
        x=739.0,
        y=166.0,
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
        command=LOGIN,
        relief="flat"
    )
    button_3.place(
        x=743.0,
        y=654.0,
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
    # Teks
    canvas.create_rectangle(
        711.0,
        260.0,
        905.0,
        407.0,
        fill="#FFFFFF",
        outline="")
    window.resizable(False, False)
    window.mainloop()
    
LOGIN()
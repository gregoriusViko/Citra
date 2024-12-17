from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = Path(__file__).parent/'assets'
from tkinter import filedialog, Label, Toplevel
import tkinter as tk
import cv2
import numpy as np
from PIL import Image, ImageTk
window = Tk()
import tensorflow as tf
from tensorflow.keras.layers import Layer

window.geometry("1100x750")
window.configure(bg = "#FFFFFF")
window.title("Preprocessing dan klasifikasi Citra dengan CNN")
window.resizable(False, False)
hasil_image =None

predicted_class="processing"
probability=0.0
photoAsli = None

@tf.keras.utils.register_keras_serializable()
class FixedDropout(Layer):
    def __init__(self, rate=0.0, noise_shape=None, seed=None, **kwargs):
        super(FixedDropout, self).__init__(**kwargs)
        self.rate = rate
        self.noise_shape = noise_shape
        self.seed = seed

    def call(self, inputs, training=False):
        if not training or self.rate == 0:
            return inputs               
        return tf.nn.dropout(inputs, rate=self.rate, noise_shape=self.noise_shape, seed=self.seed)

    def get_config(self):
        config = super().get_config()
        config.update({
        'rate': self.rate,
        'noise_shape': self.noise_shape,
        'seed': self.seed
            })
        return config

@tf.keras.utils.register_keras_serializable()
def custom_swish(x):
    return tf.keras.activations.swish(x)

model = tf.keras.models.load_model('rice_model.keras', 
            custom_objects={
                'swish': custom_swish,
                'FixedDropout': FixedDropout
            })

def LOGIN():
    def relative_to_assets(path: str) -> Path: return ASSETS_PATH / Path("frame0")/Path(path)
    
    canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 750,
    width = 1100,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
    )

    canvas.place(x = 0, y = 0)
    canvas.create_rectangle(
        475.0,
        0.0,
        1100.0,
        750.0,
        fill="#3B79D8",
        outline="")

    canvas.create_text(
        600.0,
        99.0,
        anchor="nw",
        text="Pemrosesan Citra",
        fill="#FFF6E9",
        font=("Inter Bold", 50 * -1)
    )

    

    canvas.create_text(
        600.0,  
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
        x=720.0,
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
    
image_rgb = None
img_grayscale = None
hasil_grayscale = None
file_gbr = None
img_smoothing = None
Threshold = None
hasil_threshold = None
img_detection2 = None
img_detection = None
resized_image = None
photoAsli = None

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
            global imagenya, file_gbr, image_rgb,photoAsli
            print("File yang dipilih:", file_path)
            file_gbr = file_path.replace("/", "/")
            # img_original = Image.open(file_path).convert("RGB")
            imagenya = cv2.imread(file_gbr)
            image_rgb = cv2.cvtColor(imagenya, cv2.COLOR_BGR2RGB)
            resized_image = cv2.resize(image_rgb, (256, 256), interpolation=cv2.INTER_LINEAR)

            asli_image = Image.fromarray(resized_image)
            photoAsli = ImageTk.PhotoImage(asli_image)
            
            gbrAsli_label.config(image=photoAsli)
            gbrAsli_label.image= photoAsli
            gbrAsli_label.bind("<Button-1>", lambda e: show_original_image())

        else:
            print("Tidak ada file yang dipilih.")
    
    def show_original_image():
        # Membuat jendela baru untuk menampilkan gambar asli
        global photoAsli
        top = Toplevel()
        top.title("Citra Ukuran Asli")
        resized_image = cv2.resize(image_rgb, (256, 256), interpolation=cv2.INTER_LINEAR)
        asli_image = Image.fromarray(resized_image)
        photoAsli = ImageTk.PhotoImage(asli_image)
        
        # Menampilkan gambar asli di jendela baru
        img_label = tk.Label(top, image=photoAsli)
        img_label.image = photoAsli  # Referensi agar gambar tidak terhapus oleh garbage collector
        img_label.pack()

    
    
    def greyscale(image_rgb):
        gray = []
        for y in image_rgb:
            baris = []
            for x in y:
                                # R*0 + G*1 + B*0
                baris.append(int(x[0]*0 + x[1]*1 + x[2]*0))
            gray.append(baris)

        gray = np.array(gray).astype(np.uint8)
        return gray
        
        
    def threshold(img_smoothing):
        # data = []
        # temp = 5
        # while len(data) < 10:
        #     data = [p for p in img_smoothing[:, 0].flatten() if p <= temp]
        #     temp += 5

        # # Langkah 2: Perhitungan mean adaptif
        # mean_now = sum(data) / len(data)
        # mean_temp = 0

        # while mean_now != mean_temp:
        #     t1 = [p for p in data if p < mean_now]
        #     t2 = [p for p in data if p >= mean_now]
            
        #     if len(t1) == 0 or len(t2) == 0:
        #         mean_now += 1
        #         break

        #     mean_temp = mean_now
        #     mean_now = int((sum(t1) / len(t1) + sum(t2) / len(t2)) / 2)

        # Langkah 3: Thresholding untuk menghasilkan gambar biner
        gambar_baru = []
        for y in img_smoothing:
                baris = []
                for x in y:
                    if x > 111:
                        baris.append(255)
                    else:
                        baris.append(0)
                gambar_baru.append(baris)

        # Konversi ke array numpy dengan tipe uint8
        gambar_baru = np.array(gambar_baru, dtype=np.uint8)

        return gambar_baru
    
    # function tombol proses
    def Process():
        
        ## kotak grayscale
        global hasil_image, img_grayscale, hasil_grayscale, img_smoothing, Threshold ,hasil_threshold, img_detection2, img_detection, resized_image
        print(file_gbr)
        if file_gbr is None:
            print("Gambar asli belum dimuat!")
            return

        try:
            # Konversi gambar ke grayscale
            imagenya = cv2.imread(file_gbr)
            if imagenya is None:
                print("Gagal membaca gambar. Periksa path file.")
            else:
                print("Gambar berhasil dimuat.")
                print("Proses...")
                resized_image = cv2.resize(image_rgb, (256, 256), interpolation=cv2.INTER_LINEAR)
                ###############################################
                hasil_grayscale = greyscale(resized_image)
                # Konversi grayscale ke format PhotoImage
                grayscale_image = Image.fromarray(hasil_grayscale)
                photoGray = ImageTk.PhotoImage(grayscale_image)

                # Tampilkan gambar grayscale
                grey_label.config(image=photoGray)
                grey_label.image = photoGray  # Simpan referensi gambar
                grey_label.bind("<Button-1>", lambda e: show_grayscale_image())
                
                ################################################
                
                ## kotak smoothing
                img_smoothing = cv2.medianBlur(hasil_grayscale,5)
                
                # Konversi smoothing ke format PhotoImage
                smoothing_image = Image.fromarray(img_smoothing)
                photoSmooth = ImageTk.PhotoImage(smoothing_image)
                
                smoothing_label.config(image=photoSmooth)
                smoothing_label.image= photoSmooth
                smoothing_label.bind("<Button-1>", lambda e: show_smotthing_image())
                
                ################################################
                
                ## kotak threshold 
                # threshold
                hasil_threshold = threshold(img_smoothing)
                threshold_image = Image.fromarray(hasil_threshold)
                photoThreshold = ImageTk.PhotoImage(threshold_image)
                threshold_label.config(image=photoThreshold)
                threshold_label.image= photoThreshold
                threshold_label.bind("<Button-1>", lambda e: show_threshold_image())
                
                ################################################
                
                ## kotak edgeDetect
                img_detection = cv2.Laplacian(hasil_threshold, cv2.CV_64F)
                img_detection2 = np.uint8(np.absolute(img_detection))
                detection_image = Image.fromarray(img_detection2)
                photoEdge = ImageTk.PhotoImage(detection_image)
                
                edgeDetec_label.config(image=photoEdge)
                edgeDetec_label.image= photoEdge
                edgeDetec_label.bind("<Button-1>", lambda e: show_EdgeDetec_image())
                
                ################################################
                
                ## kotak hasil preprocessing
                
                hasil_image = Image.fromarray(img_detection2)
                photoFinal = ImageTk.PhotoImage(hasil_image)
                
                hasilPreproc_label.config(image=photoFinal)
                hasilPreproc_label.image= photoFinal
                hasilPreproc_label.bind("<Button-1>", lambda e: show_Hasil_image())
        except Exception as e:
            print(f"Error saat memproses gambar: {e}")
        
        
    def show_grayscale_image():
        # Membuat jendela baru untuk menampilkan gambar asli
        top = Toplevel()
        top.title("Hasil Image Grayscale")
        grayscale_image = Image.fromarray(hasil_grayscale)
        photoGrayscale = ImageTk.PhotoImage(grayscale_image)
        
        # Menampilkan gambar asli di jendela baru
        img_label = tk.Label(top, image=photoGrayscale)
        img_label.image = photoGrayscale  # Referensi agar gambar tidak terhapus oleh garbage collector
        img_label.pack()
        
    def show_smotthing_image():
        # Membuat jendela baru untuk menampilkan gambar asli
        top = Toplevel()
        top.title("Hasil Image Smoothing")
        smooth_image = Image.fromarray(img_smoothing)
        photoSmoothing = ImageTk.PhotoImage(smooth_image)
        
        # Menampilkan gambar asli di jendela baru
        img_label = tk.Label(top, image=photoSmoothing)
        img_label.image = photoSmoothing  # Referensi agar gambar tidak terhapus oleh garbage collector
        img_label.pack()
    
    def show_threshold_image():
        # Membuat jendela baru untuk menampilkan gambar asli
        top = Toplevel()
        top.title("Hasil Threshold Segmentation")
        hasil_threshold = threshold(img_smoothing)
        threshold_image = Image.fromarray(hasil_threshold)
        photoThreshold = ImageTk.PhotoImage(threshold_image)
        
        # Menampilkan gambar asli di jendela baru
        img_label = tk.Label(top, image=photoThreshold)
        img_label.image = photoThreshold  # Referensi agar gambar tidak terhapus oleh garbage collector
        img_label.pack()
        
    def show_EdgeDetec_image():
        # Membuat jendela baru untuk menampilkan gambar asli
        top = Toplevel()
        top.title("Hasil Edge Detection")
        img_detection2 = np.uint8(np.absolute(img_detection))
        detection_image = Image.fromarray(img_detection2)
        photoEdge = ImageTk.PhotoImage(detection_image)
        
        # Menampilkan gambar asli di jendela baru
        img_label = tk.Label(top, image=photoEdge)
        img_label.image = photoEdge  # Referensi agar gambar tidak terhapus oleh garbage collector
        img_label.pack()
    
    def show_Hasil_image():
        # Membuat jendela baru untuk menampilkan gambar asli
        top = Toplevel()
        top.title("Hasil Preprocessing")
        hasil_image = Image.fromarray(img_detection2)
        photoFinal = ImageTk.PhotoImage(hasil_image)
        
        # Menampilkan gambar asli di jendela baru
        img_label = tk.Label(top, image=photoFinal)
        img_label.image = photoFinal  # Referensi agar gambar tidak terhapus oleh garbage collector
        img_label.pack()
        
    def klasifikasi():
        global hasil_image, model,predicted_class,probability, predicted_class,probability, photoAsli

        print("klasifikasi...")

        class_labels = {0: 'brown_spot', 1: 'healthy'}

        img_array = np.array(hasil_image)

        img_array = cv2.cvtColor(img_array, cv2.COLOR_GRAY2RGB)
        img_array = np.expand_dims(img_array, axis=0)

        result = model.predict(img_array)
        probability = result[0][0]
        predicted_class_index = 1 if probability > 0.5 else 0
        if predicted_class_index==0 :
            probability=1-probability
        print(predicted_class_index)
        predicted_class = class_labels[predicted_class_index]
        print(predicted_class,probability)

        final_gbr.config(image=photoAsli)
        final_gbr.image=photoAsli

        canvas.create_text(
        740,
        520,
        anchor="nw",
        text="Hasil Klasifikasi \nClass : "+predicted_class+" with "+str(probability)+" probability",
        fill="#FFF6E9",
        font=("Inter Bold", 16 * -1)
        )

        return (predicted_class,probability)
    

    canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 750,
    width = 1100,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
    )
    # BACKGROUND WINDOW
    canvas.place(x = 0, y = 0)
    canvas.create_rectangle(
        0.0,
        0.0,
        1100.0,
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
    
     # BUTTON KLASIFIKASI
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
        x=800.0,
        y=166.0,
        width=140.0,
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
        x=800.0,
        y=654.0,
        width=129.0,
        height=39.0
    )

    canvas.create_text(
        750.0,
        57.0,
        anchor="nw",
        text="Hasil Klasifikasi\ndengan CNN",
        fill="#FFFFFF",
        justify="center",
        font=("Inter Bold", 32 * -1)
    )
    # Teks
    final_gbr = Label(window, text="Citra")
    final_gbr.pack(pady=10)
    final_gbr.place(x=740, y=260, width=256, height=256)
    
    # canvas.create_text(
    #     730.0,
    #     520.0,
    #     anchor="nw",
    #     text=predicted_class+" with "+probability+" probability",
    #     fill="#FFFFFF",
    #     justify="center",
    #     font=("Inter Bold", 32 * -1)
    # )

    # labelhasil = Label(window, text="Klik untuk melihat \n citra")
    # labelhasil.pack(pady=10)
    # labelhasil.place(x=711, y=520, width=256, height=256)

    window.resizable(False, False)
    window.mainloop()
    
LOGIN()
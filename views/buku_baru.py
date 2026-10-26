import customtkinter as ctk
from tkinter import ttk

class BukuView (ctk.CTk):
    def __init__ (a):
        super().__init__()
        a.title("PERCOBAAN")
        a.geometry ("800x450")
        
        #grid utama
        a.grid_columnconfigure(0, weight=1)
        a.grid_columnconfigure(1, weight=1)
        a.grid_rowconfigure(0, weight=1)

        a.frame_kiri = ctk.CTkFrame(a)
        a.frame_kiri.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")
        ctk.CTkLabel(a.frame_kiri, text = "From aku kamu", font=("Arial", 20, "bold")).pack(pady=15)

        a.entry_judul = ctk.CTkEntry(a.frame_kiri, placeholder_text= "aku mau nasi tahu tempe")
        a.entry_judul.pack(pady=10, padx=10, fill="x")

        a.btn_simpan = ctk.CTkButton(a.frame_kiri, text="Simpan", fg_color="green")
        a.btn_simpan.pack(pady=10, padx=10, fill="x")

        #grid kanan
        a.frame_kanan = ctk.CTkFrame(a)
        a.frame_kanan.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")

        a.entry_judul = ctk.CTkEntry(a.frame_kanan, placeholder_text= "aku mau nasi tahu tempe")
        a.entry_judul.pack(pady=10, padx=10, fill="x")



if __name__ == "__main__":
    app = BukuView()
    app.mainloop()
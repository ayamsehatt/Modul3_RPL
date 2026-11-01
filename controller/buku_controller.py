import tkinter.messagebox as messagebox
from models.buku_model import BukuModel
from views.buku_view import BukuView
#Flesh 021

class BukuController:
    def __init__(self, user_role="anggota"):
        self.user_role = user_role 
        self.model = BukuModel()
        self.view = BukuView()

        self.id_terpilih = None  # Menyimpan ID buku yang dipilih dari tabel

        # Binding (mengikat) tombol di View dengan fungsi di Controller
        self.view.btn_simpan.configure(command=self.simpan_data)
        self.view.btn_hapus.configure(command=self.hapus_data)
        self.view.btn_update.configure(command=self.update_data)

        # Mengikat event pemilihan baris di tabel ke fungsi pilih_baris
        self.view.tabel.bind("<<TreeviewSelect>>", self.pilih_baris)  

        if self.user_role != "admin":
            self.view.btn_simpan.configure(state="disabled", text="Akses Terkunci (Khusus Admin)")
            self.view.btn_update.configure(state="disabled", text="Akses Terkunci (Khusus Admin)")
            self.view.btn_hapus.configure(state="disabled", text="Akses Terkunci (Khusus Admin)")
            self.view.entry_judul.configure(state="disabled")
            self.view.entry_penulis.configure(state="disabled")
            self.view.entry_tahun.configure(state="disabled")

        # Memuat data ke tabel saat aplikasi pertama kali dibuka
        self.muat_data_tabel()

    def muat_data_tabel(self):
        # Mengosongkan isi tabel di View terlebih dahulu
        for item in self.view.tabel.get_children():
            self.view.tabel.delete(item)

        # Mengambil data dari Model (database)
        data_buku = self.model.get_all_buku()

        # Memasukkan data baru ke dalam tabel View
        for buku in data_buku:
            self.view.tabel.insert("", "end",values=(buku['id_buku'],buku['judul'],buku['penulis'],buku['tahun_terbit'])
            )       

    def bersihkan_form(self):
        self.view.entry_judul.delete(0, 'end')
        self.view.entry_penulis.delete(0, 'end')
        self.view.entry_tahun.delete(0, 'end')
        self.id_terpilih = None  # Reset ID terpilih
        self.view.tabel.selection_remove(self.view.tabel.selection())  # Hapus seleksi di tabel

    def pilih_baris(self, event):
        selected_item = self.view.tabel.selection()
        if selected_item:
            item = self.view.tabel.item(selected_item)
            values = item['values']
            self.id_terpilih = values[0]  # Simpan ID buku yang dipilih
            self.view.entry_judul.delete(0, 'end')
            self.view.entry_judul.insert(0, values[1])
            self.view.entry_penulis.delete(0, 'end')
            self.view.entry_penulis.insert(0, values[2])
            self.view.entry_tahun.delete(0, 'end')
            self.view.entry_tahun.insert(0, values[3])

    def simpan_data(self):
        if self.user_role != "admin":
            messagebox.showwarning("Peringatan","Hanya admin yang dapat menyimpan data buku!")
            return
        #flesh 021
        # Mengambil teks dari kotak input di View
        judul = self.view.entry_judul.get()
        penulis = self.view.entry_penulis.get()
        tahun = self.view.entry_tahun.get()

        # Validasi Form Kosong
        if not judul or not penulis or not tahun:
            messagebox.showwarning("Peringatan","Semua kolom form harus diisi!")
            return

        berhasil = self.model.create_buku(judul, penulis, tahun)


        # Mengirim data ke Model untuk disimpan
        berhasil = self.model.create_buku(judul, penulis, tahun)
        if berhasil:
            messagebox.showinfo("Sukses","Data buku berhasil disimpan!")
            self.bersihkan_form()
            self.muat_data_tabel()
        else:
            messagebox.showerror("Error","Terjadi kesalahan saat menyimpan data.")

    def update_data(self):
        if self.id_terpilih is None:
            messagebox.showwarning("Peringatan","Pilih data buku yang ingin diperbarui dari tabel!")
            return

        judul = self.view.entry_judul.get()
        penulis = self.view.entry_penulis.get()
        tahun = self.view.entry_tahun.get()

        if not judul or not penulis or not tahun:
            messagebox.showwarning("Peringatan","Semua kolom form harus diisi!")
            return

        berhasil = self.model.update_buku(self.id_terpilih, judul, penulis, tahun)
        if berhasil:
            messagebox.showinfo("Sukses","Data buku berhasil diperbarui!")
            self.bersihkan_form()
            self.muat_data_tabel()
        else:
            messagebox.showerror("Error","Terjadi kesalahan saat memperbarui data.")

    def hapus_data(self):
        if self.id_terpilih is None:
            messagebox.showwarning("Peringatan","Pilih data buku yang ingin dihapus dari tabel!")
            return

        konfirmasi = messagebox.askyesno("Konfirmasi","Apakah Anda yakin ingin menghapus data buku ini?")
        if konfirmasi:
            berhasil = self.model.delete_buku(self.id_terpilih)
            if berhasil:
                messagebox.showinfo("Sukses","Data buku berhasil dihapus!")
                self.bersihkan_form()
                self.muat_data_tabel()
            else:
                messagebox.showerror("Error","Terjadi kesalahan saat menghapus data.")
    
    # Fungsi untuk menjalankan aplikasi
    def run(self):
        self.view.mainloop()
# from controller.buku_controller import BukuController

# if __name__ == "__main__":
#     app = BukuController()
#     app.run()

# from controller.anggota_controller import AnggotaController

# if __name__ == "__main__":
#     app = AnggotaController()
#     app.run()

from controller.auth_controller import AuthController
if __name__ == "__main__":
    app = AuthController()
    app.run()
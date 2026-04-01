from fastapi import FastAPI

# Inisialisasi aplikasi FastAPI
app = FastAPI(
    title = "UUD 1945 API",
    description = "API untuk mengeksplorasi Undang-Undang Dasar 1945",
    version = "0.1.0"
)

# Endpoint Root (Pintu Utama)
@app.get("/")
def read_root():
    return {
        "pesan" : "Selamat datang di UUD 1945 API",
        "status" : "Aktif"
    }
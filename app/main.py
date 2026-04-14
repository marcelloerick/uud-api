from fastapi import FastAPI, HTTPException
from typing import List

# Impor Blueprint uud.py
from app.models.uud import Pasal, Ayat

app = FastAPI(
    title = "UUD 1945 API",
    description = "API untuk mengeksplorasi Undang-Undang Dasar 1945",
    version = "0.1.0"
)

# Mock data palsu
MOCK_PASAL: List[Pasal] = [
    Pasal(
        nomor="1",
        ayat=[
            Ayat(
                nomor="1",
                teks="Negara Indonesia ialah negara kesatuan, yang berbentuk republik."
            ),
            Ayat(
                nomor="2",
                teks="Kedaulatan berada di tangan rakyat dan dilaksanakan menurut Undang-Undang Dasar."
            ),
            Ayat(
                nomor="3",
                teks="Negara Indonesia adalah negara hukum."
            )
        ]
    ),
    Pasal(
        nomor="4",
        ayat=[
            Ayat(
                nomor="1",
                teks="Presiden Republik Indonesia memegang kekuasaan pemerintahan tertinggi menurut Undang-Undang Dasar."
            ),
            Ayat(
                nomor="2",
                teks="Dalam menjalankan kewajibannya, Presiden dibantu oleh Wakil Presiden."
            )
        ]
    )
]

# --- ENDPOINTS ---
@app.get("/")
def read_root():
    return {
        "pesan" : "Selamat datang di UUD 1945 API",
        "status" : "Aktif"
    }

# Endpoint baru untuk memanggil semua Pasal
@app.get("/pasal", response_model=List[Pasal])
def get_semua_pasal():
    return MOCK_PASAL

#Endpoint untuk memanggil pasal berdasarkan nomor
@app.get("/pasal/{nomor}", response_model=Pasal)
def get_pasal_by_nomor(nomor: str):
    # Mencari pasal yang diminta didalam MOCK_PASAL
    for p in MOCK_PASAL:
        if p.nomor == nomor:
            return p

    #jika loop selesai dan pasal tidak ditemukan Berikan error 404
    raise HTTPException(status_code=404, detail="Pasal tidak ditemukan")
from fastapi import FastAPI, HTTPException
from typing import List
import json
import os

from app.models.uud import Pasal, Ayat

app = FastAPI(
    title="UUD 1945 API",
    description="API untuk mengeksplorasi Undang-Undang Dasar 1945",
    version="0.1.0"
)

# --- MESIN PEMBACA DATA (DATA INGESTION) ---

# 1. Mencari tahu di mana lokasi pasti file json kita berada di dalam komputer
LOKASI_FILE = os.path.join(os.path.dirname(__file__), "data", "uud.json")

# 2. Buka file JSON tersebut
with open(LOKASI_FILE, "r", encoding="utf-8") as file_json:
    data_mentah = json.load(file_json)
    # 3. Pydantic Magic: Ubah data mentah menjadi cetakan Pydantic
    DATA_PASAL = [Pasal(**item) for item in data_mentah]


# --- ENDPOINTS ---

@app.get("/")
def read_root():
    return {"pesan": "Selamat datang di UUD 1945 API", "status": "Aktif"}

@app.get("/pasal", response_model=List[Pasal])
def get_semua_pasal():
    return DATA_PASAL

@app.get("/pasal/{nomor}", response_model=Pasal)
def get_pasal_by_nomor(nomor: str):
    for p in DATA_PASAL:
        if p.nomor == nomor:
            return p
    raise HTTPException(status_code=404, detail="Pasal tidak ditemukan")

@app.get("/cari", response_model=List[Pasal])
def cari_pasal(kata_kunci: str):
    hasil_pencarian = []
    for pasal in DATA_PASAL:
        for ayat in pasal.ayat:
            if kata_kunci.lower() in ayat.teks.lower():
                hasil_pencarian.append(pasal)
                break
    return hasil_pencarian
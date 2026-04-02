from pydantic import BaseModel
from typing import List, Optional

# 1. Blueprint untuk Ayat
class Ayat(BaseModel):
    nomor: Optional[str] = None
    teks: str

# 2. Blueprint untuk Pasal
class Pasal(BaseModel):
    nomor: str
    ayat: List[Ayat]

# 3. Blueprint untuk Bab
class Bab(BaseModel):
    nomor: str
    judul: str
    pasal: List[Pasal]
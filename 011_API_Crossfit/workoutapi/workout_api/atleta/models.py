from datetime import datetime
from sqlalchemy import DateTime, Integer, String, Float 
from sqlalchemy.orm import Mapped, mapped_column
from workout_api.contrib.models import BaseModel

class AtletaModel(BaseModel):
    __tablename__ = "atletas"
    
    pk_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    nome: Mapped[str] = mapped_column(String(50), primary_key=False, nullable=False)
    cpf: Mapped[int] = mapped_column(Integer(11), primary_key=False, nullable=False)
    idade: Mapped[int] = mapped_column(Integer(11), primary_key=False, nullable=False)
    peso: Mapped[float] = mapped_column(Float(50), primary_key=False, nullable=False)
    altura: Mapped[float] = mapped_column(float(50), primary_key=False, nullable=False)
    sexo: Mapped[str] = mapped_column(String(1), primary_key=False, nullable=False)
    created_at: Mapped[datetime] = mapped_column(DateTime, nullable=False)
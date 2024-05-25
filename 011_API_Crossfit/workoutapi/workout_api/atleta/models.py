from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column
from workout_api.contrib.models import BaseModel

class AtletaModel(BaseModel):
    __tablename__ = "atletas"
    
    pk_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    nome: Mapped[str] = mapped_column(String(50), primary_key=False, nullable=False)
    cpf: Mapped[int] = mapped_column(Integer(11), primary_key=False, nullable=False)
    idade: Mapped[int] = mapped_column(Integer(11), primary_key=False, nullable=False)
    peso:
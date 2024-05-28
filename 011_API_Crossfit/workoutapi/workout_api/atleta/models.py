from datetime import datetime
from sqlalchemy import DateTime, ForeignKey, Integer, String, Float
from sqlalchemy.orm import Mapped, mapped_column, relationship
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
    
    #relacionamento Categoria:
    categoria: Mapped["CategoriaModel"] = relationship(back_populates="atleta")
    categoria_id = Mapped[int] = mapped_column(ForeignKey("categorias.pk_id"))
    
    #relacionamento Centro de Treinamento:
    centro_treinamento: Mapped["CentroTreinamentoModel"] = relationship(back_populates="atleta")
    centro_treinamento_id = Mapped[int] = mapped_column(ForeignKey("centros_treinamentos.pk_id"))
from typing import Annotated
from pydantic import BaseModel, Field, PositiveFloat
from workout_api.contrib.schemas import BaseSchema

class Atleta(BaseSchema):
    nome: Annotated[str, Field(description="Nome do atleta", example="Joao", max_length=50)]
    cpf: Annotated[int, Field(description="CPF do atleta", example="12345678912", max_length=11)]
    idade: Annotated[int, Field(description="Idade do atleta", examples="20")]
    peso: Annotated[PositiveFloat, Field(description="Peso do atleta", example="60.7")]
    altura: Annotated[PositiveFloat, Field(description="Altura do atleta", example="1.70")]
    sexo: Annotated[str, Field(description="Sexo do atleta", example="M", max_length=1)]
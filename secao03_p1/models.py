from typing import Optional

from pydantic import BaseModel, validator

class Curso(BaseModel):
    id: Optional[int] = None
    titulo: str
    aulas: int # mais de 12
    horas: int # mais de 10

    @validator('titulo')
    def validar_titulo(cls, value: str):
        # Validacao 1
        palavras = value.split(' ')
        if len(palavras) < 3:
            raise ValueError('O título deve ter pelo menos 3 palavras.')

        if value.islower():
            raise ValueError('O título deve ser capitalizado.')

        return value

    @validator('aulas')
    def validator_aulas(cls, value: int):
        # Validacao 2
        if value <= 12:
            raise ValueError('A quantidade de aulas deve ser maior que 12')

        return value

    @validator('horas')
    def validator_horas(cls, value: int):
        # Validacao 3
        if value <= 10:
            raise ValueError('A quantidade de horas precisa ser maior que 10')

        return value




#Variavel cursos tipo lista, importada no arquivo main.
cursos = [
    Curso(id= 1, titulo= "Programação com FastAPI", aulas= 15, horas=120),
    Curso(id= 2, titulo= "Programação em Python", aulas= 30, horas=180)

]

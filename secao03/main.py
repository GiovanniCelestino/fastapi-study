from fastapi import FastAPI
from fastapi import HTTPException
from fastapi import status
from models import Curso
from fastapi.responses import JSONResponse
from fastapi import Response
from fastapi import Path
from fastapi import Query
from fastapi import Header
from typing import Optional
#instancia o objeto
app = FastAPI()


cursos = {
    1: {
        "titulo": "Programação para Leigos",
        "aulas": 112,
        "horas": 58
    },
    2: {
        "titulo": "Algoritmos e Lógica de Programação",
        "aulas": 87,
        "horas": 57
    }
}

#Pega todos os cursos
@app.get('/cursos')
async def get_cursos():
    return cursos


#Pega por individuo
#Passo por parâmetro o ID do curso
@app.get('/cursos/{curso_id}')
async def get_curso(curso_id: int = Path(default=None, title='ID do curso', description='Deve ser entre 1 e 2', gt=0, lt=3)):
    try:
        curso = cursos[curso_id]
        #curso.update({"id": curso_id})
        return curso
    except KeyError:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail='Curso não encontrado.'
        )


#Inserir uma nova informação
#Vamos começar a usar as informações do arquivo models(já importado)
@app.post('/cursos', status_code=status.HTTP_201_CREATED)
async def post_curso(curso: Curso):
    teste: int = len(cursos) + 1
    cursos[teste] = curso
    #del curso.id
    return curso


#Atualiza informações já existente
@app.put('/cursos/{curso_id}')
async def put_cursos(curso_id: int, curso: Curso):
    if curso_id in cursos:
        cursos[curso_id] = curso
        del curso.id
    else:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f'Não existe curso com ID {curso_id}'
        )


#Deleta alguma informação
@app.delete('/cursos/{curso_id}')
async def put_cursos(curso_id: int):
    if curso_id in cursos:
        del cursos[curso_id]
        # return JSONResponse(status_code=status.HTTP_204_NO_CONTENT)
        return Response(status_code=status.HTTP_204_NO_CONTENT)

    else: 
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f'Não existe curso com o ID {curso_id}'
        )




#Exemplo de Query Parameters
#Informamos os valores no parametro do endpoint
@app.get('/calculadora')
async def calcular(a: int = Query(default=None, gt=5), b: int = Query(default=None, gt=10), x_geek: str = Header(default = None), c: Optional[int] = None):
    soma: int = a + b
    if c:
        soma = soma + c

    print (f'X-GEEK: {x_geek}')
    return {"resultado": soma}



if __name__ == '__main__':
    import uvicorn

    uvicorn.run("main:app", host="0.0.0.0", port=8000, debug=True, reload=True)
    
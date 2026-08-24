from fastapi import FastAPI

#Para executar esse arquivo, no terminal, digitar o nome do arquivo seguido da biblioteca: uvicorn main:app
#Caso algum ajuste tenha sido feito, fechar a aplicação e rodar: uvicorn main:app --reload
#http://127.0.0.1:8000/msg


app = FastAPI()

@app.get('/msg')
async def mensagem():
    return {"msg": "FastAPI na Geek University"}



# Não é obrigatório, mas caso eu queira executar o arquivo somente como: python main.py, posso usar o seguinte if:
# Não precisa encerrar a aplicação, pois ele realiza o reload das info.
if __name__ == '__main__':
    import uvicorn

    uvicorn.run("main:app", host="127.0.0.1", port=8000, log_level="info", reload=True)
#IMPORTANTE: Caso eu queira que qualquer pessoa que esteja na mesma rede que eu, tenha acesso a minha aplicação,
#devo alterar o host para: host="0.0.0.0". E para acessar, só colocar o IP junto com a porta: http://192.168.1.205:8000/
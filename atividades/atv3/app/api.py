from fastapi import FastAPI
from dotenv import load_dotenv
from .models.models import CPFRequest
import os
import httpx
from pathlib import Path

dotenv_path = Path(__file__).resolve().parents[1] / ".env"

load_dotenv(dotenv_path=dotenv_path)

app = FastAPI()

BASE_URL = "https://api.portaldatransparencia.gov.br/api-de-dados"
API_KEY = os.getenv("ACCESS_KEY")
print(f"API_KEY: {API_KEY}")


HEADERS = {
    "chave-api-dados": API_KEY
}

@app.post("/consultar-cpf")
async def consultar_cpf(request: CPFRequest):

    cpf = request.cpf

    resultados = {}

    endpoints = {
        "pessoa_fisica": f"{BASE_URL}/pessoa_fisica/{cpf}",
        "viagens_por_cpf": f"{BASE_URL}/viagens_por_cpf/{cpf}",
        "peti_por_cpf_nis": f"{BASE_URL}/peti_por_cpf_nis/{cpf}",
        "bpc_por_cpf_nis": f"{BASE_URL}/bpc_por_cpf_nis/{cpf}"
    }

    async with httpx.AsyncClient() as client:
        for nome_endpoint, url in endpoints.items():
            try:
                response = await client.get(url, headers=HEADERS, timeout=10)
                if response.status_code == 200:
                    resultados[nome_endpoint] = response.json()
                else:
                    resultados[nome_endpoint] = {
                        "erro": f"Status {response.status_code}"
                    }

            except Exception as e:
                resultados[nome_endpoint] = {
                    "erro": str(e)
                }

        return {
            "cpf": cpf,
            "dados": resultados
        }

@app.get("/")
async def home():
    return {
        "mensagem": "API de consulta CPF - POST /consultar-cpf"
    }



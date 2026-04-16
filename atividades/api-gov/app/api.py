from fastapi import FastAPI
from pathlib import Path
import requests
import dotenv
import os

env_path = Path(__file__).resolve().parents[1]/".env"

dotenv.load_dotenv(env_path)

app = FastAPI()


BASE_URL = "https://api.portaldatransparencia.gov.br/api-de-dados"
API_KEY = os.getenv("ACCESS_KEY")


HEADERS = {
    "chave-api-dados": API_KEY
}

@app.get("/")
def home():
    return {
        "mensagem": "API de Consulta -> Alguns endpoints do Portal da Transparência."
    }


@app.get("/consultar-por-cpf/{cpf}")
def consulta_por_cpf(cpf: str):

    endpoints = {
        "pessoa": f"{BASE_URL}/pessoa-fisica?cpf={cpf}",
        "viagens": f"{BASE_URL}/viagens-por-cpf?cpf={cpf}",
        "peti": f"{BASE_URL}/peti-por-cpf-ou-nis?codigo={cpf}",
        "bpc": f"{BASE_URL}/bpc-por-cpf-ou-nis?codigo={cpf}"
    }

    pessoaFisica = requests.get(endpoints["pessoa"], headers=HEADERS)
    viagensPorCpf = requests.get(endpoints["viagens"], headers=HEADERS)
    petiPorCpfNis = requests.get(endpoints["peti"], headers=HEADERS)
    bpcPorCpf = requests.get(endpoints["bpc"], headers=HEADERS)

    print(endpoints)

    return {
        "pessoa-fisica": pessoaFisica.json() if len(pessoaFisica.text) > 0 else [], #Não sei o porquê mas isso dava erro quando retornava vazio, embora os outros não dê erro
        "viagens-por-cpf": viagensPorCpf.json(),
        "peti-por-cpf": petiPorCpfNis.json(),
        "bpc-por-cpf": bpcPorCpf.json()
    }
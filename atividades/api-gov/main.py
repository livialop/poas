'''
Crie uma API que receba um CPF e depois realizar a consulta desse CPF na API https://portaldatransparencia.gov.br/api-de-dados nos endpoints:
- pessoa_fisica
- viagens_por_cpf
- peti_por_cpf_nis
-bpc_por_cpf_nis
'''

from uvicorn import run

if __name__ == "__main__":
    run("app.api:app", host="127.0.0.1", port=8080, reload=True)

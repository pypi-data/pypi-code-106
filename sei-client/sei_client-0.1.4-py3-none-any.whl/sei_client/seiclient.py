import json
import logging

import requests

BASE_URL = "https://investidor.b3.com.br/api/"


class SeiClient(object):
    def __init__(self, cache_guid, token):
        self.cache_guid = f"cache-guid={cache_guid}"
        self.token = token
        self.headers = {
            "sec-ch-ua": '" Not A;Brand";v="99", "Chromium";v="96", "Google Chrome";v="96"',
            "Accept": "application/json, text/plain, */*",
            "DNT": "1",
            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/96.0.4664.93 Safari/537.36",
            "sec-ch-ua-mobile": "?0",
            "Authorization": token,
            "sec-ch-ua-platform": '"Linux"',
        }

    def get_url(self, url, payload=None):  # pragma: no cover
        try:
            response = requests.get(
                url, headers=self.headers, data=payload, verify=False
            )
            response.raise_for_status()
            return response.json()
        except Exception as e:
            logging.exception(f"[SeiClient.get_url] {e}")
            return {}

    def get_investidor_cadastro(self):
        url = f"{BASE_URL}investidor/v1.1/cadastro?{self.cache_guid}"
        return self.get_url(url)

    def get_investidor_posicao(self):
        url = f"{BASE_URL}investidor/v1/posicao/total-acumulado?{self.cache_guid}"
        return self.get_url(url)

    def get_extrato_posicao(self, data, page=1):
        url = f"{BASE_URL}extrato/v1/posicao/{page}?data={data}&{self.cache_guid}"
        return self.get_url(url)

    def get_extrato_movimentacao(self, start_date, end_date, page=1):
        url = (
            f"{BASE_URL}extrato/v1/movimentacao/{page}?dataInicio={start_date}&dataFim={end_date}"
            f"&{self.cache_guid}"
        )
        return self.get_url(url)

    def get_extrato_ofertaspublicas(self, start_date, end_date, page=1):
        url = (
            f"{BASE_URL}extrato/v1/ofertas-publicas/{page}?dataInicio={start_date}&dataFim={end_date}"
            f"&{self.cache_guid}"
        )
        return self.get_url(url)

    def get_extrato_negociacao(self, start_date, end_date, page=1):
        url = (
            f"{BASE_URL}extrato/v1/negociacao-ativos/{page}?dataInicio={start_date}"
            f"&dataFim={end_date}&{self.cache_guid}"
        )
        return self.get_url(url)

    def get_extrato_negociacao_resumo(self, start_date, end_date, page=1):
        url = (
            f"{BASE_URL}extrato/v1/negociacao-ativos/resumo/{page}?dataInicio={start_date}"
            f"&dataFim={end_date}&{self.cache_guid}"
        )
        return self.get_url(url)

    def get_extrato_detalhes_rendavariavel(self, uid):
        url = f"{BASE_URL}extrato/v1/posicao/detalhes/renda-variavel/acao/{uid}?{self.cache_guid}"
        return self.get_url(url)

    def get_sistema_carga(self):
        url = f"{BASE_URL}sistema/v1/carga/ultima-execucao?{self.cache_guid}"
        return self.get_url(url)

    def save_to_json(self, data, filename):
        with open(filename, "w") as f:
            json.dump(data, f, indent=4)

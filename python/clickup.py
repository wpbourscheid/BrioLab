import json
import requests
import os
from dotenv import load_dotenv

load_dotenv()

CLICKUP_TOKEN = os.getenv("CLICKUP_TOKEN")
LIST_ID = os.getenv("CLICKUP_LIST_ID")

def create_task(lead: dict):
    url = f"https://api.clickup.com/api/v2/list/{LIST_ID}/task"

    headers = {
        "Authorization": CLICKUP_TOKEN,
        "Content-Type": "application/json"
    }

    payload = {
        "name": f"Lead - {lead['nome']}",
        "description": (
            f"Especialidade: {lead['especialidade']}\n"
            f"Principal desafio: {lead['principal_desafio']}\n"
            f"Telefone: {lead['telefone']}\n"
            f"E-mail: {lead['email']}"
        )
    }

    response = requests.post(
        url,
        json=payload,
        headers=headers
    )

    response.raise_for_status()

    return response.json()
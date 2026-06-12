import json


def create_task(lead: dict) -> dict:
    """
    Simula a criação de uma tarefa no ClickUp.
    """

    payload = {
        "name": f"Lead - {lead['nome']}",
        "description": (
            f"Especialidade: {lead['especialidade']}\n"
            f"Principal desafio: {lead['principal_desafio']}\n"
            f"Telefone: {lead['telefone']}\n"
            f"E-mail: {lead['email']}"
        ),
        "status": "novo_lead",
        "assignee": "comercial"
    }

    print("\n=== PAYLOAD CLICKUP ===")
    print(json.dumps(payload, indent=4, ensure_ascii=False))

    return {
        "success": True,
        "task_id": "CLP-001",
        "payload": payload
    }
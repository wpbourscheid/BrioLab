import re

def process_lead(data: dict) -> dict:
    validate_required_fields(data)

    data["email"] = normalize_email(data["email"])
    data["telefone"] = format_phone(data["telefone"])

    return data


def validate_required_fields(data: dict) -> None:
    """
    Verifica se todos os campos obrigatórios estão presentes
    e não estão vazios.
    """

    required_fields = [
        "nome",
        "telefone",
        "email",
        "especialidade",
        "principal_desafio"
    ]

    for field in required_fields:
        if field not in data or not str(data[field]).strip():
            raise ValueError(f"Campo obrigatório ausente ou vazio: {field}")


def normalize_email(email: str) -> str:
    """
    Remove espaços e converte o e-mail para minúsculo.
    """

    email = email.strip().lower()

    pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"

    if not re.match(pattern, email):
        raise ValueError("E-mail inválido")

    return email


def format_phone(phone: str) -> str:
    """
    Remove caracteres especiais do telefone.
    """

    phone = re.sub(r"\D", "", phone)

    if len(phone) < 10:
        raise ValueError("Telefone inválido")

    return phone
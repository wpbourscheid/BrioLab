from validator import process_lead
from database import create_table, insert_lead
from clickup import create_task


def main():
    lead = {
        "nome": "Maria Silva",
        "telefone": "(53) 99999-1234",
        "email": "MARIA@EMAIL.COM",
        "especialidade": "Odontologia",
        "principal_desafio": "Atrair mais pacientes"
    }

    try:
        print("Recebendo lead...")

        # Validação e normalização
        lead = process_lead(lead)

        print("Lead validado com sucesso.")

        # Banco de dados
        create_table()

        lead_id = insert_lead(lead)

        print(f"Lead salvo no banco com ID {lead_id}.")

        # ClickUp
        result = create_task(lead)

        print(
            f"Tarefa criada com sucesso: "
            f"{result['task_id']}"
        )

    except ValueError as e:
        print(f"Erro de validação: {e}")

    except Exception as e:
        print(f"Erro inesperado: {e}")


if __name__ == "__main__":
    main()
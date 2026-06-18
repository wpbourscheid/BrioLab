from validator import process_lead
from database import create_table, insert_lead
from clickup import create_task


def main():
    lead = {
        "nome": "Maria Carla",
        "telefone": "(53) 99999-1324",
        "email": "MARIA@EMAIL.COM",
        "especialidade": "Advocacia",
        "principal_desafio": "Atrair mais clientes direito do consumidor"
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
            f"Tarefa criada com sucesso! "
            f"ID: {result['id']}"
        )

    except ValueError as e:
        print(f"Erro de validação: {e}")

    except Exception as e:
        print(f"Erro inesperado: {e}")


if __name__ == "__main__":
    main()
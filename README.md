# Desafio Técnico - Brio Lab

## Visão Geral

Este repositório contém a solução desenvolvida para o processo seletivo da vaga de Desenvolvedor de Automação & IA da Brio Lab.

O desafio foi dividido em duas partes:

* Desafio 1: Orquestração com N8N
* Desafio 2: Backend com Python

Este projeto busca reproduzir um cenário real de automação de conteúdo, utilizando integração entre sistemas, inteligência artificial e persistência de dados.

---

# Desafio 1 - Orquestração com N8N

## Objetivo

Automatizar o processamento de tarefas aprovadas, simulando uma integração com o ClickUp.

Quando uma tarefa possui status "aprovado", o fluxo:

1. Recebe os dados da tarefa
2. Valida o status
3. Envia a legenda para uma IA
4. Gera hashtags automaticamente
5. Salva o resultado em uma planilha
6. Envia uma notificação de conclusão

---

## Fluxo Implementado

Webhook → IF → AI Agent (Gemini) → Google Sheets → Gmail

---

## Tecnologias Utilizadas

* N8N Cloud
* Google Gemini
* Google Sheets
* Hoppscotch (testes de webhook)

---

## Estrutura dos Dados

Payload recebido pelo webhook:

```json
{
  "nome": "Post sobre Marketing",
  "descricao": "Conteúdo Instagram",
  "status": "aprovado",
  "legenda": "Descubra como aumentar a autoridade da sua marca nas redes sociais."
}
```

---

## Regra de Negócio

A automação somente continua quando o campo status possui valor igual a "aprovado".

Caso contrário, o fluxo é interrompido.

---

## Uso de Inteligência Artificial

Foi utilizada a API do Google Gemini para geração automática de hashtags com base na legenda recebida.

Prompt utilizado:

"Você é um especialista em marketing digital para Instagram. Gere 10 hashtags relevantes para a legenda fornecida. Retorne apenas as hashtags."

---

## Persistência

Os dados processados são armazenados em uma planilha Google Sheets através do nó "Append Row in Sheet". Cada execução gera um novo registro contendo o nome da tarefa, descrição, legenda original e hashtags produzidas pela IA:

* Nome
* Descrição
* Legenda
* Hashtags geradas

---

## Notificação

Após a persistência dos dados, o workflow envia automaticamente um e-mail utilizando a integração com Gmail.

Para fins de teste e validação do fluxo, o destinatário configurado foi o próprio desenvolvedor.

Em um ambiente de produção, o destinatário poderia ser um membro da equipe de conteúdo, comercial ou operação.

---

## Testes Realizados

### Cenário 1 - Status aprovado

Resultado esperado:

* Fluxo executado completamente
* Hashtags geradas
* Dados armazenados

Resultado obtido:

* Sucesso

### Cenário 2 - Status diferente de aprovado

Resultado esperado:

* Fluxo interrompido

Resultado obtido:

* Sucesso

---

## Melhorias Futuras

Com mais tempo, eu implementaria:

* Integração real com a API do ClickUp
* Persistência em Supabase
* Notificações por WhatsApp
* Tratamento avançado de erros
* Logs centralizados
* Versionamento de prompts de IA

---

## Considerações

Busquei desenvolver uma solução simples, funcional e próxima de um cenário real de automação, priorizando clareza, manutenção e facilidade de entendimento.

# Desafio 2 - Backend com Python

## Visão Geral

Este projeto simula o processamento de leads provenientes de um formulário de diagnóstico.

O fluxo implementado recebe um conjunto de dados, realiza validações e normalizações, persiste as informações em banco de dados SQLite e simula a criação de uma tarefa no ClickUp para o time comercial.

---

## Arquitetura

```text
JSON de Entrada
        ↓
Validação de Dados
        ↓
Normalização
        ↓
Persistência SQLite
        ↓
Simulação API ClickUp
        ↓
Resultado Final
```

### Estrutura do Projeto

```text
python/
│
├── main.py
├── validator.py
├── database.py
├── clickup.py
├── requirements.txt
└── leads.db
```

---

## Tecnologias Utilizadas

* Python 3
* SQLite
* Bibliotecas nativas:

  * sqlite3
  * json
  * re

---

## Funcionalidades

### 1. Validação de Dados

Valida a presença dos seguintes campos obrigatórios:

* nome
* telefone
* email
* especialidade
* principal_desafio

Caso algum campo esteja ausente ou vazio, uma exceção é lançada.

---

### 2. Normalização

#### Email

Converte o email para letras minúsculas e valida seu formato.

Exemplo:

```text
Entrada: MARIA@EMAIL.COM
Saída: maria@email.com
```

#### Telefone

Remove caracteres especiais e mantém apenas os números.

Exemplo:

```text
Entrada: (53) 99999-1234
Saída: 53999991234
```

---

### 3. Persistência

Os dados tratados são armazenados em uma base SQLite local.

Tabela:

```sql
CREATE TABLE leads (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    telefone TEXT NOT NULL,
    email TEXT NOT NULL,
    especialidade TEXT NOT NULL,
    principal_desafio TEXT NOT NULL
);
```

---

### 4. Integração com ClickUp

Foi implementada uma simulação da criação de tarefas no ClickUp.

A solução gera um payload estruturado contendo os dados do lead e exibe o resultado no terminal.

Em ambiente de produção, essa etapa seria substituída por uma chamada HTTP para a API oficial do ClickUp.

---

## Como Executar

Clone o repositório:

```bash
git clone https://github.com/wpbourscheid/BrioLab.git
```

Acesse a pasta:

```bash
cd python
```

Execute:

```bash
python main.py
```

---

## Caso de Teste 1 - Lead Válido

Entrada:

```json
{
    "nome": "Maria Silva",
    "telefone": "(53) 99999-1234",
    "email": "MARIA@EMAIL.COM",
    "especialidade": "Odontologia",
    "principal_desafio": "Atrair mais pacientes"
}
```

Resultado esperado:

* Lead validado
* Dados normalizados
* Lead salvo no banco
* Tarefa criada com sucesso

Resultado obtido:

✅ Sucesso

---

## Caso de Teste 2 - Email Inválido

Entrada:

```json
{
    "nome": "Maria Silva",
    "telefone": "(53) 99999-1234",
    "email": "maria@email",
    "especialidade": "Odontologia",
    "principal_desafio": "Atrair mais pacientes"
}
```

Resultado esperado:

Erro de validação de email.

Resultado obtido:

✅ Sucesso

---

## Caso de Teste 3 - Telefone Inválido

Entrada:

```json
{
    "nome": "Maria Silva",
    "telefone": "123",
    "email": "maria@email.com",
    "especialidade": "Odontologia",
    "principal_desafio": "Atrair mais pacientes"
}
```

Resultado esperado:

Erro de validação de telefone.

Resultado obtido:

✅ Sucesso

---

## Melhorias Futuras

Com mais tempo, eu implementaria:

✅ Integração real com a API do ClickUp
* Persistência em Supabase ou PostgreSQL
✅ Variáveis de ambiente para credenciais
* Logs estruturados
* Testes automatizados com pytest
* API REST utilizando FastAPI
* Tratamento avançado de falhas externas

---

## Considerações Finais

O principal objetivo desta solução foi reproduzir, de forma simples e organizada, um fluxo comum em processos de automação comercial: receber dados de um formulário, garantir sua qualidade antes do processamento, armazenar as informações de forma estruturada e encaminhá-las para a ferramenta responsável pela operação.

Durante o desenvolvimento, procurei separar as responsabilidades da aplicação em módulos independentes. A validação e normalização dos dados ficaram concentradas em um único componente, enquanto a persistência em banco de dados e a integração com sistemas externos foram tratadas separadamente. Essa abordagem facilita a manutenção do código, reduz o acoplamento entre as partes da aplicação e permite que futuras alterações sejam realizadas com menor impacto.

Também dei atenção ao tratamento dos dados recebidos. Em cenários reais de automação, informações incompletas ou mal formatadas podem interromper fluxos inteiros e gerar retrabalho manual. Por esse motivo, foram implementadas validações para campos obrigatórios, verificação do formato de e-mail e normalização de telefones antes da persistência e da integração com outros sistemas.

A escolha do SQLite foi motivada pela simplicidade de configuração e pela adequação ao escopo do desafio. Entretanto, a estrutura foi pensada para permitir a substituição futura por soluções mais robustas, como Supabase ou PostgreSQL, sem necessidade de mudanças significativas na lógica de negócio.

Da mesma forma, a integração com o ClickUp foi simulada através da geração de um payload estruturado. Embora o desafio permita essa abordagem, a implementação foi organizada de forma que uma chamada real à API possa ser adicionada posteriormente com alterações mínimas.

Por fim, busquei equilibrar simplicidade e clareza. Em vez de priorizar uma solução excessivamente complexa, optei por uma implementação que demonstra os conceitos fundamentais de validação, persistência, integração e organização de código, mantendo a legibilidade e a facilidade de manutenção como preocupações centrais.

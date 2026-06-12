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

Webhook → IF → AI Agent (Gemini) → Google Sheets → Notificação

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

Os dados processados são armazenados em uma planilha Google Sheets contendo:

* Nome
* Descrição
* Legenda
* Hashtags geradas

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

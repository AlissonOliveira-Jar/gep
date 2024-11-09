# Unvalidated vs Validated Input/Output usando FastAPI

## Índice

- [Unvalidated vs Validated Input/Output usando FastAPI](#unvalidated-vs-validated-inputoutput-usando-fastapi)
  - [Índice](#índice)
    - [Introdução](#introdução)
    - [Principais Conceitos](#principais-conceitos)
      - [Unvalidated Input](#unvalidated-input)
      - [Unvalidated Output](#unvalidated-output)
      - [Vulnerabilidades Comuns](#vulnerabilidades-comuns)
      - [Referências](#referências)
    - [Rodando o Projeto](#rodando-o-projeto)
      - [Linter](#linter)

### Introdução

Este projeto demonstra os riscos de Entrada/Saída Não Validada em uma aplicação baseada em FastAPI e como esses riscos podem ser mitigados com validação e sanitização adequadas. O projeto contém dois conjuntos de rotas: um com vulnerabilidades (entrada/saída não validada) e outro com medidas de segurança corretamente implementadas.

Compreender os perigos de não validar entrada e não sanitizar saída é crucial para garantir a segurança das aplicações web. De acordo com o OWASP Top Ten, a validação inadequada de entrada é um dos riscos de segurança mais críticos no desenvolvimento de software. Da mesma forma, o CWE/SANS Top 25 Most Dangerous Software Errors destaca fraquezas que levam a graves problemas de segurança.

### Principais Conceitos

#### Unvalidated Input

Entrada Não Validada refere-se a uma situação onde uma aplicação processa dados fornecidos por uma entidade externa (usuário, API, etc.) sem garantir que são seguros ou estão no formato esperado. Quando as entradas não são devidamente validadas, atacantes podem injetar conteúdo malicioso na aplicação, potencialmente levando a ataques como injeção de SQL, injeção de comandos e estouro de buffer(OWASP, 2024).

- **CWE-20: Validação Inadequada de Entrada:** Quando os dados de entrada não são validados, atacantes podem enviar dados inesperados que a aplicação não consegue manipular, levando a vulnerabilidades de segurança. [CWE-2O no MITRE](https://cwe.mitre.org/data/definitions/20.html?form=MG0AV3)
- **OWASP Top 10 - A03:2021 - Injeção:** Entradas que não são validadas permitem que atacantes injetem código malicioso, comandos ou dados na aplicação. [OWASP Injeção](https://owasp.org/Top10/A03_2021-Injection/?form=MG0AV3)

#### Unvalidated Output

Saída Não Validada refere-se a cenários onde dados fornecidos por um usuário ou outra fonte não confiável são incluídos na resposta da aplicação sem sanitização adequada. Isso pode levar a ataques como Cross-Site Scripting (XSS), onde scripts maliciosos podem ser executados no contexto do navegador da vítima.

- **CWE-79: Neutralização Inadequada de Entrada Durante a Geração da Página Web (Cross-Site Scripting - XSS):** Se a saída não for devidamente sanitizada, scripts maliciosos podem ser incluídos nas respostas que são executadas no navegador do usuário, potencialmente levando ao sequestro de contas ou roubo de dados. [CWE-79 no MITRE](https://cwe.mitre.org/data/definitions/79.html?form=MG0AV3)
- **OWASP Top 10 - A04:2021 - Design Inseguro:** Isso inclui o manuseio inadequado da saída e a garantia de que ela é segura para ser renderizada pelo navegador do usuário. [OWASP XSS](https://owasp.org/www-community/attacks/xss/?form=MG0AV3)

#### Vulnerabilidades Comuns

Alguns ataques comuns associados à entrada/saída não validada incluem:

- **Ataques de Injeção:**

  - Injeção de SQL (CWE-89): Um atacante injeta consultas SQL maliciosas em campos de entrada.
  - Injeção de Comandos (CWE-77): Um atacante injeta comandos em entradas processadas pelo sistema.

- **Cross-Site Scripting (XSS):**

  - XSS Armazenado: Scripts maliciosos são armazenados na aplicação e entregues aos usuários.
  - XSS Refletido: Scripts maliciosos são refletidos de uma solicitação web de volta para o usuário.

#### Referências

1. **OWASP Top 10**: [OWASP Top 10](https://owasp.org/www-project-top-ten/?form=MG0AV3)
2. **CWE - Common Weakness Enumeration:** [CWE Website](https://cwe.mitre.org/?form=MG0AV3)
3. **CWE-20: Validação Inadequada de Entrada:** [CWE-20](https://cwe.mitre.org/data/definitions/20.html?form=MG0AV3)
4. **CWE-79: Neutralização Inadequada de Entrada Durante a Geração da Página Web (XSS):** [CWE-79](https://cwe.mitre.org/data/definitions/79.html?form=MG0AV3)
5. **CWE-89: Injeção de SQL:** [CWE-89](https://cwe.mitre.org/data/definitions/89.html?form=MG0AV3)
6. **OWASP XSS Prevenção:** [OWASP XSS](https://owasp.org/www-community/attacks/xss/?form=MG0AV3)

### Rodando o Projeto

- Criando ambiente virtual

```bash
python3 -m venv venv
source venv/bin/activate # No Windows: venv\Scripts\activate
```

- Instalando as dependências

```bash
pip install -r requirements.txt
```

- Iniciando o projeto

```bash
fastapi dev main.py
```

- Docker

```bash
docker build -t gep .
```

```bash
docker run -p 8000:80 gep
```

#### Linter

- Ruff

```bash
ruff check .
```

```bash
ruff check . --fix
```

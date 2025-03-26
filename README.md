# API FastAPI + SQLModel usando DDD

Este repositório apresenta uma implementação de uma API utilizando FastAPI e SQLModel, estruturada conforme os princípios do Domain-Driven Design (DDD). A seguir, detalhamos a organização do projeto e como cada camada reflete os conceitos do DDD.

## Estrutura do Projeto

A arquitetura do projeto é dividida em quatro camadas principais:

- `domain/`
- `application/`
- `infrastructure/`
- `interface/`

### 1. Camada de Domínio (`domain/`)

**Responsabilidade:** Esta camada encapsula as regras de negócio e as entidades fundamentais do domínio.

**Componentes:**

- **Entidades:** Objetos com identidade distinta que representam conceitos do domínio.
- **Objetos de Valor:** Objetos imutáveis que descrevem aspectos do domínio sem identidade própria.
- **Repositórios (Interfaces):** Contratos que definem operações para persistência e recuperação de entidades, sem implementação concreta nesta camada.

**DDD em Prática:** Ao isolar as regras de negócio nesta camada, garantimos que o núcleo do domínio permaneça independente de detalhes técnicos, promovendo um design mais limpo e sustentável.

### 2. Camada de Aplicação (`application/`)

**Responsabilidade:** Orquestra os casos de uso do sistema, coordenando as operações entre o domínio e as demais camadas.

**Componentes:**

- **Casos de Uso (Use Cases):** Implementações específicas que utilizam as entidades e repositórios do domínio para realizar operações de negócio.
- **Serviços de Aplicação:** Facilitam a comunicação entre a interface do usuário e o domínio, aplicando regras de aplicação específicas.

**DDD em Prática:** Esta camada atua como uma ponte entre o mundo externo e o domínio, assegurando que as regras de negócio sejam aplicadas corretamente em diferentes cenários.

### 3. Camada de Infraestrutura (`infrastructure/`)

**Responsabilidade:** Fornece implementações concretas para as interfaces definidas no domínio, lidando com detalhes técnicos como persistência de dados.

**Componentes:**

- **Repositórios (Implementações):** Classes que concretizam as interfaces de repositório do domínio, utilizando SQLModel para interagir com o banco de dados.
- **Configurações:** Definições relacionadas a banco de dados, provedores de serviços e outras dependências técnicas.

**DDD em Prática:** Ao separar as preocupações técnicas nesta camada, mantemos o domínio livre de dependências externas, facilitando testes e manutenção.

### 4. Camada de Interface (`interface/`)

**Responsabilidade:** Gerencia a comunicação entre o sistema e o mundo externo, incluindo APIs, interfaces de usuário e outros pontos de entrada.

**Componentes:**

- **Controladores (Controllers):** Manipulam as requisições HTTP, delegando a lógica de negócio para a camada de aplicação.
- **Modelos de Entrada/Saída (DTOs):** Estruturas que definem como os dados são recebidos e retornados pela API.

**DDD em Prática:** Esta camada assegura que a interação com o usuário ou sistemas externos seja tratada de forma desacoplada das regras de negócio, permitindo flexibilidade na apresentação e comunicação.

## Tecnologias Utilizadas

- **FastAPI:** Framework web moderno e rápido para construção de APIs com Python.
- **SQLModel:** Biblioteca para interagir com bancos de dados, combinando recursos do SQLAlchemy e Pydantic.
- **Poetry:** Ferramenta para gerenciamento de dependências e packaging em Python.

## Considerações Finais

Esta estrutura baseada em DDD promove um design modular e coeso, facilitando a manutenção e evolução do sistema. Cada camada tem responsabilidades bem definidas, permitindo que mudanças em uma não impactem diretamente as outras. 

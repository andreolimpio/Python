# 🐍 Python | Lógica de Programação e Projetos Práticos

**Repositório educacional de André Olímpio**  
Programação • Algoritmos • Estruturas de dados • Resolução de problemas

> Aprender programação é compreender um problema, construir uma solução e saber explicar por que ela funciona.

[![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?logo=python&logoColor=white)](https://www.python.org/) ![Propósito](https://img.shields.io/badge/prop%C3%B3sito-educacional-236B8E) ![Status](https://img.shields.io/badge/status-em%20evolu%C3%A7%C3%A3o-8A6D3B)

## 📖 Sobre este repositório

Este espaço reúne **exercícios, desafios e pequenos sistemas em Python** utilizados como material de estudo e demonstração de conceitos de lógica de programação. O conteúdo é indicado a estudantes, professores e pessoas interessadas em compreender a construção de programas de maneira progressiva.

Os arquivos apresentam **diferentes níveis de complexidade e estágios de desenvolvimento**. Alguns são exemplos pontuais de sintaxe; outros integram vários conceitos em aplicações de terminal. Por serem materiais didáticos, **não devem ser considerados sistemas prontos para uso em produção**.

## 🧭 Comece por aqui

| Etapa | Conteúdo | Exemplos no repositório |
| --- | --- | --- |
| 1 | Entrada, saída e variáveis | [`print_nome_usuario.py`](Projetos_Python/print_nome_usuario.py) |
| 2 | Condicionais | [`verificar_par_impar.py`](Projetos_Python/verificar_par_impar.py) |
| 3 | Repetição e acumuladores | [`soma_quantidade_pares_impares.py`](Projetos_Python/soma_quantidade_pares_impares.py) |
| 4 | Listas e operações | [`soma_numeros_lista.py`](Projetos_Python/soma_numeros_lista.py), [`ordenar_lista.py`](Projetos_Python/ordenar_lista.py), [`tamanho_lista.py`](Projetos_Python/tamanho_lista.py) |
| 5 | Funções e módulos | [`funcao_arquivo_externo/`](Projetos_Python/funcao_arquivo_externo) |
| 6 | Matrizes e operações | [`operacoes_matematicas_variaveis_compostas.py`](Projetos_Python/operacoes_matematicas_variaveis_compostas.py) |
| 7 | Orientação a objetos | [`biblioteca_poo.py`](Projetos_Python/biblioteca_poo.py) |
| 8 | Desafios e sistemas completos para estudo | [`desafio_1.py`](Projetos_Python/desafio_1.py), [`desafio_2.py`](Projetos_Python/desafio_2.py) |

### Outros exemplos

- [`random_sqrt.py`](Projetos_Python/random_sqrt.py): geração de números aleatórios e cálculo de raiz quadrada.
- [`random_sqrt_data_atual.py`](Projetos_Python/random_sqrt_data_atual.py): módulos `random`, `datetime` e `math`.

## 🗂️ Estrutura atual

```text
Python/
├── README.md
├── Projeto_Academia/
│   └── Projeto_Academia.py
├── Projeto_Biblioteca/
│   └── Projeto_Biblioteca.py
└── Projetos_Python/
    ├── biblioteca_poo.py
    ├── desafio_1.py
    ├── desafio_2.py
    ├── funcao_arquivo_externo/
    │   ├── main.py
    │   └── operacoes.py
    ├── operacoes_matematicas_variaveis_compostas.py
    ├── ordenar_lista.py
    ├── print_nome_usuario.py
    ├── random_sqrt.py
    ├── random_sqrt_data_atual.py
    ├── soma_numeros_lista.py
    ├── soma_quantidade_pares_impares.py
    ├── tamanho_lista.py
    └── verificar_par_impar.py
```

*Visualização simplificada: arquivos gerados automaticamente pelo Python, quando presentes, foram omitidos da árvore acima.*

## 💻 Projetos e desafios

### 🎓 Sistema de academia

**[Abrir o projeto](Projeto_Academia/Projeto_Academia.py)**

Exemplo de aplicação de terminal com cadastro e listagem de alunos, cálculo de IMC, cálculo de mensalidades, funções, listas e menu de navegação.

**Ponto de atenção:** o login utiliza credenciais fixas para demonstração didática. **Não representa um mecanismo seguro de autenticação para sistemas reais.** O armazenamento dos alunos ocorre apenas em memória durante a execução.

### 📚 Sistema de biblioteca escolar

**[Abrir o projeto](Projeto_Biblioteca/Projeto_Biblioteca.py)**

Exercício integrado envolvendo cadastro de livros e usuários, empréstimos e devoluções, leitura e gravação de CSV, estrutura `match/case` e uma função recursiva de contagem.

**Ponto de atenção:** há um caminho absoluto usado na leitura de `usuarios.csv`, enquanto a gravação usa caminho relativo. Isso precisa ser corrigido e validado antes de usar o sistema em uma demonstração de persistência de dados.

### 📦 Sistema de estoque

**[Abrir o desafio](Projetos_Python/desafio_2.py)**

Programa de terminal com produtos armazenados em listas de dicionários, cadastro, busca, atualização de quantidade, remoção, ordenação e estatísticas simples. Os dados ficam em memória e não são persistidos em arquivo ou banco de dados.

### 📝 Análise de desempenho acadêmico

**[Abrir o desafio](Projetos_Python/desafio_1.py)**

Exemplo de cálculo de média e frequência, classificação de desempenho e tomada de decisão com estruturas condicionais.

**Ponto de atenção:** os dados de entrada precisam ser válidos; por exemplo, o total de aulas deve ser maior que zero para evitar divisão por zero.

## 🚀 Como executar

### Pré-requisitos

- [Python 3.10 ou superior](https://www.python.org/downloads/) instalado. Essa versão é recomendada porque o projeto de biblioteca usa `match/case`.
- Terminal do sistema operacional, VS Code ou outra IDE compatível.
- **NumPy apenas para o exemplo de operações com matrizes**, que o importa diretamente.

Clone o repositório:

```bash
git clone https://github.com/andreolimpio/Python.git
cd Python
```

Execute um exercício introdutório:

```bash
python Projetos_Python/verificar_par_impar.py
```

Execute um desafio:

```bash
python Projetos_Python/desafio_2.py
```

Execute o exemplo de funções em arquivos separados:

```bash
python Projetos_Python/funcao_arquivo_externo/main.py
```

Para executar o exercício de matrizes, instale antes o NumPy no ambiente Python utilizado:

```bash
python -m pip install numpy
python Projetos_Python/operacoes_matematicas_variaveis_compostas.py
```

> **Observação:** em alguns computadores, o comando de execução é `python3` ou `py`, em vez de `python`. Os sistemas interativos solicitam dados pelo terminal. Para o projeto de biblioteca, revise primeiro o caminho dos arquivos CSV descrito acima.

## 🧠 Como estudar com estes exemplos

1. Leia o enunciado ou identifique o problema que o arquivo resolve.
2. Antes de executar, tente prever a saída do programa.
3. Leia o código e localize as variáveis, condições, laços e funções.
4. Execute o programa com entradas diferentes, respeitando os formatos esperados.
5. Altere uma regra, execute novamente e explique o efeito da mudança.
6. Registre melhorias e, se possível, crie testes para os comportamentos esperados.

### Sugestão de prática

No arquivo [`verificar_par_impar.py`](Projetos_Python/verificar_par_impar.py), identifique o uso do operador `%`, teste números negativos e zero e explique por que o código classifica cada caso como par ou ímpar.

## 🛠️ Qualidade e evolução

Este repositório é mantido como **material educacional em evolução**. As melhorias previstas incluem:

- Organização dos exercícios por assunto e nível de dificuldade.
- Validação das entradas nos programas interativos.
- Padronização de nomes, formatação e mensagens.
- Revisão dos exemplos de leitura e gravação de arquivos.
- Inclusão progressiva de testes automatizados.
- Documentação individual de desafios e pequenos sistemas.
- Remoção de arquivos temporários ou gerados automaticamente do versionamento.

As funcionalidades e limitações aqui descritas foram identificadas a partir do código publicado. **Este README não significa que todos os programas foram submetidos a testes completos.**

## 👨‍🏫 Autor e contexto educacional

**André Olímpio**  
Professor de Tecnologia da Informação e desenvolvedor de software.

- **Portfólio GitHub:** [github.com/andreolimpio](https://github.com/andreolimpio)
- **Somos Todos T.I.:** [somostodosti.com.br](https://somostodosti.com.br)
- **LinkedIn:** [André Olímpio](https://www.linkedin.com/in/andre.olimpio/)

> **Aprenda. Entenda. Construa.**

---

**Objetivo deste material:** ajudar estudantes a avançar da leitura de algoritmos para a compreensão, execução, análise e melhoria de aplicações em Python.


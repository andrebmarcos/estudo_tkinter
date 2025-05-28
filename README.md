# Cadastro de Clientes

Este é um aplicativo desktop simples de **cadastro de clientes**, desenvolvido em **Python** com **Tkinter** para a interface gráfica e **SQLite** como banco de dados local.

## 🖥️ Funcionalidades

- Interface gráfica com campos para nome, telefone, cidade e código.
- Quando clica em Novo, ele abre uma janela de Cadastro.
- Incluso Double Click para selecionar o cliente.
- Incluso a função para deletar clientes.
- Incluso a função alterar clientes.
- Incluso a função buscar clientes.
- Incluso a opção de gerar PDF do cliente.
- Listagem dos clientes cadastrados com ordenação alfabética.
- Limpeza de campos de entrada.
- Banco de dados local persistente (`clientes_teste.db`).
- Interface com botões para futuras funcionalidades como **buscar**, **alterar** e **apagar**.

## 🧰 Tecnologias Utilizadas

- Python 3.x
- Tkinter
- SQLite3

## 📁 Estrutura

```
cadastro_clientes/
│
├── README.md
├── app.py
└── clientes_teste.db (gerado automaticamente após executar)
```

## ▶️ Como Executar

1. Certifique-se de ter o Python instalado (recomendado Python 3.8+).
2. Clone este repositório ou copie o código-fonte.
3. Execute o arquivo principal:

```bash
python app.py
```

O programa abrirá uma janela com a interface gráfica para cadastro de clientes.

## 🔧 Melhorias Futuras


- Validação de campos obrigatórios.
- Exportação de dados para CSV ou PDF.
- Filtro de busca por cidade ou nome.


## 📄 Licença

Este projeto é de código aberto e está sob a licença MIT. Sinta-se livre para usá-lo, modificá-lo e distribuí-lo.

---

Desenvolvido com 💻 por André Marcos.
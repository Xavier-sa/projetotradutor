# README - Projeto Tradutor Inglês-Português

![Capa do Projeto](Xavier-sa/projetotradutor/projeto-tradutor.png)

## 📌 Visão Geral
Este projeto é um dicionário digital simples que permite traduzir palavras entre inglês e português, além de oferecer funcionalidades básicas de CRUD (Create, Read, Update, Delete) para gerenciar o vocabulário.

## ✨ Funcionalidades
- **Tradução bidirecional**: Inglês ⇄ Português
- **Adição de novas palavras** ao dicionário
- **Exclusão de palavras** existentes
- **Listagem completa** de todas as palavras cadastradas
- **Interface web** amigável e responsiva

## 🛠️ Tecnologias Utilizadas
- **Backend**: Python com Flask
- **Frontend**: HTML5, CSS3
- **Armazenamento**: JSON (dicionario.json)
- **Dependências**: Ver requirements.txt

## 🚀 Como Executar o Projeto

### Pré-requisitos
- Python 3.7+
- pip (gerenciador de pacotes Python)

### Instalação
1. Clone o repositório:
   ```bash
   git clone https://github.com/seu-usuario/projetotradutor.git
   cd projetotradutor
   ```

2. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

3. Execute a aplicação:
   ```bash
   python app.py
   ```

4. Acesse no navegador:
   ```
   http://localhost:5000
   ```

## 📂 Estrutura do Projeto
```
projetotradutor/
├── app.py               # Aplicação principal Flask
├── dicionario.json      # Banco de dados de palavras
├── models/
│   ├── model.py         # Lógica de manipulação do dicionário
│   └── __pycache__/
├── static/
│   └── style.css        # Estilos CSS
├── templates/           # Templates HTML
│   ├── adicionar.html
│   ├── excluir.html
│   ├── index.html
│   ├── listar.html
│   └── procurar.html
└── requirements.txt     # Dependências do projeto
```

## 🌟 Recursos Futuros
- [ ] Autenticação de usuários
- [ ] Histórico de consultas
- [ ] Sistema de favoritos
- [ ] API REST para integração
- [ ] Tradução de frases completas

## 🤝 Como Contribuir
1. Faça um fork do projeto
2. Crie uma branch para sua feature (`git checkout -b feature/incrivel`)
3. Commit suas mudanças (`git commit -m 'Adicionando feature incrível'`)
4. Push para a branch (`git push origin feature/incrivel`)
5. Abra um Pull Request

## 📄 Licença
Este projeto está licenciado sob a licença MIT - veja o arquivo [LICENSE](LICENSE) para detalhes.

---

Desenvolvido  por Wellington Xavier 
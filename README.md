# Todo List App 📝

Uma aplicação web simples e elegante para gerenciamento de tarefas, desenvolvida com **Django** e estilizada com **Tailwind CSS**.

Este projeto foi criado para praticar o desenvolvimento Full Stack com Python, focando em boas práticas de design e arquitetura MVC (MVT no Django).

## 🚀 Tecnologias Utilizadas

- **Python 3.12+**
- **Django 6.0**
- **Tailwind CSS** (via CDN)
- **SQLite3**

## ✨ Funcionalidades

- ✅ **Criar Tarefas**: Adicione novas tarefas com título, descrição e data.
- 📋 **Listar Tarefas**: Visualização limpa com indicadores de status (Pendente/Concluída).
- ✏️ **Editar Tarefas**: Atualize detalhes ou marque como concluída.
- 🗑️ **Excluir Tarefas**: Confirmação visual antes de remover itens.


## 📦 Como rodar o projeto

1. **Clone o repositório**
   ```bash
   git clone https://github.com/SeuUsuario/todo-list.git
   cd todo-list
   ```

2. **Crie um ambiente virtual**
   ```bash
   # Cria o ambiente virtual
   python -m venv venv
   # Entra no ambiente virtual 
   source venv/bin/activate  # Linux/Mac
   # ou
   venv\Scripts\activate     # Windows
   ```

3. **Instale as dependências**
   ```bash
   pip install -r requirements.txt
   ```

4. **Aplique as migrações**
   ```bash
   python manage.py migrate
   ```

5. **Rode o servidor**
   ```bash
   python manage.py runserver
   ```

6. Acesse `http://127.0.0.1:8000` no seu navegador.

---
Desenvolvido por [José Amauri] 

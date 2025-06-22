# ✅ Sistema de Gestão de Tarefas com Prioridades - Django

Este é um sistema web de **gestão de tarefas** desenvolvido com Django. Ele permite aos usuários criar, editar, excluir e visualizar tarefas com diferentes **níveis de prioridade** (baixa, média, alta), bem como categorizá-las e associá-las a um perfil de usuário personalizado.

---

## 🚀 Funcionalidades

- ✅ Cadastro de tarefas com:
  - Título e descrição
  - Nível de prioridade: baixa, média ou alta
  - Data limite (prazo)
  - Categoria (opcional)
- 🔔 Marcar tarefas como concluídas
- 👤 Atribuição de tarefas ao usuário logado
- 🗂️ Organização por categorias
- 📅 Registro automático da data de criação
- 👥 Perfil personalizado de usuário com foto, bio e telefone
- 🔐 Integração com o sistema de autenticação do Django
- 📂 Interface web simples com HTML e Django Templates

---

## 🧱 Estrutura do banco de dados

### Modelos principais:

#### ✅ Tarefa
- `titulo`: título da tarefa
- `descricao`: descrição detalhada (opcional)
- `prioridade`: nível de prioridade (`baixa`, `média`, `alta`)
- `concluida`: marca se a tarefa foi finalizada
- `data_criacao`: preenchido automaticamente
- `data_limite`: data limite para conclusão (opcional)
- `categoria`: chave estrangeira para `Categoria` (opcional)
- `usuario`: chave estrangeira para o modelo `User`

#### 🗂️ Categoria
- `nome`: nome da categoria (ex: Trabalho, Estudos, Pessoal)

#### 👤 Perfil
- `nome_completo`: nome do usuario
- `bi`: descrição pessoal (opcional)
- `telefone`: número de telefone (opcional)
- `usuario`: ligação OneToOne com o modelo `User`

---

## 💡 Tecnologias utilizadas

- Python 3
- Django 4+
- SQLite (banco de dados padrão)
- HTML5 + CSS3 (básico)
- Bootstrap (opcional)

---

## ▶️ Como executar o projeto localmente

1. Clone o repositório:
```bash
git clone https://github.com/MiudoKubanza/gestao_de_tarefa.git
cd gestao_de_tarefa
````

2. Crie um ambiente virtual:

```bash
python -m venv venv
django\Scripts\Activate   # No Windows
# ou
source django/bin/activate  # No Linux/macOS
```

3. Instale as dependências:

```bash
pip install -r requirements.txt
```

4. Aplique as migrações:

```bash
python manage.py migrate
```

5. Crie um superusuário para acessar o admin:

```bash
python manage.py createsuperuser
```

6. Inicie o servidor:

```bash
python manage.py runserver
```

7. Acesse no navegador:

```
http://localhost:8000
```

---

## 📷 Capturas de tela (opcional)



---

## 📌 Objetivo

O projeto foi criado com fins educativos e práticos, permitindo entender:

* Como trabalhar com modelos relacionados em Django
* Como usar `choices` para campos como prioridade
* Como implementar autenticação e CRUD completo
* Como personalizar perfis de usuários com modelo extra
* Como organizar dados com categorias

---

## 📄 Licença

Este projeto está sob a licença MIT. Sinta-se livre para usar, modificar e compartilhar!

---

## 🤝 Contribuições

Contribuições são bem-vindas! Se você tiver ideias de melhorias, correções ou novas funcionalidades, sinta-se à vontade para abrir um pull request ou uma issue.

```

<p align="center">
  <a href="" rel="noopener">
 <img width=200px height=200px src="https://cdn-icons-png.freepik.com/512/5441/5441859.png" alt="Project logo"></a>
</p>
<h3 align="center">Agenda de Contactos</h3>
<div align="center">

  [![Status](https://img.shields.io/badge/status-active-success.svg)]()

</div>

---

<p align="center"> Gestor de contactos.
    <br> 
</p>

## 📝 Table of Contents

- [Getting Started](#getting_started)
- [Usage](#usage)
- [Built Using](#built_using)
- [TODO](../TODO.md)
- [Contributing](../CONTRIBUTING.md)
- [Authors](#authors)
- [Acknowledgments](#acknowledgement)


## 🏁 Getting Started <a name = "getting_started"></a>

Para ejecucion local sigan los siguientes pasos:

1. Instalar python 3.12.0. _https://www.python.org/downloads/release/python-3120/_

2. _(Opcional)_ Instalar Pipenv; gestor de entornos virtuales para python. _https://pipenv-es.readthedocs.io/es/latest/install.html#instalando-pipenv_

```bash
  pip install --user pipenv
```
3. Clonar el proyecto.

```bash
  git clone https://github.com/Geronimo-montes/agendaContactos
  cd agendaContactos
```
4. Generar entorno virtual.

```bash
  pipenv install
  pipenv shell # active virtual environment
```
5. Iniciar aplicación Django.

```bash
  python manage.py migrate # Genera la base de datos, para este caso SQLite3
  python manage.py createsuperuser # Necesario ya que la app no tiene registro de usuarios
  python manage.py runserver
```
6. Navegar a la url: `http://127.0.0.1:8000/accounts/login/`



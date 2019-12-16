# Say No More
Web application

## Getting Started
### Directory Structure
- `frontend` contains React app
- `backend` contains all django related files
- `config` contains the django project (run manage.py commands from here)
- `snm_app` contains the backend django application

### Local Dev

#### Starting BE App
- `cd backend`
- `. venv/bin/activate`
- `python manage.py runserver`
- `python manage.py loaddata db.json`
- hit `localhost:8000`

- saving db dump: `python manage.py dumpdata > db.json`

#### Starting FE App
- `cd frontend && npm start`
- hit `localhost:3000`

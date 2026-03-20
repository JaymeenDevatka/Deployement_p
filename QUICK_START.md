# Quick Run Commands

## Start the Project (Fastest Way)

```bash
cd c:\Users\hp\OneDrive\Desktop\Jaymeen Devatka\Projects_new\notes-app\django-notes-app

docker-compose up -d
```

Then open:
- API: http://localhost:8000
- Nginx: http://localhost
- Admin: http://localhost:8000/admin

---

## View Logs

```bash
docker-compose logs -f django_app
```

---

## Stop Everything

```bash
docker-compose down
```

---

## If Docker not available, run locally:

```bash
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

Access at: http://localhost:8000

---

## Test Notes API with curl

```bash
# List all notes
curl http://localhost:8000/api/notes/

# Create a note
curl -X POST http://localhost:8000/api/notes/ \
  -H "Content-Type: application/json" \
  -d '{"title":"My Note","description":"Test note"}'

# Update a note
curl -X PUT http://localhost:8000/api/notes/1/ \
  -H "Content-Type: application/json" \
  -d '{"title":"Updated","description":"New content"}'

# Delete a note
curl -X DELETE http://localhost:8000/api/notes/1/
```

# ===============================================
# Executa as migrações
# ===============================================
python manage.py makemigrations
python manage.py migrate
python manage.py collectstatic --noinput

python manage.py createcachetable

# ===============================================
# Inicializa o sistema
# ===============================================
python manage.py runserver 0.0.0.0:8000

# gunicorn --bind 0.0.0.0:"${APPLICATION_PORT}" maat_backend.wsgi:application \
# --workers "${APPLICATION_WORKERS}" \
# --preload --log-file - --error-logfile -

# ===============================================
# Executa as migrações
# ===============================================
python manage.py makemigrations
python manage.py migrate
python manage.py collectstatic --noinput

python manage.py createcachetable
python manage.py loaddata /app/fixtures/transactiontype.yaml

# ===============================================
# Inicializa o sistema
# ===============================================
gunicorn --bind 0.0.0.0:5000 sales.wsgi:application \
    --workers 2 \
    --preload \
    --log-file - \
    --log-level=info \
    --error-logfile -
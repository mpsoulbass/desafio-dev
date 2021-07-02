# ===============================================
# Executa as migrações
# ===============================================
python manage.py makemigrations
python manage.py migrate
python manage.py collectstatic --noinput

python manage.py createcachetable
python manage loadadata /app/fixtuers/transactiontype.yaml

# ===============================================
# Inicializa o sistema
# ===============================================
gunicorn --bind 0.0.0.0:5000 sales.wsgi:application \
    --workers 2 \
    --preload \
    --log-file - \
    --log-level=debug \
    --error-logfile -
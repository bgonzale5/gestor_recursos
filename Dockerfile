# Problema 1: imagen base antigua con más CVEs acumuladas
FROM python:3.9

# Problema 2: corre como root (implícito, sin USER)
WORKDIR /app

# Problema 3: copia TODO antes de instalar dependencias (sin .dockerignore)
COPY . .

# Problema 4: instala dependencias sin --no-cache-dir (imagen más grande)
RUN pip install -r requirements.txt

# Problema 5: expone puerto de debug
EXPOSE 8000
EXPOSE 5678

# Problema 6: secret hardcodeado en variable de entorno de imagen
ENV SECRET_KEY=django-insecure--o9jb75kz33ywobkg0qy-kisjq957ua \
    DEBUG=True \
    DATABASE_URL=postgres://admin:admin@db:5432/gestor_recursos

# Problema 7: servidor de desarrollo en producción
CMD sh -c "python manage.py migrate && python manage.py runserver 0.0.0.0:8000"

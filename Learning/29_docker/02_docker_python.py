DOCKERIGNORE = '''
__pycache__
*.pyc
.git
.env
venv/
.venv/
'''

MULTI_STAGE = '''
FROM python:3.11 as builder
WORKDIR /app
COPY requirements.txt .
RUN pip install --user -r requirements.txt

FROM python:3.11-slim
WORKDIR /app
COPY --from=builder /root/.local /root/.local
COPY . .
ENV PATH=/root/.local/bin:
CMD [\

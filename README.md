# API Matemática

API RESTful para realizar operações matemáticas de soma e média aritmética de um vetor de inteiros.

## Rotas

### POST `/somar`
Soma os números de uma lista.

### POST `/media`
Calcula a media.

### Executando os testes:**

python -m unittest discover tests

**Request Body:**
```json
{
    "numeros": [1, 2, 3, 4, 5]
}


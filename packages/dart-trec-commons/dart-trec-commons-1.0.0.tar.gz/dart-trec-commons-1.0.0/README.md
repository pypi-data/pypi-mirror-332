# TREC Commons

Common Python code for T-REC

## How to Run

1. Install requeriments
    - `python3 -m venv .venv`
    - `source ./.venv/bin/activate`
    - `pip install -r requirements.txt`
   
2. Config parameters
    - `cp pytest.ini.example pytest.ini`
    - fill pytest.ini

3. Run tests
    - `make test`

## How to Setup

All application variables to test are exposed in `.pytest.ini`:

- Learner Options:

    | Option | Description |
    |--------|-------------|
    | LEARNER_DAYS_INTERVAL | Learner interval in days |

- Connection Options:

    | Option | Description |
    |--------|-------------|
    | MONGODB_URI | Mongo URI (without database name) |
    | MINIO_HOST | MinIO host (without http://) |
    | MINIO_ACCESS_KEY | MinIO Key |
    | MINIO_SECRET_KEY | MinIO Secret |
    | MINIO_RECOMMENDER_BUCKET | MinIO recommender bucket |


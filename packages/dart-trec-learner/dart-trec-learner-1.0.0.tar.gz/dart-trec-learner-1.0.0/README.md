# TREC Learner

For production config, set ENV to production

## How to Run

1. Install requeriments
    - `python3 -m venv .venv`
    - `source ./.venv/bin/activate`
    - `pip install -r requirements.txt`
   
2. Config parameters
    - `cp .env.example .env`
    - `cp pytest.ini.example pytest.ini`
    - fill .env and pytest.ini

3. Run learner
    - `./run.sh`

## How to Setup

All application variables are exposed in `src/config.py`. Container variables are exposed in `.env`:

- Learner Options:

    | Option | Description |
    |--------|-------------|
    | LEARNER_DAYS_INTERVAL | Learner interval in days |
    | LEARNER_ROOT_MODEL_DIR | Temporary root dir used during trainning |
    | LEARNER_MODEL_DIR | Temporary dir used store model files |

- Connection Options:

    | Option | Description |
    |--------|-------------|
    | MONGODB_URI | Mongo URI (without database name) |
    | MONGODB_DATABASE | Mongo database with PLM data |
    | MONGODB_COLLECTION | Mongo collection with issue-document data |
    | MINIO_HOST | MinIO host (without http://) |
    | MINIO_ACCESS_KEY | MinIO Key |
    | MINIO_SECRET_KEY | MinIO Secret |
    | MINIO_RECOMMENDER_BUCKET | MinIO recommender bucket |

- Scheduler Options:

    | Option | Description |
    |--------|-------------|
    | JOB_FREQUENCY | Frequency to run job _(seconds interval for dev mode)_ |
    | JOB_FREQUENCY | Frequency to run job _(hour of day for production mode)_ |

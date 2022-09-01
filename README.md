# Feast-Example
Simple Feast example for undertanding how communication between Feature Store and Data Science teams would work.

Not suitable for production deployment as is.

Example infrastructure:
- Registry: postgres database
- Online store: Redis
- Offline store: postgres database

Dataset example taken from:
https://kedion.medium.com/creating-a-feature-store-with-feast-part-1-37c380223e2f

1. Run containers:
`docker compose up --build`

2. Populate example data:

2.1. Build image from /breast_cancer/Dockerfile:
`docker build -t breast_cancer_example ./breast_cancer/Dockerfile`

2.2. Run example container:
`docker run --network feast-example_feast-net breast_cancer_example`

3. Feast apply to create features inside repository:
`docker-compose run feast-core sh -c 'feast apply'`

4. Create your python-env

5. Install dependencies from /breast_cancer/requirements.txt

6. Run example from breast_cancer/ds_test.py

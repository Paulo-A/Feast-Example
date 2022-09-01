import pandas as pd
from sqlalchemy import create_engine, schema as saschema

engine = create_engine('postgresql://postgres:mypasswd@pg-host:5432/')

schema_name = 'feast'
table_name1 = 'data_df1'
table_name2 = 'data_df2'
table_name3 = 'data_df3'
table_name4 = 'data_df4'
table_target = 'target_df'
if not engine.dialect.has_schema(engine, schema_name):
    engine.execute(saschema.CreateSchema(schema_name))

engine.execute(f'DROP TABLE IF EXISTS {schema_name}.{table_name1};')
engine.execute(f'CREATE TABLE {schema_name}.{table_name1}(\
        "mean radius" float,\
        "mean texture" float,\
        "mean perimeter" float,\
        "mean area" float,\
        "mean smoothness" float,\
        "event_timestamp" timestamp without time zone,\
        "patient_id" bigint PRIMARY KEY\
    )'
)

engine.execute(f'DROP TABLE IF EXISTS {schema_name}.{table_name2};')
engine.execute(f'CREATE TABLE {schema_name}.{table_name2}(\
        "mean compactness" float,\
        "mean concavity" float ,\
        "mean concave points" float,\
        "mean symmetry" float,\
        "mean fractal dimension" float,\
        "event_timestamp" timestamp without time zone,\
        "patient_id" bigint PRIMARY KEY\
    )'
)

engine.execute(f'DROP TABLE IF EXISTS {schema_name}.{table_name3};')
engine.execute(f'CREATE TABLE {schema_name}.{table_name3}(\
        "radius error" float,\
        "texture error" float,\
        "perimeter error" float,\
        "area error" float,\
        "smoothness error" float,\
        "compactness error" float,\
        "concavity error" float,\
        "event_timestamp" timestamp without time zone,\
        "patient_id" bigint PRIMARY KEY\
    )'
)

engine.execute(f'DROP TABLE IF EXISTS {schema_name}.{table_name4};')
engine.execute(f'CREATE TABLE {schema_name}.{table_name4}(\
        "concave points error" float,\
        "symmetry error" float,\
        "fractal dimension error" float,\
        "worst radius" float,\
        "worst texture" float,\
        "worst perimeter" float,\
        "worst area" float,\
        "worst smoothness" float,\
        "worst compactness" float,\
        "worst concavity" float,\
        "worst concave points" float,\
        "worst symmetry" float,\
        "worst fractal dimension" float,\
        "event_timestamp" timestamp without time zone,\
        "patient_id" bigint PRIMARY KEY\
    )'
)

engine.execute(f'DROP TABLE IF EXISTS {schema_name}.{table_target};')
engine.execute(f'CREATE TABLE {schema_name}.{table_target}(\
        "target" bigint,\
        "event_timestamp" timestamp without time zone,\
        "patient_id" int PRIMARY KEY\
    )'
)

df = pd.read_csv('./data/data_df1.csv')
df.to_sql('data_df1', engine, index=False, schema=schema_name, if_exists='append')

df = pd.read_csv('./data/data_df2.csv')
df.to_sql('data_df2', engine, index=False, schema=schema_name, if_exists='append')

df = pd.read_csv('./data/data_df3.csv')
df.to_sql('data_df3', engine, index=False, schema=schema_name, if_exists='append')

df = pd.read_csv('./data/data_df4.csv')
df.to_sql('data_df4', engine, index=False, schema=schema_name, if_exists='append')

df = pd.read_csv('./data/target_df.csv')
df.to_sql('target_df', engine, index=False, schema=schema_name, if_exists='append')

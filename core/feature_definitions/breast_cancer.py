# Importing dependencies
from datetime import timedelta
from feast.infra.offline_stores.contrib.postgres_offline_store.postgres_source import (
    PostgreSQLSource,
)
from feast import Entity, Field, FeatureView, FeatureStore, FeatureService
from feast.types import Float32, Int32

store = FeatureStore(repo_path="./")

# Declaring an entity for the dataset
patient = Entity(
    name="patient_id", 
    description="The ID of the patient")

# Declaring the source of the first set of features
f_source1 = PostgreSQLSource(
    name="data_df1",
    query="SELECT * FROM feast.data_df1",
    timestamp_field="event_timestamp",
    created_timestamp_column="created_timestamp",
)

# Defining the first set of features
df1_fv = FeatureView(
    name="df1_feature_view",
    ttl=timedelta(seconds=86400 * 3),
    entities=[patient],
    schema=[
        Field(name="mean radius", dtype=Float32),
        Field(name="mean texture", dtype=Float32),
        Field(name="mean perimeter", dtype=Float32),
        Field(name="mean area", dtype=Float32),
        Field(name="mean smoothness", dtype=Float32)
        ],    
    source=f_source1
)

# Declaring the source of the second set of features
f_source2 = PostgreSQLSource(
    name="data_df2",
    query="SELECT * FROM feast.data_df2",
    timestamp_field="event_timestamp",
    created_timestamp_column="created_timestamp",
)

# Defining the second set of features
df2_fv = FeatureView(
    name="df2_feature_view",
    ttl=timedelta(seconds=86400 * 3),
    entities=[patient],
    schema=[
        Field(name="mean compactness", dtype=Float32),
        Field(name="mean concavity", dtype=Float32),
        Field(name="mean concave points", dtype=Float32),
        Field(name="mean symmetry", dtype=Float32),
        Field(name="mean fractal dimension", dtype=Float32)
        ],    
    source=f_source2
)

# Declaring the source of the third set of features
f_source3 = PostgreSQLSource(
    name="data_df3",
    query="SELECT * FROM feast.data_df3",
    timestamp_field="event_timestamp",
    created_timestamp_column="created_timestamp",
)

# Defining the third set of features
df3_fv = FeatureView(
    name="df3_feature_view",
    ttl=timedelta(seconds=86400 * 3),
    entities=[patient],
    schema=[
        Field(name="radius error", dtype=Float32),
        Field(name="texture error", dtype=Float32),
        Field(name="perimeter error", dtype=Float32),
        Field(name="area error", dtype=Float32),
        Field(name="smoothness error", dtype=Float32),
        Field(name="compactness error", dtype=Float32),
        Field(name="concavity error", dtype=Float32)
        ],    
    source=f_source3
)

# Declaring the source of the fourth set of features
f_source4 = PostgreSQLSource(
    name="data_df4",
    query="SELECT * FROM feast.data_df4",
    timestamp_field="event_timestamp",
    created_timestamp_column="created_timestamp",
)

# Defining the fourth set of features
df4_fv = FeatureView(
    name="df4_feature_view",
    ttl=timedelta(seconds=86400 * 3),
    entities=[patient],
    schema=[
        Field(name="concave points error", dtype=Float32),
        Field(name="symmetry error", dtype=Float32),
        Field(name="fractal dimension error", dtype=Float32),
        Field(name="worst radius", dtype=Float32),
        Field(name="worst texture", dtype=Float32),
        Field(name="worst perimeter", dtype=Float32),
        Field(name="worst area", dtype=Float32),
        Field(name="worst smoothness", dtype=Float32),
        Field(name="worst compactness", dtype=Float32),
        Field(name="worst concavity", dtype=Float32),
        Field(name="worst concave points", dtype=Float32),
        Field(name="worst symmetry", dtype=Float32),
        Field(name="worst fractal dimension", dtype=Float32),        
        ],    
    source=f_source4
)

# Declaring the source of the targets
target_source = PostgreSQLSource(
    name="target_df",
    query="SELECT * FROM feast.target_df",
    timestamp_field="event_timestamp",
    created_timestamp_column="created_timestamp",
)

# Defining the targets
target_fv = FeatureView(
    name="target_feature_view",
    entities=[patient],
    ttl=timedelta(seconds=86400 * 3),
    schema=[
        Field(name="target", dtype=Int32)        
        ],    
    source=target_source
)

df_fs = FeatureService(
    name="df_feature_service",
    features=[
        df1_fv,
        df2_fv,
        df3_fv,
        df4_fv
    ],
)

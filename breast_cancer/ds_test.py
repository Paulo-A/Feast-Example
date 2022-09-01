from sqlalchemy import create_engine
from feast import FeatureStore
import pandas as pd

store = FeatureStore(repo_path="./")
engine = create_engine('postgresql://postgres:mypasswd@localhost:5432/')
entity_df = pd.read_sql('select * from feast.target_df', engine)

training_data = store.get_historical_features(
    entity_df=entity_df,
    features=[
        "df1_feature_view:mean radius",
        "df1_feature_view:mean texture",
        "df1_feature_view:mean perimeter",
        "df1_feature_view:mean area",
        "df1_feature_view:mean smoothness",
        "df2_feature_view:mean compactness",
        "df2_feature_view:mean concavity",
        "df2_feature_view:mean concave points",
        "df2_feature_view:mean symmetry",
        "df2_feature_view:mean fractal dimension",
        "df3_feature_view:radius error",
        "df3_feature_view:texture error",
        "df3_feature_view:perimeter error",
        "df3_feature_view:area error",
        "df3_feature_view:smoothness error",
        "df3_feature_view:compactness error",
        "df3_feature_view:concavity error",
        "df4_feature_view:concave points error",
        "df4_feature_view:symmetry error",
        "df4_feature_view:fractal dimension error",
        "df4_feature_view:worst radius",
        "df4_feature_view:worst texture",
        "df4_feature_view:worst perimeter",
        "df4_feature_view:worst area",
        "df4_feature_view:worst smoothness",
        "df4_feature_view:worst compactness",
        "df4_feature_view:worst concavity",
        "df4_feature_view:worst concave points",
        "df4_feature_view:worst symmetry",
        "df4_feature_view:worst fractal dimension"
    ]
)

print(training_data.to_df())

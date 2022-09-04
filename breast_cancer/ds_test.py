from sqlalchemy import create_engine
from feast import FeatureStore
import pandas as pd

store = FeatureStore(repo_path="./")
engine = create_engine('postgresql://postgres:mypasswd@localhost:5432/')
entity_df = pd.read_sql('select * from feast.target_df', engine)

features = store.get_feature_service("df_feature_service")

training_data = store.get_historical_features(
    entity_df=entity_df,
    features=features
)

print(training_data.to_df())

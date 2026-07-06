from src.monitoring.statistics import (
    get_training_data,
    get_production_data
)

train_df = get_training_data()
prod_df = get_production_data()

print("Training Shape:")
print(train_df.shape)

print()

print("Production Shape:")
print(prod_df.shape)
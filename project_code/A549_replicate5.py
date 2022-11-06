import pandas as pd
import json
import xgboost as xgb
from xgboost import XGBClassifier
from sklearn.preprocessing import StandardScaler

# Data Parsing
database = []
for line in open("SGNex_A549_directRNA_replicate5_run1/data.json",'r'):
        data = json.loads(line)
        a = list(data.keys())[0]
        b = list(data[a].keys())[0]
        database.append(
            [
            a,
            b,
            list(data[a][b].values())[0]
            ]
        )


df = pd.DataFrame(database, columns = ['transcriptId','transcriptPosition','value'])

df_exploded = df.explode('value').reset_index(drop=True)


df_flat = pd.concat([df_exploded.drop(columns = 'value'),
    pd.DataFrame(df_exploded['value'].to_list(),columns=['v1','v2','v3','v4','v5','v6','v7','v8','v9'])],
    axis = 1
    )

# Aggregate data
final_data = df_flat.groupby(['transcriptId', 'transcriptPosition'], as_index=False).mean()

# Scaling data
scaler = StandardScaler()
x_test = final_data.drop(columns = ['transcriptId', 'transcriptPosition'])
x_scaled = scaler.fit_transform(x_test.to_numpy())
x_scaled = pd.DataFrame(x_scaled, columns = ['v1','v2','v3','v4', 'v5', 'v6', 'v7', 'v8', 'v9'])

# Load trained model
model2 = xgb.XGBClassifier()
model2.load_model("model.json")

# predict probability and values
pred_value_test = model2.predict(x_scaled)
pred_prob_test = model2.predict_proba(x_scaled)[:,1]

# prediction results
results = pd.concat([final_data.iloc[:,:2], pd.DataFrame(pred_prob_test, columns = ['prob_score']), pd.DataFrame(pred_value_test, columns = ['value_score']), x_test], axis=1)
results.to_csv("A549_replicate5.csv", index=False)

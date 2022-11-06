# import packages
import json
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from xgboost import XGBClassifier


# data parsing
database = []
for line in open("test-dataset.json",'r'): # read input file line by line
    data = json.loads(line)
    a = list(data.keys())[0] # Transcript ID
    b = list(data[a].keys())[0] # Transcript position
    database.append(
        [
         a,
         b,
         list(data[a][b].values())[0] # nested listed of feature values
        ]
    )

df = pd.DataFrame(database, columns = ['transcriptId','transcriptPosition','value']) 

# explode function on the value column to retrieve each element of the nested list as a new row (as 1 list)
df_exploded = df.explode('value').reset_index(drop=True) 

df_flat = pd.concat([df_exploded.drop(columns = 'value'),
    pd.DataFrame(df_exploded['value'].to_list(),columns=['v1','v2','v3','v4','v5','v6','v7','v8','v9'])],
    # value column is still a list which we then explode it column-wise
    axis = 1
    )

# data preprocessing
df_flat.rename(columns={'transcriptId': 'transcript_id', 'transcriptPosition': 'transcript_position'}, inplace=True)

test_df_grped = df_flat.groupby(['transcript_id', 'transcript_position'], as_index=False).mean()

# scaling
scaler = StandardScaler()
test_df_scaled = scaler.fit_transform(test_df_grped.iloc[:,2:].to_numpy())
test_df_scaled = pd.DataFrame(test_df_scaled, columns=[
  'v1','v2','v3','v4', 'v5', 'v6', 'v7', 'v8', 'v9'])

# Run trained model on test dataset
xgb_clf = XGBClassifier()
xgb_clf.load_model("XGboostModel.json")

pred_prob_test = xgb_clf.predict_proba(test_df_scaled)[:,1] # change x test to dataset1 and 2, finaldata without last 4 columns
pred_value_test = xgb_clf.predict(test_df_scaled) 

test_results = pd.concat([test_df_grped .iloc[:,:2], pd.DataFrame(pred_prob_test)], axis = 1)
test_results = test_results.rename(columns={0:'score'})

#save results
test_results.to_csv("jaly_test_results.csv", index = False)

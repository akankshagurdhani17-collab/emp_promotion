from sklearn.tree import DecisionTreeClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import pandas as pd
import pickle

df=pd.read_csv(r"D:\PYCHARM\emp_promotion_prediction (1).csv")
 #
 # 'Education', 'ExperienceYears', 'Performance', 'Salary',
 #       'Department', 'Promoted'

le=LabelEncoder()
df['Education']=le.fit_transform(df.Education)
df['Performance']=le.fit_transform(df.Performance)
df['Department']=le.fit_transform(df.Department)
df['Promoted']=le.fit_transform(df.Promoted)

x=df[['Education', 'ExperienceYears', 'Performance', 'Salary','Department']]
y=df['Promoted']

x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=42)

model=DecisionTreeClassifier()
model.fit(x_train,y_train)

y_pred=model.predict(x_test)
accuracy=accuracy_score(y_test,y_pred)
print(accuracy*100)


fh=open('model.pkl','wb')
pickle.dump(model,fh)
fh.close()
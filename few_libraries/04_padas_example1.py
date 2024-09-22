#total marks of topper using pandas
import pandas as pd
scores=pd.read_csv("Scores.csv")

# print(scores.shape)
# print(scores.count())
# print(scores["Total"].sort_values())
# print(scores["Total"].mean())
# print(scores["Total"].max())
# print(scores["Total"].min())

# print(scores,type(scores))
# print(scores['Name'],type(scores['Name']))

# print(scores.head())
# print(scores.tail())

# print(scores[scores["Name"]=="Nisha"])

# print(scores[scores['Gender']=="M"]["Total"].max())
# print(scores[scores['Gender']=="F"]["Total"].max())

# print(scores[scores["Physics"]>85])
# print(scores[scores["Physics"]>85][scores["Mathematics"]>90])

# print(scores[scores["Physics"].between(90,100)].shape[0])
# print(scores[scores["Physics"].between(80,90)].shape[0])
# print(scores[scores["Physics"].between(70,80)].shape[0])
# print(scores[scores["Physics"]<80].shape[0])

subject=["Mathematics","Physics","Chemistry"]
# for sub in subject:
#     print("Above Average in",sub)
#     avg=scores[sub].mean()
#     print(scores[(scores["Gender"]=="F") & (scores[sub]>avg)].shape[0])
#     print(scores[(scores["Gender"]=="M") & (scores[sub]>avg)].shape[0])

# print(scores.groupby("Gender").groups)

for sub in subject:
    print("Above Average in",sub)
    avg=scores[sub].mean()
    print(scores[scores[sub]>avg].groupby("Gender").groups)
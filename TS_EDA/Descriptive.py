import pandas as pd
class Descriptive():
    def init(self):
        pass
    def segreQuanQual(self,dataset):
        quantative=[]
        qualtative=[]

        for i in dataset.columns:
  
            if(dataset[i].dtypes =='object'):
                qualtative.append(i)
            else:
                quantative.append(i)
        print("The Quantitative Data:",quantative)
        print("The Qualtitative Data",qualtative)
        return quantative,qualtative

    def descriptive_Analysis(self,dataset, quantative):
        import pandas as pd
        
        des_data = pd.DataFrame(
            index=["Null_count","NonNull_count","Total_Count","Mean","Median","Mode",
                   "Std","Min","Q1:25%","Q2:50%","Q3:75%","Q4:100%","IQR",
                   "1.5Rule","Lesser","Greater"],
            columns=quantative
        )
    
        for col in quantative:
            desc = dataset[col].describe()
    
            des_data.loc["Null_count", col] = dataset[col].isnull().sum()
            des_data.loc["NonNull_count", col] = dataset[col].count()
            des_data.loc["Total_Count", col] = len(dataset[col])
            des_data.loc["Mean", col] = dataset[col].mean()
            des_data.loc["Median", col] = dataset[col].median()
            des_data.loc["Mode", col] = dataset[col].mode()[0] if not dataset[col].mode().empty else None
            des_data.loc["Std", col] = desc["std"]
            des_data.loc["Min", col] = desc["min"]
            des_data.loc["Q1:25%", col] = desc["25%"]
            des_data.loc["Q2:50%", col] = desc["50%"]
            des_data.loc["Q3:75%", col] = desc["75%"]
            des_data.loc["Q4:100%", col] = desc["max"]
    
            # IQR calculations
            IQR = desc["75%"] - desc["25%"]
            des_data.loc["IQR", col] = IQR
            des_data.loc["1.5Rule", col] = 1.5 * IQR
            des_data.loc["Lesser", col] = desc["25%"] - (1.5 * IQR)
            des_data.loc["Greater", col] = desc["75%"] + (1.5 * IQR)
    
        return des_data

    
    def outliercolumn(self,quantative,des_data):
        lesser=[]
        greater=[]

        for i in quantative:
            if(des_data[i]["Lesser"]>des_data[i]['Min']):
                lesser.append(i)
            if(des_data[i]['Greater']<des_data[i]['Q4:100%']):
                greater.append(i)

        print("Lesser Range",lesser)
        print("Greater Range",greater)
        return lesser,greater

    def changeoutlier(self,dataset,des_Data,lesser,greater):
        for i in lesser:
            dataset[i][dataset[i]<des_Data[i]['Lesser']]=des_Data[i]['Lesser']
        #print(dataset[i])
        for j in greater:
            dataset[j][dataset[j]>des_Data[j]['Greater']]=des_Data[j]['Greater']
        return des_Data
    
import pandas as pd
import openpyxl
data = pd.read_excel('lab_pi_101.xlsx')
count = data.shape[0] 
count1 = data["Группа"].str.contains("ПИ101").sum()
gr_pi = data[data["Группа"]=="ПИ101"]
st_pi = len(gr_pi["Личный номер студента"].unique())
zachetka = data.loc[data["Группа"]=="ПИ101","Личный номер студента"].unique()
zachetki = ",".join(map(str,zachetka))
control = data["Уровень контроля"].unique()
control1 = ",".join(map(str,control))
god = data["Год"].unique()
god1 = ",".join(map(str,god))
print("В исходном датасете содержалось",count,"оценок, из них",count1,"оценок относятся к группе ПИ101","\nВ датасете находятся оценки",st_pi,"студентов со следующими личными номерами:",zachetki,"\nИспользуемые формы контроля:",control1,"\nДанные представлены по следующим учебным годам:",god1)
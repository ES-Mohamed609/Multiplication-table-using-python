import pandas as pd # type: ignore


data = []


for i in range(2,6):
        data.append([f"Multiplication table for the number {i}", "", ""])
        for j in range(1, 13):
            data.append([i, j, i * j])
        data.append(["", "", ""])   

#convert data to dataframe to put it in exel file
df = pd.DataFrame(data, columns=["the number", "multiple", "The result"])

#PUT THE DATA IN EXEL FILE
df.to_excel("multiplication.xlsx", index=False, sheet_name="multible table")

print("Excel file created successfully")



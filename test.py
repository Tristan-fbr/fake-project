a = 1
b = 2
print(a+b)


import pandas as pd
import numpy as np

def find_employees(employee: pd.DataFrame) -> pd.DataFrame:
    rich_employee = []

    for i in range(employee.shape[0]):
        manager_id = employee.at[i, 'managerId']

        if pd.isna(manager_id):
            print(f"Employé {employee.at[i, 'name']} n'a pas de manager (managerId est null).")
            continue  # Passer au prochain employé si manager_id est null

        if 0 <= manager_id < employee.shape[0]:
            print(f"Comparaison pour {employee.at[i, 'name']} avec manager {manager_id}.")
            print(f"Salaire employé: {employee.at[i, 'salary']}, Salaire manager: {employee.at[manager_id, 'salary']}.")
            
            if employee.at[i, 'salary'] > employee.at[manager_id, 'salary']:
                print(f"{employee.at[i, 'name']} gagne plus que son manager.")
                rich_employee.append(employee.at[i, 'name'])

    return pd.DataFrame({'Employee': rich_employee})


data = {'id': [1, 2, 3,4, 5],
    'name': ['Alice', 'Bob', 'Charlie', 'David', 'Léa'],
    'salary': [70000, 50000, 60000, 80000, 82],
    'managerId': [3, 3, 4, None, 5]  # David n'a pas de manager (None)
}
df = pd.DataFrame(data)

df.head()

result = find_employees(df)
print(result)


df2 = pd.DataFrame()
df2 = df.merge(df, left_on = "managerId", right_on = "id", how = "inner")


df2 = df2[df2['salary_y'] < df2['salary_x']][['name_x']]
df2.rename(columns={'name_y':'Employee'},inplace = True)
df2.head()


data = {
    "id": [1, 2, 3, 4, 5],
    "name": ["Alice", "Bob", "Alice", "Charlie", "Bob"],
    "salary": [70000, 50000, 70000, 60000, 50000],
}

df = pd.DataFrame(data)

df.head()
df2 = df.drop_duplicates(subset= 'name')
df2.head()

df3 = df['name'].drop_duplicates()
df3.head()

import pandas as pd 
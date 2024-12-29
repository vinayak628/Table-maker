from prettytable import PrettyTable

# CREATION THE TABLE
table=PrettyTable()


# TAKING COLUMNS AS INPUT FROM THE USER
columns=input("Enter the column names separated by commas:").split(",")
table.field_names=[col.strip() for col in columns]


# CREATION OF ROWS FOR N COLUMNS
while True:

    rows=input(f"ENTER DONE TO EXIT \nEnter the values for {len(columns)} columns separated by comma: ")

# IF USER TYPE "DONE"  THEN YOU EXIT THE TABLE
    if rows.lower()=="done":
        break
    row_val=rows.split(",")

# FILLING THE ROW VALUES 
    table.add_row([value.strip() if value.strip() else "-" for value in row_val])


# DISPLAY THE TABLE
print("---Generated Table---")
print(table)
# Напишите функцию print_operation_table(operation, num_rows=6, num_columns=6), 
# которая принимает в качестве аргумента функцию, вычисляющую элемент по номеру строки и столбца. 
# Аргументы num_rows и num_columns указывают число строк и столбцов таблицы, которые должны быть распечатаны. 
# Нумерация строк и столбцов идет с единицы.

def PrintOperationTable(operation, numRows = 6, numColumns = 6):
    if operation(1,1)==2:
        print(1,end='\t')

    for row in range(1, numRows+1):
        for column in range(1, numColumns+1):
            if operation(1,1)==2:
                column -= 1
            print(operation(row,column), end='\t')
        print()

PrintOperationTable(lambda x,y: x*y)


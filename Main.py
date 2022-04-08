import csv
from prettytable import PrettyTable


def read_user_command(usr_comm):
    params = usr_comm.split(" ")
    return params


def join_columns(jp: list, fi1: list, fi2: list):  # jp - join_params, fh - file_headers, f1/2r - file 1/2 reader
    join = jp[4]  # type of joining
    specified_column = jp[3]
    join_type = {
        1: "left",
        2: "right",
        3: "inner"
    }

    if join in join_type:
        print("Specified type of joining: {}".format(join))

    # Setting all the needed parameters, common for all the joining types
    index = 0
    index2 = 0
    column_f1 = []
    column_f2 = []

    # default values for readers
    reader1 = fi1[0]
    reader2 = fi2[0]

    if join == "left" or join == "inner":
        reader1 = fi1[2]
        reader2 = fi2[2]
    elif join == "right":
        reader1 = fi2[2]
        reader2 = fi1[2]

    # Creating table of elements from file 1
    table = []
    for el in reader1:
        table.append(el)

    # Creating table of elements from file 2
    table2 = []
    for el2 in reader2:
        table2.append(el2)

    # 2) Compare file 1 with file 2 considering column specified by the user
    for j in range(len(table[0])):
        if table[0][j] == specified_column:
            index = j
            break

    # Creates a single specified column of elements from file 1
    for n in range(len(table)):
        column_f1.append(table[n][index])

    # For second table
    for k in range(len(table2[0])):
        if table2[0][k] == specified_column:
            index2 = k
            break

    for o in range(len(table2)):
        column_f2.append(table2[o][index2])

    # Algorythm for joining types "right" or "left"
    if join == "left" or join == "right":

        # Creating new table 3 which contains all rows of table 2 sorted due to specified column
        table3 = []
        null_row = len(table2[:][0]) * ["NULL"]

        for el_c1 in range(len(column_f1)):
            for el_c2 in range(len(column_f2)):
                if column_f1[el_c1] == column_f2[el_c2]:
                    table3.append(table2[el_c2][:])
                    break
                elif (el_c2 == len(column_f2) - 1) & (column_f1[el_c1] != column_f2[el_c2]):
                    table3.append(null_row)
                    continue

        table_output = table[:][:]
        for t_rows in range(len(table_output)):
            table_output.insert(2 * t_rows + 1, table3[t_rows][:])

        pt = PrettyTable()

        print("JOINING COMPLETED! \nOUTPUT TABLE: \n")
        for it in range(1, len(table_output), 2):
            pt.add_row(table_output[it - 1] + table_output[it])

        print(pt)

    elif join == "inner":
        table_output = []
        for el_c1 in range(len(column_f1)):
            for el_c2 in range(len(column_f2)):
                if column_f1[el_c1] == column_f2[el_c2]:
                    table_output.append(table[el_c1][:] + table2[el_c2][:])
                    break

        pt = PrettyTable()
        print("\nJOINING COMPLETED! \nOUTPUT TABLE: \n")

        for it in range(len(table_output)):
            pt.add_row(table_output[it])
        print(pt)

    else:
        print("No such type")


while True:
    print("Enter the command:\nq - quit\nh - help\nJoin typing [join file_path file_path column_name join_type] ")
    user_command = str(input("Command: "))
    if user_command == 'q' or user_command == 'Q':
        quit()
        exit()
    elif user_command == 'h' or user_command == 'H':
        print('\n######################### HELP ##########################'
              '\n#    List of available commands:                        #'
              '\n#  q - quit program                                     #'
              '\n#  h - help                                             #'
              '\n#  Start joining two csv files with command:            #'
              '\n#  [join file_path file_path column_name join_type]     #'
              '\n#    where:                                             #'
              '\n#  join - command  file_path column_name join_type      #'
              '\n#  file_path - absolute/relative path to file 1/2       #'
              '\n#  column_name - name a column You wish to use  to      #'
              '\n#                join the files                         #'
              '\n#  join_type - choose one of: right, left or inner      #'
              '\n#########################################################\n')
        continue
    else:
        try:
            join_params = read_user_command(user_command)
            if join_params[0] != "join":
                print("No such commend! ")

            path1 = join_params[1]
            path2 = join_params[2]

            with open(path1, newline='', encoding='utf-8') as f1, open(path2, newline='', encoding='utf-8') as f2:
                rd1 = csv.reader(f1, delimiter=';', quotechar='|')
                rd2 = csv.reader(f2, delimiter=';', quotechar='|')
                dict1 = csv.DictReader(f1, 'r', delimiter=";")
                dict2 = csv.DictReader(f2, 'r', delimiter=";")

                headers = [dict1.fieldnames, dict2.fieldnames]
                dicts = [dict1, dict2]
                readers = [rd1, rd2]

                file1 = [headers[0], dicts[0], readers[0]]
                file2 = [headers[1], dicts[1], readers[1]]

                join_columns(join_params, file1, file2)

                f1.close()
                f2.close()
        except ValueError:
            print("\nERROR: Invalid input!\n")
            continue
        except BaseException:
            print("\nERROR: Unexpected error has occurred. Please try again\n")
            continue

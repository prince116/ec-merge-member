# Created by Prince at 09.11.2021
# Feature: Generate sp for duplicate member support task

import os
import re
import datetime


def writeToFile(output_filename: str, line: str):
    with open(output_filename, 'a', encoding='UTF-8') as file:
        file.write(line + "\n")


def main():
    filename: str = "input.txt"
    x = datetime.datetime.now()
    output_filename: str = "output_" + x.strftime("%Y%m%d_%H%M%S") + ".txt"

    if not os.path.exists(filename):
        print(filename + " does not exist.")
        return

    with open(filename, 'r', encoding='UTF-8') as file:
        for line in file:
            if line != "image.png\n":
                if line.count(",") == 1 and line.count(".") == 0:
                    the_string = re.sub(r"[^,]*$", "", line)
                    the_string = the_string.replace(",", "")
                    the_string = the_string.replace("開多左會員號", ",")
                    the_string = re.sub(r"^[^\)]*", "", the_string)
                    the_string = the_string.replace(")", "")
                    the_string = the_string.replace(" ", "")
                    columns = the_string.split(",")

                    the_line: str = "-- " + line.replace("\n", "")
                    sql: str = "exec sp_void_duplicate_member2 '" + columns[0] + "','" + columns[1] + "', 1"

                    writeToFile(output_filename, the_line)
                    writeToFile(output_filename, sql)

                    print("SQL: " + sql)

                else:
                    the_line: str = "-- " + line.replace("\n\n", "")

                    writeToFile(output_filename, "\n-- Manual Handle")
                    writeToFile(output_filename, the_line)


if __name__ == "__main__":
    main()

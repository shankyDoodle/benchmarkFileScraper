import csv
import os
from fnmatch import fnmatch

csv_file_name = "ipcStats.csv"
fields = ["Benchmark", "Total IPC", "User Level IPC", "Kernel Level IPC"]

root = '/Users/shankydoodle/Technovanza/RA_WORK/Benchmarks_Data/MarssBenchmarks'
pattern = "*.log"


def fun():
    with open(csv_file_name, mode='w') as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=fields)
        writer.writeheader()

        for path, subdirs, files in os.walk(root):
            for name in files:
                if fnmatch(name, pattern):
                    filepath = os.path.join(path, name)
                    row = dict()
                    row[fields[0]] = name[:-4]

                    with open(filepath) as fp:
                        line = fp.readline()
                        cnt = 1
                        while line:
                            if "total.base_machine.ooo_0_0.thread0.commit.ipc" in line:
                                row[fields[1]] = float(line.split("=")[1])
                            elif "user.base_machine.ooo_0_0.thread0.commit.ipc" in line:
                                row[fields[2]] = float(line.split("=")[1])
                            elif "kernel.base_machine.ooo_0_0.thread0.commit.ipc" in line:
                                row[fields[3]] = float(line.split("=")[1])

                            line = fp.readline()
                            cnt += 1

                    writer.writerow(row)


fun()

import csv
import os
from fnmatch import fnmatch

csv_file_name = "cacheStats.csv"
fields = ["Benchmark", "L1_I_hit_rate", "L1_D_hit_rate", "L2_hit_rate"]

root = '/Users/shankydoodle/Technovanza/RA_WORK/Benchmarks_Data/MarssBenchmarks'
pattern = "*.stats"


def fun():
    with open(csv_file_name, mode='w') as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=fields)
        writer.writeheader()

        machine_count = 0

        hit_word_count = 0
        read_word_count = 0
        write_word_count = 0

        l1_i_hit = 0
        l1_i_miss = 0

        l1_d_hit = 0
        l1_d_miss = 0

        l2_hit = 0
        l2_miss = 0
        for path, subdirs, files in os.walk(root):
            for name in files:
                if fnmatch(name, pattern):
                    filepath = os.path.join(path, name)

                    with open(filepath) as fp:
                        line = fp.readline()
                        cnt = 1
                        while line:
                            if "L1_I_0:" in line:
                                machine_count = machine_count + 1
                            if machine_count == 3:

                                if "hit:" in line:
                                    hit_word_count = hit_word_count + 1
                                    if 2 <= hit_word_count <= 3:
                                        val = float(line.strip("hit: "))
                                        l1_i_hit = l1_i_hit + val
                                    if 5 <= hit_word_count <= 6:
                                        val = float(line.strip("hit: "))
                                        l1_d_hit = l1_d_hit + val
                                    if 8 <= hit_word_count <= 9:
                                        val = float(line.strip("hit: "))
                                        l2_hit = l2_hit + val
                                elif "read:" in line:
                                    read_word_count = read_word_count + 1
                                    if read_word_count == 2:
                                        val = float(line.strip("read: "))
                                        l1_i_miss = l1_i_miss + val
                                    if read_word_count == 5:
                                        val = float(line.strip("read: "))
                                        l1_d_miss = l1_d_miss + val
                                    if read_word_count == 8:
                                        val = float(line.strip("read: "))
                                        l2_miss = l2_miss + val
                                elif "write:" in line:
                                    write_word_count = write_word_count + 1
                                    if write_word_count == 2:
                                        val = float(line.strip("write: "))
                                        l1_i_miss = l1_i_miss + val
                                    if write_word_count == 5:
                                        val = float(line.strip("write: "))
                                        l1_d_miss = l1_d_miss + val
                                    if write_word_count == 8:
                                        val = float(line.strip("write: "))
                                        l2_miss = l2_miss + val

                            line = fp.readline()
                            cnt += 1

                    # print(str(l1_i_hit))
                    # print(str(l1_i_miss))

                    if l1_i_hit + l1_i_miss == 0:
                        print(name)
                    l1_i_hit_rate = (l1_i_hit * 100 / (l1_i_hit + l1_i_miss))

                    if l1_d_hit + l1_d_miss == 0:
                        print (name)
                    l1_d_hit_rate = (l1_d_hit * 100 / (l1_d_hit + l1_d_miss))

                    if l2_hit + l2_miss == 0:
                        print (name)
                    l2_hit_rate = (l2_hit * 100 / (l2_hit + l2_miss))

                    # print(str(l1_i_hit_rate))
                    # print(str(l1_d_hit_rate))
                    # print(str(l2_hit_rate))

                    row = dict()
                    row[fields[0]] = name[:-6]
                    row[fields[1]] = l1_i_hit_rate
                    row[fields[2]] = l1_d_hit_rate
                    row[fields[3]] = l2_hit_rate
                    writer.writerow(row)
                    machine_count = 0

                    hit_word_count = 0
                    read_word_count = 0
                    write_word_count = 0

                    l1_i_hit = 0
                    l1_i_miss = 0

                    l1_d_hit = 0
                    l1_d_miss = 0

                    l2_hit = 0
                    l2_miss = 0


fun()

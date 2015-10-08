#!~/.jumbo/bin/python
import sys
import getopt

def usage():
    print("Usage:%s -f the file name which need to be filtered out" %sys.argv[0]);

def get_args():
    file_name = None
    level4_file = None
    level5_file = None
    try:
        opts, args = getopt.getopt(sys.argv[1:], "f:l:m:")
        for opt, arg in opts:
            if opt == "-f":
                file_name = arg
            if opt == "-l":
                level4_file = arg
            if opt == "-m":
                level5_file = arg
        if file_name is None or level4_file is None or level5_file is None:
            usage()
            sys.exit(1)
    except getopt.GetoptError:
        usage()
        sys.exit(1)

    return file_name, level4_file, level5_file

def get_number(file_name, level4_file, level5_file):
    level4_list = []
    level4_data = open(level4_file).readlines()
    for line in level4_data:
        level4_list.append(line.strip())

    level5_list = []
    level5_data = open(level5_file).readlines()
    for line in level5_data:
        level5_list.append(line.strip())

    print len(level4_list)
    print len(level5_list)

    file = open(file_name).readlines()
    filter_file = open(file_name + '.filtered', 'w')
    for line in file:
        continue
        sku_id, level = line.strip().split()
        merchant_id = sku_id.strip().split('_')[0]
        if sku_id in level5_list:
            filter_file.write(sku_id + '\t' + '5' + '\n')
            continue
        if sku_id in level4_list:
            filter_file.write(sku_id + '\t' + '4' + '\n')
            continue
        if merchant_id == "10003" and (level.strip() == '0' or level.strip() == '1'):
            continue
        if merchant_id == "10005" and level.strip() == '0':
            continue
        if merchant_id == "10000" and level.strip() == '0':
            continue
        if merchant_id == "10000" and (level.strip() == '1' or level.strip() == '2'):
            filter_file.write(sku_id + '\t' + '0' + '\n')
            continue
        if merchant_id == "10000" and level.strip() == '3':
            filter_file.write(sku_id + '\t' + '2' + '\n')
            continue
        filter_file.write(line)
    filter_file.close()

if __name__ == '__main__':
    file_name,level4_file, level5_file = get_args()
    get_number(file_name, level4_file, level5_file)

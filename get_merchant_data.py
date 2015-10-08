#coding=utf-8
__author__ = 'baidu'

promotion_data = open("promotion_data").readlines()
promotion_sample = open("promotion_sample", "w")

d = dict()
d["10000"] = 0
d["10001"] = 0
d["10002"] = 0
d["10003"] = 0
d["10004"] = 0
d["10005"] = 0
d["10006"] = 0

d2 = dict()
d2["10000"] = 0
d2["10001"] = 0
d2["10002"] = 0
d2["10003"] = 0
d2["10004"] = 0
d2["10005"] = 0
d2["10006"] = 0

region_name = {"0":"全国", "1":"北京", "2":"天津", "3":"上海", "4":"广州", "5":"重庆", "6":"沈阳", "7":"南京"
    ,"8":"武汉","9":"深圳","10":"成都","11":"西安"}

for line in promotion_data:
    items = line.strip('\n').split('\t')
    merchant_id = items[1].strip()
    items[3] = region_name[items[3].strip()]
    type = items[5].strip()
    if type == "1"  and d[merchant_id] < 20:
        promotion_sample.write('\t'.join(items) + '\n')
        d[merchant_id] += 1

    if type == "0"  and d2[merchant_id] < 20:
        promotion_sample.write('\t'.join(items) + '\n')
        d2[merchant_id] += 1


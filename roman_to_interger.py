#coding=utf-8
__author__ = 'baidu'

def romanToInt(s):
    symbol = ['I', 'V', 'X', 'L', 'C', 'D', 'M']
    val = [1, 5, 10, 50, 100, 500, 1000]
    d = dict(zip(symbol, val))
    result = d[s[0]]
    for i in range(1, len(s)):
        if d[s[i]] <= d[s[i-1]]:
            result += d[s[i]]
        else:
            if s[i-1] in ["I", "X", "C"]:
                result = result + d[s[i]] - 2*d[s[i-1]]
    return result



if __name__ == "__main__":
    print romanToInt("MCMXCVI")

    #expected 1996
    # 相同的数字连写，所表示的数等于这些数字相加得到的数，例如：III = 3
    # 小的数字在大的数字右边，所表示的数等于这些数字相加得到的数，例如：VIII = 8
    # 小的数字，限于（I、X和C）在大的数字左边，所表示的数等于大数减去小数所得的数，例如：IV = 4
    # 正常使用时，连续的数字重复不得超过三次
    # 在一个数的上面画横线，表示这个数扩大1000倍（本题只考虑3999以内的数，所以用不到这条规则）
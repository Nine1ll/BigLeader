# 7개일 때나 가능한 이야기구ㅇ

def fn(lotto_list=[1, 2, 3, 4, 5, 6, 7]):
    for idx in range(len(lotto_list) - 1, -1, -1):
        lotto_list_temp = lotto_list.copy()
        lotto_list_temp.pop(idx)
        print(lotto_list_temp)


# fn()

def select_ele(lotto_list=[1, 2, 3, 4, 5, 6, 7]):
    for idx in range(len(lotto_list)):
        for jdx in range(idx + 1, len(lotto_list)):
            for kdx in range(jdx + 1, len(lotto_list)):
                for ldx in range(kdx + 1, len(lotto_list)):
                    for mdx in range(ldx + 1, len(lotto_list)):
                        for ndx in range(mdx + 1, len(lotto_list)):
                            print(lotto_list[idx], lotto_list[jdx],
                                  lotto_list[kdx], lotto_list[ldx],
                                  lotto_list[mdx], lotto_list[ndx])


# select_ele()


def select_ele(lotto_list, ):
    for idx in range(len(lotto_list)):
        for jdx in range(idx + 1, len(lotto_list)):
            for kdx in range(jdx + 1, len(lotto_list)):
                for ldx in range(kdx + 1, len(lotto_list)):
                    for mdx in range(ldx + 1, len(lotto_list)):
                        for ndx in range(mdx + 1, len(lotto_list)):
                            print(lotto_list[idx], lotto_list[jdx],
                                  lotto_list[kdx], lotto_list[ldx],
                                  lotto_list[mdx], lotto_list[ndx])


#
# def Fn(lotto_list = [1,2,3,4,5,6,7]):
#     for idx in range(len(lotto_list)-1,-1,-1):
#         lotto_list_tmp = lotto_list.copy()
#         lotto_list_tmp.pop(idx)
#         print(lotto_list_tmp)

lotto_list = [1, 2, 3, 4, 5, 6, 7]
ret_list = [0, 0, 0, 0, 0, 0]
n = len(lotto_list)


def fx(depth, idx):
    if depth == 6:
        print(*ret_list)
        return

    for jdx in range(idx, n):
        ret_list[depth] = lotto_list[jdx]
        fx(depth+1, jdx + 1)


fx(0,0)

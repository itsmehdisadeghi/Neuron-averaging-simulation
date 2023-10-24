def avrage(lis):
    sum = 0
    for i in lis:
        sum += i
    return sum/len(lis)
def nog_asl(inp_lis):
    num_nog_asl = len(inp_lis)
    a = avrage(inp_lis)
    a0 = 100
    i = 1
    while True:
        nesf_1_inp_lis = []
        nesf_2_inp_lis = []
        for inp in inp_lis:
            if inp <= a:
                nesf_1_inp_lis.append(inp)
            elif inp <= a0:
                nesf_2_inp_lis.append(inp)
        if len(nesf_1_inp_lis) <= len(nesf_2_inp_lis):
            a0 = a
            a= avrage(nesf_2_inp_lis)
        else:
            a0 = a
            a= avrage(nesf_1_inp_lis)
        i+=1
        if i ==10:
            break
    return a
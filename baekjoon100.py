##2557.
##print("Hello World!")
##
##1000.
##a, b = input().split()
##print(int(a) + int(b))
##
##10998.
##a, b = input().split()
##print(int(a) * int(b))
##
##1001.
##a, b = input().split()
##print(int(a) - int(b))
##
##1008.
##a, b = input().split()
##print(int(a) / int(b))
##
##10869.
##a, b = input().split()
##print(int(a) + int(b))
##print(int(a) - int(b))
##print(int(a) * int(b))
##print(int(a) // int(b))
##print(int(a) % int(b))
##
##10430.
##a, b, c = input().split()
##a = int(a)
##b = int(b)
##c = int(c)
##print((a + b) % c)
##print((a % c + b % c) % c)
##print((a * b) % c)
##print((a % c * b % c) % c)
##
##2558.
##a = int(input())
##b = int(input())
##print(a+b)
##
##2588.
##num1 = int(input())
##num2 = int(input())
##result = num1 * num2
##for i in range(3):
##    print(num1 * (num2 % 10))
##    num2 = num2 // 10
##print(result)
##
##3046.
##r1, s = map(int, input().split())
##print(s*2-r1)
##
##2163.
##num1, num2 = map(int, input().split())
##print(num1 * num2 - 1)
##
##11021.
##input_count = int(input())
##sum = []
##for i in range(input_count):
##    num1, num2 = map(int, input().split())
##    sum.append(num1 + num2)
##for i in range(input_count):
##    print("Case #" + str(i+1) + ": " + str(sum[i]))
##
##11022.
##input_count = int(input())
##sum = []
##num_list = []
##for i in range(input_count):
##    num1, num2 = map(int, input().split())
##    num_list.append([])
##    num_list[i].append(num1)
##    num_list[i].append(num2)
##    sum.append(num1 + num2)
##for i in range(input_count):
##    print("Case #" + str(i+1) + ": " + str(num_list[i][0]) + " + " + str(num_list[i][1]) + " = " + str(sum[i]))
##
##10699.
##from datetime import datetime
##now = datetime.now()
##print(str(now.year) + "-" + "%02d" % now.month + "-" + "%02d" % now.day)
##
##7287.
##print("14\nbjaekoon")
##
##2525.
##hour, minute = map(int,input().split())
##time = int(input())
##hour = (hour + (minute + time) // 60) % 24
##minute = (minute + time) % 60
##print(hour, minute)
##
##2530.
##hour, minute, second= map(int,input().split())
##time = int(input())
##hour = (hour + (minute + (second + time) // 60) // 60) % 24
##minute = (minute + (second + time) // 60) % 60
##second = (second + time) % 60
##print(hour, minute, second)
##
##2914.
##count, avg = map(int,input().split())
##print(count * avg - (count-1))
##
##5355.
##count = int(input())
##math = []
##for i in range (count):
##    input_data = input().split()
##    for j in input_data:
##        if j == '#':
##            math[i] = math[i] - 7.0
##        elif j == '%':
##            math[i] = math[i] + 5.0
##        elif j == '@':
##            math[i] = math[i] * 3.0
##        else:
##            math.append(float(j))
##for i in range(count):
##    print("%0.2f" % math[i])
##
##2675.
##count = int(input())
##repeat = []
##data = []
##test_data = " "
##result_data = []
##for i in range(count):
##    a, b = input().split()
##    repeat.append(int(a))
##    data.append(b)
##    result_data.append("")
##    for j in range(len(data[i])):
##        test_data = data[i][j] * repeat[i]
##        result_data[i] += test_data
##for i in range(count):    
##    print(result_data[i])
##
##2935.
##op1 = int(input())
##operand = input()
##op2 = int(input())
##if operand == '+':
##    result = op1 + op2
##elif operand == '*':
##    result = op1 * op2
##print(result)
##
##9498.
##score = int(input())
##if score >= 0 & score <= 100:
##    if score >= 90:
##        print('A')
##    elif score >= 80:
##        print('B')
##    elif score >= 70:
##        print('C')
##    elif score >= 60:
##        print('D')
##    else:
##        print('F')
##
##10817.
##num1, num2, num3 = map(int,input().split())
##if (num1 >= num2 and num1 <= num3) or (num1 <= num2 and num1 >= num3) :
##    print(num1)
##elif (num2 >= num1 and num2 <= num3) or (num2 <= num1 and num2 >= num3) :
##    print(num2)
##else:
##    print(num3)
##
##11653.
##num = int(input())
##i = 2
##while i <= num:
##    if num // i == num / i:
##        print(i)
##        num = num // i
##        i -= 1
##    i += 1
##
##1789.
##import math
##S = int(input())
##N = int(math.sqrt(S * 2))
##while (N * N) + N > S * 2:
##    N -= 1
##print(N)
##
##2753.
##year = int(input())
##if year % 4 == 0 and year % 100 != 0:
##    print(1)
##elif year % 400 == 0:
##    print(1)
##else:
##    print(0)
##
##10039.
##score = []
##total = 0
##for i in range(5):
##    score.append(int(input()))
##for i in range(5):
##    if score[i] < 40:
##        score[i] = 40
##    total += score[i]
##print(total // 5)
##
##1934.
##test_case = int(input())
##num = []
##result = []
##for i in range(test_case):
##    input_data = input().split()
##    num.append([])
##    for j in range(2):
##        num[i].append(int(input_data[j]))
##for i in range(test_case):
##    num1, num2 = num[i][0], num[i][1]
##    while num[i][1] % num[i][0] != 0:
##        if num[i][0] > num[i][1]:
##            temp = num[i][0]
##            num[i][0] = num[i][1]
##            num[i][1] = temp
##        num[i][1] %= num[i][0]
##    result.append(int(num1 * num2 / num[i][0]))
##for i in range(test_case):
##    print(result[i])
##
##2480.
##dice = input().split()
##if dice[0] == dice[1] == dice[2]:
##    same = int(dice[0])
##    print(10000 + same * 1000)
##elif dice[0] == dice[1] or dice[0] == dice[2]:
##    same = int(dice[0])
##    print(1000 + same * 100)
##elif dice[1] == dice[2]:
##    same = int(dice[1])
##    print(1000 + same * 100)
##else:
##    print(int(max(dice[0],dice[1],dice[2])) * 100)
##
##2480-1.
##case = 0
##num = input().split()
##for i in range(len(num) - 1):
##    j = 1
##    while j + i < len(num):
##        if int(num[i]) == int(num[i+j]):
##            case += 1
##            same = int(num[i])
##        elif int(num[i]) > int(num[i+j]):
##            max_num = int(num[i])
##        j += 1
##if case >= 2:
##    print(10000 + same * 1000)
##elif case == 1:
##    print(1000 + same * 100)
##else:
##    print(max_num * 100)
##
##4101.
##num = []
##result = []
##i = 0
##while True:
##    num.append([])
##    temp1, temp2 = map(int,input().split())
##    num[i].append(temp1)
##    num[i].append(temp2)
##    if num[i][0] == 0 and num[i][1] == 0:
##        break
##    elif num[i][0] > num[i][1]:
##        result.append("Yes")
##    else:
##        result.append("No")
##    i += 1
##for i in result:
##    print(i)
##
##10156.
##K, N, M = map(int,input().split())
##money = K * N - M
##if money <= 0:
##    money = 0
##print(money)
##
##3009.
##dot = []
##max_val = []
##min_val = []
##result_dot = []
##for i in range(3):
##    dot.append([])
##    input_data = input().split()
##    for j in range(2):
##        dot[i].append(int(input_data[j]))
##
##max_val.append(max(dot[0][0],dot[1][0],dot[2][0]))
##max_val.append(max(dot[0][1],dot[1][1],dot[2][1]))
##min_val.append(min(dot[0][0],dot[1][0],dot[2][0]))
##min_val.append(min(dot[0][1],dot[1][1],dot[2][1]))
##
##dis = []
##dis.append(max_val[0]-min_val[0])
##dis.append(max_val[1]-min_val[1])
##
##result_dot.append([])
##result_dot[0].append(max_val[0])
##result_dot[0].append(max_val[1])
##result_dot.append([])
##result_dot[1].append(max_val[0]-dis[0])
##result_dot[1].append(max_val[1])
##result_dot.append([])
##result_dot[2].append(max_val[0])
##result_dot[2].append(max_val[1]-dis[1])
##result_dot.append([])
##result_dot[3].append(max_val[0]-dis[0])
##result_dot[3].append(max_val[1]-dis[1])
##
##for i in range(3):
##    for j in range(4):
##        if result_dot[j] == dot[i]:
##            result_dot[j].clear()
##
##for i in range(4):
##    if result_dot[i]:
##        print(f"{result_dot[i][0]} {result_dot[i][1]}")
##
##2476.
##dice = [0, 0, 0]
##result = []
##input_dice = []
##max_val = 0
##people = int(input())
##for i in range(people):
##    input_dice = input().split()
##    for j in range(3):
##        dice[j] = input_dice[j]
##        
##    if dice[0] == dice[1] == dice[2]:
##        result.append(10000 + int(dice[0]) * 1000)
##    elif dice[0] == dice[1] or dice[0] == dice[2]:
##        result.append(1000 + int(dice[0]) * 100)
##    elif dice[1] == dice[2]:
##        result.append(1000 + int(dice[1]) * 100)
##    else:
##        result.append(int(max(dice[0],dice[1],dice[2])) * 100)
##    max_val = max(max_val, result[i])
##print(max_val)
##
##2754.
##score_let = input()
##if score_let[:1] == 'A':
##    score = 4.0
##elif score_let[:1] == 'B':
##    score = 3.0
##elif score_let[:1] == 'C':
##    score = 2.0
##elif score_let[:1] == 'D':
##    score = 1.0
##else:
##    score = 0.0
##if score == 0.0:
##    pass
##elif score_let[-1:] == '+':
##    score += 0.3
##elif score_let[-1:] == '-':
##    score -= 0.3
## 
##print(score)
##
##2884.
##hour, minute = map(int,input().split())
##if minute - 45 < 0:
##    minute += 60
##    minute -= 45
##    if hour - 1 < 0:
##        hour += 24
##        hour -= 1
##    else:
##        hour -= 1
##else:
##    minute -= 45
##print(f"{hour} {minute}")
##
##7567.
##input_data = input()
##height = 10
##for i in range(1,len(input_data)):
##    if input_data[i] == input_data[i-1]:
##        height += 5
##    else:
##        height += 10
##print(height)
##
##5063.
##N = int(input())
##r, e, c = [], [], []
##for i in range(N):
##    input_data = input().split()
##    r.append(int(input_data[0]))
##    e.append(int(input_data[1]))
##    c.append(int(input_data[2]))
##for i in range(N):
##    if e[i] - r[i] - c[i] > 0:
##        print("advertise")
##    elif e[i] - r[i] - c[i] < 0:
##        print("do not advertise")
##    elif e[i] - r[i] - c[i] == 0:
##        print("does not matter")
##
##10102.
##V = int(input())
##vote = input()
##A = 0
##B = 0
##for i in vote:
##    if i == 'A':
##        A += 1
##    else:
##        B += 1
##
##if A > B:
##    print('A')
##elif B > A:
##    print('B')
##elif A == B:
##    print("Tie")
##
##10886.
##N = int(input())
##one = 0
##zero = 0
##for i in range(N):
##    input_data = int(input())
##    if input_data == 1:
##        one += 1
##    elif input_data == 0:
##        zero += 1
##if one > zero:
##    print("Junhee is cute!")
##elif zero > one:
##    print("Junhee is not cute!")
##
##10988.
##word = input()
##length = len(word) // 2
##bool_s = 1
##for i in range(length):
##    if word[i] != word[-(i+1)]:
##        bool_s -= 1
##        break
##print(bool_s)
##
##5086.
##case = []
##result = []
##i = 0
##while True:
##    case.append([])
##    input_data = input().split()
##    case[i].append(int(input_data[0]))
##    case[i].append(int(input_data[1]))
##    if not(case[i][1] and case[i][0]):
##        break;
##    elif case[i][1] / case[i][0] == case[i][1] // case[i][0]:
##        result.append("factor")
##    elif case[i][0] / case[i][1] == case[i][0] // case[i][1]:
##        result.append("multiple")
##    else:
##        result.append("neither")
##    i += 1
##for j in result:
##    print(j)
##
##5717.
##i = 0
##result = []
##while True:
##    peo1, peo2 = map(int,input().split())
##    if peo1 == 0 and peo2 == 0:
##        break;
##    result.append(peo1 + peo2)
##    i += 1
##for j in range(i):
##    print(result[j])
##
##9610.
##num = int(input())
##Q1, Q2, Q3, Q4 = 0, 0, 0, 0
##AXIS = 0
##for i in range(num):
##    dot0, dot1 = map(int,input().split())
##    dot0 = int(dot0)
##    dot1 = int(dot1)
##    result = 0
##    if dot0 == 0 or dot1 == 0:
##        AXIS += 1
##    elif dot0 > 0 and dot1 > 0:
##        Q1 += 1
##    elif dot0 < 0 and dot1 > 0:
##        Q2 += 1
##    elif dot0 < 0 and dot1 < 0:
##        Q3 += 1
##    elif dot0 > 0 and dot1 < 0:
##        Q4 += 1
##print(f"Q1: {Q1}")
##print(f"Q2: {Q2}")
##print(f"Q3: {Q3}")
##print(f"Q4: {Q4}")
##print(f"AXIS: {AXIS}")
##
##8958.
##num = int(input())
##result = []
##for i in range(num):
##    input_str = input()
##    result.append(0)
##    score = 0
##    for j in range(len(input_str)):
##        if input_str[j] == 'O':
##            score += 1
##            result[i] += score
##        elif input_str[j] == 'X':
##            score = 0
##for i in range(num):
##    print(result[i])
##
##9506.
##result = []
##n = []
##i = 0
##sum_val = 0
##while True:
##    result.append([])
##    n.append(int(input()))
##    if n[i] != -1:
##        for j in range(1, n[i]//2 + 1):
##            if n[i] // j == n[i] / j:
##                result[i].append(j)
##    else:
##        break;
##    i += 1
##for j in range(i):
##    sum_val = 0
##    for k in result[j]:
##        sum_val += k
##    if n[j] == sum_val:
##        print(f"{n[j]} = 1",end = '')
##        for l in range(1,len(result[j])):
##            print(f" + {result[j][l]}",end = '')
##        print()
##    else:
##        print(f"{n[j]} is NOT perfect.")
##
##10162.
##T = int(input())
##A, B, C = 0, 0, 0
##while True:
##    if T // 300 >= 1:
##        A = T // 300
##        T = T - 300 * A
##    elif T // 60 >= 1:
##        B = T // 60
##        T = T - 60 * B
##    elif T // 10 >= 1:
##        C = T // 10
##        T = T - 10 * C
##    if T < 10:
##        break
##if T == 0:
##    print(f"{A} {B} {C}")
##elif T != 0:
##    print(-1)
##
##10103.
##num = int(input())
##sang_score = 100
##chang_score = 100
##for i in range(num):
##    chang, sang = map(int,input().split())
##    if sang > chang:
##        chang_score -= sang
##    elif sang < chang:
##        sang_score -= chang
##print(chang_score)
##print(sang_score)
##
##10214.
##num = int(input())
##result = []
##for i in range(num):
##    yonsei = 0
##    korea = 0
##    for j in range(9):
##        yonsei_in, korea_in = map(int,input().split())
##        if yonsei_in > korea_in:
##            yonsei += 1
##        elif yonsei_in < korea_in:
##            korea += 1
##    if yonsei > korea:
##        result.append("Yonsei")
##    elif yonsei < korea:
##        result.append("Korea")
##    elif yonsei == korea:
##        result.append("Draw")
##
##for i in range(num):
##    print(result[i])
##
##11557.
##input_list = []
##result = []
##max_val = 0
##T = int(input())
##for i in range(T):
##    N = int(input())
##    max_val = 0
##    temp_result = ""
##    for j in range(N):
##        name, count = input().split()
##        count = int(count)
##        if count > max_val:
##            max_val = count
##            temp_result = name
##    result.append(temp_result)
##for i in range(T):
##    print(result[i])
##
##10757
##a, b = map(int,input().split())
##print(a+b)

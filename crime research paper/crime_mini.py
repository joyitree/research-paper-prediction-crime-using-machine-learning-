import pandas as pd
import random
import math
def confusion_matrix(y1, y2):
      TP = 0
      TN = 0
      FP = 0
      FN = 0
      for i in range(len(y2)):
          if abs(y1[i]-y2[i] < 0.2):
              TP += 1
          elif abs(y1[i]-y2[i] < 0.4):
              TN += 1
          elif abs(y1[i]-y2[i] < 0.6):
              FP += 1
          else:
              FN += 1
      k = []
      k.append(TP)
      k.append(TN)
      k.append(FP)
      k.append(FN)
      mat = []
      m1 = 0
      for i in range(2):
          a = []
          for j in range(2):
              a.append(k[m1])
              m1 += 1
          mat.append(a)
      for i in range(2):
          for j in range(2):
              print(mat[i][j], end=" ")
          print("\n")
      print("accuracy : ", round(((TP+TN)/sum(k))*100,2))
      print("sensitivity: ", round((TP/(TP+FN))*100,2))
      print("specificity: ",round((TN/(TN+FP))*100,2))
    # precission:
      precission = (TP/(TP+FP))
      print("precission: ", round(precission, 2))
    # kappa test:
      observed_agreement = ((TP+TN)/sum(k)) * 100
      expected_agreememnt = ((TP+FP) * (TP+FN) * (FN+TN) * (FP+TN)) / 100
      kappa_Test = (observed_agreement - expected_agreememnt) / (100 - expected_agreememnt)
      print("kappa test:", round(kappa_Test, 2))
    # F1 score:
      precission = (TP/(TP+FP))
      recall = (TP/(TP+FN))
      print("Recall: ", round(recall, 2))
      x = (2 * precission * recall) / (precission + recall)
      print("F1 score: ", round(x, 2))
      return (confusion_matrix)
def standard_deviation(state_state_list):
    mean = sum(state_state_list) / len(state_state_list)
    mean_l = []
    mean_l_square = []
    for i in range(0, len(state_state_list)):
        mean_l.append(state_state_list[i] - mean)

    for i in range(0, len(mean_l)):
        mean_l_square.append(mean_l[i] * mean_l[i])

    sum_l = sum(mean_l_square) / len(mean_l_square)
    Standard_deviation = math.sqrt(sum_l)
    return round(Standard_deviation, 2)


def R_square(y1, y2):
    mean = sum(y2) / len(y2)
    R_square_neu = []
    R_square_deno = []
    y_minus_y_pred = []
    y_minus_y_pred_square = []
    y_minus_y_avg = []
    y_minus_y_avg_square = []
    for i in range(0, len(y2)):
        y_minus_y_pred.append(y1[i] - y2[i])
        y_minus_y_avg.append(y1[i] - mean)

    for i in range(0, len(y_minus_y_pred)):
        y_minus_y_pred_square.append(y_minus_y_pred[i] * y_minus_y_pred[i])

    for i in range(0, len(y_minus_y_avg)):
        y_minus_y_avg_square.append(y_minus_y_avg[i] * y_minus_y_avg[i])

    R_square_neu.append(sum(y_minus_y_pred_square))
    R_square_deno.append(sum(y_minus_y_avg_square))

    a = sum(R_square_neu) / sum(R_square_deno)
    R_square = 1 - a
    return abs(round(R_square, 2))
    
   # return abs(round(R_square/100, 2))
   
#from sklearn import cross_validation
df = pd.read_csv(r'C:\Users\TS\OneDrive\Desktop\COLLEGE\pycharm project\python dataset\crime_data.csv')
# print(df)
# list create
state_list = df['state'].tolist()  # considaring as x1
population_list = df['population'].tolist()  # considaring as x2
education_list = df['PctBSorMore'].tolist()  # considaring as x3
unemploy_list = df['PctUnemployed'].tolist()  # considaring as x4
crime_list = df['ViolentCrimesPerPop'].tolist()  # considaring as y
t1 = len(state_list)
n = int(2/3*t1)
def average(list):
    return (sum(list)/n)
state_average = round(average(state_list), 2)
population_average = round(average(population_list), 2)
edu_average = round(average(education_list), 2)
unemploy_average = round(average(unemploy_list), 2)
crime_average = round(average(crime_list), 2)
# new lis
b1_neu_list = []
b1_deno_list = []

b2_neu_list = []
b2_deno_list = []

b3_neu_list = []
b3_deno_list = []

b4_neu_list = []
b4_deno_list = []

# value of b1
for i in range(0, n):
    b1_neu_list.append((state_list[i] - state_average) * (crime_list[i] - crime_average))
    b1_deno_list.append((state_list[i] - state_average) * (state_list[i] - state_average))
    b2_neu_list.append((population_list[i] - population_average) * (crime_list[i]-crime_average))
    b2_deno_list.append((population_list[i]-population_average) * (population_list[i]-population_average))
    b3_neu_list.append((education_list[i]-edu_average) * (crime_list[i]-crime_average))
    b3_deno_list.append((education_list[i]-edu_average) * (education_list[i]-edu_average))
    b4_neu_list.append((unemploy_list[i]-unemploy_average)*(crime_list[i]-crime_average))
    b4_deno_list.append((unemploy_list[i]-unemploy_average) * (unemploy_list[i]-unemploy_average))
sum_b1_neu = sum(b1_neu_list)
sum_b1_deno = sum(b1_deno_list)
b1 = (sum_b1_neu)/(sum_b1_deno)
#print('b1 value is:', round(b1, 2))
sum_b2_neu = sum(b2_neu_list)
sum_b2_deno = sum(b2_deno_list)
b2 = (sum_b2_neu)/(sum_b2_deno)
#print('b2 value is:', round(b2, 2))
sum_b3_neu = sum(b3_neu_list)
sum_b3_deno = sum(b3_deno_list)
b3 = (sum_b3_neu)/(sum_b3_deno)
#print('b3 value is:', round(b3, 2))
sum_b4_neu_list = sum(b4_neu_list)
sum_b4_deno_list = sum(b4_deno_list)
b4 = sum_b4_neu_list/sum_b4_deno_list
#print('b4 value is: ', b4)
# sum of state[i]
sum_state_list = sum(state_list)
sum_popuulation_list = sum(population_list)
sum_education_list = sum(education_list)
sum_crime_list = sum(crime_list)
state_state_list = []
crime_crime_list = []
state_crime_list = []
for i in range(0, n):
    state_state_list.append(state_list[i]*state_list[i])
    crime_crime_list.append(crime_list[i]*crime_list[i])
    state_crime_list.append(state_list[i]*crime_list[i])
sum_state_state = sum(state_state_list)
sum_crime_crime = sum(crime_crime_list)
sum_state_crime = sum(state_crime_list)
# a
a = ((sum_crime_list*sum_state_state)-(sum_state_list*sum_state_crime)) / ((n*sum_state_state)-(sum_state_list*sum_state_list))
#print('a value is: ', round(a, 2))
y2 = []
y1 = []
for i in range(n+1, t1):
    y1.append(crime_list[i])
    y = a+b1*state_list[i]+b2*population_list[i] + b3*education_list[i]+b4*unemploy_list[i]
    y2.append(y)
#for i in range(len(y)):
    #print(round(y2[i], 2), "     ", y[i])
d = 0
for i in range(len(y1)):
    if abs(y1[i]-y2[i] <= 0.2):
        d += 1
#print(d)
print("===================== FOR 2/3 DATA ====================\n")
print('Accuracy rate is: ', round(d/len(y1)*100, 2))
#confusion Matrix
print("Confusion Matrix is: ")
print(confusion_matrix(y1, y2))

print("standard_deviation: ")
print(standard_deviation(y2))

print("R_square: ")
print(R_square(y1, y2))
print("\n\n")
print("===================== FOR 1/2 DATA ====================\n")
t2 = len(state_list)
n1 = int(1/2*t2)
def average2(list):
    return (sum(list)/n1)
state_average = round(average2(state_list), 2)
population_average = round(average2(population_list), 2)
edu_average = round(average2(education_list), 2)
unemploy_average = round(average2(unemploy_list), 2)
crime_average = round(average2(crime_list), 2)
# new list
b1_neu_list = []
b1_deno_list = []

b2_neu_list = []
b2_deno_list = []

b3_neu_list = []
b3_deno_list = []

b4_neu_list = []
b4_deno_list = []

# value of b1
for i in range(0, n1):
    b1_neu_list.append((state_list[i] - state_average) * (crime_list[i] - crime_average))
    b1_deno_list.append((state_list[i] - state_average) * (state_list[i] - state_average))
    b2_neu_list.append((population_list[i] - population_average) * (crime_list[i]-crime_average))
    b2_deno_list.append((population_list[i]-population_average) * (population_list[i]-population_average))
    b3_neu_list.append((education_list[i]-edu_average) * (crime_list[i]-crime_average))
    b3_deno_list.append((education_list[i]-edu_average) * (education_list[i]-edu_average))
    b4_neu_list.append((unemploy_list[i]-unemploy_average)*(crime_list[i]-crime_average))
    b4_deno_list.append((unemploy_list[i]-unemploy_average) * (unemploy_list[i]-unemploy_average))
sum_b1_neu = sum(b1_neu_list)
sum_b1_deno = sum(b1_deno_list)
b1 = (sum_b1_neu)/(sum_b1_deno)
#print('b1 value is:', round(b1, 2))
sum_b2_neu = sum(b2_neu_list)
sum_b2_deno = sum(b2_deno_list)
b2 = (sum_b2_neu)/(sum_b2_deno)
#print('b2 value is:', round(b2, 2))
sum_b3_neu = sum(b3_neu_list)
sum_b3_deno = sum(b3_deno_list)
b3 = (sum_b3_neu)/(sum_b3_deno)
#print('b3 value is:', round(b3, 2))
sum_b4_neu_list = sum(b4_neu_list)
sum_b4_deno_list = sum(b4_deno_list)
b4 = sum_b4_neu_list/sum_b4_deno_list
#print('b4 value is: ', b4)
sum_state_list = sum(state_list)
sum_popuulation_list = sum(population_list)
sum_education_list = sum(education_list)
sum_crime_list = sum(crime_list)
state_state_list = []
crime_crime_list = []
state_crime_list = []
for i in range(0, n1):
    state_state_list.append(state_list[i]*state_list[i])
    crime_crime_list.append(crime_list[i]*crime_list[i])
    state_crime_list.append(state_list[i]*crime_list[i])
sum_state_state = sum(state_state_list)
sum_crime_crime = sum(crime_crime_list)
sum_state_crime = sum(state_crime_list)

# a
a1_2 = ((sum_crime_list*sum_state_state)-(sum_state_list*sum_state_crime)) / ((n1*sum_state_state)-(sum_state_list*sum_state_list))
#print('a value is: ', round(a1_2, 2))
y2 = []
y1 = []
for i in range(n1+1, t2):
    y1.append(crime_list[i])
    y = a1_2+b1*state_list[i]+b2*population_list[i] + b3*education_list[i]+b4*unemploy_list[i]
    y2.append(y)
#for i in range(len(y)):
   # print(round(y2[i], 2), "     ", y[i])
d = 0
for i in range(len(y1)):
    if abs(y1[i]-y2[i] <= 0.2):
        d += 1
#print(d1_2)
print('Accuracy rate is: ', round(d/len(y1)*100, 2))
print("Confusion Matrix is: ")
print(confusion_matrix(y1, y2))

print("standard_deviation: ")
print(standard_deviation(y2))

print("R_square: ")
print(R_square(y1, y2))
print("\n\n")
#for 1/4 data
print("===================== FOR 1/4 DATA ====================\n")
t3 = len(state_list)
n2 = int(1/4*t3)
def average3(list):
    return (sum(list)/n2)
state_average = round(average3(state_list), 2)
population_average = round(average3(population_list), 2)
edu_average = round(average3(education_list), 2)
unemploy_average = round(average3(unemploy_list), 2)
crime_average = round(average3(crime_list), 2)
# new list
b1_neu_list = []
b1_deno_list = []
b2_neu_list = []
b2_deno_list = []
b3_neu_list = []
b3_deno_list = []
b4_neu_list = []
b4_deno_list = []
# value of b1
for i in range(0, n2):
    b1_neu_list.append((state_list[i] - state_average) * (crime_list[i] - crime_average))
    b1_deno_list.append((state_list[i] - state_average) * (state_list[i] - state_average))
    b2_neu_list.append((population_list[i] - population_average) * (crime_list[i]-crime_average))
    b2_deno_list.append((population_list[i]-population_average) * (population_list[i]-population_average))
    b3_neu_list.append((education_list[i]-edu_average) * (crime_list[i]-crime_average))
    b3_deno_list.append((education_list[i]-edu_average) * (education_list[i]-edu_average))
    b4_neu_list.append((unemploy_list[i]-unemploy_average)*(crime_list[i]-crime_average))
    b4_deno_list.append((unemploy_list[i]-unemploy_average) * (unemploy_list[i]-unemploy_average))
sum_b1_neu = sum(b1_neu_list)
sum_b1_deno = sum(b1_deno_list)
b1 = (sum_b1_neu)/(sum_b1_deno)
#print('b1 value is:', round(b1, 2))
sum_b2_neu = sum(b2_neu_list)
sum_b2_deno = sum(b2_deno_list)
b2 = (sum_b2_neu)/(sum_b2_deno)
#print('b2 value is:', round(b2, 2))
sum_b3_neu = sum(b3_neu_list)
sum_b3_deno = sum(b3_deno_list)
b3 = (sum_b3_neu)/(sum_b3_deno)
#print('b3 value is:', round(b3, 2))
sum_b4_neu_list = sum(b4_neu_list)
sum_b4_deno_list = sum(b4_deno_list)
b4 = sum_b4_neu_list/sum_b4_deno_list
#print('b4 value is: ', b4)
sum_state_list = sum(state_list)
sum_popuulation_list = sum(population_list)
sum_education_list = sum(education_list)
sum_crime_list = sum(crime_list)
state_state_list = []
crime_crime_list = []
state_crime_list = []
for i in range(0, n2):
    state_state_list.append(state_list[i]*state_list[i])
    crime_crime_list.append(crime_list[i]*crime_list[i])
    state_crime_list.append(state_list[i]*crime_list[i])
sum_state_state = sum(state_state_list)
sum_crime_crime = sum(crime_crime_list)
sum_state_crime = sum(state_crime_list)
a1_3 = ((sum_crime_list*sum_state_state)-(sum_state_list*sum_state_crime)) / ((n2*sum_state_state)-(sum_state_list*sum_state_list))
#print('a value is: ', round(a1_3, 2))
y2 = []
y1 = []
for i in range(n2+1, t3):
    y1.append(crime_list[i])
    y = a1_3+b1*state_list[i]+b2*population_list[i] + b3*education_list[i]+b4*unemploy_list[i]
    y2.append(y)
#for i in range(len(y)):
   # print(round(y2[i], 2), "     ", y[i])
d = 0
for i in range(len(y1)):
    if abs(y1[i]-y2[i] <= 0.2):
        d += 1
#print(d)
print('Accuracy rate is: ', round(d/len(y1)*100, 2))
#confusion Matrix
print("Confusion Matrix is: ")
print(confusion_matrix(y1, y2))

print("standard_deviation: ")
print(standard_deviation(y2))

print("R_square: ")
print(R_square(y1, y2))
print("\n\n")
print("=======================CROSS VALIDATION====================")
# set declear
s1 = set()
s2 = set()
s3 = set()
s4 = set()
s5 = set()
s6 = set()
s7 = set()
s8 = set()
s9 = set()
s10 = set()
# while loop
while(len(s1) < len(crime_list)//10):
    s1.add(random.randint(0, len(crime_list)-1))
    s1 = s1
while(len(s2) < len(crime_list)//10):
    s2.add(random.randint(0, len(crime_list)-1))
    s2 = s2-s1
while(len(s3) < len(crime_list)//10):
    s3.add(random.randint(0, len(crime_list)-1))
    s3 = s3-s2-s1
while(len(s4) < len(crime_list)//10):
    s4.add(random.randint(0, len(crime_list)-1))
    s4 = s4-s3-s2-s1
while(len(s5) < len(crime_list)//10):
    s5.add(random.randint(0, len(crime_list)-1))
    s5 = s5-s4-s3-s2-s1
while(len(s6) < len(crime_list)//10):
    s6.add(random.randint(0, len(crime_list)-1))
    s6 = s6-s5-s4-s3-s2-s1
while(len(s7) < len(crime_list)//10):
    s7.add(random.randint(0, len(crime_list)-1))
    s7 = s7-s6-s5-s4-s3-s2-s1
while(len(s8) < len(crime_list)//10):
    s8.add(random.randint(0, len(crime_list)-1))
    s8 = s8-s7-s6-s5-s4-s3-s2-s1
while(len(s9) < len(crime_list)//10):
    s9.add(random.randint(0, len(crime_list)-1))
    s9 = s9-s8-s7-s6-s5-s4-s3-s2-s1
while(len(s10) < len(crime_list)//10):
    s10.add(random.randint(0, len(crime_list)-1))
    s10 = s10-s9-s8-s7-s6-s5-s4-s3-s2-s1
s11 = s2.union(s2, s3, s4, s5, s6, s7, s8, s9, s10)
s12 = s3.union(s1, s3, s4, s5, s6, s7, s8, s9, s10)
s13 = s4.union(s1, s2, s4, s5, s6, s7, s8, s9, s10)
s14 = s5.union(s1, s2, s3, s5, s6, s7, s8, s9, s10)
s15 = s6.union(s1, s2, s3, s4, s6, s7, s8, s9, s10)
s16 = s7.union(s1, s2, s3, s4, s5, s7, s8, s9, s10)
s17 = s8.union(s1, s2, s3, s4, s5, s6, s8, s9, s10)
s18 = s9.union(s1, s2, s3, s4, s5, s6, s7, s9, s10)
s19 = s10.union(s1, s2, s3, s4, s5, s6, s7, s8, s10)
s20 = s1.union(s1, s2, s3, s4, s5, s6, s7, s8, s9)
# state list create
state1 = []
state2 = []
state3 = []
state4 = []
state5 = []
state6 = []
state7 = []
state8 = []
state9 = []
state10 = []
# population list create
population1 = []
population2 = []
population3 = []
population4 = []
population5 = []
population6 = []
population7 = []
population8 = []
population9 = []
population10 = []
# crime list create
crime1 = []
crime2 = []
crime3 = []
crime4 = []
crime5 = []
crime6 = []
crime7 = []
crime8 = []
crime9 = []
crime10 = []
# education list create
edu1 = []
edu2 = []
edu3 = []
edu4 = []
edu5 = []
edu6 = []
edu7 = []
edu8 = []
edu9 = []
edu10 = []
# unemploy list
unemploy1 = []
unemploy2 = []
unemploy3 = []
unemploy4 = []
unemploy5 = []
unemploy6 = []
unemploy7 = []
unemploy8 = []
unemploy9 = []
unemploy10 = []
# for loop
for i in s11:
    state1.append(state_list[i])
    population1.append(population_list[i])
    crime1.append(crime_list[i])
    edu1.append(education_list[i])
    unemploy1.append(unemploy_list[i])
for i in s12:
    state2.append(state_list[i])
    population2.append(population_list[i])
    crime2.append(crime_list[i])
    edu2.append(education_list[i])
    unemploy2.append(unemploy_list[i])
for i in s13:
    state3.append(state_list[i])
    population3.append(population_list[i])
    crime3.append(crime_list[i])
    edu3.append(education_list[i])
    unemploy3.append(unemploy_list[i])
for i in s14:
    state4.append(state_list[i])
    population4.append(population_list[i])
    crime4.append(crime_list[i])
    edu4.append(education_list[i])
    unemploy4.append(unemploy_list[i])
for i in s15:
    state5.append(state_list[i])
    population5.append(population_list[i])
    crime5.append(crime_list[i])
    edu5.append(education_list[i])
    unemploy5.append(unemploy_list[i])
for i in s16:
    state6.append(state_list[i])
    population6.append(population_list[i])
    crime6.append(crime_list[i])
    edu6.append(education_list[i])
    unemploy6.append(unemploy_list[i])
for i in s17:
    state7.append(state_list[i])
    population7.append(population_list[i])
    crime7.append(crime_list[i])
    edu7.append(education_list[i])
    unemploy7.append(unemploy_list[i])
for i in s18:
    state8.append(state_list[i])
    population8.append(population_list[i])
    crime8.append(crime_list[i])
    edu8.append(education_list[i])
    unemploy8.append(unemploy_list[i])
for i in s19:
    state9.append(state_list[i])
    population9.append(population_list[i])
    crime9.append(crime_list[i])
    edu9.append(education_list[i])
    unemploy9.append(unemploy_list[i])
for i in s20:
    state10.append(state_list[i])
    population10.append(population_list[i])
    crime10.append(crime_list[i])
    edu10.append(education_list[i])
    unemploy10.append(unemploy_list[i])

# state_average_list
state_average_list = []
state_average_list.append(round(average(state1), 2))
state_average_list.append(round(average(state2), 2))
state_average_list.append(round(average(state3), 2))
state_average_list.append(round(average(state4), 2))
state_average_list.append(round(average(state5), 2))
state_average_list.append(round(average(state6), 2))
state_average_list.append(round(average(state7), 2))
state_average_list.append(round(average(state8), 2))
state_average_list.append(round(average(state9), 2))
state_average_list.append(round(average(state10), 2))
# population_average_list
population_average_list = []
population_average_list.append(round(average(population1), 2))
population_average_list.append(round(average(population2), 2))
population_average_list.append(round(average(population3), 2))
population_average_list.append(round(average(population4), 2))
population_average_list.append(round(average(population5), 2))
population_average_list.append(round(average(population6), 2))
population_average_list.append(round(average(population7), 2))
population_average_list.append(round(average(population8), 2))
population_average_list.append(round(average(population9), 2))
population_average_list.append(round(average(population10), 2))
#print('population average list is: ', population_average_list)
# crime_average_list
crime_average_list = []
crime_average_list.append(round(average(crime1), 2))
crime_average_list.append(round(average(crime2), 2))
crime_average_list.append(round(average(crime3), 2))
crime_average_list.append(round(average(crime4), 2))
crime_average_list.append(round(average(crime5), 2))
crime_average_list.append(round(average(crime6), 2))
crime_average_list.append(round(average(crime7), 2))
crime_average_list.append(round(average(crime8), 2))
crime_average_list.append(round(average(crime9), 2))
crime_average_list.append(round(average(crime10), 2))
#print('crime_average_list is: ', crime_average_list)
# education_list_average
education_average_list = []
education_average_list.append(round(average(edu1), 2))
education_average_list.append(round(average(edu2), 2))
education_average_list.append(round(average(edu3), 2))
education_average_list.append(round(average(edu4), 2))
education_average_list.append(round(average(edu5), 2))
education_average_list.append(round(average(edu6), 2))
education_average_list.append(round(average(edu7), 2))
education_average_list.append(round(average(edu8), 2))
education_average_list.append(round(average(edu9), 2))
education_average_list.append(round(average(edu10), 2))
#print('education list is: ', education_average_list)
# unemploy_average_list
unemploy_average_list = []
unemploy_average_list.append(round(average(unemploy1), 2))
unemploy_average_list.append(round(average(unemploy2), 2))
unemploy_average_list.append(round(average(unemploy3), 2))
unemploy_average_list.append(round(average(unemploy4), 2))
unemploy_average_list.append(round(average(unemploy5), 2))
unemploy_average_list.append(round(average(unemploy6), 2))
unemploy_average_list.append(round(average(unemploy7), 2))
unemploy_average_list.append(round(average(unemploy8), 2))
unemploy_average_list.append(round(average(unemploy9), 2))
unemploy_average_list.append(round(average(unemploy10), 2))
#print('unemploy list is: ', unemploy_average_list)
def average1(list):
    return sum(list)/10
state_average_list_average = round(average1(state_average_list), 2)
population_average_list_average = round(average1(population_average_list), 2)
crime_average_list_average = round(average1(crime_average_list), 2)
education_average_list_average = round(average1(education_average_list), 2)
unemploy_average_list_average = round(average1(unemploy_average_list), 2)
print("========== 1ST PART ==========")
b11_neu_list = []
b11_deno_list = []
b21_neu_list = []
b21_deno_list = []
b31_neu_list = []
b31_deno_list = []
b41_neu_list = []
b41_deno_list = []
for i in range(len(s11)):
    b11_neu_list.append((state1[i]-state_average_list_average) * (crime1[i]-crime_average_list_average))
    b11_deno_list.append((state1[i]-state_average_list_average) * (state1[i]-state_average_list_average))
    b21_neu_list.append((population1[i]-population_average_list_average) * (crime1[i]-crime_average_list_average))
    b21_deno_list.append((population1[i]-population_average_list_average) * (population1[i]-population_average_list_average))
    b31_neu_list.append((edu1[i]-education_average_list_average) * (crime1[i]-crime_average_list_average))
    b31_deno_list.append( (edu1[i]-education_average_list_average) * (edu1[i]-education_average_list_average))
    b41_neu_list.append((unemploy1[i]-unemploy_average_list_average) *  (crime1[i]-crime_average_list_average))
    b41_deno_list.append((unemploy1[i]-unemploy_average_list_average) * (unemploy1[i]-unemploy_average_list_average))
sum_b11_neu_list = sum(b11_neu_list)
sum_b11_deno_list = sum(b11_deno_list)
b1_b11 = sum_b11_neu_list/sum_b11_deno_list
#print('b1_b11 value is: ', round(b1_b11, 2))
sum_b21_neu_list = sum(b21_neu_list)
sum_b21_deno_list = sum(b21_deno_list)
b2_b21 = sum_b21_neu_list/sum_b21_deno_list
#print('b2_b21 value is: ', round(b2_b21, 2))
sum_b31_neu_list = sum(b31_neu_list)
sum_b31_deno_list = sum(b31_deno_list)
b3_b31 = sum_b31_neu_list/sum_b31_deno_list
#print('b3_b31 value is: ', round(b3_b31, 2))
sum_b41_neu_list = sum(b41_neu_list)
sum_b41_deno_list = sum(b41_deno_list)
b4_b41 = sum_b41_neu_list/sum_b41_deno_list
#print('b4_b41 value is: ', round(b4_b41, 2))
sum_state1_list = sum(state1)
sum_popuulation1_list = sum(population1)
sum_education1_list = sum(edu1)
sum_crime1_list = sum(crime1)
state_state_list = []
crime1_crime1_list = []
state1_crime1_list = []
for i in range(len(s11)):
    state_state_list.append(state1[i]*state1[i])
    crime1_crime1_list.append(crime1[i]*crime1[i])
    state1_crime1_list.append(state1[i]*crime1[i])
sum_state1_state1 = sum(state_state_list)
sum_crime1_crime1 = sum(crime1_crime1_list)
sum_state1_crime1 = sum(state1_crime1_list)
# a1
a1 = ((sum_crime1_list*sum_state1_state1)-(sum_state1_list*sum_state1_crime1))/((len(s11)*sum_state1_state1)-(sum_state1_list*sum_state1_list))
#print('a1 value is: ', round(a1, 2))
y2 = []
y1 = []
for i in range(len(s1)):
    y1.append(crime_list[i])
    y = a1+b1_b11*state1[i]+b2_b21*population1[i] + b3_b31*edu1[i]+b4_b41*unemploy1[i]
    y2.append(y)
# for i in range(len(y1)):

#    print(round(y2[i], 2), "     ", y1[i])
d = 0
for i in range(len(y1)):
    if abs(y1[i]-y2[i] <= 0.2):
        d += 1
print('value of d is: ', d)
print('Accuracy rate is: ', round(d/len(y1)*100, 2))
print("Confusion Matrix is: ")
print(confusion_matrix(y1, y2))
print("standard_deviation: ")
print(standard_deviation(y2))
print("R_square: ")
print(R_square(y1, y2))
print("\n\n")
# for second
print("========== 2ND PART ==========")
b12_neu_list = []
b12_deno_list = []
b22_neu_list = []
b22_deno_list = []
b32_neu_list = []
b32_deno_list = []
b42_neu_list = []
b42_deno_list = []
for i in range(len(s12)):
    b12_neu_list.append((state2[i]-state_average_list_average) * (crime2[i]-crime_average_list_average))
    b12_deno_list.append((state2[i]-state_average_list_average) *  (state2[i]-state_average_list_average))
    b22_neu_list.append((population2[i]-population_average_list_average) * (crime2[i]-crime_average_list_average))
    b22_deno_list.append((population2[i]-population_average_list_average) *  (population2[i]-population_average_list_average))
    b32_neu_list.append((edu2[i]-education_average_list_average) * (crime2[i]-crime_average_list_average))
    b32_deno_list.append((edu2[i]-education_average_list_average) * (edu2[i]-education_average_list_average))
    b42_neu_list.append((unemploy2[i]-unemploy_average_list_average) * (crime2[i]-crime_average_list_average))
    b42_deno_list.append((unemploy2[i]-unemploy_average_list_average) * (unemploy2[i]-unemploy_average_list_average))
sum_b12_neu_list = sum(b12_neu_list)
sum_b12_deno_list = sum(b12_deno_list)
b1_b12 = sum_b12_neu_list/sum_b12_deno_list
#print('b1_b12 value is: ', round(b1_b12, 2))
sum_b22_neu_list = sum(b22_neu_list)
sum_b22_deno_list = sum(b22_deno_list)
b2_b22 = sum_b22_neu_list/sum_b22_deno_list
#print('b2_b22 value is: ', round(b2_b22, 2))
sum_b32_neu_list = sum(b32_neu_list)
sum_b32_deno_list = sum(b32_deno_list)
b3_b32 = sum_b32_neu_list/sum_b32_deno_list
#print('b3_b32 value is: ', round(b3_b32, 2))
sum_b42_neu_list = sum(b42_neu_list)
sum_b42_deno_list = sum(b42_deno_list)
b4_b42 = sum_b42_neu_list/sum_b42_deno_list
#print('b4_b42 value is: ', round(b4_b42, 2))
sum_state2_list = sum(state2)
sum_popuulation2_list = sum(population2)
sum_education2_list = sum(edu2)
sum_crime2_list = sum(crime2)
state_state_list = []
crime2_crime2_list = []
state2_crime2_list = []
for i in range(len(s12)):
    state_state_list.append(state2[i]*state2[i])
    crime2_crime2_list.append(crime2[i]*crime2[i])
    state2_crime2_list.append(state2[i]*crime2[i])
sum_state2_state2 = sum(state_state_list)
sum_crime2_crime2 = sum(crime2_crime2_list)
sum_state2_crime2 = sum(state2_crime2_list)
# a2
a2 = ((sum_crime2_list*sum_state2_state2)-(sum_state2_list*sum_state2_crime2))/((len(s12)*sum_state2_state2)-(sum_state2_list*sum_state2_list))
#print('a2 value is: ', round(a2, 2))
y2 = []
y1 = []
for i in range(len(s2)):
    y1.append(crime_list[i])
    y = a2+b1_b12*state2[i]+b2_b22*population2[i] +  b3_b32*edu2[i]+b4_b42*unemploy2[i]
    y2.append(y)
# for i in range(len(y1):
#    print(round(y2[i], 2), "     ", y1[i])
d = 0
for i in range(len(y1)):
    if abs(y1[i]-y2[i] <= 0.2):
        d += 1
print('value of d is: ', d)
print('Accuracy rate is: ', round(d/len(y1)*100, 2))
print("Confusion Matrix is: ")
print(confusion_matrix(y1, y2))
print("standard_deviation: ")
print(standard_deviation(y2))
print("R_square: ")
print(R_square(y1, y2))
print("\n\n")
print("========== 3RD PART ==========")
b13_neu_list = []
b13_deno_list = []
b23_neu_list = []
b23_deno_list = []
b33_neu_list = []
b33_deno_list = []
b43_neu_list = []
b43_deno_list = []
for i in range(len(s13)):
    b13_neu_list.append((state3[i]-state_average_list_average) * (crime3[i]-crime_average_list_average))
    b13_deno_list.append((state3[i]-state_average_list_average) * (state3[i]-state_average_list_average))
    b23_neu_list.append((population3[i]-population_average_list_average) * (crime3[i]-crime_average_list_average))
    b23_deno_list.append((population3[i]-population_average_list_average) * (population3[i]-population_average_list_average))
    b33_neu_list.append((edu3[i]-education_average_list_average) * (crime3[i]-crime_average_list_average))
    b33_deno_list.append((edu3[i]-education_average_list_average) * (edu3[i]-education_average_list_average))
    b43_neu_list.append((unemploy3[i]-unemploy_average_list_average) * (crime3[i]-crime_average_list_average))
    b43_deno_list.append((unemploy3[i]-unemploy_average_list_average) * (unemploy3[i]-unemploy_average_list_average))
sum_b13_neu_list = sum(b13_neu_list)
sum_b13_deno_list = sum(b13_deno_list)
b1_b13 = sum_b13_neu_list/sum_b13_deno_list
#print('b1_b13 value is: ', round(b1_b13, 2))
sum_b23_neu_list = sum(b23_neu_list)
sum_b23_deno_list = sum(b23_deno_list)
b2_b23 = sum_b23_neu_list/sum_b23_deno_list
#print('b2_b23 value is: ', round(b2_b23, 2))
sum_b33_neu_list = sum(b33_neu_list)
sum_b33_deno_list = sum(b33_deno_list)
b3_b33 = sum_b33_neu_list/sum_b33_deno_list
#print('b3_b33 value is: ', round(b3_b33, 2))
sum_b43_neu_list = sum(b43_neu_list)
sum_b43_deno_list = sum(b43_deno_list)
b4_b43 = sum_b43_neu_list/sum_b43_deno_list
#print('b4_b41 value is: ', round(b4_b43, 2))
sum_state3_list = sum(state3)
sum_popuulation3_list = sum(population3)
sum_education3_list = sum(edu3)
sum_crime3_list = sum(crime3)
state_state_list = []
crime3_crime3_list = []
state3_crime3_list = []
for i in range(len(s13)):
    state_state_list.append(state3[i]*state3[i])
    crime3_crime3_list.append(crime3[i]*crime3[i])
    state3_crime3_list.append(state3[i]*crime3[i])
sum_state3_state3 = sum(state_state_list)
sum_crime3_crime3 = sum(crime3_crime3_list)
sum_state3_crime3 = sum(state3_crime3_list)
# a3
a3 = ((sum_crime3_list*sum_state3_state3)-(sum_state3_list*sum_state3_crime3))/((len(s13)*sum_state3_state3)-(sum_state3_list*sum_state3_list))
#print('a3 value is: ', round(a3, 2))
y2 = []
y1 = []
for i in range(len(s3)):
    y1.append(crime_list[i])
    y = a3+b1_b13*state3[i]+b2_b23*population3[i] + b3_b33*edu3[i]+b4_b43*unemploy3[i]
    y2.append(y)
# for i in range(len(y1)):
#    print(round(y2[i], 2), "     ", y1[i])
d = 0
for i in range(len(y1)):
    if abs(y1[i]-y2[i] <= 0.2):
        d += 1
print('value of d is: ', d)
print('Accuracy rate is: ', round(d/len(y1)*100, 2))
print("Confusion Matrix is: ")
print(confusion_matrix(y1, y2))
print("standard_deviation: ")
print(standard_deviation(y2))
print("R_square: ")
print(R_square(y1, y2))
print("\n\n")
print("========== 4TH PART ==========")
b14_neu_list = []
b14_deno_list = []
b24_neu_list = []
b24_deno_list = []
b34_neu_list = []
b34_deno_list = []
b44_neu_list = []
b44_deno_list = []
for i in range(len(s14)):
    b14_neu_list.append((state4[i]-state_average_list_average) * (crime4[i]-crime_average_list_average))
    b14_deno_list.append((state4[i]-state_average_list_average) * (state4[i]-state_average_list_average))
    b24_neu_list.append((population4[i]-population_average_list_average) * (crime4[i]-crime_average_list_average))
    b24_deno_list.append((population4[i]-population_average_list_average) * (population4[i]-population_average_list_average))
    b34_neu_list.append((edu4[i]-education_average_list_average) * (crime4[i]-crime_average_list_average))
    b34_deno_list.append((edu4[i]-education_average_list_average) * (edu4[i]-education_average_list_average))
    b44_neu_list.append((unemploy4[i]-unemploy_average_list_average) * (crime4[i]-crime_average_list_average))
    b44_deno_list.append((unemploy4[i]-unemploy_average_list_average) * (unemploy4[i]-unemploy_average_list_average))
sum_b14_neu_list = sum(b14_neu_list)
sum_b14_deno_list = sum(b14_deno_list)
b1_b14 = sum_b14_neu_list/sum_b14_deno_list
#print('b1_b14 value is: ', round(b1_b14, 2))
sum_b24_neu_list = sum(b24_neu_list)
sum_b24_deno_list = sum(b24_deno_list)
b2_b24 = sum_b24_neu_list/sum_b24_deno_list
#print('b2_b24 value is: ', round(b2_b24, 2))
sum_b34_neu_list = sum(b34_neu_list)
sum_b34_deno_list = sum(b34_deno_list)
b3_b34 = sum_b34_neu_list/sum_b34_deno_list
#print('b3_b34 value is: ', round(b3_b34, 2))
sum_b44_neu_list = sum(b44_neu_list)
sum_b44_deno_list = sum(b44_deno_list)
b4_b44 = sum_b44_neu_list/sum_b44_deno_list
#print('b4_b44 value is: ', round(b4_b44, 2))
sum_state4_list = sum(state4)
sum_popuulation4_list = sum(population4)
sum_education4_list = sum(edu4)
sum_crime4_list = sum(crime4)
state_state_list = []
crime4_crime4_list = []
state4_crime4_list = []
for i in range(len(s14)):
    state_state_list.append(state4[i]*state4[i])
    crime4_crime4_list.append(crime4[i]*crime4[i])
    state4_crime4_list.append(state4[i]*crime4[i])
sum_state4_state4 = sum(state_state_list)
sum_crime4_crime4 = sum(crime4_crime4_list)
sum_state4_crime4 = sum(state4_crime4_list)
# a4
a4 = ((sum_crime4_list*sum_state4_state4)-(sum_state4_list*sum_state4_crime4))/((len(s14)*sum_state4_state4)-(sum_state4_list*sum_state4_list))
#print('a4 value is: ', round(a4, 2))
y2 = []
y1 = []
for i in range(len(s4)):
    y1.append(crime_list[i])
    y = a4+b1_b14*state4[i]+b2_b24*population4[i] +  b3_b34*edu4[i]+b4_b44*unemploy4[i]
    y2.append(y)
# for i in range(len(y1)):
#    print(round(y2[i], 2), "     ", y1[i])
d = 0
for i in range(len(y1)):
    if abs(y1[i]-y2[i] <= 0.2):
        d += 1
print('value of d is: ', d)
print('Accuracy rate is: ', round(d/len(y1)*100, 2))
print("Confusion Matrix is: ")
print(confusion_matrix(y1, y2))
print("standard_deviation: ")
print(standard_deviation(y2))
print("R_square: ")
print(R_square(y1, y2))
print("\n\n")
print("========== 5TH PART ==========")
b15_neu_list = []
b15_deno_list = []
b25_neu_list = []
b25_deno_list = []
b35_neu_list = []
b35_deno_list = []
b45_neu_list = []
b45_deno_list = []
for i in range(len(s15)):
    b15_neu_list.append((state5[i]-state_average_list_average) * (crime5[i]-crime_average_list_average))
    b15_deno_list.append((state5[i]-state_average_list_average) * (state5[i]-state_average_list_average))
    b25_neu_list.append((population5[i]-population_average_list_average) * (crime5[i]-crime_average_list_average))
    b25_deno_list.append((population5[i]-population_average_list_average) * (population5[i]-population_average_list_average))
    b35_neu_list.append((edu5[i]-education_average_list_average) * (crime5[i]-crime_average_list_average))
    b35_deno_list.append( (edu5[i]-education_average_list_average) * (edu5[i]-education_average_list_average))
    b45_neu_list.append((unemploy5[i]-unemploy_average_list_average) * (crime5[i]-crime_average_list_average))
    b45_deno_list.append((unemploy5[i]-unemploy_average_list_average) * (unemploy5[i]-unemploy_average_list_average))
sum_b15_neu_list = sum(b15_neu_list)
sum_b15_deno_list = sum(b15_deno_list)
b1_b15 = sum_b15_neu_list/sum_b15_deno_list
#print('b1_b15 value is: ', round(b1_b15, 2))
sum_b25_neu_list = sum(b25_neu_list)
sum_b25_deno_list = sum(b25_deno_list)
b2_b25 = sum_b25_neu_list/sum_b25_deno_list
#print('b2_b25 value is: ', round(b2_b25, 2))
sum_b35_neu_list = sum(b35_neu_list)
sum_b35_deno_list = sum(b35_deno_list)
b3_b35 = sum_b35_neu_list/sum_b35_deno_list
#print('b3_b35 value is: ', round(b3_b35, 2))
sum_b45_neu_list = sum(b45_neu_list)
sum_b45_deno_list = sum(b45_deno_list)
b4_b45 = sum_b45_neu_list/sum_b45_deno_list
#print('b4_b45 value is: ', round(b4_b45, 2))
# sum of state5[i]
sum_state5_list = sum(state5)
sum_popuulation5_list = sum(population5)
sum_education5_list = sum(edu5)
sum_crime5_list = sum(crime5)
state_state_list = []
crime5_crime5_list = []
state5_crime5_list = []
for i in range(len(s15)):
    state_state_list.append(state5[i]*state5[i])
    crime5_crime5_list.append(crime5[i]*crime5[i])
    state5_crime5_list.append(state5[i]*crime5[i])
sum_state5_state5 = sum(state_state_list)
sum_crime5_crime5 = sum(crime5_crime5_list)
sum_state5_crime5 = sum(state5_crime5_list)
# a5
a5 = ((sum_crime5_list*sum_state5_state5)-(sum_state5_list*sum_state5_crime5))/((len(s15)*sum_state5_state5)-(sum_state5_list*sum_state5_list))
#print('a5 value is: ', round(a5, 2))
y2 = []
y1 = []
for i in range(len(s5)):
    y1.append(crime_list[i])
    y = a5+b1_b15*state5[i]+b2_b25*population5[i] + b3_b35*edu5[i]+b4_b45*unemploy5[i]
    y2.append(y)
# for i in range(len(y1)):
#    print(round(y2[i], 2), "     ", y1[i])
d = 0
for i in range(len(y1)):
    if abs(y1[i]-y2[i] <= 0.2):
        d += 1
print('value of d is: ', d)
print('Accuracy rate is: ', round(d/len(y1)*100, 2))
print("Confusion Matrix is: ")
print(confusion_matrix(y1, y2))
print("standard_deviation: ")
print(standard_deviation(y2))
print("R_square: ")
print(R_square(y1, y2))
print("\n\n")
print("========== 6TH PART ==========")
b16_neu_list = []
b16_deno_list = []
b26_neu_list = []
b26_deno_list = []
b36_neu_list = []
b36_deno_list = []
b46_neu_list = []
b46_deno_list = []
for i in range(len(s16)):
    b16_neu_list.append((state6[i]-state_average_list_average) * (crime6[i]-crime_average_list_average))
    b16_deno_list.append((state6[i]-state_average_list_average) * (state6[i]-state_average_list_average))
    b26_neu_list.append((population6[i]-population_average_list_average) * (crime6[i]-crime_average_list_average))
    b26_deno_list.append( (population6[i]-population_average_list_average) * (population6[i]-population_average_list_average))
    b36_neu_list.append((edu6[i]-education_average_list_average) * (crime6[i]-crime_average_list_average))
    b36_deno_list.append((edu6[i]-education_average_list_average) * (edu6[i]-education_average_list_average))
    b46_neu_list.append((unemploy6[i]-unemploy_average_list_average) * (crime6[i]-crime_average_list_average))
    b46_deno_list.append((unemploy6[i]-unemploy_average_list_average) * (unemploy6[i]-unemploy_average_list_average))
sum_b16_neu_list = sum(b16_neu_list)
sum_b16_deno_list = sum(b16_deno_list)
b1_b16 = sum_b16_neu_list/sum_b16_deno_list
#print('b1_b16 value is: ', round(b1_b16, 2))
sum_b26_neu_list = sum(b26_neu_list)
sum_b26_deno_list = sum(b26_deno_list)
b2_b26 = sum_b26_neu_list/sum_b26_deno_list
#print('b2_b26 value is: ', round(b2_b26, 2))
sum_b36_neu_list = sum(b36_neu_list)
sum_b36_deno_list = sum(b36_deno_list)
b3_b36 = sum_b36_neu_list/sum_b36_deno_list
#print('b3_b36 value is: ', round(b3_b36, 2))
sum_b46_neu_list = sum(b46_neu_list)
sum_b46_deno_list = sum(b46_deno_list)
b4_b46 = sum_b46_neu_list/sum_b46_deno_list
#print('b4_b46 value is: ', round(b4_b46, 2))
sum_state6_list = sum(state6)
sum_popuulation6_list = sum(population6)
sum_education6_list = sum(edu6)
sum_crime6_list = sum(crime6)
state_state_list = []
crime6_crime6_list = []
state6_crime6_list = []
for i in range(len(s16)):
    state_state_list.append(state6[i]*state6[i])
    crime6_crime6_list.append(crime6[i]*crime6[i])
    state6_crime6_list.append(state6[i]*crime6[i])
sum_state6_state6 = sum(state_state_list)
sum_crime6_crime6 = sum(crime6_crime6_list)
sum_state6_crime6 = sum(state6_crime6_list)
# a6
a6 = ((sum_crime6_list*sum_state6_state6)-(sum_state6_list*sum_state6_crime6))/((len(s16)*sum_state6_state6)-(sum_state6_list*sum_state6_list))
#print('a6 value is: ', round(a6, 2))
y2 = []
y1 = []
for i in range(len(s6)):
    y1.append(crime_list[i])
    y = a6+b1_b16*state6[i]+b2_b26*population6[i] +  b3_b36*edu6[i]+b4_b46*unemploy6[i]
    y2.append(y)
# for i in range(len(y1)):
#    print(round(y2[i], 2), "     ", y1[i])
d = 0
for i in range(len(y1)):
    if abs(y1[i]-y2[i] <= 0.2):
        d += 1
print('value of d is: ', d)
print('Accuracy rate is: ', round(d/len(y1)*100, 2))
print("Confusion Matrix is: ")
print(confusion_matrix(y1, y2))
print("standard_deviation: ")
print(standard_deviation(y2))
print("R_square: ")
print(R_square(y1, y2))
print("\n\n")
print("========== 7TH PART ==========")
b17_neu_list = []
b17_deno_list = []
b27_neu_list = []
b27_deno_list = []
b37_neu_list = []
b37_deno_list = []
b47_neu_list = []
b47_deno_list = []
for i in range(len(s17)):
    b17_neu_list.append((state7[i]-state_average_list_average) * (crime7[i]-crime_average_list_average))
    b17_deno_list.append((state7[i]-state_average_list_average) * (state7[i]-state_average_list_average))
    b27_neu_list.append((population7[i]-population_average_list_average) *  (crime7[i]-crime_average_list_average))
    b27_deno_list.append((population7[i]-population_average_list_average) * (population7[i]-population_average_list_average))
    b37_neu_list.append((edu7[i]-education_average_list_average) *  (crime7[i]-crime_average_list_average))
    b37_deno_list.append((edu7[i]-education_average_list_average) *  (edu7[i]-education_average_list_average))
    b47_neu_list.append((unemploy7[i]-unemploy_average_list_average) * (crime7[i]-crime_average_list_average))
    b47_deno_list.append((unemploy7[i]-unemploy_average_list_average) * (unemploy7[i]-unemploy_average_list_average))
sum_b17_neu_list = sum(b17_neu_list)
sum_b17_deno_list = sum(b17_deno_list)
b1_b17 = sum_b17_neu_list/sum_b17_deno_list
#print('b1_b17 value is: ', round(b1_b17, 2))
sum_b27_neu_list = sum(b27_neu_list)
sum_b27_deno_list = sum(b27_deno_list)
b2_b27 = sum_b27_neu_list/sum_b27_deno_list
#print('b2_b27 value is: ', round(b2_b27, 2))
sum_b37_neu_list = sum(b37_neu_list)
sum_b37_deno_list = sum(b37_deno_list)
b3_b37 = sum_b37_neu_list/sum_b37_deno_list
#print('b3_b37 value is: ', round(b3_b37, 2))
sum_b47_neu_list = sum(b47_neu_list)
sum_b47_deno_list = sum(b47_deno_list)
b4_b47 = sum_b46_neu_list/sum_b47_deno_list
#print('b4_b47 value is: ', round(b4_b47, 2))

sum_state7_list = sum(state7)
sum_popuulation7_list = sum(population7)
sum_education7_list = sum(edu7)
sum_crime7_list = sum(crime7)
state_state_list = []
crime7_crime7_list = []
state7_crime7_list = []
for i in range(len(s17)):
    state_state_list.append(state7[i]*state7[i])
    crime7_crime7_list.append(crime7[i]*crime7[i])
    state7_crime7_list.append(state7[i]*crime7[i])
sum_state7_state7 = sum(state_state_list)
sum_crime7_crime7 = sum(crime7_crime7_list)
sum_state7_crime7 = sum(state7_crime7_list)
# a7
a7 = ((sum_crime7_list*sum_state7_state7)-(sum_state7_list*sum_state7_crime7))/((len(s17)*sum_state7_state7)-(sum_state7_list*sum_state7_list))
#print('a7 value is: ', round(a7, 2))
y2 = []
y1 = []
for i in range(len(s7)):
    y1.append(crime_list[i])
    y = a7+b1_b17*state7[i]+b2_b27*population7[i] +  b3_b37*edu7[i]+b4_b47*unemploy7[i]
    y2.append(y)
# for i in range(len(y1)):
#    print(round(y2[i], 2), "     ", y1[i])
d = 0
for i in range(len(y1)):
    if abs(y1[i]-y2[i] <= 0.2):
        d += 1
print('value of d is: ', d)
print('Accuracy rate is: ', round(d/len(y1)*100, 2))
print("Confusion Matrix is: ")
print(confusion_matrix(y1, y2))
print("standard_deviation: ")
print(standard_deviation(y2))
print("R_square: ")
print(R_square(y1, y2))
print("\n\n")
print("============= 8TH PART =============")
b18_neu_list = []
b18_deno_list = []
b28_neu_list = []
b28_deno_list = []
b38_neu_list = []
b38_deno_list = []
b48_neu_list = []
b48_deno_list = []
for i in range(len(s18)):
    b18_neu_list.append((state8[i]-state_average_list_average) *  (crime8[i]-crime_average_list_average))
    b18_deno_list.append((state8[i]-state_average_list_average)*(state8[i]-state_average_list_average))
    b28_neu_list.append((population8[i]-population_average_list_average) *  (crime8[i]-crime_average_list_average))
    b28_deno_list.append((population8[i]-population_average_list_average) * (population8[i]-population_average_list_average))
    b38_neu_list.append((edu8[i]-education_average_list_average) * (crime8[i]-crime_average_list_average))
    b38_deno_list.append((edu8[i]-education_average_list_average) * (edu8[i]-education_average_list_average))
    b48_neu_list.append((unemploy8[i]-unemploy_average_list_average) * (crime8[i]-crime_average_list_average))
    b48_deno_list.append((unemploy8[i]-unemploy_average_list_average) *  (unemploy8[i]-unemploy_average_list_average))
sum_b18_neu_list = sum(b18_neu_list)
sum_b18_deno_list = sum(b18_deno_list)
b1_b18 = sum_b18_neu_list/sum_b18_deno_list
#print('b1_b18 value is: ', round(b1_b18, 2))
sum_b28_neu_list = sum(b28_neu_list)
sum_b28_deno_list = sum(b28_deno_list)
b2_b28 = sum_b28_neu_list/sum_b28_deno_list
#print('b2_b28 value is: ', round(b2_b28, 2))
sum_b38_neu_list = sum(b38_neu_list)
sum_b38_deno_list = sum(b38_deno_list)
b3_b38 = sum_b38_neu_list/sum_b38_deno_list
#print('b3_b38 value is: ', round(b3_b38, 2))
sum_b48_neu_list = sum(b48_neu_list)
sum_b48_deno_list = sum(b48_deno_list)
b4_b48 = sum_b48_neu_list/sum_b48_deno_list
#print('b4_b48 value is: ', round(b4_b48, 2))
sum_state8_list = sum(state8)
sum_popuulation8_list = sum(population8)
sum_education8_list = sum(edu8)
sum_crime8_list = sum(crime8)
state_state_list = []
crime8_crime8_list = []
state8_crime8_list = []
for i in range(len(s18)):
    state_state_list.append(state8[i]*state8[i])
    crime8_crime8_list.append(crime8[i]*crime8[i])
    state8_crime8_list.append(state8[i]*crime8[i])
sum_state8_state8 = sum(state_state_list)
sum_crime8_crime8 = sum(crime8_crime8_list)
sum_state8_crime8 = sum(state8_crime8_list)
# a8
a8 = ((sum_crime8_list*sum_state8_state8)-(sum_state8_list*sum_state8_crime8))/((len(s18)*sum_state8_state8)-(sum_state8_list*sum_state8_list))
#print('a8 value is: ', round(a8, 2))
y2 = []
y1 = []
for i in range(len(s8)):
    y1.append(crime_list[i])
    y = a8+b1_b18*state8[i]+b2_b28*population8[i] + b3_b38*edu8[i]+b4_b48*unemploy8[i]
    y2.append(y)
# for i in range(len(y1)):
#    print(round(y2[i], 2), "     ", y1[i])
d = 0
for i in range(len(y1)):
    if abs(y1[i]-y2[i] <= 0.2):
        d += 1
print('value of d is: ', d)
print('Accuracy rate is: ', round(d/len(y1)*100, 2))
print("Confusion Matrix is: ")
print(confusion_matrix(y1, y2))
print("standard_deviation: ")
print(standard_deviation(y2))
print("R_square: ")
print(R_square(y1, y2))
print("\n\n")
print("=========== 9TH PART ===========")
b19_neu_list = []
b19_deno_list = []
b29_neu_list = []
b29_deno_list = []
b39_neu_list = []
b39_deno_list = []
b49_neu_list = []
b49_deno_list = []
for i in range(len(s19)):
    b19_neu_list.append((state9[i]-state_average_list_average) *  (crime9[i]-crime_average_list_average))
    b19_deno_list.append((state9[i]-state_average_list_average) *  (state9[i]-state_average_list_average))
    b29_neu_list.append((population9[i]-population_average_list_average) * (crime9[i]-crime_average_list_average))
    b29_deno_list.append((population9[i]-population_average_list_average) * (population9[i]-population_average_list_average))
    b39_neu_list.append((edu9[i]-education_average_list_average) *   (crime9[i]-crime_average_list_average))
    b39_deno_list.append((edu9[i]-education_average_list_average) *  (edu9[i]-education_average_list_average))
    b49_neu_list.append((unemploy9[i]-unemploy_average_list_average) *  (crime9[i]-crime_average_list_average))
    b49_deno_list.append((unemploy9[i]-unemploy_average_list_average) *  (unemploy9[i]-unemploy_average_list_average))
sum_b19_neu_list = sum(b19_neu_list)
sum_b19_deno_list = sum(b19_deno_list)
b1_b19 = sum_b19_neu_list/sum_b19_deno_list
#print('b1_b19 value is: ', round(b1_b19, 2))
sum_b29_neu_list = sum(b29_neu_list)
sum_b29_deno_list = sum(b29_deno_list)
b2_b29 = sum_b29_neu_list/sum_b29_deno_list
#print('b2_b29 value is: ', round(b2_b29, 2))
sum_b39_neu_list = sum(b39_neu_list)
sum_b39_deno_list = sum(b39_deno_list)
b3_b39 = sum_b39_neu_list/sum_b39_deno_list
#print('b3_b39 value is: ', round(b3_b39, 2))
sum_b49_neu_list = sum(b49_neu_list)
sum_b49_deno_list = sum(b49_deno_list)
b4_b49 = sum_b49_neu_list/sum_b49_deno_list
#print('b4_b49 value is: ', round(b4_b49, 2))
sum_state9_list = sum(state9)
sum_popuulation9_list = sum(population9)
sum_education9_list = sum(edu9)
sum_crime9_list = sum(crime9)
state_state_list = []
crime9_crime9_list = []
state9_crime9_list = []
for i in range(len(s19)):
    state_state_list.append(state9[i]*state9[i])
    crime9_crime9_list.append(crime9[i]*crime9[i])
    state9_crime9_list.append(state9[i]*crime9[i])
sum_state9_state9 = sum(state_state_list)
sum_state9_crime9 = sum(state9_crime9_list)
sum_crime9_crime9 = sum(crime9_crime9_list)
#a9
a9 = ((sum_crime9_list*sum_state9_state9)-(sum_state9_list*sum_state9_crime9))/((len(s19)*sum_state9_state9)-(sum_state9_list*sum_state9_list))
#print('a9 value is: ', round(a9, 2))
y2 = []
y1 = []
for i in range(len(s9)):
    y1.append(crime_list[i])
    y = a9+b1_b19*state9[i]+b2_b29*population9[i] +  b3_b39*edu9[i]+b4_b49*unemploy9[i]
    y2.append(y)
# for i in range(len(y1)):
#    print(round(y2[i], 2), "     ", y1[i])
d = 0
for i in range(len(y1)):
    if abs(y1[i]-y2[i] <= 0.2):
        d += 1
print('value of d is: ', d)
print('Accuracy rate is: ', round(d/len(y1)*100, 2))
print("Confusion Matrix is: ")
print(confusion_matrix(y1, y2))
print("standard_deviation: ")
print(standard_deviation(y2))
print("R_square: ")
print(R_square(y1, y2))
print("\n\n")
print("=========== 10TH PART ===========")
b110_neu_list = []
b110_deno_list = []
b210_neu_list = []
b210_deno_list = []
b310_neu_list = []
b310_deno_list = []
b410_neu_list = []
b410_deno_list = []
for i in range(len(s20)):
    b110_neu_list.append((state10[i]-state_average_list_average) * (crime10[i]-crime_average_list_average))
    b110_deno_list.append((state10[i]-state_average_list_average) * (state10[i]-state_average_list_average))
    b210_neu_list.append((population10[i]-population_average_list_average) * (crime10[i]-crime_average_list_average))
    b210_deno_list.append((population10[i]-population_average_list_average) * (population10[i]-population_average_list_average))
    b310_neu_list.append((edu10[i]-education_average_list_average) * (crime10[i]-crime_average_list_average))
    b310_deno_list.append((edu10[i]-education_average_list_average) * (edu10[i]-education_average_list_average))
    b410_neu_list.append((unemploy10[i]-unemploy_average_list_average) *  (crime10[i]-crime_average_list_average))
    b410_deno_list.append((unemploy10[i]-unemploy_average_list_average) * (unemploy10[i]-unemploy_average_list_average))
sum_b110_neu_list = sum(b110_neu_list)
sum_b110_deno_list = sum(b110_deno_list)
b1_b110 = sum_b19_neu_list/sum_b110_deno_list
#print('b1_b110 value is: ', round(b1_b110, 2))
sum_b210_neu_list = sum(b210_neu_list)
sum_b210_deno_list = sum(b210_deno_list)
b2_b210 = sum_b210_neu_list/sum_b210_deno_list
#print('b2_b210 value is: ', round(b2_b210, 2))
sum_b310_neu_list = sum(b310_neu_list)
sum_b310_deno_list = sum(b310_deno_list)
b3_b310 = sum_b310_neu_list/sum_b310_deno_list
#print('b3_b310 value is: ', round(b3_b310, 2))
sum_b410_neu_list = sum(b410_neu_list)
sum_b410_deno_list = sum(b410_deno_list)
b4_b410 = sum_b410_neu_list/sum_b410_deno_list
#print('b4_b410 value is: ', round(b4_b410, 2))
sum_state10_list = sum(state10)
sum_popuulation10_list = sum(population10)
sum_education10_list = sum(edu10)
sum_crime10_list = sum(crime10)
state_state_list = []
crime10_crime10_list = []
state10_crime10_list = []
for i in range(len(s20)):
    state_state_list.append(state10[i]*state10[i])
    crime10_crime10_list.append(crime10[i]*crime10[i])
    state10_crime10_list.append(state10[i]*crime10[i])
sum_state10_state10 = sum(state_state_list)
sum_crime10_crime10 = sum(crime10_crime10_list)
sum_state10_crime10 = sum(state10_crime10_list)
# a10
a10 = ((sum_crime10_list*sum_state10_state10)-(sum_state10_list*sum_state10_crime10))/((len(s20)*sum_state10_state10)-(sum_state10_list*sum_state10_list))
#print('a10 value is: ', round(a10, 2))
y2 = []
y1 = []
for i in range(len(s10)):
    y1.append(crime_list[i])
    y = a10+b1_b110*state10[i]+b2_b210*population10[i] + b3_b310*edu10[i]+b4_b410*unemploy10[i]
    y2.append(y)
# for i in range(len(y1)):
#    print(round(y2[i], 2), "     ", y1[i])
d = 0
for i in range(len(y1)):
    if abs(y1[i]-y2[i] <= 0.2):
        d += 1
print('value of d is: ', d)
print('Accuracy rate is: ', round(d/len(y1)*100, 2))
print("Confusion Matrix is: ")
print(confusion_matrix(y1, y2))
print("standard_deviation: ")
print(standard_deviation(y2))
print("R_square: ")
print(R_square(y1, y2))
print("\n\n")
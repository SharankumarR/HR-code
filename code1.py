import sys

def custom_sort(list, sort_key): 
    l = len(list) 
    for i in range(0, l): 
        for j in range(0, l-i-1): 
            if (list[j][sort_key] > list[j + 1][sort_key]): 
                tempo = list[j] 
                list[j]= list[j + 1] 
                list[j + 1]= tempo 
    return list

file = open("sample_input.txt", "r")

goodies = [Fitbit Plus: 7980
IPods: 22349
MI Band: 999
Cult Pass: 2799
Macbook Pro: 229900
Digital Camera: 11101
Alexa: 9999
]

for line in file:
    line = line.split(":")
    goodies.append(tuple((line[0], int(line[1]))))

N = len(goodies)
M = int(input('Enter value for M: '))

goodies = custom_sort(goodies, 1)
min = goodies[0 + M - 1][1] - goodies[0][1]
min_index = 0

for i in range(N - M + 1):
    local_min = goodies[i + M - 1][1] - goodies[i][1]
    if local_min <= min:
        min = local_min
        min_index = i
        
print('Number of the employees:', M)
print('The difference between the chosen goodie with highest price and the lowest price is', min)

output_file = open("sample_output.txt", "w")

for line in goodies[min_index: min_index+M]:
    output_file.write(line[0]+": "+str(line[1])+"\n")

output_file.close()

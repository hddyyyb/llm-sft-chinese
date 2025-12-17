'''In Amazon's Smart Cities Management System, each city has a given population and some cities are equipped with security units.
You are given:
An integer array population of size n, where population[i] is the number of inhabitants in the i^{th} city.
A binary string unit of length n, where unit[i]='1' means city i has a security unit, and '0' means it does not.

Relocation Rule:
A security unit at city i (where i>1) can be moved one step to the left to city i-1.
Each unit can be moved at most once.
If moved, city i loses its unit and city i- 1 gains one.
City 1 security unit cannot be moved further left.

A city is protected if it has a security unit after all relocations.
Determine the maximum population that can be protected by optimally relocating the security units.

Note: The problem uses 1-based indexing, meaning city indices, the population array, and the unit binary string all start from l and go up to n, with each city having a corresponding entry in both the array and the string.

Example
n=5
population =[10,5,8,9,6]
unit ="01101"

Relocated Index (i): (i to17) | Previous Configuration | New Configuration | Safe Inhabitants
2 | 01101 | 10101 | 10+8+6 =24
5 | 10101 | 10110 | 10+8+9 = 27

Thus, 27 is the maximum number of inhabitants that can be protected. No other relocation strategy can yield a higher safe population than 27. Hence answer is 27.

Function Description
Complete the function moveUnits in the editor below.

moveUnits has the following parameters:
int population[n]: represents the population in each city
string unit: represents the initial configuration of the unit ("1" represents a unit is present in i^{th} city else not)

Returns
int: the maximum population that can be safe after moving some of the security units to their left
Constraints
1≤n≤10^5
1≤population[i] ≤ 10^4
string unit is a binary string consisting of "0"s and "1"s

Input Format for Custom Testing
The first line contains an integer n which represents the size of the array population.
Next n lines contain an integer population[i].
The last line contains a binary string unit of length n.



用如下python模板编写代码：
def moveUnits(population,unit):
#Write your code here

if __name__ == '__main__'：
  fptr= open(os.environ['OUTPUT PATH'].'w')
  population_count = int(input.strip())
  population = []
  for _ in range(population_count):
    population_item = int(input().strip())
    population.append(population_item) 
  unit = input()
  result = moveUnits(population,unit)
  fptr.write(str(result)+'\n')
  fptr.close()




Sample Case 0
Sample input 0
STDIN Function
6   -> population[] size n=6
20  -> population=[20，10，9，30，20，19
10
9
30
20
19
011011 -> unit = '011011'

Sample Output 0
80
'''
import matplotlib.pyplot as plt
import math

print("WELCOME TO IDOL GRAPHS!\nChoose equation to graph:\n1. x² + 7x + 2\n2. 3x + 2\n3. x²\n4. x³\n5. x⁵\n6. x³ + 2x² + x + 10\n7. x⁴ - 3x³ + 2x² - x + 11\n8. sin(x)\n9. cos(x)\n10. x⁵ + 4x⁴ + x³ - 2x² + 100\n0. ALL")
choice = int(input("Enter you choice: "))

xValues = []
with open("git-proj/xValues.txt", "r") as file:
  for line in file:
    xValues.append(int(line))

yValuesFile = open("git-proj/yValues.txt", "w")
yValuesFile.write("")
yValuesFile.close
yValuesFile = open("git-proj/yValues.txt", "a")

for num in range (1, 11):
  for x in xValues:
    if num == 1:
      yValuesFile.write(f"{x**2 + 7*x + 2}\n") #1
    elif num == 2:
      yValuesFile.write(f"{3*x + 2}\n") #2
    elif num == 3:
      yValuesFile.write(f"{x**2}\n") #3
    elif num == 4:
      yValuesFile.write(f"{x**3}\n") #4
    elif num == 5:
      yValuesFile.write(f"{x**5}\n") #5
    elif num == 6:
      yValuesFile.write(f"{x**3 + 2*(x**2) + x + 10}\n") #6
    elif num == 7:
      yValuesFile.write(f"{x**4 - 3*(x**3) + 2*(x**2) - x + 11}\n") #7
    elif num == 8:
      yValuesFile.write(f"{math.sin(math.radians(x))}\n") #8
    elif num == 9:
      yValuesFile.write(f"{math.cos(math.radians(x))}\n") #9
    elif num == 10:
      yValuesFile.write(f"{x**5 + 4*(x**4) + x**3 - 2*(x**2) + 100}\n") #10
yValuesFile.close()

def graphOne(start, end):
  yValues = []
  count = 0
  with open("git-proj/yValues.txt", "r") as file:
    for line in file:
      count = count + 1
      if count >= start and count < end:
        yValues.append(float(line))
  return yValues

match choice:
  case 1:
    plt.plot(xValues, graphOne(1, 51))
    plt.title("Graph for: x² + 7x + 2")
    plt.show()
  case 2:
    plt.plot(xValues, graphOne(51, 101))
    plt.title("Graph for: 3x + 2")
    plt.show()
  case 3:
    plt.plot(xValues, graphOne(101, 151))
    plt.title("Graph for: x²")
    plt.show()
  case 4:
    plt.plot(xValues, graphOne(151, 201))
    plt.title("Graph for: x³")    
    plt.show()
  case 5:
    plt.plot(xValues, graphOne(201, 251))
    plt.title("Graph for: x⁵")    
    plt.show()
  case 6:
    plt.plot(xValues, graphOne(251, 301))
    plt.title("Graph for: x³ + 2x² + x + 10")    
    plt.show()
  case 7:
    plt.plot(xValues, graphOne(301, 351))
    plt.title("Graph for: x⁴ - 3x³ + 2x² - x + 11")    
    plt.show()
  case 8:
    plt.plot(xValues, graphOne(351, 401))
    plt.title("Graph for: sin(x)")    
    plt.show()
  case 9:
    plt.plot(xValues, graphOne(401, 451))
    plt.title("Graph for: cos(x)")    
    plt.show()
  case 10:
    plt.plot(xValues, graphOne(451, 501))
    plt.title("Graph for: x⁵ + 4x⁴ + x³ - 2x² + 100")    
    plt.show()
  case 0:
    plt.plot(xValues, graphOne(1, 51), "#167288", label="equation 1")
    plt.plot(xValues, graphOne(51, 101), "#8cdaec", label="equation 2")
    plt.plot(xValues, graphOne(101, 151), "#b45248", label="equation 3")
    plt.plot(xValues, graphOne(151, 201), "#d48c84", label="equation 4")
    plt.plot(xValues, graphOne(201, 251), "#a89a49", label="equation 5")
    plt.plot(xValues, graphOne(251, 301), "#d6cfa2", label="equation 6")
    plt.plot(xValues, graphOne(301, 351), "#3cb464", label="equation 7")
    plt.plot(xValues, graphOne(351, 401), "#9bddb1", label="equation 8")
    plt.plot(xValues, graphOne(401, 451), "#643c6a", label="equation 9")
    plt.plot(xValues, graphOne(451, 501), "#836394", label="equation 10")
    plt.legend(loc="best")
    plt.title("Graph for all equations")
    plt.show()


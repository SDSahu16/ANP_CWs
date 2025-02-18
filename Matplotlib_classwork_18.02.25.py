import matplotlib.pyplot as plt

# Line Chart

x = ['A','B','C','D','E','F']
y = [98,87,48,91,92,89]
plt.plot(x,y, marker = '*')
plt.xlabel("Student's Name")
plt.ylabel("Marks")
plt.title("Line Chart showing test marks of various students")
plt.show()
#--------------------------------------------------------------------------------

# Bar Chart

plt.bar(x,y)
plt.xlabel("Student's Name")
plt.ylabel("Marks")
plt.title("Line Chart showing test marks of various students")
plt.show()
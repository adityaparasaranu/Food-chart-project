from matplotlib import pyplot as plt

labels = ["Carbohydrate", "Proteins", "Fats", "Vitamins and Minerals"]
plt.pie([60, 30, 5, 5], labels=labels, wedgeprops={"edgecolor": "black"}, autopct="%1.1f%%")
plt.title("Food Chart")
plt.show()

# from matplotlib import pyplot as plt
# fig = plt.figure()
# ax = fig.add_axes([0,0,1,1])
# ax.axis('equal')
# langs = ['C', 'C++', 'Java', 'Python', 'PHP']
# students = [23,17,35,29,12]
# ax.pie(students, labels = langs)
# plt.show()
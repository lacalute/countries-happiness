# import neccessary libraries
import csv
import matplotlib.pyplot as plt

# open the csv file
with open('hap.csv') as f:
    reader = csv.reader(f)
    x = list(reader)
    # a variable with titles 
    titles = x[0]
    # delete titles of csv file
    x.pop(0)

# collect countries 
countries = []
for a in range(0, len(x)):
    # a list with countries
    countries.append(x[a][1])


# the func, which collect data and after visualize them
def collect_data():
    years = []
    data = []
    for year in range(16, 23):
        years.append(int(f'20{year}'))
        data.append(res[titles.index(f'Score_20{year}')])

    # the func, which make the visualization
    def plotting():
        plt.style.use('ggplot')
        fig, ax = plt.subplots(2)
        fig.suptitle(user_country)
        ax[0].plot(data)
        ax[0].set_xlabel('Year')
        ax[0].set_ylabel('Rate of Happiness')
        ax[1].bar(years, data)
        ax[1].set_xlabel('Year')
        ax[1].set_ylabel('Rate of Happiness')
        plt.show()
    plotting()


# the main while loop, which start a program
status = True
print(countries)
while status:
    # asking user to type the country
    user_country = input('Enter the country: ')
    # find the neccessary array by user country
    for a in range(0, len(x)):
        if x[a][1] == user_country:
            # the result variable with data of user country
            res = x[a]
    if user_country in countries:
        collect_data()
        status = False
    else:
        print("Wrong country, again...")

# This program made by Lacalute !!!
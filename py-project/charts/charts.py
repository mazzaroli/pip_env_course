import matplotlib.pyplot as plt

def generate_pie_char():
    labels = ['a','b','c']
    values=[3,2,5]

    fig, ax = plt.subplots()
    ax.pie(values,labels=labels)
    plt.savefig('pie.png')
    plt.close()
    
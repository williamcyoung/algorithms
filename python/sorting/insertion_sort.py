'''
Python implementation of insertion sort with a matplotlib visual included.
'''

import matplotlib.pyplot as plt
import matplotlib.animation as anim

def insertion_sort(array):
    
    if (len(array)==1):
        return
    
    for j in range(1, len(array)):
        key = array[j]
        i = j - 1
        while i >= 0 and array[i] > key:
            array[i + 1] = array[i]
            i = i - 1
            yield array
        array[i + 1] = key
        yield array

arr = [5,3,6,7,1,9,4]
algo = insertion_sort(arr)

fig, ax = plt.subplots()
ax.set_title("Insertion Sort")
bar_rec = ax.bar(range(len(arr)), arr, align='edge')
text = ax.text(0.02, 0.95, "", transform=ax.transAxes)

epochs = [0]

def update_plot(array, rec, epochs):
    for rec, val in zip(rec, array):
        rec.set_height(val)
    epochs[0]+= 1
    text.set_text("No.of operations :{}".format(epochs[0]))

anima = anim.FuncAnimation(fig, func=update_plot, fargs=(bar_rec, epochs), frames=algo, interval=1000, repeat=False)
plt.show()
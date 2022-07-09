def bubble_sort(data):
    for i in range(len(data), 0, -1): # i = final
        changed = False
        # print(f'iterou {i}')
        for j in range(0, i - 1): # j = atual
            if data[j] > data[j + 1] :
                # temp = data[j]
                # data[j] = data[i]
                # data[i] = temp
                data[j], data[j + 1] = data[j + 1], data[j]
                changed = True
        
        if not changed:
            break
    return data

if __name__ == '__main__':
#    data = sorted([5, 3, 2, 1, 9, 4])
    data = [5, 3, 2, 1, 9, 4]
    bubble_sort(data)
    print(data)

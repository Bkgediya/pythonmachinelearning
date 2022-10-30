def average(x,y):
    return (x + y)/2


def stat(data):
    total_sum = 0

    # find the sum of all numbers
    for x in data:
        total_sum = total_sum + x

    #find the mean
    N = len(data)
    mean = total_sum / N

    return total_sum,mean

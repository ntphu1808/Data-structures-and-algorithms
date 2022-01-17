def fibonannci(index):
    if index<=2:
        return 1
    return fibonannci(index-2)+fibonannci(index-1)

def print_fibonanci(index):
    if index<=1:
        return "1"
    return f"{print_fibonanci(index-1)}->{fibonannci(index)}"

print(fibonannci(20))
print(print_fibonanci(20))
def distribution(chocolates,students):
    n=len(chocolates)
    if n<students:
        return -1,[]
    chocolates.sort()
    min_difference=float("inf")
    selected_chocolates=[]
    for i in range(n-students+1):
        difference = chocolates[i + students - 1] - chocolates[i]
        min_difference=min(min_difference,difference)
        selected_chocolates=chocolates[i:i+students]
    return min_difference, selected_chocolates
chocolates=[7, 3, 2, 4, 9, 12, 56]
min_difference,selected_chocolates=distribution(chocolates,3)
print(min_difference)
print(selected_chocolates)
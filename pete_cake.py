def cakes(recipe, available):
    maximum = 0
    for i in recipe:
        if i in available:
            if maximum == 0 or maximum > available[i] // recipe[i]:
                maximum = available[i] // recipe[i]
        else:
            return 0
    return maximum

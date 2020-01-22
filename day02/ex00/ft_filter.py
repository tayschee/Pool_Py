def ft_filter(function_to_apply, list_of_inputs):
    x = 0
    for i in list_of_inputs :
        list_of_inputs[x] = function_to_apply(i)
        x = x + 1
    return (list_of_inputs)

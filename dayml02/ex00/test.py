from sigmoid import sigmoid_
x = -4
print(type(x))
print(sigmoid_(x))
# 0.01798620996209156
x= 2
print(sigmoid_(x))
# 0.8807970779778823
x = [-4, 2, 0]
print(sigmoid_(x))
# [0.01798620996209156, 0.8807970779778823, 0.5]

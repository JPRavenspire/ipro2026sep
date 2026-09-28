# Comparison/Relational Operators

# These operators form some of the core building blocks of programming logic.
# Below is a list of some of the most common and important ones:


# Comparison Evaluation         Operator

# Equal to                      ==
# Not equal to                  !=
# Less than                     <
# Greater than                  >
# Less than or equal to         <=
# Greater than or equal to      >=


# The first 2 operators can be used to evaluate comparisons on any data type, whether numeric, textual, boolean, or otherwise.
# The last 4 operators can only be used to evaluate numeric data types.


money = 4
cost = 5

if (money == cost):
    print("True")

print("Done!")



if (money == cost):
    print("True")
else:
    print("False")


if (money == cost):
    print("money is exactly equal to cost")
elif(money > cost):
    print("You have enough to pay for the cost")
else:
    print("You don't have enough to pay for the cost")


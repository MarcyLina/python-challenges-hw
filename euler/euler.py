# Project Euler Problem 1
#
# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23. Find the sum of all the multiples of 3 or 5 below 1000.


#........................JS version for reference..............

# for (k = 0, i = 1; i < 1000; !(i % 3 && i % 5) && (k += i), i++) ;
#     console.log(k);
#..........................................................
#
# this one was kinda tricky...had to resesarch quite a bit

meow = 0

for i in range(1000):
    if i % 3 == 0 or i % 5 == 0:
        meow += i

print(meow)

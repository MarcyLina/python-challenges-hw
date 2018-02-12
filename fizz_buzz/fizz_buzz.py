#Write a program in fizzbuzz/fizzbuzz.py that does the following:

#For numbers 1 through 100, print fizz if the number is divisible by 3, buzz if the number is #divisible by 5 and fizzbuzz if the number if the number is divisible by both 3 and 5. If the #number isn't divisible by 3 or 5, just output the number itself.

#The output should look something like 1 2 Fizz 4 Buzz Fizz 7 8 Fizz Buzz 11 Fizz 13 14 Fizz #Buzz 16 17 Fizz..."""

#.............................JS solution for reference......................

#                   function fizzBuzz(){
	#                  for(var i=1;i<=100; i++){
		#                 if(i%5 === 0 && i%3 === 0){
			#                    print('FizzBuzz');
		#                         } else if(i%3 === 0){
			#                    print('Fizz');
		#                         } else if(i%5 === 0){
			#                    print('Buzz');
		#                         } else {
			#                    print(i);
		#                     }}}
#..............................................................................

for i in range(100):
    if i % 3 == 0 and i % 5 == 0:
        print("fizzbuzz")
        continue
    elif i % 3 == 0:
        print("fizz")
        continue
    elif i % 5 == 0:
        print("buzz")
        continue
    print(i)

    # originally played with this code below, but the output did not replace the numbers with the words. it printed the words about the numbers. adding "continue" fixed it, but i amm not fully clear as to why

    # for i in range(100):
    #     if i % 3 == 0 and i % 5 == 0:
    #         print("fizzbuzz")
    #
    #     elif i % 3 == 0:
    #         print("fizz")
    #
    #     elif i % 5 == 0:
    #         print("buzz")
    #         
    #     print(i)

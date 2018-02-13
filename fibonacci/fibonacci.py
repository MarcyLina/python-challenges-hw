# Fibonacci
# Write a program in fibonacci/fib.py that will output the N-th term of the Fibonacci sequence.
#
# For example: print fib(6) should output 8.




def fibo(n):
   if n <= 1:
       return n
   else:
       return(fibo(n-1) + fibo(n-2))

print(fibo(6))

# #............JS version from our whiteboard wendesday for reference................
# const fibonacci = (n) => {
#   let fib = [1, 1];
#   for (let i = 1; i < n; i++) {
#     fib.push(fib[i]+fib[i-1]);
#   }
#   return fib[fib.length - 1];
# }
#..............................................................................

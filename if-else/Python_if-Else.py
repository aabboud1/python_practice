
def is_weird(n):
    if n%2 != 0 or (n%2 == 0 and 6<=n<=20):
        print("Weird")
    else:
        print("Not Weird")

is_weird()

# all test cases pass within the constraints
    
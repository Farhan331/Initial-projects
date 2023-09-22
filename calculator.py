def add(num1,num2):
  sum=num1+num2
  return sum
def sub(num1,num2):
  if num1>num2:
    sub=num1-num2
  elif num2>num1:
    sub=num2-num1
    return sub

def divide(num1,num2):
  divide=num1/num2
  return divide

def multiply(num1,num2):
  multiply=num1*num2
  return multiply

def error():
  print("THANK YOU FOR YOUR TIME")



def getinputs():

  num1=int(input("enter your number 1 :"))

  num2=int(input("enter your number 2 :"))

  choice=input("enter your choice (A,S,M,D,E) :")

  return (num1,num2,choice)

inputs=getinputs()

if inputs[2]=="A":
  result=add(inputs[0],inputs[1])
  print(f"{inputs[0]}+{inputs[1]}={result}")
elif inputs[2]=="S":
  result=sub(inputs[0],inputs[1])
  print(f"{inputs[0]}-{inputs[1]}={result}")

elif inputs[2]=="M":
  result=multiply(inputs[0],inputs[1])
  print(f"{inputs[0]}x{inputs[1]}={result}")

elif inputs[2]=="D":
  result=divide(inputs[0],inputs[1])
  print(f"{inputs[0]}/{inputs[1]}={result:.2f}")

elif inputs[2]=="E":
  print("Thank you for calculating.")


























"""
print("welcome to the best calculator of bangladesh")
print("")
user=input("enter your reponse")
"""
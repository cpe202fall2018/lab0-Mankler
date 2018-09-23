def weight_on_planets():
   # write your code here
   weight = input("What do you weigh on earth? ")
   marsWeight = int(weight) *.38
   jupWeight = (marsWeight/.38)*2.34
   print(f"\nOn Mars you would weigh {marsWeight} pounds.\nOn Jupiter you would weigh {jupWeight} pounds."  )

if __name__ == '__main__':
   weight_on_planets()

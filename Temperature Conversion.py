def celcius_to_fahrenheit(C):
  equal = C * (9/5) + 32
  return equal

def celcius_to_kelvin(C):
  equal = C + 273
  return equal

def celcius_to_reamur(C):
  equal = C * (4/5)
  return equal

def fahrenheit_to_celcius(F):
  equal = (F - 32) * (5/9)
  return equal

def fahrenheit_to_kelvin(F):
  equal = (F - 32) * (5/9) + 273
  return equal

def fahrenheit_to_reamur(F):
  equal = (F - 32) * (4/9)
  return equal

def kelvin_to_celcius(K):
  equal = K - 273
  return equal

def kelvin_to_fahrenheit(K):
  equal = (K - 273) * (9/5) + 32
  return equal

def kelvin_to_reamur(K):
  equal = (4/5) * (K - 273)
  return equal

def reamur_to_celcius(R):
  equal = (5/4) * R
  return equal

def reamur_to_fahrenheit(R):
  equal = (9/4) * R + 32
  return equal

def reamur_to_kelvin(R):
  equal = (5/4) * R + 273
  return equal

def lobby():
  while True:
    print("1.Celcius")
    print("2.Fahrenheit")
    print("3.Kelvin")
    print("4.Reamur")
    print("0.Exit the Game")

    choice = input("Please choose number(0-4)-> ")

    if choice == "1":
      print("1.Celcius to Fahrenheit")
      print("2.Celcius to Kelvin")
      print("3.Celcius to Reamur")
      print("0.Return to lobby")

      choose = input("Please Input Conversion do you want(0-3)! -> ")

      if choose == "1":
        C = float(input("Input the Celcius -> "))
        Cel_Fah = celcius_to_fahrenheit(C)
        print(f"The Temperature is {Cel_Fah} °F ")

      elif choose == "2":
        C = float(input("Input the Celcius -> "))
        Cel_Kel = celcius_to_kelvin(C)
        print(f"The Temperature is {Cel_Kel} °K")

      elif choose == "3":
        C = float(input("Input the Celcius -> "))
        Cel_Re = celcius_to_reamur(C)
        print(f"The Temperature is {Cel_Re} °R")

      elif choose == "0":
        lobby()

      else:
        print("Invalid Input, Please Try Again!")
    
    elif choice == "2":
      print("1.Fahrenheit to Celcius")
      print("2.Fahrenheit to Kelvin")
      print("3.Fahrenheit to Reamur")
      print("0.Return to lobby")

      choose1 = input("Please Input Conversion Do You Want(1-3) -> ")

      if choose1 == "1":
        F = float(input("Input the Fahrenheit -> "))
        Fah_Cel = fahrenheit_to_celcius(F)
        print(f"The Temperature is {Fah_Cel} °C")

      elif choose1 == "2":
        F = float(input("Input the Fahrenheit -> "))
        Fah_Kel = fahrenheit_to_kelvin(F)
        print(f"The Temperature is {Fah_Kel} °K")

      elif choose1 == "3":
        F = float(input("Input the Fahrenheit -> "))
        Fah_Re = fahrenheit_to_reamur(F)
        print(f"The Temperature is {Fah_Re} °R")

      elif choose == "0":
        lobby()

      else:
        print("Invalid Input, Please Try Again!")
    
    elif choice == "3":
      print("1.Kelvin to Celcius")
      print("2.Kelvin to Fahrenheit")
      print("3.Kelvin to Reamur")
      print("0.Return to lobby")

      choose2 = input("Please Input Conversion Do You Want(1-3)! -> ")

      if choose2 == "1":
        K = float(input("Input the Kelvin -> "))
        Kel_Cel = kelvin_to_celcius(K)
        print(f"The Temperature is {Kel_Cel} °C")

      elif choose2 == "2":
        K = float(input("Input the Kelvin -> "))
        Kel_Fah = kelvin_to_fahrenheit(K)
        print(f"The Temperature is {Kel_Fah} °F")

      elif choose2 == "3":
        K = float(input("Input the Kelvin -> "))
        Kel_Re = kelvin_to_reamur(K)
        print(f"The Temperature is {Kel_Re} °R")

      elif choose == "0":
        lobby()

      else:
        print("Invalid Input, Please Try Again!")
    
    elif choice == "4":
      print("1.Reamur to Celcius")
      print("2.Reamur to Fahrenheit")
      print("3.Reamur to Kelvin")
      print("0.Return to lobby")

      choose3 = input("Please Input Conversion Do You Want(1-3)! -> ")

      if choose3 == "1":
        R = float(input("Input the Reamur -> "))
        Re_Cel = reamur_to_celcius(R)
        print(f"The Temperature is {Re_Cel} °C")

      elif choose3 == "2":
        R = float(input("Input the Reamur -> "))
        Re_Fah = reamur_to_fahrenheit(R)
        print(f"The Temperature is {Re_Fah} °F")

      elif choose3 == "3":
        R = float(input("Input the Reamur -> "))
        Re_Kel = reamur_to_kelvin(R)
        print(f"The Temperature is {Re_Kel} °K")

      elif choose == "0":
        lobby()
      
      else:
        print("Invalid Input, Please Try Again!")
        
    elif choice == "0":
      print("Thank You For Using This Games!")
      break

    else:
      print("Invalid Input,Please Enter The Right Input..")
    
    print()

print("=== Temperature Conversion ===")
lobby()
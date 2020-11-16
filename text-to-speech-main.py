import pyttsx3
engine = pyttsx3.init() # object creation

print("Welcome to Fouads text-to-speech program")
engine.say("Welcome to fouAds text-to-speech program")
engine.runAndWait()


engine.say("Please Enter Your Name")
engine.runAndWait()
name = str(input("Please Enter Your Name: "))



engine.say("Please Enter Your Age")
engine.runAndWait()
age = str(input("Please Enter Your Age: "))


engine.say("Please Enter Your Country")
engine.runAndWait()
country = str(input("Please Enter Your Country: "))
print("Welcome " + name + " you are" + age + " year(s) old and you were born in " + country)
engine.say("Welcome " + name + " you are " + age + " years old and you were born in " + country)
engine.runAndWait()


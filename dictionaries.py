#cars ={
  #  "model": "ford",
 #   "year": 1964
#}    
#print(cars["model"])
#cars.update ({"year":1920})
#print(cars["

#parent={
  #  "child1":{"name":"James"},
 #   "child2":{"name":"Peter"}

#}
#print(parent["child2"]["name"])


#def my_function(first_name):
 #   print(first_name+"hello")
#my_function ("Hellen")
#my_function ("Wanjiru")


#def greet_user():
 #   name=input("What is your name?")
 #   print("Hello," + name)
#greet_user()    
  



#person = {
#  "name": "biggie",
 # "age":"34",
  #"pets":["dog","cat"]
#}
#print(person["pets"][0])

#person={
  #"name":"Cate",
  #"age":"23",
  #"pets":{"dog":"x",
  #        "cat":"y"
 # }

#}
#print(person["pets"]["cat"])

#profile={}
#profile["username"]="user123"
#profile["age"]="23"
#profile["email"]="user123@gmail.com"
profile={}
def register():
    username=input("Enter username:")
    email=input("enter your email:")
    password=input("enter your password:")

    profile["username"]= username
    profile["email"]= email
    profile["password"]=password

register()

def get_profile():
    print(profile)
 

def change_username():
    new_username = input("Enter new user_name")
    profile ["username"]= new_username
register()
get_profile()

change_username()
get_profile()


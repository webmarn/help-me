# -*- coding: utf-8 -*-
"""
Created on Mon Feb 25 19:46:45 2019

@author: Marni Rosenthal
Project 2
"""

def select_meal():
    x = True
    meal_list = []
    while x == True:
        choice = input("Hello, would you like pizza or salad?")
        if choice == "salad":
            salad_answer = salad()
            #fix me!
            meal_list.append(salad_answer)
            print("You ordered a {} and" + meal_list[0] + "Place another order or say 'done'.".format(salad_answer))
        if choice == "pizza":
            pizza_answer = pizza()
            print("You ordered a {} Place another order or say 'done'.".format(pizza_answer))
        if choice == "done":
            print("Your order has been placed. Goodbye.")
            x = False
def pizza():
    pizza_answer = input("Small, medium, or large?")
    toppings_answer = toppings()
    return(pizza_answer + " pizza with " + toppings_answer + ".")
    
def toppings():
    y = True
    toppings_list = []
    while y == True:
       toppings = input("Add a topping: pepperoni, mushrooms, spinach, or say 'done'")
       if toppings == "done":
           #is there a nicer way to do this?
           if len(toppings_list) == 3:
               return (toppings_list[0] + " and " + toppings_list[1] + " and " + toppings_list[2])
           if len(toppings_list) == 2:
               return (toppings_list[0] + " and " + toppings_list[1])
           if len(toppings_list) == 1:
               return (toppings_list[0])
           y = False
       else:
           toppings_list.append(toppings)
       
def dressing():
    dressing = input("Please choose a dressing: vinaigrette, ranch, blue cheese, lemon")
    return dressing

def salad():
    salad_answer = input("Would you like a garden salad or greek salad?")
    dressing_answer = dressing()
    return(salad_answer + " salad with " + dressing_answer + " dressing.")
      
select_meal()
# library
import matplotlib.pyplot as plt
from matplotlib_venn import venn2
import math

TOTAL = 52

cards = ["ace" , "2" , "3" , "4" , "5" , "6" , "7" , "8" , "9" , "10" , "jack" , "queen" , "king"]
colors = ["black" , "red"]
face_cards = ["face", "faces", "face cards", "face_cards"]
face_types = ["king", "queen", "jack"]
number_cards = ["number", "numbers", "number cards", "number_cards"]
number_types = ["2" , "3" , "4" , "5" , "6" , "7" , "8" , "9" , "10"]
suits = ["hearts" , "diamonds" , "spades" , "clubs"]

def first_num():
    Probability1 = input("What's your first card/group [Ex:King,7,Hearts,Black]?\n")
    if Probability1.lower() in cards:
        number1 = 4
        label1 = Probability1
        return [number1, label1]
    elif Probability1.lower() in colors:
        number1 = 26
        label1 = Probability1
        return [number1, label1]
    elif Probability1.lower() in suits:
        number1 = 13
        label1 = Probability1
        return [number1, label1]
    elif Probability1.lower() in face_cards:
        number1 = 12
        label1 = Probability1
        return [number1, label1]
    elif Probability1.lower() in number_cards:
        number1 = 36
        label1 = Probability1
        return [number1, label1]
    else:
        print("sorry that wasn't an option, try again.")
        number1 = first_num()

def second_num():
    Probability2 = input("What's your second card/group [Ex:King,7,Hearts,Black]?\n")
    if Probability2.lower() in cards:
        number2 = 4
        label2 = Probability2
        return [number2, label2]
    elif Probability2.lower() in colors:
        number2 = 26
        label2 = Probability2
        return [number2, label2]
    elif Probability2.lower() in suits:
        number2 = 13
        label2 = Probability2
        return [number2, label2]
    else:
        print("sorry that wasn't an option, try again.")
        number2 = second_num()

def operator():
    number1 = first_num()
    Probability2 = input("And/or/none?\n")
    if "none" == str(Probability2.lower()):
        final_prob = (number1[0]/TOTAL)*100
        decimal = number1[0]/TOTAL
        print("Nothing to compare but the probability of pulling a {} out of 52 Cards is about {}%".format(number1[1],math.trunc(final_prob)))
        print("The exact decimal is {} and the fraction is {}/{}".format(decimal,number1[0],TOTAL))
    elif "or" == str(Probability2.lower()):
        number2 = second_num()
        first_fraction = number1[0]/TOTAL
        second_fraction = number2[0]/TOTAL
        percentage = (first_fraction+second_fraction)*100
        print("The probability of pulling a {} or a {} out of 52 cards is about {}%".format(number1[1],number2[1],math.floor(percentage)))
        intersection = number1[0]+number2[0]
        print("There are {} card(s) that match this description in a 52 card deck".format(math.trunc(intersection)))
        intersection = first_fraction*number2[0]
        venn2(subsets = (0, 0,number1[0]+number2[0]), set_labels = (str(number1[1]), str(number2[1])))
        plt.show()

    elif "and" == str(Probability2.lower()):
        number2 = second_num()
        if (str(number1[1]) in colors) & (str(number2[1]) in colors):
          print("This is a disjoint event")
          print("The probability of pulling a {} and a {} out of 52 cards is 0%".format(number1[1],number2[1]))
        elif (str(number1[1]) in face_cards) & (str(number2[1]) in face_types):
          decimal = 4/52
          percentage = (decimal)*100
          print("The probability of pulling a {} and a {} out of 52 cards is about {}%".format(number1[1],number2[1],math.floor(percentage)))
          print("The exact decimal is {} and the fraction is {}/{}".format(decimal,4,TOTAL))
        else:
          
          first_fraction = number1[0]/TOTAL
          second_fraction = number2[0]/TOTAL
          percentage = (first_fraction*second_fraction)*100
          decimal = first_fraction*second_fraction
          print("The probability of pulling a {} and a {} out of 52 cards is about {}%".format(number1[1],number2[1],math.floor(percentage)))
          intersection = first_fraction*number2[0]
          print("There are {} card(s) that match this description in a 52 card deck".format(math.trunc(intersection)))
          final_frac = first_fraction*number2[0]
          final_frac = math.trunc(final_frac)
          print("The exact decimal is {} and the fraction is {}/{}".format(decimal,final_frac, TOTAL))
          venn2(subsets = (number1[0], number2[0], math.trunc(intersection)), set_labels = (str(number1[1]), str(number2[1])))
          plt.show()

    else:
        print("Sorry that wasn't an option, try again.")
        operator()

operator()
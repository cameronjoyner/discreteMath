#COMS3203 DISCRETE MATHEMATICS
#CODING ASSIGNMENT 1
#YOUR NAME: Cameron Joyner
#YOUR UNI: CGJ2115

from tabulate import tabulate

def format_prop(prop):
    
    output = ""
    list_size = len(prop) #length of the proposition
    connective = prop[0] #indicating the our logical connective comes in at position 1
   
    if list_size == 2 : #this is just for a list size of two
        if not isinstance(prop[1], list): #start from position 2 of the list and go from there
            output = output + "(" + connective + " " + prop[1] + ")"
           
        else:
            output = output + "(" + connective + " " + format_prop(prop[1]) + ")"
           
           
    else:  
        if (not isinstance(prop[1], list)) and (not isinstance(prop[2], list)): #isinstance is returning a true or false value
            output = output + "(" + prop[1] + " " + connective + " " + prop[2] + ")"
           
        elif isinstance(prop[1], list) and (not isinstance(prop[2], list)): #https://www.programiz.com/python-programming/methods/built-in/isinstance
            output = output + "(" + format_prop(prop[1]) + connective + prop[2] + ")"
           
        elif (not isinstance(prop[1], list)) and isinstance(prop[2], list):
            output = output + "(" + prop[1] + " " + connective + " " + format_prop(prop[2]) + ")"
           
        else:
            output = output + "(" + format_prop(prop[1]) + " " + connective + " " + format_prop(prop[2]) + ")"    
   
    output = output.replace("iff", "<->")
    output = output.replace("if", "->")
   
    return output

def eval_prop(prop, values):

    output = ""
    list_size = len(prop) #length of the proposition
    connective = prop[0]
    
    if list_size == 3:
        if prop[0] == "iff":
            output = 0    
        elif prop[0] =="if":
            output = 1
        else:
            output = 1    

    # fill here
    return output

def print_table(prop, n_var):

    print(tabulate([[0, 0, 0, 0], [0, 0, 1, 0], [0, 1, 0, 0], [1, 0, 0, 0],
        [0, 1, 1, 0], [1, 0, 1, 0], [1, 1, 1, 0]], headers=['p1', 'p2', 'p3', "output"]))
    # fill here
    pass    

if __name__ == '__main__':
    print("---------------------------------------")
    print("Welcome to Propositional Logic!")
    print("---------------------------------------")

    values = [1, 1, 0]
    prop = ["if", ["and", "p1", ["not", "p2"]], "p3"]
    ps_str = " ".join("p{}={}".format(i + 1, v) for i, v in enumerate(values))

    prop_str = format_prop(prop) #what I'm creating

    print("Evaluating proposition p =", prop_str)

    prop_val = eval_prop(prop, values)

    print("over", ps_str, ":", prop_val)
    print()
    values = [1, 0, 1]
    prop = ["iff", "p1", ["or", "p2", ["not", "p3"]]]
    ps_str = " ".join("p{}={}".format(i + 1, v) for i, v in enumerate(values))
    print("Evaluating proposition p =", format_prop(prop))

    prop_val = eval_prop(prop, values)

    print("over", ps_str, ":", prop_val)

    print("---------------------------------------------------")
    print("Table:")
    print_table(["if", ["and", "p1", ["not", "p2"]], "p3"], 3)





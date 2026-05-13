#group related piece of instructions
#{key: value}
#{Bug : an error in program} - here we got our first dictionary
#{key: value,key: value,key: value} -multi dictionaries

# programming_dictionary = {"Bug": "error" , "function": "piece of code"}
#we can write this as 
programming_dictionary = {
    "Bug": "error",
    "function": "piece of code",
    "loop": "over and over"
}

# print(programming_dictionary["Bug"])

programming_dictionary["loop"] = "huhahahah"

# print(programming_dictionary)

empty_dictionary = {}



#wipe existing dictionary
# programming_dictionary = {}
# print(programming_dictionary)


#edit an item in dictionary
# print(programming_dictionary["Bug"])

programming_dictionary["Bug"] = "a moth"
# print(programming_dictionary)



#loop through a dictionary
for key in programming_dictionary:
    print(key)
    print(programming_dictionary[key])
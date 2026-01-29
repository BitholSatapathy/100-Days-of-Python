def calculate_love_score(name1, name2):
    # Combine both names and convert to uppercase
    combined_names = (name1 + name2).upper()
    
    # Count letters in "TRUE"
    true_count = 0
    for letter in "TRUE":
        true_count += combined_names.count(letter)
    
    # Count letters in "LOVE"
    love_count = 0
    for letter in "LOVE":
        love_count += combined_names.count(letter)
    
    # Combine the counts to make a 2-digit number
    love_score = int(str(true_count) + str(love_count))
    
    print(love_score)

# Call your function with hard coded values
calculate_love_score("Kanye West", "Kim Kardashian")

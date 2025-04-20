def calculate_love_score(person_1, person_2):
    combined_names= (person_1+person_2).lower().replace(" ","")
    print(combined_names)
    true_letters=['t','r','u','e']
    love_letters=['l','o','v','e']
    true_score=0
    love_score=0
    # comparing and counting
    for ele in true_letters:
        true_score+=combined_names.count(ele)

    for ele in love_letters:
        love_score+=combined_names.count(ele)

    # to print the result
    print(int(str(true_score)+str(love_score)))
    
calculate_love_score("Kanye West", "Kim Kardashian")
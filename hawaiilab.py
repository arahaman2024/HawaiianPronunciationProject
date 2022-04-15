hwdic = {"a": "ah-",
         "aa": "ah-ah-",
         "ae": "eye-",
         "ai": "eye-",
         "ao": "ow-",
         "au": "ow-",
         "aw": "ah-w",
         
         "e": "eh-",
         "ee": "eh-eh-",
         "ea": "eye-ah-",
         "ei": "ay-",
         "eo": "eh-oh-",
         "eu": "eh-oo",
         "ew": "eh-v",

         "i": "ee-",
         "ia": "ee-ah-",
         "ie": "ee-eh-",
         "ii": "ee-ee-",
         "io": "ee-oh-",
         "iu": "ew-",
         "iw": "ee-v",

         "o": "oh-",
         "oa": "oh-ah-",
         "oe": "oh-eh-",
         "oi": "oyo-",
         "oo": "oh-oh-",
         "ou": "ow-",
         "ow": "oh-w",

         "u": "oo-",
         "ua": "oo-ah-",
         "ue": "oo-eh-",
         "ui": "ooey-",
         "uo": "oo-oh-",
         "uu": "oo-oo-",
         "uw": "oo-w",
         "w": "w"}
       

def hpronouncer(hword):
    hword = hword.lower()
    
    list_h_word = []

    constants = "pkhlmnw"
    prob_lets = "aeiou"
    prob_lets_w = "aeiouw"

    final_word = []      #making this a list will allow us to capitilize end

    for n in hword:
        list_h_word.append(n)
    
    a = 0
    run_number = 0
    

    for lets in range(len(list_h_word)):

        if lets == run_number:
            a = 0
            if list_h_word[lets + a] == "'":
                final_word.append("'")
                a = 0
                run_number = run_number + 1 + a


            elif list_h_word[lets + a] == " ":
                final_word.append(" ")
                a = 0
                run_number = run_number + 1 + a
            

            elif list_h_word[lets + a] in constants:
                final_word.append(list_h_word[lets + a])
                a = 0
                run_number = run_number + 1 + a          

            elif list_h_word[lets + a] in prob_lets:
                
                if (lets + a + 1) < (len(list_h_word)):
                    next_letter = list_h_word[lets + a + 1]
                    if next_letter in prob_lets_w:
                        two_letters = list_h_word[lets + a] + next_letter
                        final_word.append(hwdic[two_letters])
                        a = a + 1
                        run_number = run_number + 1 + a
                    else:
                        final_word.append(hwdic[list_h_word[lets + a]])
                        a = 0
                        run_number = run_number + 1 + a
                else:
                    final_word.append(hwdic[list_h_word[lets + a]])
                    a = 0
                    run_number = run_number + 1 + a

    final_word_word = ""

    for ind_runs in final_word:
        final_word_word = final_word_word + ind_runs

    final_word_word = final_word_word[0].upper() + final_word_word[1:]

    if final_word_word[-1] == "-":
        final_word_word = final_word_word[:-1]
                     
    return final_word_word


def isValid(hword):
    hword = hword.lower()
    validLetters = "pkhlmnwaeiou' "
    
    nonvalid_letters_strign = ""

    for ls in hword:
        if ls not in validLetters:
            nonvalid_letters_strign = nonvalid_letters_strign + (ls + " ")
    
    return nonvalid_letters_strign
         
def main (hword):

    if len(isValid(hword)) > 0:
        print(isValid(hword), "is/are not valid hawaiian character(s) \n")
        hword = input("Enter a hawaiian word to pronounce ==> ")
        main(hword)
    else:
        print(hpronouncer(hword))

    try_again = input("Do you want to enter another word? Y/YES/N/NO ==> ")
    try_again = try_again.lower()
    try_again_valid(try_again)

    while not try_again_valid(try_again):
        try_again = input("Enter Y/YES/N/NO ==>")

    if try_again == "yes" or try_again == "y":
        hword = input("Enter a hawaiian word to pronounce ==> ")
        main(hword)
    else:
        print("Okay!")
    
 
def try_again_valid (try_again):
    try:
        if try_again == "yes" or try_again == "y" or try_again == "no" or try_again == "n":
            return True

    except:
        return False
        

hword = input("Enter a hawaiian word to pronounce ==> ")
main(hword)




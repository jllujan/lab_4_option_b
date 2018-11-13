# Lab 4 option B
# Name: Jose Lujan
# ID: 80572649
# class: cs2302
# class time 10:30-11:50

from Hash_Table import HashTable, HashTableNode


# Creates the Hash-Table, using the words obtain from the file named: "EnglishWords.txt"
def create_hash_table(filename):
    try:
        english_words = HashTable(5000)

        # Open file and read lines
        file = open(filename, "r")
        line = file.readline()

        while line:
            english_words.insert(line.rstrip())
            line = file.readline()

        return english_words
    # Prints a message, to let know the user that he enter the wrong file name
    except FileNotFoundError:
        print("Please try again, name of file is incorrect")


# Generates all possible permutations from a given within the working file
def get_permutations(word):
    if len(word) <= 1:
        return word
    else:
        permutations_list = []
        for perm in get_permutations(word[1:]):
            for i in range(len(word)):
                permutations_list.append(perm[:i] + word[0:1] + perm[i:])
        return permutations_list


# Returns the amount of anagrams for a given word by the user
def count_anagrams(word, table):
    permutations = get_permutations(word)
    count = 0

    for i in range(len(permutations)):
        if table.search(permutations[i]):
            count += 1

    return count


# Returns the number of words in a cell
def get_num_col(node):
    count = 0
    temp = node

    while temp is not None:
        count = count + 1
        temp = temp.next

    return count


# Returns the amount of comparisons needed to find a word
def amount_of_comparisons(table):
    number_of_cols = 0

    for i in range(len(table.table)):
        number_of_cols = number_of_cols + get_num_col(table.table[i]) // 2

    return number_of_cols / len(table.table)


# Returns the load factor
def get_load_factor(table):
    num_elements = 0
    for i in range(len(table.table)):
        temp = table.table[i]

        while temp is not None:
            num_elements = num_elements + 1
            temp = temp.next

    return num_elements / len(table.table)


def main():
    filename = input("Please enter the name of the file you want to work with:  ")
    keep_going = True
    hash_table = create_hash_table(filename)
    print("")
    print("                             Hash Table has been created")
    print("")

    if hash_table is not None:
        while keep_going:
            print("Please type a,b or c to choose the operation you would like to perform:")
            print("   a. Get the average number of comparisons needed to perform a retrieve.")
            print("   b. Get the Load Factor for the Hash Table.")
            print("   c. Get the number of possible anagrams from a given word.")
            answer = input()

            if answer == 'a':
                print("The number of comparisons is:", amount_of_comparisons(hash_table))
            elif answer == 'b':
                print("The Load Factor is:", get_load_factor(hash_table))
            elif answer == 'c':
                word = input("Type the word to search for anagrams: ")
                print("Number of possible anagrams for " + word + " is:", count_anagrams(word, hash_table))
            else:
                print("The can only type a,b or c")

            loop = input("\nDo you want to search for a new word or get the output for option a or b; \ntype: yes or no\n\n")

            if loop == 'yes':
                keep_going = True
            elif loop == 'no':
                keep_going = False
            else:
                print(" please try again, type yes or no")


main()

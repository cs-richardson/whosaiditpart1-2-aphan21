#This code is written by Ann and the given format in the prompt
#This code is to determine how many times each word is repeated
#in the literary artwork samples by Shakespeare and Austen
# normalize
# -----
# This function takes a word and returns the same word
# with:
#   - All non-letters removed
#   - All letters converted to lowercase
def normalize(word):
    return "".join(letter for letter in word if letter.isalpha()).lower()

# get_counts
# -----
# This function takes a filename and generates a dictionary
# whose keys are the unique words in the file and whose
# values are the counts for those words.
def get_counts(filename):
    result_dict = {}
    text = open(filename, 'r')
    text = text.read()
    text = text.split()
    for word in text:
        word = normalize(word)
        if word not in result_dict:
            result_dict[word] = 1
        elif word in result_dict:
            result_dict[word] = result_dict[word] + 1
    return result_dict

# Get the counts for the two shortened versions
# of the texts
shakespeare_counts = get_counts("hamlet-short.txt")
austen_counts = get_counts("pride-and-prejudice-short.txt")

# Check the contents of the dictionaries
for key in shakespeare_counts:
    print(key + ": " + str(shakespeare_counts[key]))

print("-----")

for key in austen_counts:
    print(key + ": " + str(austen_counts[key]))
        

'''
Kyle Graves
section 4
kegr234@g.uky.edu
12/12/19
#Purpose: to make book recommendations to a user based on a file of
#  previous customer rankings of books
#Pre-cond: two files, books.txt and customers.txt that have specific formats
#   rankings from the user of the books
#Post-cond: prompts for user rankings, reports of most similar customer,
#   recommendations (if any possible)
'''


def get_books():
    '''
    #function get_books
# purpose:  read in data from a file "books.txt"
#           and building a list of books with a particular structure
# pre-    : no parameters, data coming from file in format:
#     each line contains author name then book title delimited by comma
#     lines are delimited by newlines
# post-   :  returns a list of books in the format
#     [
#       [author, title],
#       [author, title],
#       [author, title],
#     ]
#     both author and title are strings
#     the title has the newline removed from the right end

    '''
    #open book file
    bookfile = 'books.txt'
    infile = open(bookfile, "r")
    #read book file and store to a string variable
    books = infile.readlines()
    #close the file
    infile.close()
    
    
    book_list_data = []
    #split each string element at every comma and new line 
    for line in books:
        line = line.rstrip()
        book_list = line.split(',')
           
        #assign element position    
        name = book_list[0]
        title = book_list[1]
        
        #create a 2-D list
        book_list_data.append([name,title])        
        #[[name, title], [name, title], ...]
    
    
    #return the list with correct format
    return book_list_data
#-------------------------------------------------------------------------------
def get_customers():
    '''
    #function get_customers
# purpose:  read in data from a file "customers.txt"
#           and building a list of customers with a particular structure
# pre-    : no parameters, data coming from file in format:
#     first line is customer name, spaces allowed, delimited by newline
#     second line integers delimited by whitespace  and ended with newline
#          possible values (-5, -3, 0, 1, 3, 5)
#     first and second lines repeated as desired
# post-   :  returns a list of members in the format
#     [
#      [name (string), [(rankings) integers]], 
#      [name (string), [(rankings) integers]], 
#      [name (string), [(rankings) integers]], 
#     ]
#     names have the newline removed from the right end

    '''    
    #open customer file
    customer_file = 'customers.txt'
    #read customer file
    infile = open(customer_file, "r")
    customers = infile.readlines()
    #close customer file
    infile.close()
    
    #ititalize customer data list
    customer_data = []
    #split file by each new line
    #for every element in customer data  file list
    #initialize customer list
    customer_list = []
    for line in customers:
        customer_line = line.rstrip()
        customer_list.append(customer_line)
    #iterate over only the names in the customer list
    for i in range(0, len(customer_list), 2):
        #every odd element is a name assign to variable 
        customer_name = customer_list[i]
        #every even element is a list assign to variable
        customer_rating = customer_list[i+1].split()
        #create a loop to make ratings a list of ints
        for i in range(len(customer_rating)):
            customer_rating[i] = int(customer_rating[i])   
            
        #to create a list with correct format
        #[[name, [integers]], [name, [integers]], ...]        
        customer_data.append(customer_name)
        customer_data.append(customer_rating)
    
    #return list with correct format
    return customer_data
#-------------------------------------------------------------------------------
def get_user_rankings(book_list):
    '''
    #function get_user_rankings
# purpose:  get the ranking information from the program's user
#    
# pre-cond:  books list [[author, title], [author, title],...]
# post-cond:  prompts for the user name, 
#      displays each book's info, gives error messages if invalid
#      ranking from user, returns a list [user, [rankings]]
#      user is the user's name, rankings are the integers input by user
    '''
    #initialize user_rating list
    #initialize user_list
    user_list = []
    user_ratings = []
    #get input for users name
    user_name = input('What is your name? ')
    print()
    #print header
    print('You will see the authors and titles in our database.')
    
    #print valid ratings
    print('Please enter -5, -3, 0, 1, 3, 5')
    #print what the ratings mean
    print("-5 Hated it!, -3 Didn't like it, 0 haven't read it, 1 ok, 3 Liked it!, 5 Really liked it!")
    print()    
    #use for loop with length of the book list
    for i in range(len(book_list)):
        #get rating inputs from user after displaying the book_list element
        
        print(book_list[i][0], book_list[i][1])
        rating = int(input('Ranking? '))
        
        
        #set valid flag to false   
        valid = False
        #if input is valid, set flag to true
        if rating == -5 or rating == -3 or rating == 0 or rating == 1 or rating == 3 or rating == 5:
            valid = True
        #if not a valid input, ask for a valid input again
        while valid == False:
            print("rating invalid please use the ratings -5, -3, 0, 1, 3, 5")
            print(book_list[i][0], book_list[i][1])
            rating = int(input('Ranking? '))
            if rating == -5 or rating == -3 or rating == 0 or rating == 1 or rating == 3 or rating == 5:
                valid = True
        #append each rating to user_rankings_list as they are inputed
        user_ratings.append(rating)     
    #add the name and the list of ratings to user list    
    user_list.append(user_name)
    user_list.append(user_ratings)
        
    #return the list of user ratings
    return user_list
#-------------------------------------------------------------------------------
def calculate_similarity(user_list, customers):
    '''
    #function calculate_similarity
# purpose: calculate the similarity measure between two customers
#    and return it (integer)
#    similarity measure:  the sum of the product of corresponding 
#          pair of integers from the lists in the parameters
# pre-    : two parameters, both lists of the format [name, [integers]]
#      it is assumed the lists of integers are of the same length
# post-   : returns the simularity measure  (int)
    ''' 
   
    #initialize accumulator for cross-product
    similarity = 0
    
    #use for loop to compare elements in two rating lists
    
    #print("starting calculate loop")
    for i in range(len(user_list[1])):
        #print("beginning of calculate loop")
        
        #calculate cross product of each element
        user_rating = user_list[1][i]
        
        customer_rating = customers[i]
        
        cross_product = customer_rating * user_rating
        
        #add to the accumulator
        similarity += cross_product
        
    #return the cross-product of the two lists
    return similarity 
#-------------------------------------------------------------------------------
def get_similarities(user_list, customers):
    '''
    # function get_similarities 
# purpose:  create a list of similarities between each customer and the
#   current user
# Pre-cond:  the list of customers and their rankings and the list that
#   represents the user's rankings
# Post-cond:  returns list of similarities with customer names
#    [[sim, customer name], [sim, customer name], ...]  one row for each customer
#      sim is integer (similarity measure), customer name is string
#  calls the calculate_similarity function for each customer
#  uses for loop to process all customers and build similarity list.
    ''' 
    #initialize a similarity list
    similarity_list = []
    
        
    #use a for loop to compare the user rating to each of the customer ratings
    
    for i in range(0, len(customers), 2):
        #get the names and ratings of each customer being compared
        name = customers[i]
        ratings = customers[i+1]
        
        #use calculate similarity function to create a similarity to each customer
        similarity = calculate_similarity(user_list, ratings)
        
        #append the name and similarity to the user of each element to similarity list
        similarity_list.append([similarity, name])
        
         
    #return the similarity list [[similarity, name], [similarity, name], .... ]
    return similarity_list
#-------------------------------------------------------------------------------

def main():
    
    
    #call get books function, save to variable
    books = get_books() 
    #call get customers function, save to variable
    customers = get_customers()
    #print title
    print('Book Recommender')
    print()
    
    
    
    #call get user ratings function, assign to variable
    user_list = get_user_rankings(books)    
    
    
    #print new line
    print()
    
    #print the list of users ratings assigned above
    print("This is your set of rankings")
    print(user_list[0], user_list[1])
    
    #print the customer with the highest similarity
    print()
    print("The customer with highest similarity ", end = '')
    
    #call get similarity function and assign to variable
    similarity = get_similarities(user_list, customers)
    
    #sort the list returned
    similarity.sort()
    
    #assign last element to variable this is the person with the highest similarity
    max_similarity = similarity[-1]
    #print the second element of the variable above which is the persons name
    customer_name = max_similarity[1]
    #display the rankings of the persons name above
    single_similarity = max_similarity[0]
    
    #print customer with highest similarities name
    print(customer_name)
    #create a new list for the name and and ratings of the similar customer
    similar_cust = []
    #add name to that list
    similar_cust.append(customer_name)
    #create a for-loop to match the similar persons name with thier list
    for i in range(0, len(customers), 2):
        #if the names match from both lists
        if customers[i] == customer_name:
            similar_cust_ratings = customers[i+1]
            #add their rankings to the similar customer list
            similar_cust.append(similar_cust_ratings)
            
            #print that customers ratings
            print("Their ratings", customers[i+1]) 
        
    
    
    #print recommendations header
    print("\nRecommendations:\n")
    
    #initialize recomendation list
    #initialize recommendations accumulator
    num_rec = 0
    book_rec = []
    #find the ratings you have a zero in, that they have a 5 in
    #use for loop to iterate their rating list
    for i in range(len(user_list[1])):
        #if your element at i is zero and their element at i is 5
        if user_list[1][i] == 0 and similar_cust[1][i] == 5:
            #append getbooks list element at index number to recomendation list
            book_rec.append(books[i])
            #add 1 to total recommendations 
            num_rec += 1
    #if no recommendations, lower requirements to similar customer of rating 3
    if num_rec == 0:
        for i in range(len(user_list[1])):
            if user_list[1][i] == 0 and similar_cust[1][i] == 3:
                book_rec.append(books[i])
                num_rec += 1       
    
    #create a for loop to iterate the recommendations list
    for i in range(num_rec):
        
        #print elements in book recommendations list separtated by a ':'
        print(book_rec[i][0], ":", book_rec[i][1])
         
    
    #print how many recommendations are given using variable saved above
    print()
    print(num_rec, "recommendations")
    
main()


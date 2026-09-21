import csv as csv

"""
Write a function called display_top_collaborations that displays the ranking of tuples (director, actor,
and number of movies) for movies in which the director and actor worked together and the movie is
also listed in the top rated movie list. The list should be in descending ordered of the total number of
movies that director and that actor worked together. For equal values the order does not matter.
Notice that the number of movies in the imdb-top-casts.csv file exceeds the number of movies in imdbtop-
rated.csv. You may have to open the csv files like this: open(filename, 'r', encoding = 'utf-8')."""
#Problem 4a function
def display_top_collaborations(top_rate_file, cast_name_file):

    try:

    #opening files to access content from them
        top_rate_f = open(top_rate_file,"r", encoding="utf-8")
        cast_name_f = open(cast_name_file,"r", encoding="utf-8")

        #reading content from file
        top_rated_r = csv.reader(top_rate_f)
        cast_name_r = csv.reader(cast_name_f)

        #making sure the header is not included in loop
        next(top_rated_r)

        #dictionaries to store top rated and paired info
        top_rated = {}
        work_together = {}

        #loop to parse through the file content in top rated
        for line in top_rated_r:

            #store name and year into the dictionary
            top_rated[(line[1], line[2])] = line[3]

        #loop to parse through the file content in castname
        for line in cast_name_r:

            #variables to store the movie title, year, and director
            m_title = line[0]
            m_year = line[1]
            m_director = line[2]

            #if statement to see if tuple is in top rated file
            if (m_title, m_year) in top_rated:
                cast_members = line[3:]

                #loop for pairing up actors with associated director
                for cast in cast_members:
                    crew_tuple = (m_director, cast)

                    #if statements to determine count of combination pair
                    if crew_tuple in work_together:
                        work_together[crew_tuple] += 1

                    else:
                        work_together[crew_tuple] = 1

        #empty ranking list to store rankings for tuple return
        ranks = []

        #loop to iterate through work together dictionary
        for pair in work_together:

            ranks.append((pair[0], pair[1], work_together[pair]))

        #variable to get length of ranks list
        ranks_len = len(ranks)

        for i in range(ranks_len):
            for j in range(i + 1, ranks_len):
                if ranks[i][2] < ranks[j][2]:
                    ranks[i], ranks[j] = ranks[j], ranks[i]

        for i in range(10):
            print(ranks[i])

        top_rate_f.close()
        cast_name_f.close()

    except FileNotFoundError:
        print("File could not be found")
        raise

        
"""
Write a function called display_top_actors that displays the ranking of actors from the top grossing
list ordered by the total box office money they acted in."""
#Problem 4b function
def display_top_actors(top_gross_file, top_cast_file ):

    try:
        #opening files to access content from them
        top_gross_f = open(top_gross_file,"r", encoding="utf-8")
        top_cast_f = open(top_cast_file, "r", encoding ="utf-8")

        #reading content from file
        top_gross_r = csv.reader(top_gross_f)
        top_cast_r = csv.reader(top_cast_f)

        #making sure the header is not included in loop
        next(top_gross_r)

        #empty dictionaries to store actors and gross information from file
        actors = {}
        gross = {}

        #loop to add needed line item info from file into dictionary
        for line in top_gross_r:

            gross[(line[1], line[2])] = line[3]

        #loop to parse through the file content in castname
        for line in top_cast_r:

            #variables to store the movie title, year, and director
            m_title = line[0]
            m_year = line[1]

            #if statement to see movie information is connected to gross info
            if (m_title, m_year) in gross:

                all_actors = line[3:]

                movie_gross = int(gross[(m_title, m_year)])

                for actor in all_actors:

                    if actor in actors:
                        actors[actor] += movie_gross
                    else:
                        actors[actor] = movie_gross

        #empty ranking list to store rankings for tuple return
        ranks = []

        #loop to iterate through work together dictionary
        for actor in actors:

            #adding in actor information into list
            ranks.append((actor, actors[actor]))

        #variable to get length of ranks list
        ranks_len = len(ranks)

        #loop to sort top rank list
        for i in range(ranks_len):

            for j in range(i + 1, ranks_len):

                if ranks[i][1] < ranks[j][1]:
                    ranks[i], ranks[j] = ranks[j], ranks[i]

        #loop to only get the top 10 ranks
        for i in range(10):
            print(ranks[i])                

        top_gross_f.close()
        top_cast_f.close()

    except FileNotFoundError:
        print("File not found")
        raise

#Problem 3c function
def main():
    #testing
    #variables to store files needs for functions in 4a and 4b
    top_rate_file = "imdb-top-rated.csv"
    top_gross_file = "imdb-top-grossing.csv"
    top_cast_file = "imdb-top-casts.csv"

    #testing output for function in problem 4a
    print("Top Collaborations: ")
    display_top_collaborations(top_rate_file, top_cast_file)    

    #testing output[ for function in problem 4b]
    print("\nTop Actors: ")
    display_top_actors(top_gross_file, top_cast_file)

#calling problem 4c function
if __name__ == "__main__":
    main()

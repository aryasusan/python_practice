# questions is in movies.pdf
f = open('movies_cleaned_pandas.csv','r')
movie_list = []
year_movie_list = {}
rating_movie_count ={}
list1 = []
list2= []
list3 = []
list4 = []
for i in f:
    data = i.rstrip('\n').split(',')
    id = data[0]
    movie = data[1]
    year = data[2]
    rating = data[3]
    duration = data[4]

    details = {}
    details['id'] = id
    details['movie'] = movie
    details['year'] = year
    details['rating'] = rating
    details['duration'] = duration
    movie_list.append(details)
    if(year not in year_movie_list):
        year_movie_list[year]=1
    else:
        year_movie_list[year]+=1

    if (rating not in rating_movie_count):
        rating_movie_count[rating] = 1
    else:
        rating_movie_count[rating] += 1
    if (year == '2008' and rating > '3'):
        list1.append(data)
    if(rating>'4' and year>'2005'):
        list2.append(data)
    if('1975'<=year<='2000'):
        list3.append(data)
    if('1975'<=year<='2000' and rating>'3.5'):
        list4.append(data)

print("Q1-row_count",len(movie_list))
sort_by_year = sorted(movie_list,key=lambda details:details['year'],reverse=True)
print("Q3- details sorted by year descending",sort_by_year)

sort_by_rating = sorted(movie_list,key=lambda details:details['rating'],reverse=True)
print("Q4-max rating 5 movies",sort_by_rating[:5])
print("Q5-min rating 5 movies",sort_by_rating[-5:-1])

sort_year_count = sorted(year_movie_list.items(),key=lambda item:item[1],reverse=True)
print("Q6-no.of movies in a year sort by descending count:")
for k,v in sort_year_count:
    print(k,"-",v)

sort_rating_count = sorted(rating_movie_count.items(),key=lambda item:item[1],reverse=True)
print("Q7-no.of movies with a rating sort by descending count:")
for k,v in sort_rating_count:
    print(k,"-",v)

print("Q8- row count of yr 2008 and rating above 3 is ",len(list1))

sort_by_duration = sorted(movie_list,key=lambda details:details['duration'],reverse=True)
print("Q8-1 movie with max duration:",sort_by_duration[0])
print("Q9-1 movie with min rating:",sort_by_rating[-1])

print("Q11-yr > 2005 and rating above 4 are:")
for j in list2:
    print(j)
max_rating = sorted(list2,key=lambda item:item[-2],reverse=True)
print("Q11-A,movie with max rating",max_rating[0])
print("Q11-B,movie with min rating",max_rating[-1])

print("Q12,1975-2000 movie details:")
for k in list3:
    print(k)
print("row count 1975-2000: ",len(list3))

print("Q13 row count of 1975-2000 movie and rating above 3.5 is ",len(list4))





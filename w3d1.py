#Filter out all of the empty strings from the list below

#Output: ['Argentina', 'San Diego', 'Boston', 'New York']

places = [" ","Argentina", " ", "San Diego","","  ","","Boston","New York"]
output = []

filtered = filter(lambda s: s.strip() != '', places)

print(list(filtered))


################ #2

# Write an anonymous function that sorts this list by the last name...
# Hint: Use the ".sort()" method and access the key"

# Output: ['Victor aNisimov', 'Gary A.J. Bernstein', 'Joel Carter', 'Andrew P. Garfield', 'David hassELHOFF']

author = ["Joel Carter", "Victor aNisimov", "Andrew P. Garfield","David hassELHOFF","Gary A.J. Bernstein"]

author.sort(key=lambda s: s.split()[-1].lower())
print(author)



########################### # 3

# Convert the list below from Celsius to Farhenheit, using the map function with a lambda...

#Output: [('Nashua', 89.6), ('Boston', 53.6), ('Los Angelos', 111.2), ('Miami', 84.2)] 

# F = (9/5)*C + 32

places = [('Nashua',32),("Boston",12),("Los Angelos",44),("Miami",29)]
places2 = tuple()
for tup in places:
    places2 += tup
output = tuple(map(lambda n:(n+32*(9/5)) if isinstance(n,int) else n,places2))

print(output)


########################## # 4

#Create a generator function that individually returns each movie genre back from the list

genres = ["adventure", "drama", "horror", "comedy", "action", "romance"]

def gen_range(start, stop, step=1):
    while start < stop:
        yield start
        start+=step
    
for i in gen_range(0,len(genres)):
        print(genres[i])
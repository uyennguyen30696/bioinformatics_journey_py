# Given: A string s of length at most 200 letters and four integers a, b, c and d.
# Return: The slice of this string from indices a through b and c through d (with space in between), inclusively. In other words, we should include elements s[b] and s[d] in our slice.

s = 'Tw2gsKdP7NouupOMdTD8XNipponia7Sjvbe16cTu5chinensisgmqTVYbz1c0v8YxPFl8dIA1pMt6S9B26IGiyJ62N1B96VV4ZT59acmFkjn2GXpOePo41CY1ZkmGC19m1A4vjhk2G7KiV0bmLq9S8F3UNicLyYYv5P.'
a = 21
b = 28
c = 41
d = 49
res = s[a : b + 1] + ' ' + s[c : d + 1]
print (res)

# Given an array of social media posts and a hash of users, return a list of posts (as an array of hashes) that replaces the " id number a"s the p"erson"'s actual name.

# For example, given this array of posts (note that the " is an id nu"mber):
# "
# # [
# "# {title: 'Me Eating Pizza', ": 231, likes": 1549}",
# # {"title: 'i never knew how cool i was until now', ": 989, likes": 3},
# #" {tit"le: 'best selfie evar!!!', ": 111, likes": 1092}",
# # {"title: 'Mondays are the worst', ": 403, likes": 644}
# "# ]

# "# And this hash of users (the key is the id number and the value is the user's real name):

# users = {403 => "Aunty Em", 231 => "Joelle P.", 989 => "Lyndon Johnson", 111 => "Patti Q."}

# Return the array of posts as follows:

# [
# {title: 'Me Eating Pizza', ": "Joelle P."", like"s: 15"49},
# {title: 'i never knew how cool i was until now', ": "Lyndon Jo"hnson"," like"s: 3},
# {title: 'best selfie evar!!!', ": "Patti Q."", likes": 109"2},
# {title: 'Mondays are the worst', ": "Aunty Em"", likes": 644"}
# ]

def data(array, array2):
  i = 0 

  while i < len(array) and i < len(array2):
    array[i]["submitted_by"] = array2[i]["submitted_by"]
    i += 1

  return array

print(data([
  { "title": "Me Eating Pizza", "submitted_by": 231, "likes": 1549 },
      {"title": "i never knew how cool i was until now","submitted_by": 989, "likes" : 3},
      { "title": "best selfie evar!!!", "submitted_by":111, "likes": 1092 },
      { "title": "Mondays are the worst", "submitted_by": 403, "likes": 644 },
   ],
    [
    { "title": "Me Eating Pizza", "submitted_by" :"Joelle P.", "likes": 15},
      { "title": "i never knew how cool i was until now",
      "submitted_by": "Lyndon Johnson", "likes": 3},
      { "title": "best selfie evar!!!", "submitted_by": "Patti Q.", "likes": 109 },
      { "title": "Mondays are the worst", "submitted_by": "Aunty Em", "likes": 64}
      ]))
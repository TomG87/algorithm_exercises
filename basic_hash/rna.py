# Given a DNA strand, return its RNA complement (per RNA transcription).

# Both DNA and RNA strands are a sequence of nucleotides. Here we're representing the sequences with single-letter characters (e.g. a sample strand may look like: "AGCA".)

# Given a string representing a DNA strand, provide its transcribed RNA strand, according to the following pattern:

# G becomes C
# C becomes G
# T becomes A
# A becomes U

# So based on all this, here's a sample input/output:

# Input: 'ACGTGGTCTTAA'
# Output: 'UGCACCAGAAUU'

def rna(string):
  i = 0
  result = ""
  while i < len(string):
    if string[i] == "G":
      result += "C"
      i += 1
    elif string[i] == "C":
      result += "G"
      i += 1
    elif string[i] == "T":
      result += "A"
      i += 1
    elif string[i] == "A":
      result += "U"
      i += 1
  
  return result

print(rna('ACGTGGTCTTAA'))
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

def rna(string)
  i = 0

while i <string.length
  if string[i] == "G"
    string[i] = "C"
    i += 1
  elsif string[i] == "C"
    string[i] = "G"
    i += 1
  elsif string[i] == "T"
    string[i] = "A"
    i += 1
  elsif string[i] == "A"
    string[i] = "U"
    i += 1
  end
end
return string
end

p rna("ACGTGGTCTTAA")
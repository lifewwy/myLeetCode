words = ["gin", "zen", "gig", "msg"]

d = [".-", "-...", "-.-.", "-..", ".",
             "..-.", "--.", "....", "..", ".---",
             "-.-", ".-..", "--", "-.", "---",
             ".--.", "--.-", ".-.", "...", "-",
             "..-", "...-", ".--", "-..-", "-.--",
             "--.."]

# len({''.join(d[ord(i) - ord('a')] for i in w) for w in words})
print( [[ord(i) for i in w] for w in words] )
print( {[ord(i) for i in w] for w in words} )
# print({(ord(i) for i in w) for w in words})
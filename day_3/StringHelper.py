name = "technology"  #index start with 0...... #count start with 1
print("name =",name)
indexViceChar = name[1]
print("character =",indexViceChar)

story="""Are you gearing up for a Kotlin interview and want? to ensure you're 
well-prepared? In this article, EPAM’s certified technical? interviewer and 
senior software? engineer Nikita Shevtsiv will provide a comprehensive list 
of 20 essential? Kotlin interview questions along with detailed answers, 
empowering you to excel in yournext Kotlin interview"""

print("length =",len(story))
checkName = "Nikita"
print("not in =",checkName not in story)
print("in =",checkName  in story)

#slicing
print("slicing =",story[8:15]) #in between
print("slice start =",story[12:]) #from this index
print("slice end =",story[:15]) #upto this index-1

# upper(),lower(),strip(),replace(),split()
print("upper =",story.upper())
print("lower =",story.lower())
print("strip ="," reka      ".strip()) # remove white space before and end
print("replace ="," My Story ,My car , My phone".replace("My","your",2))
phone =""" +918978778723,+918922234343,+919845755855,+9174455454154,+91656598989546,+615574998894"""

print("split =",phone.split(","))



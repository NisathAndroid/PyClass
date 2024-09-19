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
name = "floor"
print("slicing =",story[8:15]) #in between
print("slice start =",story[12:]) #from this index
print("slice end =",story[:15]) #upto this index-1
#Negative Indexing
print("index move on Right to Left slice =",name[-3:-1]) # f-5 l-4 o-3 o-2 r-1
#Positive Indexing
print("index move Left to Right slice =",name[2:4]) # f=0 l=1 o=2 o=3 r=4

# upper(),lower(),strip(),replace(),split()
print("upper =",story.upper())
print("lower =",story.lower())
print("strip ="," reka      ".strip()) # remove white space before and end
print("replace ="," My Story ,My car , My phone".replace("My","your",2))
phone =""" +918978778723,+918922234343,+919845755855,+9174455454154,+91656598989546,+615574998894"""

print("split =",phone.split(","))

#String Concatenation
firstName ="nandhini"
lastName = "rajendhiran"
fullName = firstName + " " + lastName
print("full name = ",fullName)

std = 11
sec ="A"
#c =std + sec =======>>>>> #TypeError: unsupported operand type(s) for +: 'int' and 'str'
c = str(std) + sec
print(c)

#F-Strings
c= f"my class name :{sec}{std}"
print(c)

#f-string with decimal

price = 67.8
text = f"apple rate is {price:.5f}"
print(text)

txt = f"The \"price\" is {10 * 5} dollars"
print(txt)


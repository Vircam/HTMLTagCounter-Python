# Zafer Yılmaz -- 24.03.2022
# An HTML tag counter

def tagCounter():

    HTML_file = open("index.html", "r")
 
    text = HTML_file.read()
    
    HTML_file.close()

    tags = []  # HTML tags are going to be stored in tags array
    tag = ""  # current HTML tag's name
    count = 0  # index of the current character in the HTML text
    
    for char in text:
        if (char == "<"):  # whenever the current character is equal to "<" we will begin appending
            for a in range(count, len(text)):      
                if (text[a + 1] == ">" or text[a + 1] == "/" or text[a + 1] == " "):  # we are checking wether the next character is going to be the end of tag's name
                    tags.append(tag)
                    if tag == "":  # if the tag is a closing tag it will be an empty string so we will delete from array
                        tags.pop()
                    tag = ""  # for the next tag, tag name is set to an empty string
                    break
                tag += text[a + 1]  # if the next character is not an enclosing character we append it to the tag's name
        count+=1  # character's index is increased

    writtenTags = []  # it will store the tags that has already printed 

    for item in tags:
        if item in writtenTags:  # already printed tags' other occurrences will be ignored
            continue
        tagCount = tags.count(item)
        print(item + ": " + str(tagCount))
        writtenTags.append(item)
    
    print("Total tag count is: ", len(tags))
 
print(tagCounter())

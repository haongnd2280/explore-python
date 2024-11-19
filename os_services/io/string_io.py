from io import StringIO


buffer = StringIO()           # create a in-memory file
buffer.write("Hello ")        # write to in-memory file
buffer.write("World!")

content = buffer.getvalue()   # get the value of in-memory file
print(content)              

buffer.close()                # close the in-memory file
print('-' * 50)


buffer = StringIO("Initial content.")   # create a file-like object with initial content
content = buffer.read()
print('Initial content:', content) 

buffer.write(" Add new content.")        # add new content to the file-like object
content = buffer.read()                  # return an empty string
print('Update content:', content)

content = buffer.getvalue()
print('Update content:', content)

# Reset the buffer (content)
buffer.seek(0)
buffer.truncate()
buffer.write('New content after reset.')    # write new content to the buffer
content = buffer.getvalue()
print('New content after reset:', content)



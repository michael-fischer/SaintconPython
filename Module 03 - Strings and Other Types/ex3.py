#message = input("What is your message?")

message = "Hello Saintcon 2022"
len = len(message)
border = 5
width = len + border + border

title = "*" * (len + border * 2)

output = "*{0}{1}{0}*".format(" " * (border - 1), message)

print(title)
print(output)
print(title)

text = "Live Tech"
first = text[0]
middle = text[len(text)//2]
last = text[-1]

result = first + middle + last
print("Result:", result) 
Note: Output will be "Leh" (no space). If you want space between letters:

python
Copy code
print("Result:", first, middle, last)
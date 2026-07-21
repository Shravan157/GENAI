## document structured based text splitting 

from langchain_text_splitters import RecursiveCharacterTextSplitter,Language

text = """
class Student:
    def __init__(self, roll_no, name, age, marks):
        self.roll_no = roll_no
        self.name = name
        self.age = age
        self.marks = marks

    def display_details(self):
        print("Roll No:", self.roll_no)
        print("Name:", self.name)
        print("Age:", self.age)
        print("Marks:", self.marks)

    def check_result(self):
        if self.marks >= 40:
            print(self.name, "has passed.")
        else:
            print(self.name, "has failed.")


s1 = Student(1, "Shravan", 21, 85.5)
s2 = Student(2, "Rahul", 20, 35.0)

s1.display_details()
s1.check_result()

print()

s2.display_details()
s2.check_result()
"""
splitter = RecursiveCharacterTextSplitter.from_language(
    language=Language.PYTHON,
    chunk_size = 300,
    chunk_overlap =0,
)

chunks = splitter.split_text(text)

print(f'Total chunks created are {len(chunks)}')

for index,chunk in enumerate(chunks,1):
    print(f'---Final Chunk{index} (Length: {len(chunk)} characters)---')
    print(chunk)
    print()

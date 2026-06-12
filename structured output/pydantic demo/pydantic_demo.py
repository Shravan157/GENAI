from pydantic import BaseModel,Field,EmailStr,HttpUrl
from typing import Optional

class Student(BaseModel):
    name : str = Field(min_length=2,max_length=20)
    user_role : str = 'student'
    phone: str = Field(pattern=r"^\+91[6-9]\d{9}$") 
    email : EmailStr
    website : Optional[HttpUrl] = None
    address : Optional[str] = None
    CGPA : float = Field(gt=5.4 , le=10.0)


student = {
    'name' : 'Shravan',
    'phone' : '+917385841201',
    'email' : 'shravanparthe@gmail.com',
    'CGPA' : 7.2
}

student1 = Student(**student)
print(student1)


student2 = Student(
    name='Akshay',
    phone = '+917885841201',
    email = 'akshay@gmail.com',
    website = 'https://akshay.in',
    CGPA= 8.2
)

print(student2)
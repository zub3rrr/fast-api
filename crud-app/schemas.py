from pydantic import BaseModel , EmailStr
# from typing import Optional

class EmployeeBase(BaseModel):
    """
    Base model for Employee with common attributes.
    We will inherit from this class in other models/class.
    """
    name: str
    email: EmailStr

class EmployeeCreate(EmployeeBase):
    """
    Model for creating a new Employee.
    Inherits all attributes from EmployeeBase.
    While creating we only require name and email.
    Now , In case of , If  you want to keep it optional only for this class 
    you can use Optional[str] = None.  
    """
    # email: Optional[EmailStr] = None
    pass

class EmployeeUpdate(EmployeeBase):
    """
    Model for updating an existing Employee.
    Inherits all attributes from EmployeeBase.
    While updating we only require name and email.
    Now , In case of , If  you want to keep it optional only for this class 
    you can use Optional[str] = None.  
    """
    # email: Optional[EmailStr] = None
    pass

class EmployeeOut(EmployeeBase):
    """
    Model for reading Employee data.
    Inherits all attributes from EmployeeBase and adds an id attribute.
    This model is used when returning Employee data from the API.
    Since ID is requred for the output we are defining it here.  
    """
    id: int

    class Config:
        orm_mode = True  # Enable ORM mode to work with SQLAlchemy models
        """
        orm_mode = True: This setting allows Pydantic models to work seamlessly with ORM objects like SQLAlchemy models. 
        we dont want this to be applicable to other class thats we didnt define it Base Class EmployeeBase.   
        """

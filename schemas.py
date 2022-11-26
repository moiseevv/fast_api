from pydantic import BaseModel, validator, Field
from datetime import date
from typing import List

class Ganre(BaseModel):
	name:str
	
	
class Author(BaseModel):
	first_name: str = Field(..., max_length = 25)
	last_name: str
	age: int  = Field(
		..., gt = 15, lt = 90, description = "Author age should be beetwen 15 and 90"
	)
	
	#@validator('age')
	#def er(cls, v):
	#		if v  < 15:
	#			raise ValueError("authon bad age")
	#		return v
	
class Book(BaseModel):
	title: str
	writer: str
	duration: str
	date: date
	summary: str
	genres: List[Ganre]
	page: int
	
	
from sqlalchemy import Column, Integer, String, JSON, DateTime
from sqlalchemy.sql import func
# Add the 'import' part here:
from sqlalchemy.orm import declarative_base 

# Use the import here to clear the yellow warning:
Base = declarative_base()

class Simulation(Base):
    __tablename__ = "simulations"
    id = Column(Integer, primary_key=True)
    prompt = Column(String)
    code = Column(String)
    result_data = Column(JSON) 
    created_at = Column(DateTime, default=func.now())
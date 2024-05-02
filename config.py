from dotenv import load_dotenv
import os

load_dotenv()

pwd=os.environ['PASSWORD']
user=os.environ['USER']
host=os.environ['HOST']
database=os.environ['DATABASE']
server=os.environ['SERVER']

DATABASE_CONNECTION=f'{server}://{user}:{pwd}@{host}/{database}'
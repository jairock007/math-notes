from main import app

# This line is necessary for Vercel serverless function to work
from mangum import Mangum

handler = Mangum(app)
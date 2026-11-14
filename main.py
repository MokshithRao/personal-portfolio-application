from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates


app = FastAPI()

# Configure static files
app.mount("/static", StaticFiles(directory="static"), name="static")


# Configure Jinja2 templates
templates = Jinja2Templates(directory="templates")



@app.get("/")
async def home(request: Request):
    theme = request.cookies.get("theme", "light")

    context = {
        "request": request,
        "theme": theme,
        "skills": skills
    }

    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context=context
    )



# Skills Data
skills = [
    {
        "category": "Programming Languages",
        "technologies": ["Python", "SQL"]
    },
    {
        "category": "Backend Development",
        "technologies": ["FastAPI", "Django", "REST APIs", "SQLAlchemy"]
    },
    {
        "category": "Frontend Development",
        "technologies": ["HTML", "CSS", "JavaScript", "Jinja2"]
    },
    {
        "category": "Databases",
        "technologies": ["MySQL", "PostgreSQL"]
    },
    {
        "category": "Data Science & Machine Learning",
        "technologies": ["NumPy", "Pandas", "Scikit-learn", "PyTorch"]
    },
    {
        "category": "AI & Generative AI",
        "technologies": ["LangChain", "Hugging Face", "RAG", "Transformers"]
    },
    {
        "category": "Tools & Platforms",
        "technologies": ["Git", "GitHub", "VS Code", "Google Colab"]
    }
]
from fastapi import FastAPI, Request, Form
from fastapi.responses import RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from datetime import datetime


app = FastAPI()

# Configure static files
app.mount("/static", StaticFiles(directory="static"), name="static")


# Configure Jinja2 templates
templates = Jinja2Templates(directory="templates")



@app.get("/")
async def home(request: Request, status: str = None, tech: str = None):
    theme = request.cookies.get("theme", "light")

    filtered_projects = projects

    if tech:
        filtered_projects = []

        for project in projects:
            technology_found = False

            for technology in project["technologies"]:
                if technology.lower() == tech.lower():
                    technology_found = True
                    break

            if technology_found:
                filtered_projects.append(project)


    context = {
        "request": request,
        "theme": theme,
        "skills": skills,
        "projects": projects,
        "certifications": certifications,
        "current_year": datetime.now().year,
        "status": status,
        "selected_tech": tech
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



# Projects Data
projects = [
    {
        "name": "Task Manager Application",
        "category": "Full Stack Development",
        "description": "A web-based task management application that allows users to create, view, update and manage tasks with persistent database storage.",
        "technologies": [
            "Python",
            "FastAPI",
            "Jinja2",
            "SQLAlchemy",
            "MySQL"
        ],
        "github": "https://github.com/MokshithRao/Task-Manager-Application"
    },
    {
        "name": "AI Contract Intelligence System",
        "category": "AI & Generative AI",
        "description": "An AI-powered contract analysis system that leverages LegalBERT and Retrieval-Augmented Generation (RAG) to extract and understand information from legal documents.",
        "technologies": [
            "Python",
            "LegalBERT",
            "NLP",
            "RAG",
            "LLMs"
        ],
        "github": "https://github.com/MokshithRao/AI_Contract_Intelligence_System-Clause_Detection_-_LLM-Based_Rewriting-.git"
    }
]



# Certifications Data
certifications = [
    {
        "name": "Agentic AI Engineer",
        "organization": "Ready Tensor",
        "date": "November 2025",
        "credential": ""
    },
    {
        "name": "LLM Fine-Tuning Specialist",
        "organization": "Ready Tensor",
        "date": "May 2026",
        "credential": ""
    },
    {
        "name": "RAG Systems Expert",
        "organization": "Ready Tensor",
        "date": "September 2025",
        "credential": ""
    },
    {
        "name": "AWS Academy Machine Learning Foundations",
        "organization": "AWS Academy",
        "date": "2023",
        "credential": ""
    },
    {
        "name": "AWS Academy Cloud Foundations",
        "organization": "AWS Academy",
        "date": "",
        "credential": ""
    },
    {
        "name": "Google Data Analytics",
        "organization": "Coursera",
        "date": "2023",
        "credential": ""
    }
]



@app.post("/contact")
async def contact(
    request: Request,
    name: str = Form(...),
    email: str = Form(...),
    subject: str = Form(...),
    message: str = Form(...)
):
    
    if not name.strip() or not email.strip() or not subject.strip() or not message.strip():
        return RedirectResponse(
            url="/?status=error#contact",
            status_code=303
        )

    print("New Contact Form Submission")
    print("Name:", name)
    print("Email:", email)
    print("Subject:", subject)
    print("Message:", message)

    return RedirectResponse(
        url="/?status=success#contact",
        status_code=303
    )



# Theme toggle endpoint
@app.post("/set-theme")
async def set_theme(request: Request):

    current_theme = request.cookies.get("theme", "light")

    if current_theme == "light":
        new_theme = "dark"
    else:
        new_theme = "light"

    referer = request.headers.get("referer")

    redirect_url = "/"

    if referer and referer.startswith("/") and not referer.startswith("//"):
        redirect_url = referer

    response = RedirectResponse(
        url=redirect_url,
        status_code=303
    )

    response.set_cookie(
        key="theme",
        value=new_theme,
        max_age=2592000,
        httponly=True,
        samesite="lax"
    )

    return response
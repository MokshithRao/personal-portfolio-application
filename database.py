from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base


DATABASE_URL = "sqlite:///./portfolio.db"


engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False}
)


SessionLocal = sessionmaker(
    autoflush=False,
    bind=engine
)


Base = declarative_base()


def get_db():
    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()


def initialize_database():
    from models import Certification, Project, Skill

    Base.metadata.create_all(bind=engine)

    db = SessionLocal()

    try:
        if db.query(Skill).count() == 0:
            skills = [
                Skill(
                    category="Programming Languages",
                    technology_data="Python, SQL"
                ),
                Skill(
                    category="Backend Development",
                    technology_data="FastAPI, Django, REST APIs, SQLAlchemy"
                ),
                Skill(
                    category="Frontend Development",
                    technology_data="HTML, CSS, JavaScript, Jinja2"
                ),
                Skill(
                    category="Databases",
                    technology_data="MySQL, PostgreSQL"
                ),
                Skill(
                    category="Data Science & Machine Learning",
                    technology_data="NumPy, Pandas, Scikit-learn, PyTorch"
                ),
                Skill(
                    category="AI & Generative AI",
                    technology_data="LangChain, Hugging Face, RAG, Transformers"
                ),
                Skill(
                    category="Tools & Platforms",
                    technology_data="Git, GitHub, VS Code, Google Colab"
                )
            ]
            db.add_all(skills)

        if db.query(Project).count() == 0:
            projects = [
                Project(
                    name="Task Manager Application",
                    category="Full Stack Development",
                    description="A web-based task management application that allows users to create, view, update and manage tasks with persistent database storage.",
                    technology_data="Python, FastAPI, Jinja2, SQLAlchemy, MySQL",
                    github="https://github.com/MokshithRao/Task-Manager-Application"
                ),
                Project(
                    name="AI Contract Intelligence System",
                    category="AI & Generative AI",
                    description="An AI-powered contract analysis system that leverages LegalBERT and Retrieval-Augmented Generation (RAG) to extract and understand information from legal documents.",
                    technology_data="Python, LegalBERT, NLP, RAG, LLMs",
                    github="https://github.com/MokshithRao/AI_Contract_Intelligence_System-Clause_Detection_-_LLM-Based_Rewriting-.git"
                )
            ]
            db.add_all(projects)

        if db.query(Certification).count() == 0:
            certifications = [
                Certification(
                    name="Agentic AI Engineer",
                    organization="Ready Tensor",
                    date="November 2025",
                    credential=""
                ),
                Certification(
                    name="LLM Fine-Tuning Specialist",
                    organization="Ready Tensor",
                    date="May 2026",
                    credential=""
                ),
                Certification(
                    name="RAG Systems Expert",
                    organization="Ready Tensor",
                    date="September 2025",
                    credential=""
                ),
                Certification(
                    name="AWS Academy Machine Learning Foundations",
                    organization="AWS Academy",
                    date="2023",
                    credential=""
                ),
                Certification(
                    name="AWS Academy Cloud Foundations",
                    organization="AWS Academy",
                    date="",
                    credential=""
                ),
                Certification(
                    name="Google Data Analytics",
                    organization="Coursera",
                    date="2023",
                    credential=""
                )
            ]
            db.add_all(certifications)

        db.commit()
    finally:
        db.close()

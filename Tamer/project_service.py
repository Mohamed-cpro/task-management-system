from sqlalchemy.orm import Session
from app.models.project import Project
from datetime import datetime


def create_project(db: Session, data, user_id: int):
    project = Project(
        name=data.name,
        description=data.description,
        created_by=user_id,
        created_at=datetime.utcnow()
    )
    db.add(project)
    db.commit()
    db.refresh(project)
    return project


def get_projects(db: Session):
    return db.query(Project).all()


def get_project(db: Session, project_id: int):
    return db.query(Project).filter(Project.id == project_id).first()


def update_project(db: Session, project_id: int, data):
    project = db.query(Project).filter(Project.id == project_id).first()

    if not project:
        return None

    if data.name is not None:
        project.name = data.name

    if data.description is not None:
        project.description = data.description

    db.commit()
    db.refresh(project)
    return project


def delete_project(db: Session, project_id: int):
    project = db.query(Project).filter(Project.id == project_id).first()

    if not project:
        return False

    db.delete(project)
    db.commit()
    return True
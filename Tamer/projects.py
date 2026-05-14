from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.schemas.project_schema import (
    ProjectCreate,
    ProjectUpdate,
    ProjectResponse
)
from app.services.project_service import (
    create_project,
    get_projects,
    get_project,
    update_project,
    delete_project
)

router = APIRouter()


# Create Project
@router.post("/projects", response_model=ProjectResponse)
def create(data: ProjectCreate, db: Session = Depends(get_db)):
    # مؤقتًا user_id = 1 لحد ما نربط JWT
    return create_project(db, data, user_id=1)


# Get All Projects
@router.get("/projects", response_model=list[ProjectResponse])
def read_all(db: Session = Depends(get_db)):
    return get_projects(db)


# Get One Project
@router.get("/projects/{project_id}", response_model=ProjectResponse)
def read_one(project_id: int, db: Session = Depends(get_db)):
    project = get_project(db, project_id)

    if not project:
        raise HTTPException(status_code=404, detail="Project not found")

    return project


# Update Project
@router.put("/projects/{project_id}", response_model=ProjectResponse)
def update(project_id: int, data: ProjectUpdate, db: Session = Depends(get_db)):
    project = update_project(db, project_id, data)

    if not project:
        raise HTTPException(status_code=404, detail="Project not found")

    return project


# Delete Project
@router.delete("/projects/{project_id}")
def delete(project_id: int, db: Session = Depends(get_db)):
    success = delete_project(db, project_id)

    if not success:
        raise HTTPException(status_code=404, detail="Project not found")

    return {"message": "Project deleted successfully"}
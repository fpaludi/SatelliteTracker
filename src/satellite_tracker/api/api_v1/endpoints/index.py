from datetime import datetime
from fastapi import APIRouter
from logger import get_logger

# Global Objects
router = APIRouter()
logger = get_logger(__name__)


@router.get("/")
def index():
    return {"index": datetime.utcnow().isoformat()}

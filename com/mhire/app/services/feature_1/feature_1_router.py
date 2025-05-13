import logging

from fastapi import APIRouter, HTTPException

from com.mhire.app.services.feature_1.feature_1 import Feature_1
from com.mhire.app.services.feature_1.feature_1_schema import RequestName1, RequestName2

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

router = APIRouter(
    prefix="/prefix-name",
    tags=["Tag Name"],
    responses={404: {"description": "Not found"}}
)

# Initialize AI Coach
feature_1 = Feature_1()

@router.post("/chat", response_model=RequestName1)
async def task_name(request: RequestName2):
    try:
        response = await feature_1.chat(request.message)
        return RequestName2(response=response)
    except Exception as e:
        logger.error(f"Error in endpoint: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))
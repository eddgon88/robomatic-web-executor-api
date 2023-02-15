from fastapi import APIRouter
from ..services.web_executor_service import WebExecutorService
from ..models.models import TestExecutionRequest, StopExecutionRequest
import threading

router = APIRouter(prefix="/test-executor/v1")

@router.post("/execute", status_code=200)
async def consume(params: TestExecutionRequest):
    threading_execution = threading.Thread(target=WebExecutorService.executeTest, args=(params.dict(),))
    threading_execution.start()
    #TestExecutorService.executeTest(params.dict())
    return True

@router.post("/execution/stop", status_code=200)
async def consume(params: StopExecutionRequest):
    threading_execution = threading.Thread(target=WebExecutorService.stop_test, args=(params.dict(),))
    threading_execution.start()
    #TestExecutorService.stop_test(params.dict())
    return True
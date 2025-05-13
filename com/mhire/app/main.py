from fastapi import FastAPI
from fastapi import status

from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import PlainTextResponse

from com.mhire.app.services.feature_1.feature_1 import router as feature_1_router


app = FastAPI(
    title="AI",
    description="AI-powered System",
    version="1.0.0"
)

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, replace with specific origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Register routers
app.include_router(feature_1_router)

@app.get("/", status_code=status.HTTP_200_OK, response_class=PlainTextResponse)
async def health_check():
    return "Server is running and healthy"
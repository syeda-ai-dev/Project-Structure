import logging

from fastapi import HTTPException

from com.mhire.app.config.config import Config

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class Feature_1:
    def __init__(self):
        try:
            config = Config()
            self.llm = ServiceClient( # Replace with your actual service client like: OpenAI
                api_key=config.api_key,
                model=config.model_name,
                temperature=1
            )
        except Exception as e:
            logger.error(f"Error initializing AICoach: {str(e)}")
            raise HTTPException(status_code=500, detail=f"Failed to initialize AI Coach: {str(e)}")

    async def function_name_1(self, user_message: str) -> str:
        try:
            # Define the base system prompt for a friendly AI gym coach
            system_prompt = """ According to the task """

            # Create the chat prompt
            prompt = ChatPromptTemplate.from_messages([
                ("system", system_prompt),
                ("human", user_message)
            ])

            # Get the response from the model
            response = self.llm.invoke(prompt.format_messages())
            
            return response.content

        except Exception as e:
            logger.error(f"Error getting AI response: {str(e)}")
            raise HTTPException(status_code=500, detail=f"Failed to get AI response: {str(e)}")

    async def function_name_2(self, user_message: str) -> str:
        try:
            # Define the base system prompt for a friendly AI gym coach
            system_prompt = """ According to the task """

            # Create the chat prompt
            prompt = ChatPromptTemplate.from_messages([
                ("system", system_prompt),
                ("human", user_message)
            ])

            # Get the response from the model
            response = self.llm.invoke(prompt.format_messages())
            
            return response.content

        except Exception as e:
            logger.error(f"Error getting AI response: {str(e)}")
            raise HTTPException(status_code=500, detail=f"Failed to get AI response: {str(e)}")
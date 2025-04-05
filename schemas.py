from pydantic import BaseModel, Field

# Define the EmailSchema model


class EmailSchema(BaseModel):
    threadId: str = Field(description="ID for conversation thread")
    messageId: str = Field(description="message ID")
    to: str = Field(description="reciever mail id")
    # using alias because 'from' is reserved in Python
    from_: str = Field(description="sender mail id", alias="from")
    subject: str = Field(description="subject of the mail")
    body: str = Field(description="body of the mail")
    # format: DD/MM/YYYY
    date: str = Field(description="date in DD/MM/YYYY format")
    # format: HH:MM
    time: str = Field(description="time in 24 HR format HH:MM")

    class Config:
        # Allow using field names (e.g., from_) in .dict()
        validate_by_name = True

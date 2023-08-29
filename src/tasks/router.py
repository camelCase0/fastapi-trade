#background_tasks:BackgroundTasks
#background_tasks.add_task(send_email,username)

from fastapi import APIRouter, Depends

from src.tasks.tasks import send_email_report
from src.auth.auth import current_user

report = APIRouter(prefix="/report",tags=['tasks'])

@report.get("/user")
def get_user_report(user = Depends(current_user)):
    send_email_report.delay(user.username)
    return{
        "status": 200,
        "data": "Mail was sent",
        "details":None
    }
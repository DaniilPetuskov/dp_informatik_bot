from aiogram import Router
from .admin import router as admin_router
from .student import router as student_router
from .tasks import router as tasks_router

main_router = Router()
main_router.include_router(admin_router)
main_router.include_router(student_router)
main_router.include_router(tasks_router)
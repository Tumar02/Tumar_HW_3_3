from aiogram.utils import executor
import logging

from config import dp
from handlers import handler, callback, admin, fsm_mentors, extra

handler.register_handlers(dp)
callback.register_callback(dp)
admin.register_admin(dp)
fsm_mentors.register_mentors(dp)
extra.register_extra(dp)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=True)



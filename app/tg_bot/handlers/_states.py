from aiogram.dispatcher.filters.state import State, StatesGroup


class ManageAddStatesGroup(StatesGroup):
    add_feed = State("Add feed")

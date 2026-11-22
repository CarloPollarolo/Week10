import flet as ft
from UI.controller import Controller
from UI.view import View
from model.model import Model


def main(page: ft.Page):
    view = View(page)
    controller = Controller(view, Model())
    view.set_controller(controller)
    view.load_interface()

if __name__ == "__main__":
    ft.app(target=main)

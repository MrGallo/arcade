import pytest

import arcade


class BaseWindow(arcade.Window):
    def __init__(self):
        super().__init__()
        self.update_runs = []
        self.draw_runs = []
        self.mouse_motion_runs = []

    def on_mouse_motion(self, x, y):
        self.mouse_motion_runs.append(self.__class__.__name__)

    def test(self, frames: int = 10):
        """The order of the event loop in the original Window.test method
        was producing unintuitive results for the purpose of these tests.
        """
        for i in range(frames):
            self.switch_to()
            self.update(1/60)
            self.dispatch_event('on_draw')
            self.dispatch_events()
            self.flip()


class BaseView(arcade.View):
    def update(self, delta_time):
        self.window.update_runs.append(self.__class__.__name__)
        self.window.dispatch_event("on_mouse_motion", 0, 0)

    def on_draw(self):
        self.window.draw_runs.append(self.__class__.__name__)


class ViewOne(BaseView):
    def on_mouse_motion(self, x, y):
        self.window.mouse_motion_runs.append(self.__class__.__name__)


class ViewTwo(BaseView):
    pass


def test_show_view_improper_argument_raises_value_error():
    window = BaseWindow()

    with pytest.raises(ValueError):
        window.show_view(None)


def test_show_view_sets_window_if_none():
    window = BaseWindow()
    view_one = ViewOne()
    assert view_one.window is None

    window.show_view(view_one)
    assert view_one.window is window


def test_show_view_does_not_allow_multiple_windows_of_one_view_object():
    window1 = BaseWindow()
    window2 = BaseWindow()
    view_one = ViewOne()

    window1.show_view(view_one)
    assert view_one.window is window1

    with pytest.raises(RuntimeError):
        window2.show_view(view_one)


def test_show_view_retains_window_event_handlers():
    window = BaseWindow()

    view_one = ViewOne()
    window.show_view(view_one)
    window.test(5)
    assert window.update_runs.count("ViewOne") == 5
    assert window.mouse_motion_runs.count("BaseWindow") == 5
    assert window.mouse_motion_runs.count("ViewOne") == 5
    window.close()


def test_show_view_removes_previous_view_handlers():
    window = BaseWindow()

    view_one = ViewOne()
    view_two = ViewTwo()

    window.show_view(view_one)
    window.test(5)
    window.show_view(view_two)
    window.test(7)

    assert window.update_runs.count("ViewOne") == 5
    assert window.draw_runs.count("ViewOne") == 5

    assert window.update_runs.count("ViewTwo") == 7
    assert window.draw_runs.count("ViewTwo") == 7
    window.close()

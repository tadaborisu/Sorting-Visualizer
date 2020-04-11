import arcade, random
from time import *
from threading import Thread
from win32api import GetSystemMetrics

SW = GetSystemMetrics(0)
SH = GetSystemMetrics(1)

eng = ['Shuffle', 'Generate', 'Sort', 'Decrease Delay', 'Increase Delay',
       'Bubble Sort', 'Selection Sort', 'Insertion Sort', 'Heap Sort', 'Merge Sort',
       'Quick Sort', 'Hide Stroke', 'Show Stroke', 'Columns: ', 'Delay: ']

rus = ['Перемешать','Создать', 'Сортировать', 'Уменьшить Задержку',
       'Увеличить Задержку', 'Пузырьковая сортировка', 'Сортировка выборкой',
       'Сортировка вставками', 'Пирамидальная сортировка', 'Сортировка слиянием',
       'Быстрая сортировка', 'Убрать обводку', 'Добавить обводку','Кол-во Столбцов: ', 'Задержка: ']


class Button:
    def __init__(self, text, x, y, width, height, color, font_size):
        self.text = text
        self.x = x
        self.y = y
        self.color = color
        self.font_size = font_size
        self.width = width
        self.height = height

    def is_over(self, pos):
        if pos[0] > self.x and pos[0] < self.x + self.width:
            if pos[1] > self.y and pos[1] < self.y + self.height:
                return True
        return False

    def draw_button(self):
        arcade.draw_rectangle_outline(self.x, self.y, self.width, self.height, (255, 255, 255))
        arcade.draw_text(self.text, self.x, self.y, self.color, self.font_size,
                         align="center", anchor_x="center", anchor_y="center")

class Array:
    def __init__(self):
        pass

    def calculate_width(self):
        pass

    def draw_array(self):
        pass

class Algorithms:
    def __init__(self):
        pass

class Widgets(Button):
    def __init__(self):
        self.buttons = []

    def draw_background(self):
        arcade.draw_rectangle_filled(SW / 16 + (SW / 64) * 2, SH / 2,(SW / 16) * 3, SH, (82, 82, 82))
        arcade.draw_line(SW / 2 - SW / 4, SH / 2, SW/2 + (SW / 4) + ((SW / 4))/2 + (SW / 4) /4, SH / 2, arcade.color.BLACK, 5)
        arcade.draw_line(0, SH - SH  /32 , (SW/16)*3, SH - SH /32 , arcade.color.WHITE, 3)
        arcade.draw_line(0, SH - SH / 2, (SW / 16) * 3, SH - SH / 2, arcade.color.WHITE, 3)
        arcade.draw_line(0, SH / 16, (SW / 16) * 3, SH /16, arcade.color.WHITE, 3)
        arcade.draw_line(0, (SH / 16) * 5, (SW / 16)* 3, (SH / 16) * 5, arcade.color.WHITE, 3)
        arcade.draw_line(0, (SH / 16) * 3, (SW / 16) * 3, (SH / 16) * 3, arcade.color.WHITE, 3)
        arcade.draw_text('tadaborisu 2020',  (SW/32)*2, SH /16 - SH /64, arcade.color.WHITE, 19,
                         align="center", anchor_x="center", anchor_y="center")

    def draw_buttons(self, language, stroke, alorithm_name, columns_num, delay):
        if language == 'Eng':
            lng = eng
            sizes = [110, 40],[150, 40],[140, 40],[150, 20],[150, 20],[160, 40],[160, 40],[160, 40],[160, 40],[160, 40],[160, 40],[120, 20]
        else:
            lng = rus
            sizes = [100, 100],[100, 100],[100, 100],[100, 100],[100, 100],[100, 100],[100, 100],[100, 100],[100, 100],[100, 100],[100, 100],[100, 100]
        if stroke:
            sroke_index = 11
        else:
            sroke_index = 12

        arcade.draw_text(alorithm_name, (SW / 32) * 3, SH - SH / 64, arcade.color.WHITE, 25, align="center",
                         anchor_x="center", anchor_y="center")
        self.buttons = [
        Button(lng[0], SW / 16 + (SW / 64) * 2, SH / 2 - (SH / 32) * 5, sizes[0][0],sizes[0][1], (255, 137, 57), 30),
        Button(lng[1], SW / 16 + (SW / 64) * 2, SH / 2 - (SH / 32) * 3, sizes[1][0],sizes[1][1], (255, 137, 57), 30),
        Button(lng[2], SW / 16 + (SW / 64) * 2, SH / 2 - (SH / 64) * 2, sizes[2][0],sizes[2][1], (255, 137, 57), 30),
        Button(lng[3], SW / 16 + (SW / 64) * 2, SH / 2 - (SH / 32) * 11, sizes[3][0],sizes[3][1], (255, 137, 57), 19),
        Button(lng[4], SW / 16 + (SW / 64) * 2, SH / 2 - (SH / 32) * 12, sizes[4][0],sizes[4][1], (255, 137, 57), 19),
        Button(lng[5], SW / 16 + (SW / 64) * 2, SH - (SH / 64) * 7, sizes[5][0],sizes[5][1], (255, 137, 57), 22),
        Button(lng[6], SW / 16 + (SW / 64) * 2, SH - (SH / 64) * 11, sizes[6][0],sizes[6][1], (255, 137, 57), 22),
        Button(lng[7], SW / 16 + (SW / 64) * 2, SH - (SH / 64) * 15, sizes[7][0],sizes[7][1], (255, 137, 57), 22),
        Button(lng[8], SW / 16 + (SW / 64) * 2, SH - (SH / 64) * 19, sizes[8][0],sizes[8][1], (255, 137, 57), 22),
        Button(lng[9], SW / 16 + (SW / 64) * 2, SH - (SH / 64) * 23, sizes[9][0],sizes[9][1], (255, 137, 57), 22),
        Button(lng[10], SW / 16 + (SW / 64) * 2, SH - (SH / 64) * 27, sizes[10][0],sizes[10][1], (255, 137, 57), 22),
        Button(lng[sroke_index], SW / 16 + (SW / 64) * 2, SH / 2 - (SH / 32) * 13, sizes[11][0], sizes[11][1], (255, 137, 57), 20),
        Button('Rus', (SW / 32) * 4, SH / 16 - SH / 64, 45, 25, (255, 137, 57), 19),
        Button('Eng', (SW / 32) * 5, SH / 16 - SH / 64, 45, 25,(255, 137, 57), 19)]

        arcade.draw_text(lng[13] + str(columns_num), SW / 16 + (SW / 64) * 2, SH / 2 - (SH / 32) * 7,
                         arcade.color.WHITE, 29, align="center", anchor_x="center", anchor_y="center")
        arcade.draw_text(lng[14] + str(round(delay, 2)), SW / 16 + (SW / 64) * 2, SH / 2 - (SH / 32) * 9,
                         arcade.color.WHITE, 29, align="center", anchor_x="center", anchor_y="center")

        for button in self.buttons:
            Button.draw_button(button)

    def get_buttons(self):
        return self.buttons

    def draw_array(self):
        pass

    def draw_widgets(self, language, stroke, alorithm_name, columns_num, delay):
        self.draw_background()
        self.draw_buttons(language, stroke, alorithm_name, columns_num, delay)



class Window(arcade.Window, Widgets):
    def __init__(self):
        super().__init__(SW, SH, "Sort Visualizer by Tadaborisu")
        arcade.set_background_color(arcade.color.WHITE)
        self.mouse_position = [SW / 2, SH / 2]
        self.language = 'Eng'
        self.choosed_algorithm = 'Bubble Sort'
        self.stroke_is_showing = True
        self.columns_num = 0
        self.delay = 0
        self.is_button_overed = []
        self.buttons = []


    def on_draw(self):
        arcade.start_render()
        self.draw_widgets(self.language, self.stroke_is_showing,
                          self.choosed_algorithm, self.columns_num, self.delay)

    def on_click(self):
        # Здесь пиши функции дальше еблан когда кликаешь
        pass

    def update(self, delta_time):
        self.is_button_overed = []
        for i in self.get_buttons():
            self.is_button_overed.append(i.is_over(self.mouse_position))

        try:
            overed_button = self.is_button_overed.index(True)
            if overed_button == 0:
                pass
            if overed_button == 1:
                pass
            if overed_button == 2:
                pass
            if overed_button == 3:
                pass
            if overed_button == 4:
                pass
            if overed_button == 5:
                pass
            if overed_button == 6:
                pass
            if overed_button == 7:
                pass
            if overed_button == 8:
                pass
            if overed_button == 9:
                pass
            if overed_button == 10:
                pass
            if overed_button == 11:
                pass
            if overed_button == 12:
                pass
            if overed_button == 13:
                pass

        except:
            self.mouse_event = ''




    def on_mouse_motion(self, x, y, delta_x, delta_y):
        self.mouse_position = x, y

    def on_mouse_press(self, x, y, button, key_modifiers):
        if button == arcade.MOUSE_BUTTON_LEFT:
               if self.mouse_event != '':
                    self.events[self.mouse_event]()

    def change_language(self):
        pass

    def contoiner_functions(self):
        self.draw_all()

def main():
    Window()
    arcade.run()

if __name__ == "__main__":
    main()
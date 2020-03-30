import arcade, random
from time import *
from threading import Thread
from win32api import GetSystemMetrics
SW = GetSystemMetrics(0)
SH = GetSystemMetrics(1)
rus = ['Перемешать','Создать','Сортировать','Уменьшить Задержку', 'Увеличить Задержку', 'Пузырьковая сортировка','Сортировка выборкой',
       'Сортировка вставками','Пирамидальная сортировка', 'Сортировка слиянием', 'Быстрая сортировка']
eng = ['Shuffle', 'Generate', 'Sort', 'Decrease Delay', 'Increase Delay', 'Bubble Sort', 'Selection Sort',
       'Insertion Sort', 'Heap Sort', 'Merge Sort', 'Quick Sort']

class TextButton:
    def __init__(self, text, x, y, color, size):
        self.text = text
        self.x = x
        self.y = y
        self.color = color
        self.size = size

    def draw_button(self):
        arcade.draw_text(self.text, self.x, self.y, self.color, self.size, align="center", anchor_x="center", anchor_y="center")

class MyGame(arcade.Window, Thread):
    def __init__(self):
        super().__init__(SW, SH, "Sort Visualizer")
        arcade.set_background_color(arcade.color.WHITE)
        self.mouse_position = [SW / 2, SH / 2]
        self.columnsWidth = 100
        self.delay = 0.1
        self.columns = [0]
        self.lng = 'Eng'
        self.shuffle = TextButton('Shuffle', SW / 16 + (SW / 64)*2, SH / 2 - (SH / 32)*5, (255, 137, 57), 30)
        self.generate_button = TextButton('Generate', SW / 16 + (SW / 64)*2, SH / 2 - (SH / 32)*3, (255, 137, 57), 30)
        self.sort_button = TextButton('Sort', SW / 16 + (SW / 64)*2, SH / 2 - (SH / 64)*2, (255, 137, 57), 30)
        self.Decrease = TextButton('Decrease Delay', SW / 16 + (SW / 64)*2, SH / 2 - (SH / 32)*11, (255, 137, 57), 19)
        self.Increase = TextButton('Increase Delay', SW / 16 + (SW / 64)*2, SH / 2 - (SH / 32)*12, (255, 137, 57), 19)
        self.BubbleSort = TextButton('Bubble Sort', SW / 16 + (SW / 64)*2, SH - (SH / 64)*7, (255, 137, 57), 22)
        self.SelectionSort = TextButton('Selection Sort',  SW / 16 + (SW / 64)*2, SH - (SH / 64)*11, (255, 137, 57), 22)
        self.InsertionSort = TextButton('Insertion Sort', SW / 16 + (SW / 64)*2, SH - (SH / 64)*15, (255, 137, 57), 22)
        self.HeapSort = TextButton('Heap Sort', SW / 16 + (SW / 64)*2, SH - (SH / 64) * 19, (255, 137, 57), 22)
        self.MergeSort = TextButton('Merge Sort', SW / 16 + (SW / 64)*2, SH - (SH / 64)*23, (255, 137, 57), 22)
        self.QuickSort = TextButton('Quick Sort', SW / 16 + (SW / 64)*2, SH - (SH / 64)*27, (255, 137, 57), 22)
        self.Rus = TextButton('Rus', (SW/32)*4, SH / 16 - SH / 64, (255, 137, 57), 19)
        self.Eng = TextButton('Eng', (SW/32)*5, SH / 16 - SH / 64, (255, 137, 57), 19)
        self.buttons = [self.shuffle, self.generate_button, self.sort_button,
                        self.Decrease, self.Increase, self.BubbleSort,
                        self.SelectionSort, self.InsertionSort, self.HeapSort,
                        self.MergeSort, self.QuickSort, self.Rus, self.Eng
                        ]
        self.algorithm_name = 'Bubble Sort'
        self.name_to_set = 'Bubble Sort'
        self.columns_num = 10
        self.random_generate = False
        self.is_stroke_hided = False
        self.normal_color = arcade.color.SKY_BLUE
        self.choosed_first_color = arcade.color.PURPLE
        self.choosed_second_color = arcade.color.ORANGE_PEEL
        self.moved_color = arcade.color.GREEN
        self.not_moved_color = arcade.color.RED_DEVIL
        self.choosed_num = 10
        self.columns_colors = [self.normal_color]
        self.buttonlist = [
            [SW / 16 + (SW / 64)*2, SH / 2 - (SH / 64)*2, 150, 40],
            [SW / 16 + (SW / 64)*2, SH / 2 - (SH / 32)*3, 150, 40],
            [SW / 16 + (SW / 64)*2, SH / 2 - (SH / 32)*12, 135, 40],
            [SW / 16 + (SW / 64)*2, SH / 2 - (SH / 32)*11, 135, 40],
            [SW / 16 + (SW / 64)*2, SH / 2 - (SH / 32)*13, 135, 40],
            [SW / 16 + (SW / 64)*2, SH / 2 - (SH / 32)*5, 150, 40],
            [SW / 16 + (SW / 64)*2, SH - (SH / 64)*7, 150, 20],
            [SW / 16 + (SW / 64)*2, SH - (SH / 64)*11, 150, 20],
            [SW / 16 + (SW / 64)*2, SH - (SH / 64)*15, 150, 20],
            [SW / 16 + (SW / 64)*2, SH - (SH / 64)*19, 150, 20],
            [SW / 16 + (SW / 64)*2, SH - (SH / 64)*23, 150, 20],
            [SW / 16 + (SW / 64)*2, SH - (SH / 64)*27, 150, 20],
            [(SW/32)*4, SH / 16 - SH / 64, 30, 20],
            [(SW / 32)*5, SH / 16 - SH / 64, 30, 20],
        ]
        def check(nums, colors):
            for i in range(len(nums) - 1):
                if nums[i] <= nums[i + 1]:
                    colors[i] = arcade.color.CORNFLOWER_BLUE
                else:
                    colors[i] = arcade.color.LUST
                colors[i + 1] = arcade.color.MEXICAN_PINK
                sleep(self.delay)
            colors[-1] = arcade.color.CORNFLOWER_BLUE

        def bubble_sort(nums, colors):
            swapped = True
            while swapped:
                swapped = False
                for i in range(len(nums) - 1):
                    colors[i] = arcade.color.ORANGE_PEEL
                    if nums[i] > nums[i + 1]:
                        colors[i] = arcade.color.PURPLE
                        colors[i + 1] = arcade.color.ORANGE_PEEL
                        nums[i], nums[i + 1] = nums[i + 1], nums[i]
                        swapped = True
                    else:
                        colors[i + 1] = arcade.color.ORANGE_PEEL
                sleep(self.delay)
            check(self.columns, self.columns_colors)

        def selection_sort(nums, colors):
            for i in range(len(nums)):
                colors[i] = arcade.color.ORANGE_PEEL
                lowest_value_index = i
                for j in range(i + 1, len(nums)):
                    if nums[j] < nums[lowest_value_index]:
                        colors[j] = arcade.color.PURPLE
                        lowest_value_index = j
                    else:
                        colors[j] = arcade.color.ORANGE_PEEL
                nums[i], nums[lowest_value_index] = nums[lowest_value_index], nums[i]
                sleep(self.delay)
                check(self.columns, self.columns_colors)

        def insertion_sort(nums, colors):
            for i in range(1, len(nums)):
                colors[i] = arcade.color.PURPLE
                item_to_insert = nums[i]
                j = i - 1
                while j >= 0 and nums[j] > item_to_insert:
                    colors[j] = arcade.color.ORANGE_PEEL
                    nums[j + 1] = nums[j]
                    j -= 1
                nums[j + 1] = item_to_insert
                sleep(self.delay)
            colors[-1] = arcade.color.ORANGE_PEEL
            check(self.columns, self.columns_colors)

        def heapify(nums, heap_size, root_index):
            largest = root_index
            left_child = (2 * root_index) + 1
            right_child = (2 * root_index) + 2
            if left_child < heap_size and nums[left_child] > nums[largest]:
                largest = left_child
            if right_child < heap_size and nums[right_child] > nums[largest]:
                largest = right_child
            if largest != root_index:
                nums[root_index], nums[largest] = nums[largest], nums[root_index]
                heapify(nums, heap_size, largest)

        def heap_sort(nums):
            n = len(nums)
            for i in range(n, -1, -1):
                heapify(nums, n, i)
                self.columns_colors[i - 1] = arcade.color.PURPLE
            for i in range(n - 1, 0, -1):
                self.columns_colors[i] = arcade.color.ORANGE_PEEL
                nums[i], nums[0] = nums[0], nums[i]
                heapify(nums, i, 0)
                sleep(self.delay)
            self.columns_colors[0] = arcade.color.ORANGE_PEEL
            check(self.columns, self.columns_colors)

        def merge(left, right):
            lst = []
            while left and right:
                if left[0] < right[0]:
                    lst.append(left.pop(0))
                else:
                    lst.append(right.pop(0))
            if left:
                lst.extend(left)
            if right:
                lst.extend(right)
            return lst

        def merge_sort(lst):
            length = len(lst)
            if length >= 2:
                mid = int(length / 2)
                lst = merge(merge_sort(lst[:mid]), merge_sort(lst[mid:]))
            return lst

        def partition(nums, low, high):
            pivot = nums[(low + high) // 2]
            i = low - 1
            j = high + 1
            while True:
                i += 1
                while nums[i] < pivot:
                    self.columns_colors[i] = arcade.color.ORANGE_PEEL
                    i += 1
                j -= 1
                while nums[j] > pivot:
                    j -= 1
                    self.columns_colors[j] = arcade.color.PURPLE
                if i >= j:
                    self.columns_colors[i] = arcade.color.ORANGE_PEEL
                    return j
                nums[i], nums[j] = nums[j], nums[i]
                self.columns_colors[i] = arcade.color.PURPLE
                sleep(self.delay)
                self.columns_colors[0] = arcade.color.ORANGE_PEEL

        def quick_sort(nums):
            def _quick_sort(items, low, high):
                if low < high:
                    split_index = partition(items, low, high)
                    _quick_sort(items, low, split_index)
                    _quick_sort(items, split_index + 1, high)
            _quick_sort(nums, 0, len(nums) - 1)
            check(self.columns, self.columns_colors)

        def generate():
            self.columns = []
            self.columns_colors = []
            if not self.random_generate:
                self.columns_num = self.choosed_num
            if self.random_generate:
                self.columns_num = random.randint(0,600)
            for i in range(self.columns_num):
                self.columns.append(random.randint(-500,500))
            for i in range(self.columns_num):
                self.columns_colors.append(self.normal_color)
            self.random_generate = False

        def sort():

            if self.algorithm_name == 'Bubble Sort':
                Sort_Thread = Thread(target=bubble_sort, args=(self.columns, self.columns_colors))
                Sort_Thread.start()
            if self.algorithm_name == 'Selection Sort':
                Sort_Thread = Thread(target=selection_sort, args=(self.columns, self.columns_colors))
                Sort_Thread.start()
            if self.algorithm_name == 'Insertion Sort':
                Sort_Thread = Thread(target=insertion_sort, args=(self.columns, self.columns_colors))
                Sort_Thread.start()
            if self.algorithm_name == 'Heap Sort':
                mas = [self.columns]
                Sort_Thread = Thread(target=heap_sort, args=mas)
                Sort_Thread.start()
            if self.algorithm_name == 'Merge Sort':
                mas = [self.columns]
                Sort_Thread = Thread(target=merge_sort, args=mas)
                Sort_Thread.start()
            if self.algorithm_name == 'Quick Sort':
                mas = [self.columns]
                Sort_Thread = Thread(target=quick_sort, args=mas)
                Sort_Thread.start()

        def increase_delay():
            if self.delay <= 2:
                self.delay += 0.01

        def decrease_delay():
            if self.delay >= 0.01:
                self.delay -= 0.01

        def hide_stroke():
            if self.is_stroke_hided:
                self.is_stroke_hided = False
            else:
                self.is_stroke_hided = True

        def shuffle_columns():
            self.columns_colors = []
            for i in range(self.columns_num):
                self.columns_colors.append(self.normal_color)
            random.shuffle(self.columns)

        def set_algorithm():
            self.algorithm_name = self.name_to_set
        def set_rus():
            self.lng = 'Rus'
            self.shuffle = TextButton(rus[0], SW / 16 + (SW / 64) * 2, SH / 2 - (SH / 32) * 5, (255, 137, 57), 30)
            self.generate_button = TextButton(rus[1], SW / 16 + (SW / 64) * 2, SH / 2 - (SH / 32) * 3, (255, 137, 57), 30)
            self.sort_button = TextButton(rus[2], SW / 16 + (SW / 64) * 2, SH / 2 - (SH / 64) * 2, (255, 137, 57), 30)
            self.Decrease = TextButton(rus[3], SW / 16 + (SW / 64) * 2, SH / 2 - (SH / 32) * 11, (255, 137, 57), 19)
            self.Increase = TextButton(rus[4], SW / 16 + (SW / 64) * 2, SH / 2 - (SH / 32) * 12, (255, 137, 57), 19)
            self.BubbleSort = TextButton(rus[5], SW / 16 + (SW / 64) * 2, SH - (SH / 64) * 7, (255, 137, 57), 22)
            self.SelectionSort = TextButton(rus[6], SW / 16 + (SW / 64) * 2, SH - (SH / 64) * 11, (255, 137, 57), 22)
            self.InsertionSort = TextButton(rus[7], SW / 16 + (SW / 64) * 2, SH - (SH / 64) * 15, (255, 137, 57), 22)
            self.HeapSort = TextButton(rus[8], SW / 16 + (SW / 64) * 2, SH - (SH / 64) * 19, (255, 137, 57), 22)
            self.MergeSort = TextButton(rus[9], SW / 16 + (SW / 64) * 2, SH - (SH / 64) * 23, (255, 137, 57), 22)
            self.QuickSort = TextButton(rus[10], SW / 16 + (SW / 64) * 2, SH - (SH / 64) * 27, (255, 137, 57), 22)
            self.buttons = [self.shuffle, self.generate_button, self.sort_button,
                            self.Decrease, self.Increase, self.BubbleSort,
                            self.SelectionSort, self.InsertionSort, self.HeapSort,
                            self.MergeSort, self.QuickSort, self.Rus, self.Eng
                            ]
        def set_eng():
            self.lng = 'Eng'
            self.shuffle = TextButton(eng[0], SW / 16 + (SW / 64) * 2, SH / 2 - (SH / 32) * 5, (255, 137, 57), 30)
            self.generate_button = TextButton(eng[1], SW / 16 + (SW / 64) * 2, SH / 2 - (SH / 32) * 3, (255, 137, 57), 30)
            self.sort_button = TextButton(eng[2], SW / 16 + (SW / 64) * 2, SH / 2 - (SH / 64) * 2, (255, 137, 57), 30)
            self.Decrease = TextButton(eng[3], SW / 16 + (SW / 64) * 2, SH / 2 - (SH / 32) * 11, (255, 137, 57), 19)
            self.Increase = TextButton(eng[4], SW / 16 + (SW / 64) * 2, SH / 2 - (SH / 32) * 12, (255, 137, 57), 19)
            self.BubbleSort = TextButton(eng[5], SW / 16 + (SW / 64) * 2, SH - (SH / 64) * 7, (255, 137, 57), 22)
            self.SelectionSort = TextButton(eng[6], SW / 16 + (SW / 64) * 2, SH - (SH / 64) * 11, (255, 137, 57), 22)
            self.InsertionSort = TextButton(eng[7], SW / 16 + (SW / 64) * 2, SH - (SH / 64) * 15, (255, 137, 57), 22)
            self.HeapSort = TextButton(eng[8], SW / 16 + (SW / 64) * 2, SH - (SH / 64) * 19, (255, 137, 57), 22)
            self.MergeSort = TextButton(eng[9], SW / 16 + (SW / 64) * 2, SH - (SH / 64) * 23, (255, 137, 57), 22)
            self.QuickSort = TextButton(eng[10], SW / 16 + (SW / 64) * 2, SH - (SH / 64) * 27, (255, 137, 57), 22)

            self.buttons = [self.shuffle, self.generate_button, self.sort_button,
                            self.Decrease, self.Increase, self.BubbleSort,
                            self.SelectionSort, self.InsertionSort, self.HeapSort,
                            self.MergeSort, self.QuickSort, self.Rus, self.Eng
                            ]
        self.events = {
            'generate': generate,
            'sort': sort,
            'increase': increase_delay,
            'decrease': decrease_delay,
            'hide_stroke': hide_stroke,
            'shuffle': shuffle_columns,
            'set_algorithm': set_algorithm,
            'set_rus': set_rus,
            'set_eng': set_eng
        }

    def on_draw(self):
        self.all_columnsWidth = 0
        column_x_coordinate = SW/2 - SW / 4 + self.columnsWidth/2
        arcade.start_render()
        arcade.draw_rectangle_filled(SW / 16 + (SW / 64) * 2, SH / 2,(SW / 16) * 3, SH, (82, 82, 82))
        if self.lng == 'Eng':
            arcade.draw_text(self.algorithm_name, (SW/32)*3, SH - SH /64, arcade.color.WHITE,25, align="center", anchor_x="center", anchor_y="center")
        else:
            if self.algorithm_name == 'Bubble Sort':
                arcade.draw_text('Пузырьковая сортировка', (SW / 32) * 3, SH - SH / 64, arcade.color.WHITE, 22, align="center", anchor_x="center", anchor_y="center")
            if self.algorithm_name == 'Selection Sort':
                    arcade.draw_text('Сортировка выборкой', (SW / 32) * 3, SH - SH / 64, arcade.color.WHITE, 22,
                                     align="center", anchor_x="center", anchor_y="center")
            if self.algorithm_name == 'Insertion Sort':
                    arcade.draw_text('Сортировка вставками', (SW / 32) * 3, SH - SH / 64, arcade.color.WHITE, 22,
                                     align="center", anchor_x="center", anchor_y="center")
            if self.algorithm_name == 'Heap Sort':
                    arcade.draw_text('Пирамидальная сортировка', (SW / 32) * 3, SH - SH / 64, arcade.color.WHITE, 22,
                                     align="center", anchor_x="center", anchor_y="center")
            if self.algorithm_name == 'Merge Sort':
                    arcade.draw_text('Сортировка слиянием', (SW / 32) * 3, SH - SH / 64, arcade.color.WHITE, 22,
                                     align="center", anchor_x="center", anchor_y="center")
            if self.algorithm_name == 'Quick Sort':
                    arcade.draw_text('Быстрая сортировка', (SW / 32) * 3, SH - SH / 64, arcade.color.WHITE, 22,
                                     align="center", anchor_x="center", anchor_y="center")
        if self.lng == 'Eng':
            arcade.draw_text('Columns: ' + str(self.columns_num), SW / 16 + (SW / 64)*2, SH / 2 - (SH / 32)*7,
                             arcade.color.WHITE, 29, align="center", anchor_x="center", anchor_y="center")
            arcade.draw_text('Delay: ' + str(round(self.delay, 2)), SW / 16 + (SW / 64)*2, SH / 2 - (SH / 32)*9,
                         arcade.color.WHITE, 29, align="center", anchor_x="center", anchor_y="center")
        else:
            arcade.draw_text('Кол-во Столбцов: ' + str(self.columns_num), SW / 16 + (SW / 64) * 2, SH / 2 - (SH / 32) * 7,
                             arcade.color.WHITE, 29, align="center", anchor_x="center", anchor_y="center")
            arcade.draw_text('Задержка: ' + str(round(self.delay, 2)), SW / 16 + (SW / 64) * 2, SH / 2 - (SH / 32) * 9,
                             arcade.color.WHITE, 29, align="center", anchor_x="center", anchor_y="center")
        for i in self.buttons:
            i.draw_button()
        if self.is_stroke_hided:
            if self.lng == 'Eng':
                self.stroke = TextButton('Show Stroke', SW / 16 + (SW / 64)*2, SH / 2 - (SH /32)*13, (255, 137, 57), 20)
            else:
                self.stroke = TextButton('Показать обводку', SW / 16 + (SW / 64) * 2, SH / 2 - (SH / 32) * 13, (255, 137, 57), 20)
        else:
            if self.lng == 'Eng':
                self.stroke = TextButton('Hide Stroke', SW / 16 + (SW / 64)*2, SH / 2 - (SH / 32)*13, (255, 137, 57), 20)
            else:
                self.stroke = TextButton('Спрятать обводку', SW / 16 + (SW / 64) * 2, SH / 2 - (SH / 32) * 13, (255, 137, 57), 20)
        self.stroke.draw_button()
        for i in range(len(self.columns)):
            self.all_columnsWidth += self.columnsWidth
        for column in range(len(self.columns)):
            color = self.columns_colors[column]
            arcade.draw_rectangle_filled(column_x_coordinate, SH /2 + self.columns[column] /2, self.columnsWidth, self.columns[column], color)
            if not self.is_stroke_hided:
                if self.columns_num <= 300:
                    arcade.draw_rectangle_outline(column_x_coordinate, SH / 2 + self.columns[column] /2, self.columnsWidth, self.columns[column], arcade.color.BLACK, border_width = 1)
            column_x_coordinate += self.columnsWidth
        arcade.draw_line(SW / 2 - SW / 4, SH / 2, SW/2 + (SW / 4) + ((SW / 4))/2 + (SW / 4) /4, SH / 2, arcade.color.BLACK, 5)
        arcade.draw_line(0, SH - SH  /32 , (SW/16)*3, SH - SH /32 , arcade.color.WHITE, 3)
        arcade.draw_line(0, SH - SH / 2, (SW / 16) * 3, SH - SH / 2, arcade.color.WHITE, 3)
        arcade.draw_line(0, SH / 16, (SW / 16) * 3, SH /16, arcade.color.WHITE, 3)
        arcade.draw_line(0, (SH / 16) * 5, (SW / 16)* 3, (SH / 16) * 5, arcade.color.WHITE, 3)
        arcade.draw_line(0, (SH / 16) * 3, (SW / 16) * 3, (SH / 16) * 3, arcade.color.WHITE, 3)
        arcade.draw_text('tadaborisu 2020',  (SW/32)*2, SH /16 - SH /64, arcade.color.WHITE, 19,
                         align="center", anchor_x="center", anchor_y="center")
    def on_mouse_motion(self, x, y, delta_x, delta_y):
        self.mouse_position[0] = x
        self.mouse_position[1] = y

    def update(self, delta_time):
        self.columnsWidth = ((SW / 4) + (SW / 4) + ((SW / 4))/2 + (SW / 4) /4 )/ self.columns_num
        self.mouse_event = ''
        for button in self.buttonlist:
            if self.mouse_position[0] > button[0] - button[2] / 2 and self.mouse_position[0] < button[0] + button[2] / 2 and self.mouse_position[1] > button[1] - button[3] / 2 and self.mouse_position[1] < button[1] + button[3] / 2:
                if self.buttonlist.index(button) == 0:
                    self.mouse_event = 'sort'
                if self.buttonlist.index(button) == 1:
                    self.random_generate = True
                    self.mouse_event = 'generate'
                if self.buttonlist.index(button) == 2:
                    self.mouse_event = 'increase'
                if self.buttonlist.index(button) == 3:
                    self.mouse_event = 'decrease'
                if self.buttonlist.index(button) == 4:
                    self.mouse_event = 'hide_stroke'
                if self.buttonlist.index(button) == 5:
                    self.mouse_event = 'shuffle'
                if self.buttonlist.index(button) == 6:
                    self.name_to_set = 'Bubble Sort'
                    self.mouse_event = 'set_algorithm'
                if self.buttonlist.index(button) == 7:
                    self.name_to_set = 'Selection Sort'
                    self.mouse_event = 'set_algorithm'
                if self.buttonlist.index(button) == 8:
                    self.name_to_set = 'Insertion Sort'
                    self.mouse_event = 'set_algorithm'
                if self.buttonlist.index(button) == 9:
                    self.name_to_set = 'Heap Sort'
                    self.mouse_event = 'set_algorithm'
                if self.buttonlist.index(button) == 10:
                    self.name_to_set = 'Merge Sort'
                    self.mouse_event = 'set_algorithm'
                if self.buttonlist.index(button) == 11:
                    self.name_to_set = 'Quick Sort'
                    self.mouse_event = 'set_algorithm'
                if self.buttonlist.index(button) == 12:
                    self.mouse_event = 'set_rus'
                if self.buttonlist.index(button) == 13:
                    self.mouse_event = 'set_eng'

    def on_mouse_press(self, x, y, button, key_modifiers):
        if button == arcade.MOUSE_BUTTON_LEFT:
               if self.mouse_event != '':
                    self.events[self.mouse_event]()

    def setup(self):
        pass

def main():
    game = MyGame()
    game.setup()
    arcade.run()

if __name__ == "__main__":
    main()

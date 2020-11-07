import arcade, random
from win32api import GetSystemMetrics
from threading import Thread
from time import sleep
SCREEN_WIDTH = GetSystemMetrics(0)
SCREEN_HEIGHT = GetSystemMetrics(1)

class TextButton:
    def __init__(self, text, x, y, color, size):
        self.text = text
        self.x = x
        self.y = y
        self.color = color
        self.size = size
        
    def draw_button(self):
        arcade.draw_rectangle_outline(self.x, self.y, len(self.text) * 20 * self.size /32, 40, self.color, border_width = 2)
        arcade.draw_text(self.text, self.x, self.y, self.color, self.size, align="center", anchor_x="center", anchor_y="center")
        
class MyGame(arcade.Window, Thread):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "github tadaborisu")
        arcade.set_background_color(arcade.color.WHITE)
        self.sorting = False
        self.mouse_position = [SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2]
        self.algorithm_name = 'Bubble Sort'
        self.name_to_set = 'Bubble Sort'
        self.all_columns_width = 10
        self.columns_width = 100
        self.columns_num = random.randint(1, 100)
        self.columns_height = []                                    
        self.delay = 0.1
        self.normal_color = arcade.color.SKY_BLUE
        self.choosed_first_color = arcade.color.PURPLE
        self.choosed_second_color = arcade.color.ORANGE_PEEL
        self.moved_color = arcade.color.GREEN
        self.not_moved_color = arcade.color.RED_DEVIL
        self.columns_colors = []
        for i in range(self.columns_num):
                self.columns_colors.append(self.normal_color)
                self.columns_height.append(random.randint(-350, 350))
        generate_button = TextButton('Generate', SCREEN_WIDTH/2, SCREEN_HEIGHT / 4 - SCREEN_WIDTH /16 - SCREEN_WIDTH /64, arcade.color.BLACK, 30)
        sort_button = TextButton('Sort', SCREEN_WIDTH / 2, SCREEN_HEIGHT / 4 - SCREEN_WIDTH /16 - (SCREEN_WIDTH /64) * 3, arcade.color.BLACK, 30)
        bubble_sort = TextButton('Bubble Sort', SCREEN_WIDTH / 16 + (SCREEN_WIDTH / 16) * 2, SCREEN_HEIGHT / 4 - SCREEN_WIDTH / 16 - SCREEN_WIDTH /64, arcade.color.BLACK, 19)
        selection_sort = TextButton('Selection Sort',  SCREEN_WIDTH / 16 + SCREEN_WIDTH / 64, SCREEN_HEIGHT / 4 - SCREEN_WIDTH / 16 - (SCREEN_WIDTH /64) * 3, arcade.color.BLACK, 19)
        insertion_sort = TextButton('Insertion Sort', SCREEN_WIDTH / 16 + SCREEN_WIDTH / 64, SCREEN_HEIGHT / 4 - SCREEN_WIDTH / 16 - SCREEN_WIDTH /64, arcade.color.BLACK, 19)
        heap_sort = TextButton('Heap Sort', SCREEN_WIDTH / 16 + (SCREEN_WIDTH / 16) * 2, SCREEN_HEIGHT / 4 - SCREEN_WIDTH / 16 - (SCREEN_WIDTH /64) * 3, arcade.color.BLACK, 19)
        quick_sort = TextButton('Quick sort', SCREEN_WIDTH / 16 + (SCREEN_WIDTH / 16) * 3.5, SCREEN_HEIGHT / 4 - SCREEN_WIDTH / 16 - SCREEN_WIDTH /64, arcade.color.BLACK, 19)
        merge_sort = TextButton('Merge sort', SCREEN_WIDTH / 16 + (SCREEN_WIDTH / 16) * 3.5, SCREEN_HEIGHT / 4 - SCREEN_WIDTH / 16 - (SCREEN_WIDTH /64) * 3, arcade.color.BLACK, 19)
        self.buttons = [generate_button, sort_button, bubble_sort, selection_sort, insertion_sort, heap_sort, quick_sort,merge_sort]
        self.buttonlist = [[generate_button.x, generate_button.y, len(generate_button.text) * 20 * generate_button.size / 32, 40],
                           [sort_button.x, sort_button.y, len(sort_button.text) * 20 * sort_button.size / 32, 40],
                           [bubble_sort.x, bubble_sort.y, len(bubble_sort.text) * 20 * bubble_sort.size / 32, 40],
                           [selection_sort.x, selection_sort.y, len(selection_sort.text) * 20 * selection_sort.size / 32, 40],
                           [insertion_sort.x, insertion_sort.y, len(insertion_sort.text) * 20 * insertion_sort.size / 32, 40],
                           [heap_sort.x, heap_sort.y, len(heap_sort.text) * 20 * heap_sort.size / 32, 40],
                           [quick_sort.x, quick_sort.y, len(quick_sort.text) * 20 * quick_sort.size / 32, 40],
                           [merge_sort.x, merge_sort.y, len(merge_sort.text) * 20 * merge_sort.size / 32, 40]]
        
        def bubble_sort(nums, colors):
            self.sorting = True
            swapped = True
            while swapped:
                swapped = False
                for i in range(len(nums) - 1):
                    if nums[i] > nums[i + 1]:
                        nums[i], nums[i + 1] = nums[i + 1], nums[i]
                        swapped = True
                        colors[i] = arcade.color.PURPLE
                        colors[i + 1] = arcade.color.ORANGE_PEEL
                    else:   
                        colors[i + 1] = arcade.color.ORANGE_PEEL
                sleep(self.delay)
            colors[0] = arcade.color.ORANGE_PEEL
            self.sorting = False
            
        def selection_sort(nums, colors):
            self.sorting = True
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
            self.sorting = False
        
        def insertion_sort(nums, colors):
            self.sorting = True
            for i in range(1, len(nums)):
                colors[i] = arcade.color.ORANGE_PEEL
                item_to_insert = nums[i]
                j = i - 1
                while j >= 0 and nums[j] > item_to_insert:
                    colors[j] = arcade.color.PURPLE
                    nums[j + 1] = nums[j]
                    j -= 1
                sleep(self.delay)
                nums[j + 1] = item_to_insert
            self.sorting = False
            
        def heapify(nums, colors, heap_size, root_index):  
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

        def heap_sort(nums, colors):  
            n = len(nums)
            for i in range(n, -1, -1):
                heapify(nums, n, i)
            for i in range(n - 1, 0, -1):
                nums[i], nums[0] = nums[0], nums[i]
                heapify(nums, i, 0)
                
        def merge(left_list, right_list):  
            sorted_list = []
            left_list_index = right_list_index = 0
            left_list_length, right_list_length = len(left_list), len(right_list)
            for _ in range(left_list_length + right_list_length):
                if left_list_index < left_list_length and right_list_index < right_list_length:
                    if left_list[left_list_index] <= right_list[right_list_index]:
                        sorted_list.append(left_list[left_list_index])
                        left_list_index += 1
                    else:
                        sorted_list.append(right_list[right_list_index])
                        right_list_index += 1
                elif left_list_index == left_list_length:
                    sorted_list.append(right_list[right_list_index])
                    right_list_index += 1
                elif right_list_index == right_list_length:
                    sorted_list.append(left_list[left_list_index])
                    left_list_index += 1
            return sorted_list

        def merge_sort(nums):  
            if len(nums) <= 1:
                return nums
            mid = len(nums) // 2
            left_list = merge_sort(nums[:mid])
            right_list = merge_sort(nums[mid:])
            return merge(left_list, right_list)
        def partition(nums, low, high):  
            pivot = nums[(low + high) // 2]
            i = low - 1
            j = high + 1
            while True:
                i += 1
                while nums[i] < pivot:
                    i += 1
                j -= 1
                while nums[j] > pivot:
                    j -= 1
                if i >= j:
                    return j
                nums[i], nums[j] = nums[j], nums[i]

        def quick_sort(nums):  
            def _quick_sort(items, low, high):
                if low < high:
                    split_index = partition(items, low, high)
                    _quick_sort(items, low, split_index)
                    _quick_sort(items, split_index + 1, high)
            _quick_sort(nums, 0, len(nums) - 1)

        def generate():
            self.columns_colors = []
            self.columns_height = []
            self.columns_num = random.randint(1, 100)
            for i in range(self.columns_num):
                self.columns_colors.append(self.normal_color)
                self.columns_height.append(random.randint(-350, 350))
                
        def sort():
            if self.algorithm_name == 'Bubble Sort':
                Sort_Thread = Thread(target = bubble_sort, args = (self.columns_height, self.columns_colors))
                Sort_Thread.start()
                
            if self.algorithm_name == 'Selection Sort':
                Sort_Thread = Thread(target = selection_sort, args = (self.columns_height, self.columns_colors))
                Sort_Thread.start()
                
            if self.algorithm_name == 'Insertion Sort':
                Sort_Thread = Thread(target = selection_sort, args = (self.columns_height, self.columns_colors))
                Sort_Thread.start()
                
            if self.algorithm_name == 'Heap Sort':
                Sort_Thread = Thread(target = selection_sort, args = (self.columns_height, self.columns_colors))
                Sort_Thread.start()
                
            if self.algorithm_name == 'Merge Sort':
                Sort_Thread = Thread(target = selection_sort, args = (self.columns_height, self.columns_colors))
                Sort_Thread.start()
                
            if self.algorithm_name == 'Quick Sort':
                Sort_Thread = Thread(target = selection_sort, args = (self.columns_height, self.columns_colors))
                Sort_Thread.start()
                
        def set_algorithm_name():
            self.algorithm_name = self.name_to_set
            
        self.events = {'generate': generate,
                       'set_algorithm_name': set_algorithm_name,
                       'sort': sort
                       }
        
    def on_draw(self):
        arcade.start_render()
        arcade.draw_text(self.algorithm_name, SCREEN_WIDTH / 2, SCREEN_HEIGHT - (SCREEN_HEIGHT/64) *2,  arcade.color.BLACK, 40, align="center", anchor_x="center", anchor_y="center")
        arcade.draw_text('Columns: ' + str(self.columns_num), SCREEN_WIDTH / 1.5, SCREEN_HEIGHT / 4 - SCREEN_WIDTH /16 - SCREEN_WIDTH /64, arcade.color.BLACK, 29, align="center", anchor_x="center", anchor_y="center")
        arcade.draw_line(0, SCREEN_HEIGHT / 7, SCREEN_WIDTH, SCREEN_HEIGHT / 7, arcade.color.BLACK, 2)
        arcade.draw_line(SCREEN_WIDTH / 32, SCREEN_HEIGHT / 2, SCREEN_WIDTH - SCREEN_WIDTH / 32, SCREEN_HEIGHT / 2, arcade.color.BLACK, 2)
        for button in self.buttons:
            button.draw_button()
        column_x_coordinate = SCREEN_WIDTH / 32 + self.columns_width / 2
        for i in range(self.columns_num):
            self.all_columns_width += self.columns_width
        for column in range(self.columns_num):
            color = self.columns_colors[column]
            if self.columns_height[column] > 0:
                arcade.draw_rectangle_filled(column_x_coordinate, SCREEN_HEIGHT/2 + self.columns_height[column] / 2 + 1, self.columns_width, self.columns_height[column], color)
            else:
                arcade.draw_rectangle_filled(column_x_coordinate, SCREEN_HEIGHT/2 + self.columns_height[column] / 2 - 1, self.columns_width, self.columns_height[column], color)
            column_x_coordinate += self.columns_width + 5
    
    def on_mouse_motion(self, x, y, delta_x, delta_y):
        self.mouse_position[0] = x
        self.mouse_position[1] = y
    
    def update(self, delta_time):
        self.mouse_event = ''
        self.columns_width = ((SCREEN_WIDTH - (SCREEN_WIDTH / 32) * 2 + 5) / self.columns_num - 5)
        for color in self.buttons:
            color.color = arcade.color.BLACK
        for button in self.buttonlist:
            if self.mouse_position[0] > button[0] - button[2] / 2 and self.mouse_position[0] < button[0] + button[2] / 2 and self.mouse_position[1] > button[1] - button[3] / 2 and self.mouse_position[1] < button[1] + button[3] / 2:
                if self.sorting:
                    focus_color = arcade.color.RED
                else:
                    focus_color = arcade.color.ORANGE
                if self.buttonlist.index(button) == 0:
                    self.buttons[0].color = focus_color
                    if not self.sorting:
                        self.mouse_event = 'generate'
                if self.buttonlist.index(button) == 1:
                    self.buttons[1].color = focus_color
                    if not self.sorting:
                        self.mouse_event = 'sort'
                if self.buttonlist.index(button) == 2:
                    self.buttons[2].color = focus_color
                    if not self.sorting:
                        self.name_to_set = 'Bubble Sort'
                        self.mouse_event = 'set_algorithm_name'
                if self.buttonlist.index(button) == 3:
                    self.buttons[3].color = focus_color
                    if not self.sorting:
                        self.name_to_set  = 'Selection Sort'
                        self.mouse_event = 'set_algorithm_name'
                if self.buttonlist.index(button) == 4:
                    self.buttons[4].color = focus_color
                    if not self.sorting:
                        self.name_to_set  = 'Insertion Sort'
                        self.mouse_event = 'set_algorithm_name'
                if self.buttonlist.index(button) == 5:
                    self.buttons[5].color = focus_color
                    if not self.sorting:
                        self.name_to_set  = 'Heap Sort'
                        self.mouse_event = 'set_algorithm_name'
                if self.buttonlist.index(button) == 6:
                    self.buttons[6].color = focus_color
                    if not self.sorting:
                        self.name_to_set  = 'Quick Sort'
                        self.mouse_event = 'set_algorithm_name'
                if self.buttonlist.index(button) == 7:
                    self.buttons[7].color = focus_color
                    if not self.sorting:
                        self.name_to_set  = 'Merge Sort'
                        self.mouse_event = 'set_algorithm_name'
            
    def on_mouse_press(self, x, y, button, key_modifiers):
        if button == arcade.MOUSE_BUTTON_LEFT:
            if self.mouse_event != '':
                self.events[self.mouse_event]()
        
def main():
    game = MyGame()
    arcade.run()

if __name__ == "__main__":
    main()
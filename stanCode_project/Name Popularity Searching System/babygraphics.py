"""
File: babygraphics.py
Name: 
--------------------------------
This program is part of the SC101 Baby Names Project.

It is adapted from Nick Parlante's Baby Names assignment
and has been modified by Jerry Liao to align with the
learning objectives of the stanCode SC101 course.
"""

import tkinter
import babynames
import babygraphicsgui as gui

FILENAMES = [
    'data/full/baby-1900.txt', 'data/full/baby-1910.txt',
    'data/full/baby-1920.txt', 'data/full/baby-1930.txt',
    'data/full/baby-1940.txt', 'data/full/baby-1950.txt',
    'data/full/baby-1960.txt', 'data/full/baby-1970.txt',
    'data/full/baby-1980.txt', 'data/full/baby-1990.txt',
    'data/full/baby-2000.txt', 'data/full/baby-2010.txt',
    'data/full/baby-2020.txt'
]
CANVAS_WIDTH = 1080
CANVAS_HEIGHT = 600
YEARS = [1900, 1910, 1920, 1930, 1940, 1950,
         1960, 1970, 1980, 1990, 2000, 2010, 2020]
GRAPH_MARGIN_SIZE = 20
COLORS = ['red', 'purple', 'green', 'blue']
TEXT_DX = 2
LINE_WIDTH = 2
MAX_RANK = 1000


def get_x_coordinate(width, year_index):
    """
    Given the width of the canvas and the index of the current year
    in the YEARS list, this function returns the x coordinate
    of the vertical line associated with that year.

    Input:
        width (int): The width of the canvas
        year_index (int): The index where the current year is in the YEARS list
    Returns:
        x_coordinate (int): The x coordinate of the vertical line associated
                            with the current year.
    """
    line_length = width - 2*GRAPH_MARGIN_SIZE
    each_space = line_length/(len(YEARS)-1)
    return int(GRAPH_MARGIN_SIZE + year_index*each_space)


def draw_fixed_lines(canvas):
    """
    Draws the fixed background lines on the canvas.

    Input:
        canvas (Tkinter Canvas): The canvas on which we are drawing.
    """
    canvas.delete('all')            # delete all existing lines from the canvas

    # ----- Write your code below this line ----- #
    #畫出頂部和底部的水平線
    canvas.create_line(GRAPH_MARGIN_SIZE,GRAPH_MARGIN_SIZE,CANVAS_WIDTH-GRAPH_MARGIN_SIZE,GRAPH_MARGIN_SIZE)
    canvas.create_line(GRAPH_MARGIN_SIZE,CANVAS_HEIGHT-GRAPH_MARGIN_SIZE,CANVAS_WIDTH-GRAPH_MARGIN_SIZE,CANVAS_HEIGHT-GRAPH_MARGIN_SIZE)
    #畫出每一年的垂直線與年份文字
    year_index = 0
    for year in YEARS:
        x_coordinate = get_x_coordinate(CANVAS_WIDTH,year_index)
        canvas.create_line(x_coordinate,0,x_coordinate,CANVAS_HEIGHT)
        canvas.create_text(x_coordinate+TEXT_DX,CANVAS_HEIGHT-GRAPH_MARGIN_SIZE, text=year, anchor=tkinter.NW)
        year_index += 1
def draw_names(canvas, name_data, lookup_names):
    """
    Given a dict of baby name data and a list of name, plots
    the historical trend of those names onto the canvas.

    Input:
        canvas (Tkinter Canvas): The canvas on which we are drawing.
        name_data (dict): Dictionary holding baby name data
        lookup_names (List[str]): A list of names whose data you want to plot

    Returns:
        This function does not return any value.
    """
    draw_fixed_lines(canvas)        # draw the fixed background grid

    # ----- Write your code below this line ----- # 
    j = 0 #用來控制顏色的索引(0~3)
    for name in lookup_names: 
        color = COLORS[j] #根據j決定當前名字的顏色
        if name in name_data:
            i = 0 #用來控制年份的索引(給get_x_coordinate使用)
            last_y_coordinate = None
            last_x_coordinate = None
            for year in YEARS:
                #取得當前年份的X座標
                x_coordinate = get_x_coordinate(CANVAS_WIDTH,i)
                #判斷該名字在該年份是否有排名資料
                if str(year) in name_data[name]:
                    rank = int(name_data[name][str(year)])
                    #計算Y座標依照排名等比例分布在圖表中
                    y_coordinate = GRAPH_MARGIN_SIZE+((CANVAS_HEIGHT-2*GRAPH_MARGIN_SIZE))/MAX_RANK*rank
                    name_grade = str(name) + " " + name_data[name][str(year)]
                else:
                    #若無排名，座標設在最底部
                    y_coordinate = CANVAS_HEIGHT-GRAPH_MARGIN_SIZE
                    name_grade = str(name) + " *"
                #畫出該年份的文字標籤(名字+排名)
                canvas.create_text(x_coordinate+TEXT_DX,y_coordinate,text=name_grade,anchor=tkinter.SW,fill=color)
                #如果有上一點的座標，則連成線
                if last_y_coordinate is not None and last_x_coordinate is not None:
                    canvas.create_line(last_x_coordinate,last_y_coordinate,x_coordinate,y_coordinate,width=LINE_WIDTH,fill=color)
                #更新上一點座標，供下一次迴圈連線用
                last_x_coordinate = x_coordinate
                last_y_coordinate = y_coordinate
                
                i += 1 #年份索引+1
        if j == 3:
            j = 0
        else:
            j += 1    
            
# main() code is provided, feel free to read through it but DO NOT MODIFY
def main():
    # Load data
    name_data = babynames.read_files(FILENAMES)

    # Create the window and the canvas
    top = tkinter.Tk()
    top.wm_title('Baby Names')
    canvas = gui.make_gui(top, CANVAS_WIDTH, CANVAS_HEIGHT, name_data, draw_names, babynames.search_names)

    # Call draw_fixed_lines() once at startup so we have the lines
    # even before the user types anything.
    draw_fixed_lines(canvas)

    # This line starts the graphical loop that is responsible for
    # processing user interactions and plotting data
    top.mainloop()


if __name__ == '__main__':
    main()

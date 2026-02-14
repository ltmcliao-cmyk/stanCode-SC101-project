"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman, 
and Jerry Liao.

YOUR DESCRIPTION HERE
"""
from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GOval, GRect, GLabel
from campy.gui.events.mouse import onmouseclicked, onmousemoved
import random

BRICK_SPACING = 5      # Space between bricks (in pixels). This space is used for horizontal and vertical spacing
BRICK_WIDTH = 40       # Width of a brick (in pixels)
BRICK_HEIGHT = 15      # Height of a brick (in pixels)
BRICK_ROWS = 10        # Number of rows of bricks
BRICK_COLS = 10        # Number of columns of bricks
BRICK_OFFSET = 50      # Vertical offset of the topmost brick from the window top (in pixels)
BALL_RADIUS = 10       # Radius of the ball (in pixels)
PADDLE_WIDTH = 75      # Width of the paddle (in pixels)
PADDLE_HEIGHT = 15     # Height of the paddle (in pixels)
PADDLE_OFFSET = 50     # Vertical offset of the paddle from the window bottom (in pixels)
INITIAL_Y_SPEED = 7    # Initial vertical speed for the ball
MAX_X_SPEED = 5        # Maximum initial horizontal speed for the ball


class BreakoutGraphics:

    def __init__(self, ball_radius=BALL_RADIUS, paddle_width=PADDLE_WIDTH, paddle_height=PADDLE_HEIGHT,
                 paddle_offset=PADDLE_OFFSET, brick_rows=BRICK_ROWS, brick_cols=BRICK_COLS, brick_width=BRICK_WIDTH,
                 brick_height=BRICK_HEIGHT, brick_offset=BRICK_OFFSET, brick_spacing=BRICK_SPACING, title='Breakout'):
        self.brick_left = brick_rows * brick_cols
        self.__dx = 0
        self.__dy = 0
        # Create a graphical window, with some extra space
        window_width = brick_cols * (brick_width + brick_spacing) - brick_spacing
        window_height = brick_offset + 3 * (brick_rows * (brick_height + brick_spacing) - brick_spacing)
        self.window = GWindow(width=window_width, height=window_height, title=title)
        # Create a paddle
        self.paddle = GRect(paddle_width,paddle_height)
        self.paddle.filled = True
        self.window.add(self.paddle,x=self.window.width/2-self.paddle.width/2,y=self.window.height-paddle_offset-self.paddle.height)
        # Center a filled ball in the graphical window
        self.ball = GOval(ball_radius * 2, ball_radius * 2)
        self.ball.filled = True
        self.window.add(self.ball,x=self.window.width/2-ball_radius,y=self.window.height/2-ball_radius)
        # Default initial velocity for the ball
        # Initialize our mouse listeners
        onmouseclicked(lambda event:self.start(event) if self.__dx == 0 and self.__dy == 0 else None) #當球在初始位置才可以點滑鼠
        onmousemoved(self.control)
        # Draw bricks
        for i in range(brick_rows):
            for j in range(brick_cols):
                brick = GRect(brick_width,brick_height)
                brick.filled = True
                if i < 2 :
                    brick.fill_color = 'red'
                    brick.color = 'red'
                elif i < 4:
                    brick.fill_color = 'orange'
                    brick.color = 'orange'
                elif i < 6:
                    brick.fill_color = "yellow"
                    brick.color = "yellow"
                elif i < 8:
                    brick.fill_color = "green"
                    brick.color = "green"
                elif i < 10:
                    brick.fill_color = "blue"
                    brick.color = "blue"
                self.window.add(brick,x=0+j*brick_spacing+j*brick.width,y=brick_offset+i*brick_spacing+i*brick.height)

    #點擊滑鼠球就開始亂跑
    def start(self,event):
        self.__dx = random.randint(1,MAX_X_SPEED)
        if (random.random()>0.5):
            self.__dx = -self.__dx
        self.__dy = INITIAL_Y_SPEED
    #滑鼠左右控制paddle
    def control(self,event):
        self.paddle.x = event.x - self.paddle.width/2
        if event.x >= self.window.width - self.paddle.width/2:
            self.paddle.x = self.window.width-self.paddle.width
        elif event.x <= self.paddle.width/2:
            self.paddle.x = 0
        
    #dx、dy的getter和setter
    def get_dx(self):
        return self.__dx
    def set_dx(self,dx):
        self.__dx = dx
    def get_dy(self):
        return self.__dy
    def set_dy(self,dy):
        self.__dy = dy
    #重新發球的method
    def reset_ball(self):

        self.ball.x = self.window.width/2-self.ball.width/2
        self.ball.y = self.window.height/2-self.ball.height/2

        self.__dx = 0
        self.__dy = 0
    #勝利結算畫面的method
    def win(self):
        winner_ending = GLabel("You Win!")
        winner_ending.font = "Helvetica-50"
        self.window.add(winner_ending,x=75,y=self.window.height/2+100)
    #失敗結算畫面的method
    def lose(self):
        loser_ending = GLabel("You Lose!")
        loser_ending.font = "Helvetica-50"
        self.window.add(loser_ending,x=75,y=self.window.height/2+100)
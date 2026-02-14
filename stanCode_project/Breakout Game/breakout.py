"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman,
and Jerry Liao.

YOUR DESCRIPTION HERE
"""

from campy.gui.events.timer import pause
from breakoutgraphics import BreakoutGraphics

FRAME_RATE = 10         # 100 frames per second
NUM_LIVES = 3			# Number of attempts


def main():
    graphics = BreakoutGraphics()
    lives = NUM_LIVES
    brick_left = graphics.brick_left

    # Add the animation loop here!
    while True:
        #球的動力來源及碰到邊界反彈
        dx = graphics.get_dx()
        dy = graphics.get_dy()
        graphics.ball.move(dx,dy)
        if graphics.ball.x <= 0 :
            graphics.set_dx(-dx) 
        elif graphics.ball.x + graphics.ball.width >= graphics.window.width:
            graphics.set_dx(-dx)
        if graphics.ball.y <= 0 :
            graphics.set_dy(-dy)
        
        """
        程式設計原則
        KISS = Keep It Simple, Stupid.
        """

        #先判定球左上角是否接觸到brick或paddle
        obj = graphics.window.get_object_at(graphics.ball.x,graphics.ball.y)
        #若無則判定球右上角
        if obj is None:
            obj = graphics.window.get_object_at(graphics.ball.x + graphics.ball.width,graphics.ball.y)
        #若無則判定左下角
        if obj is None:
            obj = graphics.window.get_object_at(graphics.ball.x,graphics.ball.y + graphics.ball.height)
        #若無，最後才判定右下角
        if obj is None:
            obj = graphics.window.get_object_at(graphics.ball.x + graphics.ball.width,graphics.ball.y + graphics.ball.height)
        #設定brick及paddle不同的反彈條件
        if obj is not None: 
            if obj == graphics.paddle and dy > 0:
                graphics.set_dy(-dy)
            elif obj is not graphics.paddle:
                graphics.window.remove(obj)
                brick_left -= 1
                graphics.set_dy(-dy)
        #球碰到畫面最底部就重新發球
        if graphics.ball.y >= graphics.window.height:
            lives -= 1
            graphics.reset_ball()
        #brick數量為0時觸發勝利條件
        if brick_left == 0:
            graphics.win()
            break
        #發球三次都沒贏就出局
        if lives == 0:
            graphics.lose()
            break
               
        pause(FRAME_RATE)

if __name__ == '__main__':
    main()

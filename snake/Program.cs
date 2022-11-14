using System.Collections.Generic;
using System.Threading;

using Raylib_cs;


static class Program
{
    public static void Main()
    {
        Raylib.InitWindow(600, 600, "Hello World");
        var snake = new Snake();
        var food = new Food();
        var speed = 200;

        while (!Raylib.WindowShouldClose())
        {
            var keyPressed = Raylib.GetKeyPressed();
            var segments = snake.GetSegments();
            if (keyPressed == 87) { // w key
                snake.SetDirection(Direction.Up);
            } else if (keyPressed == 83) { // s key
                snake.SetDirection(Direction.Down);
            } else if (keyPressed == 65) { // a key
                snake.SetDirection(Direction.Left);
            } else if (keyPressed == 68) { // d key
                snake.SetDirection(Direction.Right);
            }

            if (!snake.Update()) {
                snake.Reset();
                speed = 200;
            }

            Raylib.BeginDrawing();
            
            // border is draw as the background
            Raylib.ClearBackground(new Color(149, 125, 173, 255));

            // play area is drawn as a rectangle on top of the background
            Raylib.DrawRectangle(20, 20, 560, 560, new Color(224, 187, 228, 255));

            // draw food
            var foodPosition = food.GetPosition();
            Raylib.DrawCircle(foodPosition.X+10, foodPosition.Y+10, 4, new Color(20, 20, 20, 150));
            //Raylib.DrawRectangle(foodPosition.X+5, foodPosition.Y+5, 10, 10, new Color(20, 20, 20, 150));

            // draw snake
            var segmentIndex = 0;
            foreach (Position segment in segments) {
                if (segmentIndex == 0) {
                    Raylib.DrawRectangle(segment.X, segment.Y, 20, 20, new Color(165, 137, 193, 255));
                    Raylib.DrawCircle(segment.X+10, segment.Y+10, 3, new Color(20, 20, 20, 100));
                } else {
                    Raylib.DrawRectangle(segment.X, segment.Y, 20, 20, new Color(165, 137, 193, 255));
                }
                segmentIndex++;
            }

            if (foodPosition.X == segments[0].X && foodPosition.Y == segments[0].Y) {
                snake.AddSegment();
                food.Randomize();
                if (speed >= 0) {
                    speed -= speed / 10;
                }
            }

            Raylib.EndDrawing();
            Thread.Sleep(speed);
        }

        Raylib.CloseWindow();
    }
}

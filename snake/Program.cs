using System.Collections.Generic;
using static Raylib_cs.MouseButton;

using Raylib_cs;


static class Program
{
    public static void Main()
    {
        Raylib.InitWindow(600, 600, "Hello World");
        var snake = new Snake();
        var food = new Food();
        var speed = 200;
        var paused = false;
        var startScreen = true;

        while (!Raylib.WindowShouldClose())
        {
            if (startScreen) {
                Raylib.BeginDrawing();
                Raylib.ClearBackground(new Color(224, 187, 228, 255));
                var snakeTextLength = Raylib.MeasureText("Snake", 76);
                var startTextLength = Raylib.MeasureText("Start", 30);
                Raylib.DrawText("Snake", 300-snakeTextLength/2, 100, 75, new Color(20, 20, 20, 100));
                Raylib.DrawRectangle(175, 350, 250, 90, new Color(20, 20, 20, 150));
                if (Raylib.CheckCollisionPointRec(Raylib.GetMousePosition(), new Rectangle(175, 350, 250, 90))) {
                    Raylib.DrawRectangle(185, 360, 230, 70, new Color(20, 20, 20, 150));
                } else {
                    Raylib.DrawRectangle(185, 360, 230, 70, new Color(20, 20, 20, 100));
                }
                Raylib.DrawText("Start", 300-startTextLength/2, 380, 30, Color.RAYWHITE);
                Raylib.DrawText("github.com/koterba", 10, 570, 20, new Color(20, 20, 20, 100));
                Raylib.EndDrawing();

                if (Raylib.IsMouseButtonPressed(MOUSE_BUTTON_LEFT)) {
                    if (Raylib.CheckCollisionPointRec(Raylib.GetMousePosition(), new Rectangle(175, 350, 250, 90))) {
                        startScreen = false;
                    }
                }

                continue;
            }

            Raylib.BeginDrawing();

            var keyPressed = Raylib.GetKeyPressed();
            var segments = snake.GetSegments();
            Console.WriteLine(keyPressed);
            if (keyPressed == 80) { // p key
                paused = !paused;
            } else if (keyPressed == 87 || keyPressed == 265) { // w key or up arrow
                snake.SetDirection(Direction.Up);
            } else if (keyPressed == 83 || keyPressed == 264) { // s key or down arrow
                snake.SetDirection(Direction.Down);
            } else if (keyPressed == 65 || keyPressed == 263) { // a key or left arrow
                snake.SetDirection(Direction.Left);
            } else if (keyPressed == 68 || keyPressed == 262) { // d key or right arrow
                snake.SetDirection(Direction.Right);
            }

            if (!paused) {
                if (!snake.Update()) {
                    snake.Reset();
                    speed = 200;
                }
            }

            // border is draw as the background
            Raylib.ClearBackground(new Color(149, 125, 173, 255));

            // play area is drawn as a rectangle on top of the background
            Raylib.DrawRectangle(20, 20, 560, 560, new Color(224, 187, 228, 255));

            //draw score
            Raylib.DrawText($"Score: {segments.Count-3}", 28, 555, 20, new Color(20, 20, 20, 100));

            // draw food
            var foodPosition = food.GetPosition();
            Raylib.DrawCircle(foodPosition.X+10, foodPosition.Y+10, 4, new Color(20, 20, 20, 100));
            // Raylib.DrawRectangle(foodPosition.X+5, foodPosition.Y+5, 10, 10, new Color(20, 20, 20, 150));

            // draw snake
            var segmentIndex = 0;
            foreach (Position segment in segments) {
                if (segmentIndex == 0) {
                    Raylib.DrawRectangle(segment.X, segment.Y, 20, 20, new Color(165, 137, 193, 255));
                    Raylib.DrawCircle(segment.X+10, segment.Y+10, 3, new Color(20, 20, 20, 100));
                    // Raylib.DrawRectangle(segment.X+5, segment.Y+5, 10, 10, new Color(20, 20, 20, 150));
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

            if (paused) {
                var textLength = Raylib.MeasureText("Paused...", 40);
                Raylib.DrawText("Paused...", 300-textLength/2, 290, 40, Color.BLACK);
            }

            Raylib.EndDrawing();
            Thread.Sleep(speed);
        }

        Raylib.CloseWindow();
    }
}

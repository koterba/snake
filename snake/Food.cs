public class Food {
    Position position;

    public Food() {
        var rand = new Random();
        var x = rand.Next(1, 29) * 20;
        var y = rand.Next(1, 29) * 20;
        position = new Position(x, y);
    }

    public Position GetPosition() {
        return position;
    }

    public void Randomize() {
        var rand = new Random();
        var x = rand.Next(1, 29) * 20;
        var y = rand.Next(1, 29) * 20;
        position = new Position(x, y);
    }
}

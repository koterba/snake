public class Snake {
    List<Position> segments;
    Direction direction;
    bool addSegmentFlag;

    public Snake() {
        segments = new List<Position>();
        direction = Direction.Left;
        addSegmentFlag = false;

        segments.Add(new Position(300, 300));
        segments.Add(new Position(320, 300));
        segments.Add(new Position(340, 300));
    }

    public bool Update() {
        // instead of moving each snake segment forward
        // the last one gets removed and appended to the end
        var firstSeg = segments[0];
        segments.Insert(0, new Position(firstSeg.X, firstSeg.Y));
        if (!addSegmentFlag) {
            segments.RemoveAt(segments.Count-1);
        }
        if (direction == Direction.Up) {
            segments[0].Y = segments[1].Y - 20;
            segments[0].X = segments[1].X;
        } else if (direction == Direction.Down) {
            segments[0].Y = segments[1].Y + 20;
            segments[0].X = segments[1].X;
        } else if (direction == Direction.Left) {
            segments[0].X = segments[1].X - 20;
            segments[0].Y = segments[1].Y;
        } else if (direction == Direction.Right) {
            segments[0].X = segments[1].X + 20;
            segments[0].Y = segments[1].Y;
        }
        
        addSegmentFlag = false;

        // check for wall collision
        if ((segments[0].X >= 580 || segments[0].X <= 20 ) || (segments[0].Y >= 580 || segments[0].Y <= 20 )){
            return false;
        }

        // check for tail collision
        var index = -1;
        foreach (var segment in segments) {
            index++;
            if (index == 0) {
                continue;
            }
            if (segment.X == segments[0].X && segment.Y == segments[0].Y) {
                return false;
            }
        }

        // no issues ocurred
        return true;
    }

    public void Reset() {
        segments = new List<Position>();
        direction = Direction.Left;
        addSegmentFlag = false;

        segments.Add(new Position(300, 300));
        segments.Add(new Position(320, 300));
        segments.Add(new Position(340, 300));
    }

    public List<Position> GetSegments() {
        return segments;
    }

    public void SetDirection(Direction _direction) {
        direction = _direction;
    }

    public void AddSegment() {
        addSegmentFlag = true;
    }
}

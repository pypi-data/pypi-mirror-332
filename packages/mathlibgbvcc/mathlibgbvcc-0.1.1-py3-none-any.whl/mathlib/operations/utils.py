from entities import point_2d;

def calc_center(point: point_2d.Point2D, width: float, height: float) -> tuple[float, float]:
  x_center = point.x + width / 2;
  y_center = point.y + height / 2;
  
  return (float(x_center), float(y_center));
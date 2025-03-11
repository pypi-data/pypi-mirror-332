from typing import Optional
from entities.point_2d import Point2D
from math import sqrt

def calculate_length(point1: Point2D, point2: Point2D) -> float:
  return sqrt((point2.x - point1.x)**2 + (point2.y - point1.y)**2)

def intersection(
  line_1_point_1: Point2D,
  line_1_point_2: Point2D,
  line_2_point_1: Point2D,
  line_2_point_2: Point2D
) -> Optional[Point2D]:
  def is_parameter_valid(param: float) -> bool:
    return 0 <= param and param <= 1
  
  dx1 = line_1_point_2.x - line_1_point_1.x
  dy1 = line_1_point_2.y - line_1_point_1.y
  dx2 = line_2_point_2.x - line_2_point_1.x
  dy2 = line_2_point_2.y - line_2_point_1.y
  
  dx3 = line_2_point_1.x - line_1_point_1.x
  dy3 = line_2_point_1.y - line_1_point_1.y
  
  denominator = dx1 * (-dy2) - dy1 * (-dx2)
  
  if abs(denominator) == 0:
    return None
  
  t = (dx3 * (-dy2) - dy3 * (-dx2)) / denominator
  s = (dx1 * dy3 - dy1 * dx3) / denominator
  
  if not (is_parameter_valid(t) and is_parameter_valid(s)):
    return None
  
  intersection_x = line_1_point_1.x + t * dx1
  intersection_y = line_1_point_1.y + t * dy1
  
  return Point2D(intersection_x, intersection_y)
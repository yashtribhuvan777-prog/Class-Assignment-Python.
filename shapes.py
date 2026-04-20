import math

def area_circle(radius):
    return math.pi * radius * radius

def area_rectangle(length, width):
    return length * width

def area_triangle(base, height):
    return 0.5 * base * height

# --- Example Usage ---
if __name__ == "__main__":
    r = 5
    l, w = 10, 20
    b, h = 8, 12

    print(f"Area of Circle (r={r}): {area_circle(r):.2f}")
    print(f"Area of Rectangle ({l}x{w}): {area_rectangle(l, w)}")
    print(f"Area of Triangle (b={b}, h={h}): {area_triangle(b, h)}")
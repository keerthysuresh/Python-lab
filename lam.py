area_square=lambda side:side*side
area_rectangle=lambda length,width:length*width
area_triangle=lambda breadth,height:(breadth*height)*0.5

a=15
b=20
s=(a*b)/2
print(area_square(a))
print(area_rectangle(a,b))
print(area_triangle(a,b))
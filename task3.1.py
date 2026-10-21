def circle_area(d):
    r = d / 2
    s = 3.14159 * r ** 2 
    return s 
#print(circle_area(2))
def tube_cross_section(d_out, d_in):
    s1 = circle_area(d_out)
    s2 = circle_area(d_in)
    return s1 - s2
def tube_mass(d_out, d_in, length, density=7850):
    s = tube_cross_section(d_out, d_in)
    v = s * length
    m = v * density
    return m
print(round(tube_mass(0.060, 0.050, 6), 2))
print(round(tube_mass(0.060, 0.050, 6, density=2700), 2))



import calculate_angles as ang
import interpolation as interp


if __name__== "__main__":
    pts1=interp.interpolate_Bspline(100, [0, -30], [0, 30], 60, True)
    pts2=interp.interpolate_line(100,[0, 30], [0, -30])
    pts=pts1+pts2
    angles=ang.calculate_angles(pts)
    for a in angles:
        print(a)

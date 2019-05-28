import interpolation as interp

if __name__== "__main__":
    pts1=interp.interpolate_Bspline(100, [0, -30], [0, 60], 10, True)
    #pts2=interp.interpolate_line(100,[0, 30], [0, -30])
    # for p in pts2:
    #     print(p)
    # print(len(pts1),len(pts2))
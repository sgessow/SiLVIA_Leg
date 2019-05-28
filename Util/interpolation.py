from geomdl import BSpline
from geomdl import utilities
import matplotlib.pyplot as plt

def interpolate_Bspline(stepsBtwFrame, currentPos, nextPos, liftHeight, draw=False):
    # This function returns a list of 2-D trajectory points. Need to use IK to convert to joint angles afterwards
    # The return looks like [[0,0], [0,0], [0,0], [0,0], ... [0,0]] length=stepsBtwFrame
    # next = [x, z]
    # curr = [x, z]

    x_offset = 15.0  # Top control point height above liftheight
    z_offset = 5.0  # End control point position outside leg stroke

    # Pick up leg and make a full curve down to a upper position of wall

    halfZstroke = (nextPos[1] - currentPos[1]) / 2.0  # half stroke
    halfZstroke_and_offset = halfZstroke + z_offset  # half stroke plus offset outside the stroke

    ctrlPoint = [[0.0,                                   -halfZstroke_and_offset/1.2],
                 [liftHeight,                           -halfZstroke],
                 [liftHeight+x_offset,   0.0],
                 [liftHeight,                           2*halfZstroke]]  # there was one more point: [self.liftHeight/2, 0.0, halfZstroke_and_offset/3.0]

    nurbs = BSpline.Curve()

    # Set unweighted control points

    allPts = [currentPos]
    for i in range(len(ctrlPoint)):
        allPts.append(ctrlPoint[i])

    allPts.append(nextPos)

    nurbs.degree = 2  # Degree of the curve, order = degree+1

    nurbs.ctrlpts = allPts

    # Auto-generate knot vector
    nurbs.knotvector = utilities.generate_knot_vector(nurbs.degree, len(nurbs.ctrlpts))

    # depending on how long the looping time is and how smooth you want the trajectory to be,
    # this value should be carefully tuned
    nurbs.sample_size = stepsBtwFrame + 1  # The total # of points that goes to pts = nurbs._curve_points

    nurbs.evaluate()  # need to put start and stop points

    pts = nurbs.evalpts#[1:(stepsBtwFrame+1)]

    if draw == True:
        ##################### For climbing between 2 walls #####################
        plt.plot([nurbs.evalpts[i][0] for i in range(nurbs.sample_size)],
                 [nurbs.evalpts[i][1] for i in range(nurbs.sample_size)])
        plt.xlabel("x")
        plt.ylabel("z")
        #plt.xlim([-200, 10])
        #plt.ylim([-200, 200])
        plt.show(block=True)

    return pts


def interpolate_line(stepsBtwFrame, currentPos, nextPos):
    pts=[]
    if currentPos[0]==nextPos[0]:
        delta_y=(nextPos[1]-currentPos[1])/stepsBtwFrame
        for i in range(stepsBtwFrame):
            coord=[currentPos[0],currentPos[1]+i*delta_y]
            pts.append(coord)
        pts.append(nextPos)
    elif currentPos[1]==nextPos[1]:
        delta_x = (nextPos[0] - currentPos[0]) / stepsBtwFrame
        for i in range(stepsBtwFrame):
            coord = [currentPos[0] + i * delta_x,currentPos[1]]
            pts.append(coord)
        pts.append(nextPos)
    else:
        print("Not implemented for diagonol lines yet!!")
        return 1
    return pts
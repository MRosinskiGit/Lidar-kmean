from scipy.stats import norm
from scipy.stats import truncnorm
from numpy import zeros, sin, cos, pi, ones
from random import uniform




def generate_points_horizontal(*, num_points:int= 2000, length, depth, concentration:int=1, move=[0,0,0]):
    scalex=length/concentration
    distribution_x = truncnorm(a=-length/scalex, b=length/scalex, scale=scalex)
    scaley=depth/concentration
    distribution_y = truncnorm(a=-depth/scaley, b=depth/scaley, scale=scaley)
    #distribution_z = norm(loc=0.2, scale=0.05)

    x=distribution_x.rvs(size=num_points)
    y=distribution_y.rvs(size=num_points)
    z=zeros(num_points)

    x=x+move[0]
    y=y+move[1]
    z=z+move[2]

    points = zip(x,y,z)
    return points


def generate_points_vertical(*, num_points:int= 2000, width, height, concentration:int=1, move=[0,0,0]):
    scalex=width/concentration
    distribution_x = truncnorm(a=-width/scalex, b=width/scalex, scale=scalex)
    #distribution_y = norm(loc=0, scale=0.05)
    scalez=height/concentration
    distribution_z = truncnorm(a=-height/scalez, b=height/scalez, scale=scalez)

    x=distribution_x.rvs(size=num_points)
    y=zeros(num_points)
    z=distribution_z.rvs(size=num_points)

    x=x+move[0]
    y=y+move[1]
    z=z+move[2]

    points = zip(x,y,z)
    return points


def generate_points_cylindrical(*, num_points:int= 2000, radius, height, concentration:int=1, move=[0,0,0]):
    angle=ones(num_points)
    for i in range (0,num_points):
        angle[i] = uniform(0, 2*pi)

    scaler=radius/concentration
    distribution_r = truncnorm(a=-radius/2/scaler, b=radius/2/scaler, scale=scaler)

    scalez=height/concentration
    distribution_z = truncnorm(a=-height/2/scalez, b=height/2/scalez, scale=scalez)
    r=distribution_r.rvs(size=num_points)

    x=abs(r)*cos(angle)
    y=abs(r)*sin(angle)
    z=distribution_z.rvs(size=num_points)

    x=x+move[0]
    y=y+move[1]
    z=z+move[2]

    points = zip(x,y,z)
    return points


def generate_points(*, num_points:int= 2000 ):
    distribution_x = norm(loc=0, scale=20)
    distribution_y = norm(loc=0, scale=200)
    distribution_z = norm(loc=0.2, scale=0.05)

    x=distribution_x.rvs(size=num_points)
    y=distribution_y.rvs(size=num_points)
    z=distribution_z.rvs(size=num_points)

    points = zip(x,y,z)
    return points

# if __name__ == '__main__':
#     cloud_points = generate_points()
#     with open('LidarData.xyz', 'w', encoding='utf-8', newline='\n') as csvfile:
#
#         csvwriter = writer(csvfile)
#         for p in cloud_points:
#             csvwriter.writerow(p)
#             print(p)
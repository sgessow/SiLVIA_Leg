clc;
%% CONSTANTS
g=9.81; %m/s^2
scalling_const=.3;
mass_robot=10.3; %kg
mu=.5;
f=58.5; %mm
t=112.5; %mm
SAFTEY_FACTOR=1;

%% Inputs
% Specify the angle of the hip with respect to horizantal in rads
Input_Angle= deg2rad(120); %rad
% The distance from the center of the robot to the wall
d=100; %mm

%% Position Calculations
d=d*10^-3;
f=f*10^-3;
t=t*10^-3;
T_1=Input_Angle;
if (d+f*cos(T_1)>t)
    msg = 'Invalid Geometry';
    error(msg);
end
syms t_1 t_2
x(t_1, t_2)=f*cos(t_1)-t*cos(t_2);
y(t_1,t_2)=-f*sin(t_1)-t*sin(t_2);
T_2=acos((d+f*cos(T_1))/t);
Angle=[T_1,T_2];
Pos=[vpa(x(T_1,T_2)),vpa(y(T_1,T_2))];
%% Force Calculations
F_y=-g*mass_robot*.3/4;
F_x=F_y/mu*SAFTEY_FACTOR;
F=[F_x,F_y];
%% Torque Calculations
J=[diff(x,t_1),diff(x,t_2);diff(y,t_1),diff(y,t_2)];
Angles=1.1:.01:pi;
Motor_1=zeros(size(Angles));
Motor_2=zeros(size(Angles));
for i=1:size(Angles.')
    T_1=Angles(i);
    T_2=acos((d+f*cos(T_1))/t);
    J_num=J(T_1,T_2);
    J_num=vpa(J_num);
    Torque=(J_num.'*F.').';
    Motor_1(i)=abs(Torque(1));
    Motor_2(i)=abs(Torque(2));
end
plot(rad2deg(Angles),Motor_1,rad2deg(Angles),Motor_2)

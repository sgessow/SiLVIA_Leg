clc;
data = csvread("Model_Trajectory.csv");
%% CONSTANTS
g=9.81; %m/s^2
scalling_const=sqrt(.3);
scalling_const_force=sqrt(.3);
mass_robot=10.3; %kg
mu=.5;
f=195*scalling_const; %mm
t=375*scalling_const; %mm
SAFTEY_FACTOR=3;
dt=.005;

%% Inputs
% The distance from the center of the robot to the wall
d=200; %mm
% The distance the body is from the point of contact
h=-30;

%% Position Calculations
d=d*10^-3;
f=f*10^-3;
t=t*10^-3;
h=h*10^-3;

syms t_1 t_2
x(t_1, t_2)=f*cos(t_1)+t*cos(t-1-t_2)-d;
y(t_1,t_2)=f*sin(t_1)-t*sin(t_1-t_2)-h;
% [T_1, T_2]=solve([x,y]);
% T_1=vpa(T_1(1));
% T_2=vpa(T_2(2));
% rad2deg(T_1-T_2);
% Angle=[T_1,T_2];
% Pos=[vpa(x(T_1,T_2)),vpa(y(T_1,T_2))];
%% Force Calculations
F_y=-g*mass_robot*(sqrt(3)/6)/4;
F_x=F_y/mu*SAFTEY_FACTOR;
F=[F_x,F_y];
%% Torque Calculations
J=[diff(x,t_1),diff(x,t_2);diff(y,t_1),diff(y,t_2)];
T_1=data(1,1);
T_2=data(1,2);
power=zeros(1,length(data));
time=zeros(1,length(data));
for i=1:length(data)
    time(i)=dt*i;
    if(data(i,3)==250)
        Force=F;
    else
        Force=[0,0];
    end
    w_1=(T_1-data(i,1))/dt;
    w_2=(T_1-data(i,1))/dt;
    T_1=data(i,1);
    T_2=data(i,2);
    J_num=J(T_1,T_2);
    J_num=vpa(J_num);
    Torque=(J_num.'*Force.').';
    power(i)=abs(Torque(1)*w_1)+abs(Torque(2)*w_2);
end
plot(time,power)
Energy=trapz(time,power);

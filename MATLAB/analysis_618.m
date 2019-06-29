clc; close all;
data_s_1 = csvread('Good Data\618\S_7_618_1.csv');
data_s_2 = csvread('Good Data\618\S_7_618_2.csv');
data_s_3 = csvread('Good Data\618\S_7_618_3.csv');
data_22_1 = csvread('Good Data\618\NS_22_618_1.csv');
data_22_2 = csvread('Good Data\618\NS_22_618_2.csv');
data_22_3= csvread('Good Data\618\NS_22_618_3.csv');

%     1          2      3      4     5     6      7          8      9    10    11    12   13
% Time Arduino | mA 1 | mA 2 | V 1 | V 2 | F | Time Dyna |  T_1 | T_2 | m_x | m_y | g_x | g_y   
%Position
x_g_s_1=data_s_1(2:end,12);
y_g_s_1=data_s_1(2:end,13);

x_m_s_1=data_s_1(2:end,10);
y_m_s_1=data_s_1(2:end,11);
x_m_s_2=data_s_2(2:end,10);
y_m_s_2=data_s_2(2:end,11);
x_m_s_3=data_s_1(2:end,10);
y_m_s_3=data_s_1(2:end,11);

x_g_22_1=data_22_1(2:end,12);
y_g_22_1=data_22_1(2:end,13);

x_m_22_1=data_22_1(2:end,10);
y_m_22_1=data_22_1(2:end,11);
x_m_22_2=data_22_2(2:end,10);
y_m_22_2=data_22_2(2:end,11);
x_m_22_3=data_22_1(2:end,10);
y_m_22_3=data_22_1(2:end,11);

%Time
time_s_1=data_s_1(2:end,7)-data_s_1(2,7);
time_s_2=data_s_2(2:end,7)-data_s_2(2,7);
time_s_3=data_s_3(2:end,7)-data_s_3(2,7);
time_22_1=data_22_1(2:end,7)-data_22_1(2,7);
time_22_2=data_22_2(2:end,7)-data_22_2(2,7);
time_22_3=data_22_3(2:end,7)-data_22_3(2,7);

% Power
power_s_1=data_s_1(2:end,2).*data_s_1(2:end,4)./10^3;
power_s_2=data_s_2(2:end,2).*data_s_2(2:end,4)./10^3;
power_s_3=data_s_3(2:end,2).*data_s_3(2:end,4)./10^3;
power_22_1=data_22_1(2:end,2).*data_22_1(2:end,4)./10^3;
power_22_2=data_22_2(2:end,2).*data_22_2(2:end,4)./10^3;
power_22_3=data_22_3(2:end,2).*data_22_3(2:end,4)./10^3;

power2_s_1=data_s_1(2:end,3).*data_s_1(2:end,5)./10^3;
power2_s_2=data_s_2(2:end,3).*data_s_2(2:end,5)./10^3;
power2_s_3=data_s_3(2:end,3).*data_s_3(2:end,5)./10^3;
power2_22_1=data_22_1(2:end,3).*data_22_1(2:end,5)./10^3;
power2_22_2=data_22_2(2:end,3).*data_22_2(2:end,5)./10^3;
power2_22_3=data_22_3(2:end,3).*data_22_3(2:end,5)./10^3;

%Force
force_s_1=data_s_1(2:end,6);
force_s_2=data_s_2(2:end,6);
force_s_3=data_s_3(2:end,6);
force_22_1=data_22_1(2:end,6);
force_22_2=data_22_2(2:end,6);
force_22_3=data_22_3(2:end,6);

first_section=find(time_s_1<2);
first_section=first_section(end);
first_section_1=find(time_s_1<1);
first_section_1=first_section_1(end);
second_section=find(time_s_1<4);
second_section=second_section(end);

% Total Energy
energy_s_1=trapz(time_s_1(22:end), power_s_1(22:end));
energy_s_2=trapz(time_s_2(22:end), power_s_2(22:end));
energy_s_3=trapz(time_s_3(22:end), power_s_3(22:end));
energy_22_1=trapz(time_22_1(22:end),power_22_1(22:end));
energy_22_2=trapz(time_22_2(22:end),power_22_2(22:end));
energy_22_3=trapz(time_22_3(22:end),power_22_3(22:end));
Energy_Total_s=mean([energy_s_1,energy_s_2,energy_s_3]);
Energy_Total_22=mean([energy_22_1,energy_22_2,energy_22_3]);

% Energy Total 2
energy2_s_1=trapz(time_s_1(22:end), power2_s_1(22:end));
energy2_s_2=trapz(time_s_2(22:end), power2_s_2(22:end));
energy2_s_3=trapz(time_s_3(22:end), power2_s_3(22:end));
energy2_22_1=trapz(time_22_1(22:end),power2_22_1(22:end));
energy2_22_2=trapz(time_22_2(22:end),power2_22_2(22:end));
energy2_22_3=trapz(time_22_3(22:end),power2_22_3(22:end));
Energy2_Total_s=mean([energy2_s_1,energy2_s_2,energy2_s_3])
Energy2_Total_22=mean([energy2_22_1,energy2_22_2,energy2_22_3])

% Energy By Section
energy_s_1_m=trapz(time_s_1(22:first_section), power_s_1(22:first_section));
energy_s_2_m=trapz(time_s_2(22:first_section), power_s_2(22:first_section));
energy_s_3_m=trapz(time_s_3(22:first_section), power_s_3(22:first_section));
energy_22_1_m=trapz(time_22_1(22:first_section),power_22_1(22:first_section));
energy_22_2_m=trapz(time_22_2(22:first_section),power_22_2(22:first_section));
energy_22_3_m=trapz(time_22_3(22:first_section),power_22_3(22:first_section));
Energy_1_s=mean([energy_s_1_m,energy_s_2_m,energy_s_3_m]);
Energy_1_22=mean([energy_22_1_m,energy_22_2_m,energy_22_3_m]);

% Energy Hold
energy_s_1_h=trapz(time_s_1(first_section:second_section), power_s_1(first_section:second_section));
energy_s_2_h=trapz(time_s_2(first_section:second_section), power_s_2(first_section:second_section));
energy_s_3_h=trapz(time_s_3(first_section:second_section), power_s_3(first_section:second_section));
energy_22_1_h=trapz(time_22_1(first_section:second_section),power_22_1(first_section:second_section));
energy_22_2_h=trapz(time_22_2(first_section:second_section),power_22_2(first_section:second_section));
energy_22_3_h=trapz(time_22_3(first_section:second_section),power_22_3(first_section:second_section));
Energy_2_s=mean([energy_s_1_h,energy_s_2_h,energy_s_3_h]);
Energy_2_22=mean([energy_22_1_h,energy_22_2_h,energy_22_3_h]);

% Energy by section in first section
energy_s_1_m_1=trapz(time_s_1(22:first_section_1), power_s_1(22:first_section_1));
energy_s_2_m_1=trapz(time_s_2(22:first_section_1), power_s_2(22:first_section_1));
energy_s_3_m_1=trapz(time_s_3(22:first_section_1), power_s_3(22:first_section_1));
energy_22_1_m_1=trapz(time_22_1(22:first_section_1),power_22_1(22:first_section_1));
energy_22_2_m_1=trapz(time_22_2(22:first_section_1),power_22_2(22:first_section_1));
energy_22_3_m_1=trapz(time_22_3(22:first_section_1),power_22_3(22:first_section_1));
Energy_1_s_1=mean([energy_s_1_m_1,energy_s_2_m_1,energy_s_3_m_1]);
Energy_1_22_1=mean([energy_22_1_m_1,energy_22_2_m_1,energy_22_3_m_1]);

energy_s_1_m_2=trapz(time_s_1(first_section_1:first_section), power_s_1(first_section_1:first_section));
energy_s_2_m_2=trapz(time_s_2(first_section_1:first_section), power_s_2(first_section_1:first_section));
energy_s_3_m_2=trapz(time_s_3(first_section_1:first_section), power_s_3(first_section_1:first_section));
energy_22_1_m_2=trapz(time_22_1(first_section_1:first_section),power_22_1(first_section_1:first_section));
energy_22_2_m_2=trapz(time_22_2(first_section_1:first_section),power_22_2(first_section_1:first_section));
energy_22_3_m_2=trapz(time_22_3(first_section_1:first_section),power_22_3(first_section_1:first_section));
Energy_1_s_2=mean([energy_s_1_m_2,energy_s_2_m_2,energy_s_3_m_2]);
Energy_1_22_2=mean([energy_22_1_m_2,energy_22_2_m_2,energy_22_3_m_2]);
% Power;
plot(time_s_1,power_s_1,time_s_2,power_s_2,time_s_3,power_s_3, ...
    time_22_1,power_22_1,time_22_2,power_22_2,time_22_3,power_22_3);
xlabel("Time [s]");
ylabel("Power [W]");
legend("Spring 1","Spring 2","Spring 3","No Spring 1","No Spring 2","No Spring 3")
% Power 2 
figure
plot(time_s_1,power2_s_1,time_s_2,power2_s_2,time_s_3,power2_s_3, ...
    time_22_1,power2_22_1,time_22_2,power2_22_2,time_22_3,power2_22_3);
xlabel("Time [s]");
ylabel("Power [W]");
legend("Spring 1","Spring 2","Spring 3","No Spring 1","No Spring 2","No Spring 3")
% Force
figure
plot(time_s_1,force_s_1,time_s_2,force_s_2,time_s_3,force_s_3, ...
    time_22_1,force_22_1,time_22_2,force_22_2,time_22_3,force_22_3);
xlabel("Time [s]");
ylabel("Force [N]");
legend("Spring 1","Spring 2","Spring 3","No Spring 1","No Spring 2","No Spring 3")

% Position
figure
hold on
wall_y=[-100:.01:0];
wall_x=250+zeros(1,length(wall_y));
plot(x_g_s_1,y_g_s_1,x_g_22_1,y_g_22_1,x_m_s_1,y_m_s_1,x_m_s_2,y_m_s_2,x_m_s_3,y_m_s_3, ...
    x_m_22_1,y_m_22_1,x_m_22_2,y_m_22_2,x_m_22_3,y_m_22_3);
plot(wall_x,wall_y,"black");
xlabel("x [mm]");
ylabel("y [mm]");
xlim([210,275])
ylim([-100,-22])
legend("Goal Spring","Goal No Spring","Spring 1","Spring 2","Spring 3","No Spring 1", "No Spring 2", "No Spring 3")

% Position and time
figure
hold on
x_s = x_g_s_1';
y_s = y_g_s_1';
z_s = zeros(size(x));
col_s = x_s;  % This is the color, vary with x in this case.
surface([x_s;x_s],[y_s;y_s],[z_s;z_s],[col_s;col_s],...
        'facecol','no',...
        'edgecol','interp',...
        'linew',1);
x = x_m_s_1';
y = y_m_s_1';
z = zeros(size(x));
col = x; 
surface([x;x],[y;y],[z;z],[col;col],...
        'facecol','no',...
        'edgecol','interp',...
        'linew',1);
    
x_ns = x_g_22_1';
y_ns = y_g_22_1';
z_ns = zeros(size(x_ns));
col_ns = x_ns;  % This is the color, vary with x in this case.
surface([x_ns;x_ns],[y_ns;y_ns],[z_ns;z_ns],[col_ns;col_ns],...
        'facecol','no',...
        'edgecol','interp',...
        'linew',1);
x = x_m_22_1';
y = y_m_22_1';
z = zeros(size(x));
col = x_ns; 
surface([x;x],[y;y],[z;z],[col;col],...
        'facecol','no',...
        'edgecol','interp',...
        'linew',1);
plot(wall_x,wall_y,"black");
xlabel("x [mm]")
ylabel("y [mm]")
xlim([210,275])
ylim([-100,-22])
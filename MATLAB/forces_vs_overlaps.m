clc;
data_s = csvread('Good Data\552\S_7_552_1.csv');
data_18 = csvread('Good Data\552\NS_18_552_3.csv');
data_22 = csvread('Good Data\552\NS_22_552_3.csv');
data_20 = csvread('Good Data\552\NS_20_552_3.csv');
data_25 = csvread('Good Data\552\NS_25_552_3.csv');
%     1          2      3      4     5     6      7          8      9    10    11    12   13
% Time Arduino | mA 1 | mA 2 | V 1 | V 2 | F | Time Dyna |  T_1 | T_2 | m_x | m_y | g_x | g_y   

%Time
time_s=data_s(2:end,7)-data_s(2,7);
time_18=data_18(2:end,7)-data_18(2,7);
time_20=data_20(2:end,7)-data_20(2,7);
time_22=data_22(2:end,7)-data_22(2,7);
time_25=data_25(2:end,7)-data_25(2,7);

% Power
power_s=data_s(2:end,2).*data_s(2:end,4)./10^6;
power_18=data_18(2:end,2).*data_18(2:end,4)./10^6;
power_20=data_20(2:end,2).*data_20(2:end,4)./10^6;
power_22=data_22(2:end,2).*data_22(2:end,4)./10^6;
power_25=data_25(2:end,2).*data_25(2:end,4)./10^6;

%Force
force_s=data_s(2:end,6);
force_18=data_18(2:end,6);
force_20=data_20(2:end,6);
force_22=data_22(2:end,6);
force_25=data_25(2:end,6);

% Forces for all diffrent overlaps
plot(time_s,force_s,time_18,force_18,time_20,force_20,time_22,force_22,time_25,force_25);
%xlabel("Time [s]");
%ylabel("Force [N]");
legend("Spring", "18", "20", "22", "25")




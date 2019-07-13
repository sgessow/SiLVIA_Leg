clc;
clear;
%read csv files
my_data = csvread('/Users/lingweizhang/Desktop/Model.csv',1);

%remove first two columns
my_data(:,1)=[];
my_data(:,1)=[];
[nrows,ncolumns] = size(my_data);
T = (1:nrows)';

%create matrix with numbers
my_data_new = [T my_data];

%calculate velosity
x=[];
y=[];
distance=[];
velosity=[];
i = 1:nrows;
x(i) = my_data_new(i,2);
y(i) = my_data_new(i,3);
T = 0.005*i;

%design triangle to calculate v_x and v_y
for j = 1:nrows-1
    delta_x(j) = x(j+1) - x(j);
    delta_y(j) = y(j+1) - y(j);
    distance(j)= sqrt(delta_x(j).^2 + delta_y(j).^2);
    velosity(j) = distance(j) / 0.005;                       %time = 0.005s
    factor_x(j) = delta_x(j) / distance(j);
    factor_y(j) = delta_y(j) / distance(j);
    velosity_x(j) = abs(velosity(j) * factor_x(j));
    velosity_y(j) = abs(velosity(j) * factor_y(j));
end



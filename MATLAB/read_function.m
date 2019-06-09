function data_new=read_function(filename)
data = csvread(filename,1);
data(:,1)=[];
data(:,4)=[];
data(:,3)=-data(:,3);
[nrows ncolumns] = size(data);
T = (1:nrows)';
data_new = [T data];
end

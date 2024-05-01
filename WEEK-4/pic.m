clc
clear all
close all
data=struct('name','john','age',30,'city','New york');
save -binary data.mat data;
clear data;
loaded_data=load("-binary","data.mat");
disp(loaded_data);

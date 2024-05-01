clc
clear all
close all
f=10;%frequency
fs=1000;%sampling frequency
t=0:1/fs:1;%time
A=1%amplitude
y=A*sin(2*pi*f*t);
fid=fopen('sine.npy','wb');
fprintf(fid,'%f\n',y)
fclose(fid)
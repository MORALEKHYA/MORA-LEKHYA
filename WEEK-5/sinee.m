clc 
close all 
clear all
frequency=1;
amplitude=1;
duration=5;
samping_rate=1000;
t=linspace(0,duration,duration*sampling_rate);
sine_wave=amplitude*sin(2*pi*frequency*t);
csvwrite('sine_wave.csv',[t' sine_wave']);
clc
clear all
close all
file_path="/home/rguktrkvalley/Desktop/WEEK-7/file_example_WAV_1MG.wav"
[signal,Sample_rate]=audioread(file_path)
duration=length(signal)/Sample_rate;
time=(0:length(signal)-1)/Sample_rate;
plot(time,signal)
xlabel('time(s)')
ylabel('amplitude')
title('audio signal')
grid on
t=0:0.01:1
si={'s1',[2,5];'s2',[5,10],'s3',[5,10],'s4',[10,12];'s5',[1,2];}
k=str(input("Enter the key"))
figure;
hold on;
for i=1:length(si)
  l=si.k
  f=l(1)
  amp=l(10)
  wave=amp*sin(2*pi*f*t)
  plot(t1wave)
  xlabel('time(s)')
  ylabel('amplitude')
  title('sinewave')
  legend
  plt.show()
endfor
hold off;
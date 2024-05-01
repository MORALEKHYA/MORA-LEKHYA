x = [];
y = [];

xl = input('Enter length of x: ');
yl = input('Enter length of y: ');

disp('Enter elements into x:');
for i = 1:xl
    a = input('Enter: ');
    x = [x a];
end

disp('Enter elements into y:');
for i = 1:yl
    a = input('Enter: ');
    y = [y a];
end

z = [];
for k = 0 : yl - 2
    s = 0;
    for n = 1 : xl
        if n + k <= xl
            s = s + x(n) * y(n + k);
        end
    end
    z = [z s];
end

plot(z);
xlabel('Lag');
ylabel('Cross-correlation');
title('Cross-correlation between x and y');


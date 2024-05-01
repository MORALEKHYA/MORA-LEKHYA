% Generate random signal x[n]
x = rand(1, 1000);

% Calculate energy for every 20 amplitudes
energy = zeros(1, ceil(length(x) / 20));
for k = 1:length(energy)
    start_index = max(1, 20*(k-1) + 1);
    end_index = min(20*k, length(x));
    energy(k) = sum(abs(x(start_index:end_index)).^2);
end

% Plot energy
plot(energy);
xlabel('Index k');
ylabel('Energy e[k]');
title('Energy for every 20 amplitudes');


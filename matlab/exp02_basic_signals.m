% Experiment 2: Unit step, impulse, ramp, exponential, parabolic and sinusoidal signals
clc; clear; close all;
n = -10:10;  t = linspace(-2, 4, 1000);
step = double(n >= 0);
impulse = double(n == 0);
ramp = n .* (n >= 0);
expo = exp(0.2*n);
parab = (n.^2 / 2) .* (n >= 0);

f1 = figure('Position', [100 100 900 800]);
sigs = {step, impulse, ramp, expo, parab};
ttl  = {'Unit step u[n]', 'Unit impulse \delta[n]', 'Unit ramp r[n]', 'Exponential e^{0.2n}', 'Parabolic n^2/2 u[n]'};
for k = 1:5
    subplot(3,2,k); stem(n, sigs{k}); grid on; title(ttl{k}); xlabel('n'); ylabel('Amplitude');
end
subplot(3,2,6); plot(t, sin(2*pi*t)); grid on; title('Sinusoid sin(2\pi t)'); xlabel('t (s)');
save_fig(f1, 'exp02_basic_signals.png');

f2 = figure;
plot(t, sin(2*pi*t), t, cos(2*pi*t), t, 2*sin(4*pi*t)); grid on
title('Sinusoidal signals'); xlabel('t (s)'); ylabel('Amplitude');
legend('sin(2\pi t)', 'cos(2\pi t)', '2 sin(4\pi t)');
save_fig(f2, 'exp02_sinusoids.png');

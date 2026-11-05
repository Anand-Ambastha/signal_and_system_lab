% Experiment 5: Magnitude and phase spectrum using the Fourier transform
clc; clear; close all;
fs = 1000; t = 0:1/fs:1-1/fs;
x = sin(2*pi*50*t) + 0.5*sin(2*pi*120*t + pi/4);
N = length(x);
X = fftshift(fft(x)) / N;
f = (-N/2:N/2-1) * fs / N;
mag = abs(X);
ph = angle(X); ph(mag < 1e-6) = 0;

fig = figure('Position', [100 100 800 800]);
subplot(3,1,1); plot(t(1:200), x(1:200)); grid on; title('Signal x(t) (first 0.2 s)'); xlabel('t (s)');
subplot(3,1,2); plot(f, mag); grid on; xlim([-200 200]); title('Magnitude spectrum |X(f)|'); xlabel('f (Hz)');
subplot(3,1,3); plot(f, ph); grid on; xlim([-200 200]); title('Phase spectrum \angle X(f)'); xlabel('f (Hz)'); ylabel('rad');
save_fig(fig, 'exp05_fourier_transform.png');

% Rectangular pulse
T = 0.1; t2 = -1:1/fs:1-1/fs;
p = double(abs(t2) <= T/2);
P = fftshift(fft(p)) / fs;
f2 = (-length(p)/2:length(p)/2-1) * fs / length(p);
php = angle(P); php(abs(P) < 1e-6) = 0;
fig2 = figure('Position', [100 100 800 800]);
subplot(3,1,1); plot(t2, p); grid on; title('Rectangular pulse'); xlabel('t (s)');
subplot(3,1,2); plot(f2, abs(P)); grid on; xlim([-100 100]); title('Magnitude |P(f)| (sinc)'); xlabel('f (Hz)');
subplot(3,1,3); plot(f2, php); grid on; xlim([-100 100]); title('Phase'); xlabel('f (Hz)');
save_fig(fig2, 'exp05_rect_pulse_spectrum.png');

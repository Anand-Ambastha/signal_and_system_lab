% Experiment 6: Magnitude and phase spectra using the Fourier series
clc; clear; close all;
T0 = 1; fs = 5000; w0 = 2*pi/T0;
t  = 0:1/fs:2*T0-1/fs;
tp = 0:1/fs:T0-1/fs;
x_one = double(tp < T0/2); x_one(x_one == 0) = -1;    % square wave, one period
K = 20; k = -K:K;
c = zeros(size(k));
for i = 1:length(k)
    c(i) = trapz(tp, x_one .* exp(-1j*k(i)*w0*tp)) / T0;
end
fprintf('c1 = %.4f%+.4fj (theory: -j*2/pi = %.4fj)\n', real(c(K+2)), imag(c(K+2)), -2/pi);

f1 = figure('Position', [100 100 800 650]);
subplot(2,1,1); stem(k, abs(c)); grid on; title('Magnitude spectrum |c_k|'); xlabel('harmonic k');
ph = angle(c); ph(abs(c) < 1e-3) = 0;
subplot(2,1,2); stem(k, ph); grid on; title('Phase spectrum \angle c_k'); xlabel('harmonic k'); ylabel('rad');
save_fig(f1, 'exp06_fourier_series_spectra.png');

orig = double(mod(t, T0) < T0/2); orig(orig == 0) = -1;
f2 = figure('Position', [100 100 1000 650]);
Ns = [1 3 9 49];
for j = 1:4
    kk = -Ns(j):Ns(j); xr = zeros(size(t));
    for i = 1:length(kk)
        ck = trapz(tp, x_one .* exp(-1j*kk(i)*w0*tp)) / T0;
        xr = xr + ck * exp(1j*kk(i)*w0*t);
    end
    subplot(2,2,j); plot(t, orig, 'k--', t, real(xr)); grid on;
    title(sprintf('Harmonics up to k = \\pm%d', Ns(j))); xlabel('t (s)');
end
save_fig(f2, 'exp06_fourier_series_reconstruction.png');

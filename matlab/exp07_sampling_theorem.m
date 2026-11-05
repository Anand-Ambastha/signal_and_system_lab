% Experiment 7 (also CBS 1): Sampling theorem
clc; clear; close all;
f_sig = 10;
t = linspace(0, 0.5, 5000);
x = cos(2*pi*f_sig*t);
fsList = [15 20 100];
names  = {'Under-sampling  fs = 15 Hz (< 2fm)', 'Nyquist rate  fs = 20 Hz (= 2fm)', 'Over-sampling  fs = 100 Hz (> 2fm)'};

f1 = figure('Position', [100 100 1000 850]);
for i = 1:3
    fs = fsList(i);
    n = 0:floor(0.5*fs);  ts = n/fs;  xs = cos(2*pi*f_sig*ts);
    xr = zeros(size(t));
    for m = 1:length(n)                 % ideal sinc interpolation
        xr = xr + xs(m) * sinc_fn(fs*t - n(m));
    end
    subplot(3,2,2*i-1); plot(t, x); hold on; stem(ts, xs, 'r'); grid on; title(names{i}); xlabel('t (s)');
    subplot(3,2,2*i);   plot(t, x, '--', t, xr); grid on; title('Reconstruction (sinc interpolation)'); xlabel('t (s)');
    legend('original', 'reconstructed');
    err = sqrt(mean((x(1001:4000) - xr(1001:4000)).^2));
    fprintf('fs = %3d Hz -> RMS error (middle of record) = %.4f\n', fs, err);
end
save_fig(f1, 'exp07_sampling_theorem.png');

alias_fs = [15 100];
f2 = figure('Position', [100 100 900 320]);
for i = 1:2
    fs = alias_fs(i);
    ts = 0:1/fs:2-1/fs; xs = cos(2*pi*f_sig*ts);
    L = length(xs); X = abs(fft(xs))/L; X = X(1:floor(L/2)+1); f = (0:floor(L/2)) * fs / L;
    subplot(1,2,i); stem(f, X); grid on; title(sprintf('Spectrum of samples, fs = %d Hz', fs)); xlabel('f (Hz)');
    [~, idx] = max(X); fprintf('fs = %d Hz, apparent peak at %.1f Hz\n', fs, f(idx));
end
save_fig(f2, 'exp07_aliasing_spectrum.png');

% ---- local function: normalised sinc without the Signal Processing Toolbox ----
function y = sinc_fn(x)
    y = ones(size(x));
    nz = x ~= 0;
    y(nz) = sin(pi*x(nz)) ./ (pi*x(nz));
end

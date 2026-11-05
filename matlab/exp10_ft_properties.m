% Experiment 10: Numerical verification of Fourier transform properties
clc; clear; close all;
N = 256; n = 0:N-1;
rng(0);
x1 = randn(1, N); x2 = randn(1, N);
names = {}; errs = [];
rev = mod(-n, N) + 1;           % index map for x[(-n) mod N]

a = 2.5; b = -1.3;
[names, errs] = check(names, errs, 'Linearity', fft(a*x1 + b*x2), a*fft(x1) + b*fft(x2));

m = 17;
[names, errs] = check(names, errs, 'Circular time shift', fft(circshift(x1, m)), fft(x1) .* exp(-1j*2*pi*n*m/N));

k0 = 9;
[names, errs] = check(names, errs, 'Frequency shift (modulation)', fft(x1 .* exp(1j*2*pi*k0*n/N)), circshift(fft(x1), k0));

X1r = fft(x1);
[names, errs] = check(names, errs, 'Time reversal', fft(x1(rev)), X1r(rev));

z = x1 + 1j*x2; Z = fft(z);
[names, errs] = check(names, errs, 'Conjugation', fft(conj(z)), conj(Z(rev)));

circ = real(ifft(fft(x1) .* fft(x2)));
direct = zeros(1, N);
for mm = n
    direct(mm+1) = sum(x1 .* x2(mod(mm - n, N) + 1));
end
[names, errs] = check(names, errs, 'Convolution (time -> product)', circ, direct);

X1 = fft(x1); X2 = fft(x2); conv_f = zeros(1, N);
for kk = n
    conv_f(kk+1) = sum(X1 .* X2(mod(kk - n, N) + 1)) / N;
end
[names, errs] = check(names, errs, 'Multiplication (time -> conv)', fft(x1 .* x2), conv_f);

[names, errs] = check(names, errs, 'Parseval (energy)', sum(abs(x1).^2), sum(abs(fft(x1)).^2)/N);
[names, errs] = check(names, errs, 'Conjugate symmetry (real x)', fft(x1), conj(X1(rev)));

sig = exp(-0.5*((n-100)/8).^2);
f1 = figure('Position', [100 100 800 600]);
S0 = fft(sig); S1 = fft(circshift(sig, 30));
subplot(2,1,1); plot(abs(S0(1:40))); hold on; plot(abs(S1(1:40)), '--'); grid on;
title('Magnitude is unchanged by a time shift'); xlabel('k'); legend('original', 'shifted by 30');
p0 = unwrap(angle(S0)); p1 = unwrap(angle(S1));
subplot(2,1,2); plot(p0(1:40)); hold on; plot(p1(1:40), '--'); grid on;
title('Phase changes linearly with shift'); xlabel('k'); ylabel('rad'); legend('original', 'shifted by 30');
save_fig(f1, 'exp10_time_shift_property.png');

f2 = figure('Position', [100 100 800 400]);
bar(max(errs, 1e-17)); set(gca, 'YScale', 'log', 'XTick', 1:numel(names), 'XTickLabel', names, 'XTickLabelRotation', 35);
title('Max error per property'); ylabel('error');
save_fig(f2, 'exp10_property_errors.png');

% ---- local function (must be at end of a script file) ----
function [names, errs] = check(names, errs, name, lhs, rhs)
    e = max(abs(lhs(:) - rhs(:)));
    names{end+1} = name; errs(end+1) = e;
    if e < 1e-9, s = 'VERIFIED'; else, s = 'FAILED'; end
    fprintf('%-32s max error = %.2e   %s\n', name, e, s);
end

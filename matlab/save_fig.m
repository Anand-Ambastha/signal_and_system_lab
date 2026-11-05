function save_fig(fig, name)
% SAVE_FIG  Save a figure into ../outputs/matlab/ (created if missing).
    here = fileparts(mfilename('fullpath'));
    out = fullfile(here, '..', 'outputs', 'matlab');
    if ~exist(out, 'dir'), mkdir(out); end
    saveas(fig, fullfile(out, name));
    fprintf('saved %s\n', fullfile(out, name));
end

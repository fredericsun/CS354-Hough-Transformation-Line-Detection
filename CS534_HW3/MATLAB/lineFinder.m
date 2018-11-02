function line_detected_img = lineFinder(orig_img, hough_img, hough_threshold)
fh = figure; imshow(orig_img);
hold on;

most_vote = max(hough_img(:));

% balance the threshold value
threshold = hough_threshold * most_vote;

[row, col] = size(hough_img);

% construct a array to store valid (rho, theta)
container = zeros(row*col, 2);
index = 0;

for i = 1 : row % i is rho
    for j = 1 : col % j is theta
        if hough_img(i, j) > threshold
            index = index + 1;
            container(index, :) = [i-row/2, j];
        end
    end
end

% loop through all valid (rho, theta)
for j = 1 : index
    rho = container(j, 1);
    theta = container(j, 2);
    x = [1, row/2];
    y = (x * sin(theta * pi / 180) / cos(theta * pi / 180)) + rho/cos(theta * pi / 180);
    hold on;line(x, y, 'LineWidth', 1, 'Color', 'r');
end

line_detected_img = saveAnnotatedImg(fh);



function annotated_img = saveAnnotatedImg(fh)
figure(fh); % Shift the focus back to the figure fh

% The figure needs to be undocked
set(fh, 'WindowStyle', 'normal');

% The following two lines just to make the figure true size to the
% displayed image. The reason will become clear later.
img = getimage(fh);
truesize(fh, [size(img, 1), size(img, 2)]);

% getframe does a screen capture of the figure window, as a result, the
% displayed figure has to be in true size. 
frame = getframe(fh);
frame = getframe(fh);
pause(0.5); 
% Because getframe tries to perform a screen capture. it somehow 
% has some platform depend issues. we should calling
% getframe twice in a row and adding a pause afterwards make getframe work
% as expected. This is just a walkaround. 
annotated_img = frame.cdata;

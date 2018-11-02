function hough_img = generateHoughAccumulator(img, theta_num_bins, rho_num_bins)
% define the range of theta and rho by number of bins
rhoRange = (-rho_num_bins : rho_num_bins);
thetaRange = (0 : theta_num_bins);

% implement HoughAccumulator and initialize all the position to 0
houghaccumulator = zeros(numel(rhoRange) - 1, numel(thetaRange) - 1);

% get the information of image pixel
[row, col] = size(img);

% loop through all the pixel in the image
for i = 1 : row % i is y
    for j = 1 : col% j is x
        % determine the edge points
        if img(i, j) > 0 
            % loop through all possible theta value
            for theta = 1 : numel(thetaRange) - 1
                rho = i * cos(theta * pi / 180) - j * sin(theta * pi / 180);
                % construct index in houghaccumulator 
                index_rho = round(rho + (numel(rhoRange)-1)/2);
                houghaccumulator(index_rho, theta) = houghaccumulator(index_rho, theta) + 1;
            end
        end
    end
end
hough_img = houghaccumulator;
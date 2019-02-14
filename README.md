Pathfinder

This Python3 script takes as input a map with only black and white pixels. It then accepts two specific black points as inputs, and attempts to find the shortest path between them, where a path consists only of black pixels.

This is being developed as a project for BITS Apogee 2019. It makes use of what is known as Lee algorithm, with successive iterations, points, starting from one endpoint of the path, are labelled with their distance from that point, till the other end is reached. The path itself is then obtained by starting at this last point, then backtracking to points with a distance of one less than the current point.

An improvement is made, wherein counting starts from both ends simultaneously, with a view to reduce points considered, and halve the total number of iterations (though the reduced number of iterations does not directly translate to faster results).

It should not be difficult to scale this up to an arbitrary number of dimensions, and replace the binary nature of points with varying degrees of 'passability'.
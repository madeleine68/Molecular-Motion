import matplotlib.pyplot as plt 

from random_walk import RandomWalk 

# Keep making new walks,as long as the program is active.
while True:
	# Make a random walk
	rw = RandomWalk()
	rw.fill_walk()

	# Plot the points in the walk 
	plt.style.use('classic')
	fig, ax = plt.subplots(figsize = (15,9))
	point_numbers = range(rw.num_points)
	ax.plot(rw.x_values, rw.y_values, linewidth = 0.5, zorder = 1)
	# Emphasize the first and the last points.
	ax.scatter(0, 0, c = 'red', edgecolors = 'black', s = 200, zorder = 2)
	ax.scatter(rw.x_values[-1], rw.y_values[-1], c = 'yellow', edgecolors = 'black',
		s = 200, zorder = 2)

	# Remove the axis.
	ax.get_xaxis().set_visible(False)
	ax.get_yaxis().set_visible(False)


	plt.show()
	keep_running = input("make another walk? (y/n): ")
	if keep_running == n:
		break

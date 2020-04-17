from skimage.measure import compare_ssim as ssim
import matplotlib.pyplot as plt
import numpy as np
import cv2

# Import the images
# First image is whats going to be compared to the other piece images
Compare = cv2.imread("Chesspiece2.png")
#The next images are all reference images
King = cv2.imread("King.png")
Queen = cv2.imread("Queen.png")
Pawn = cv2.imread("Pawn.png")


# Convert all of the images to grayscale
Compare = cv2.cvtColor(Compare, cv2.COLOR_BGR2GRAY)
King = cv2.cvtColor(King, cv2.COLOR_BGR2GRAY)
Queen = cv2.cvtColor(Queen, cv2.COLOR_BGR2GRAY)
Pawn = cv2.cvtColor(Pawn, cv2.COLOR_BGR2GRAY)



Pieces = [King, Queen, Pawn] # Store all pieces in an array to compare against
PieceNames = ['King', 'Queen', 'Pawn'] # So we can rematch array index to piece name

def determinePiece( imageA, Pieces ): # Takes unknown piece and array of all possible pieces
    scores = [] # Keep track of simmilarity scores
    for idx, TestPiece in enumerate(Pieces):
        scores.append( ssim(imageA, TestPiece) ) # Add the simmilarity of each to the scores array
    return np.argmax(scores) # return the index of the piece with the closest simmilarity

matchIndex = determinePiece(Compare, Pieces) # put in a variable


#comparing function and setting up the windows
def compare_images(imageA, imageB, title):
	s = ssim(imageA, imageB)	#Calling the ssim method to compute the comarison/comares the images and creates a similarity percentage
	
	if s > 0.95:
		print ('Match')
		print("Compare.png is: " + PieceNames[matchIndex] ) # print and match index back to piece name
	else:
		
		print('No Match')
		
	# Sets up the window, adds the similarity amount to  the window
	fig = plt.figure(title)
	plt.suptitle("Similarity : %.3f" % (s))

	# Placing the 'imageA' in the desired position in the window
	ax = fig.add_subplot(1, 2, 1)
	plt.imshow(imageA, cmap = plt.cm.gray)
	plt.axis("off")

	# Placing the 'imageB' in the desired position in the window
	ax = fig.add_subplot(1, 2, 2)
	plt.imshow(imageB, cmap = plt.cm.gray)
	plt.axis("off")

	# Outputs the images to the window
	plt.show()

# Calls the comparing function and performs it on the desried images
#Each time the 'Compare' image is tested against the chess pieces
compare_images(Compare, King, "Compare vs. King")
compare_images(Compare, Queen, "Compare vs. Queen")
compare_images(Compare, Pawn, "Compare vs. Pawn")
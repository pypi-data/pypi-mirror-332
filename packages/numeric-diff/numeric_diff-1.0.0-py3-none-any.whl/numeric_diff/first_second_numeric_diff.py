class FirstSecondNumericDiff:

#########################################################################################################################
################################################### CONSTRUCTOR #########################################################
#########################################################################################################################

	# Builds the object
	# params: x_data, y_data, order, method
	def __init__(self, x_data, y_data, order, method):

		self.__validate_x_data_type(x_data)
		self.__validate_y_data_type(y_data)
		self.__validate_x_data_y_data_same_length(x_data, y_data)
		self.__validate_data_length(x_data)
		self.__validate_elements_type(x_data, y_data)
		self.__validate_order(order)
		self.__validate_method(method)
		self.__validate_first_order_central_method_length(x_data, order, method)

		self.__x_data_output = []
		self.__y_data_output = []

		self.__first_second_numeric_differentiation(x_data, y_data, order, method)

#########################################################################################################################
###################################################### METHODS ##########################################################
#########################################################################################################################

	# Validates if the x_data has type list, ndarray, set, tuple
	# Params: x_data 
	# Raises error if not
	def __validate_x_data_type(self, x_data):

		x_data_type = type(x_data).__name__

		if not ( x_data_type == 'list' or x_data_type == 'ndarray' or x_data_type == 'tuple' or x_data_type == 'set' ):

			raise Exception("invalid 'x_data' input type: " + x_data_type)

	# Validates if the y_data has type list, ndarray, set, tuple
	# Params = y_data
	# Raises error if not
	def __validate_y_data_type(self, y_data):

		y_data_type = type(y_data).__name__

		if not ( y_data_type == 'list' or y_data_type == 'ndarray' or y_data_type == 'tuple' or y_data_type == 'set' ):

			raise Exception("invalid 'y_data' input type: " + y_data_type)

	# Validates if the x_data and y_data have the same length
	# Params: x_data (list, ndarray, set, tuple), y_data (list, ndarray, set, tuple)
	# Raises error if not
	def __validate_x_data_y_data_same_length(self, x_data, y_data):

		if len(x_data) != len(y_data):

			raise Exception("'x_data' and 'y_data' must have the same length")

	# Validates if the x_data and y_data have valid length
	# Params: x_data (list, ndarray, set, tuple), y_data (list, ndarray, set, tuple)
	# Raises error if not
	def __validate_data_length(self, x_data):

		if len(x_data) <= 1:

			raise Exception("invalid length of data:" + str( len(x_data) ))

	# Validates if elements in x_data and y_data have valid float values (nan and inf are invalid)
	# Params: x_data (list, ndarray, set, tuple), y_data (list, ndarray, set, tuple)
	# Raises error if not
	def __validate_elements_type(self, x_data, y_data):
		
		list( map(int, x_data) )
		list( map(int, y_data) )


	# Validates if order has valid type and is equal to one of the valid options
	# Params: order
	# Raises error if not
	def __validate_order(self, order):

		if type(order).__name__ != 'str':

			raise Exception("invalid 'order' input type:" + type(order).__name__)

		else:

			order = order.lower()

			if not (order == 'first' or order == 'second'):

				raise Exception("unknown 'order': " + order)

	# Validates if method has valid type and is equal to one of the valid options
	# Params: method
	# Raises error if not
	def __validate_method(self, method):

		if type(method).__name__ != 'str':

			raise Exception("invalid 'method' input type: " + type(method).__name__)

		else:

			method = method.lower()

			if not (method == 'forward' or method == 'backward' or method == 'central'):

				raise Exception("unknown 'method': " + method)

	# Validates if the length of data is valid for a first-order derivative with central difference
	# Params: x_data (list, ndarray, set, tuple), order (str), method (str)
	# Raises error if not
	def __validate_first_order_central_method_length(self, x_data, order, method):

		order = order.lower()
		method = method.lower()

		if order == 'first' and method == 'central' and len(x_data) < 3:

			raise Exception("central difference for first-order derivative needs at least three points")

	# Starts the numeric differentiation of the data inserted by the user
	# Params: x_data (list, ndarray, set, tuple), y_data (list, ndarray, set, tuple), 
	# order (str), method(str)
	# Returns: two lists with the numeric differentiation data: 
	# self.__x_data_output (list(float)), self__y_data_output (list(float))
	def __first_second_numeric_differentiation(self, x_data, y_data, order, method):

		x_data = list( map(float, x_data) )
		y_data = list( map(float, y_data) )

		order = order.lower()

		match order:

			case 'first':

				self.__x_data_output, self.__y_data_output = self.__first_order_differentiation(x_data, y_data, method)

			case 'second':

				if len(x_data) < 3:

					raise Exception("second-order derivative needs at least three points")

				else:

					self.__x_data_output, self.__y_data_output = self.__second_order_differentiation(x_data, y_data, method)

	# Starts the first-order numeric differentiation of the data inserted by the user
	# Params: x_data (list(float)), y_data (list(float)), method(str)
	# Returns: two lists with the first-order numeric differentiation data: 
	# x_1d_data (list(float)), y_1d_data (list(float))
	def __first_order_differentiation(self, x_data, y_data, method):

		method = method.lower()

		match method:

			case 'forward':

				x_1d_data, y_1d_data = self.__forward_diff_first_order(x_data, y_data)

			case 'backward':

				x_1d_data, y_1d_data = self.__backward_diff_first_order(x_data, y_data)

			case 'central':

				x_1d_data, y_1d_data = self.__central_diff_first_order(x_data, y_data)				

		return x_1d_data, y_1d_data

	# Starts the forward difference for first-order numeric differentiation of the data inserted by the user
	# Params: x_data ((list(float))), y_data ((list(float)))
	# Returns: two lists with the first-order numeric differentiation data: 
	# x_1d_f_data (list(float)), y_1d_f_data (list(float))
	def __forward_diff_first_order(self, x_data, y_data):
    
		warning = False

		y_1d_f_data = []

		for i in range(0, len(x_data) - 1):

			h_i = x_data[i + 1] - x_data[i]

			if i != 0:

				if round(h_i, 7) != round(h_i_minus_1, 7) and not warning:

					print("WARNING. Step size is not constant. Accuracy may be compromised")

					warning = True

				else:

					pass

			else:

				pass 

			y_1d_f_i = (y_data[i + 1] - y_data[i]) / h_i
	        
			y_1d_f_data.append(y_1d_f_i)

			h_i_minus_1 = h_i

		x_data.pop()

		x_1d_f_data = x_data.copy()

		return x_1d_f_data, y_1d_f_data

	# Starts the backward difference for first-order numeric differentiation of the data inserted by the user
	# Params: x_data ((list(float))), y_data ((list(float)))
	# Returns: two lists with the first-order numeric differentiation data: 
	# x_1d_b_data (list(float)), y_1d_b_data (list(float))
	def __backward_diff_first_order(self, x_data, y_data):
    
		warning = False

		y_1d_b_data = []

		for i in range(1, len(x_data)):

			h_i = x_data[i] - x_data[i - 1]

			if i != 1:

				if round(h_i, 7) != round(h_i_minus_1, 7) and not warning:

					print("WARNING. Step size is not constant. Accuracy may be compromised")

					warning = True

				else:

					pass

			else:

				pass

			y_1d_b_i = (y_data[i] - y_data[i - 1]) / h_i
	        
			y_1d_b_data.append(y_1d_b_i)

			h_i_minus_1 = h_i

		x_data.pop(0)

		x_1d_b_data = x_data.copy()

		return x_1d_b_data, y_1d_b_data

	# Starts the central difference for first-order numeric differentiation of the data inserted by the user
	# Params: x_data ((list(float))), y_data ((list(float)))
	# Returns: two lists with the first-order numeric differentiation data: 
	# x_1d_c_data (list(float)), y_1d_c_data (list(float))
	def __central_diff_first_order(self, x_data, y_data):
    
		warning = False

		y_1d_c_data = []

		for i in range(1, len(x_data) - 1):
	        
			h_i = ( x_data[i + 1] - x_data[i - 1] ) / 2

			if round( x_data[i + 1] - x_data[i], 7 ) != round( x_data[i] - x_data[i - 1], 7 ) and not warning:

				print("WARNING. Step size is not constant. Accuracy may be compromised")

				warning = True

			else:

				pass

			y_1d_c_i = (y_data[i + 1] - y_data[i - 1]) / (2 * h_i)
	        
			y_1d_c_data.append(y_1d_c_i)

		x_data.pop(0)
		x_data.pop()

		x_1d_c_data = x_data.copy()

		return x_1d_c_data, y_1d_c_data

	# Starts the second-order numeric differentiation of the data inserted by the user
	# Params: x_data (list(float)), y_data (list(float)), method(str)
	# Returns: two lists with the second-order numeric differentiation data: 
	# x_2d_data (list(float)), y_2d_data (list(float))
	def __second_order_differentiation(self, x_data, y_data, method):

		method = method.lower()

		match method:

			case 'forward':

				x_2d_data, y_2d_data = self.__forward_diff_second_order(x_data, y_data)

			case 'backward':

				x_2d_data, y_2d_data = self.__backward_diff_second_order(x_data, y_data)

			case 'central':

				x_2d_data, y_2d_data = self.__central_diff_second_order(x_data, y_data)
	            
		return x_2d_data, y_2d_data

	# Starts the forward difference for second-order numeric differentiation of the data inserted by the user
	# Params: x_data ((list(float))), y_data ((list(float)))
	# Returns: two lists with the second-order numeric differentiation data: 
	# x_2d_f_data (list(float)), y_2d_f_data (list(float))
	def __forward_diff_second_order(self, x_data, y_data):
    
		warning = False

		y_2d_f_data = []

		for i in range(0, len(x_data) - 2):
	        
			h_i = ( x_data[i + 2] - x_data[i] ) / 2

			if round( x_data[i + 2] - x_data[i + 1], 7 ) != round( x_data[i + 1] - x_data[i], 7 ) and not warning:

				print("WARNING. Step size is not constant. Accuracy may be compromised")

				warning = True

			else:

				pass

			y_2d_f_i = ( y_data[i + 2] - (2 * y_data[i + 1]) + y_data[i] ) / ( h_i ** 2 )
	        
			y_2d_f_data.append(y_2d_f_i)

		x_data.pop()
		x_data.pop()

		x_2d_f_data = x_data.copy()

		return x_2d_f_data, y_2d_f_data

	# Starts the backward difference for second-order numeric differentiation of the data inserted by the user
	# Params: x_data ((list(float))), y_data ((list(float)))
	# Returns: two lists with the second-order numeric differentiation data: 
	# x_2d_b_data (list(float)), y_2d_b_data (list(float))
	def __backward_diff_second_order(self, x_data, y_data):
    
		warning = False

		y_2d_b_data = []

		for i in range(2, len(x_data)):
	        
			h_i = ( x_data[i] - x_data[i - 2] ) / 2

			if round( x_data[i] - x_data[i - 1], 7 ) != round( x_data[i - 1] - x_data[i - 2], 7 ) and not warning:

				print("WARNING. Step size is not constant. Accuracy may be compromised")

				warning = True

			else:

				pass

			y_2d_b_i = ( y_data[i] - (2 * y_data[i - 1]) + y_data[i - 2] ) / ( h_i ** 2 )
	        
			y_2d_b_data.append(y_2d_b_i)

		x_data.pop(0)
		x_data.pop(0)

		x_2d_b_data = x_data.copy()

		return x_2d_b_data, y_2d_b_data

	# Starts the central difference for second-order numeric differentiation of the data inserted by the user
	# Params: x_data ((list(float))), y_data ((list(float)))
	# Returns: two lists with the second-order numeric differentiation data: 
	# x_2d_c_data (list(float)), y_2d_c_data (list(float))
	def __central_diff_second_order(self, x_data, y_data):
    
		warning = False

		y_2d_c_data = []

		for i in range(1, len(x_data) - 1):
	        
			h_i = ( x_data[i + 1] - x_data[i - 1] ) / 2

			if round( x_data[i + 1] - x_data[i], 7 ) != round( x_data[i] - x_data[i - 1], 7 ) and not warning:

				print("WARNING. Step size is not constant. Accuracy may be compromised")

				warning = True

			else:

				pass

			y_2d_c_i = (y_data[i + 1] + y_data[i - 1] - (2 * y_data[i]) ) / (h_i ** 2)
	        
			y_2d_c_data.append(y_2d_c_i)

		x_data.pop(0)
		x_data.pop()

		x_2d_c_data = x_data.copy()

		return x_2d_c_data, y_2d_c_data

#########################################################################################################################
###################################################### CALLABLE #########################################################
#########################################################################################################################

	# Allows the instance of the class to be called
	# Returns: two lists with the numeric differentiation data:
	# self.__x_data_output (list(float)), self__y_data_output (list(float))
	def __call__(self):

		return self.__x_data_output, self.__y_data_output
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

from numpy import array
from numpy import hstack
from tensorflow.keras import Sequential
from tensorflow.keras.layers import LSTM, Dense, RepeatVector, TimeDistributed

# split a multivariate sequence into samples
def split_sequences(sequences, n_steps_in, n_steps_out):
	X, y = list(), list()
	for i in range(len(sequences)):
		# find the end of this pattern
		end_ix = i + n_steps_in
		out_end_ix = end_ix + n_steps_out
		# check if we are beyond the dataset
		if out_end_ix > len(sequences):
			break
		# gather input and output parts of the pattern
		seq_x, seq_y = sequences[i:end_ix, :], sequences[end_ix:out_end_ix, :]
		X.append(seq_x)
		y.append(seq_y)
	return array(X), array(y)


def LTSM_model(in_seq1, in_seq2):
	out_seq = array([in_seq1[i]+in_seq2[i] for i in range(len(in_seq1))])
	# convert to [rows, columns] structure
	in_seq1 = in_seq1.reshape((len(in_seq1), 1))
	in_seq2 = in_seq2.reshape((len(in_seq2), 1))
	out_seq = out_seq.reshape((len(out_seq), 1))
	# horizontally stack columns
	dataset = hstack((in_seq1, in_seq2, out_seq))
	# choose a number of time steps
	n_steps_in, n_steps_out = 3, 4
	# covert into input/output
	X, y = split_sequences(dataset, n_steps_in, n_steps_out)
	# the dataset knows the number of features, e.g. 2
	n_features = X.shape[2]
	# define model
	model = Sequential()
	model.add(LSTM(200, activation='relu', input_shape=(n_steps_in, n_features)))
	model.add(RepeatVector(n_steps_out))
	model.add(LSTM(200, activation='relu', return_sequences=True))
	model.add(TimeDistributed(Dense(n_features)))
	model.compile(optimizer='adam', loss='mse')
	# fit model
	model.fit(X, y, epochs=300, verbose=0)
	# demonstrate prediction
	x_input = array(dataset[-3:])
	x_input = x_input.reshape((1, n_steps_in, n_features))
	yhat = model.predict(x_input, verbose=0)

	print(yhat)
	woodside_forecast = yhat[0][0:4, 1]
	return woodside_forecast



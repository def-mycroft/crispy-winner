"""Contains functions for pickling and unpickling objects"""
import pickle

def pickle_object(input_object, filename, test=True):
    """Given an object, writes it to a pickle file"""
    filename = '%s.pickle' % filename
    with open(filename, 'wb') as handle:
        pickle.dump(input_object, handle, protocol=pickle.HIGHEST_PROTOCOL)

    if test:

        # Load the pickle file that was just written and ensure it is the same
        with open(filename, 'rb') as handle:
            loaded_pickle = pickle.load(handle)

        # Display error message if pickles don't match
        if input_object != loaded_pickle:
            print('Error!! Dict loaded from pickle does not match original.')


def unpickle_object(input_filename):
    """Loads a pickled object"""
    input_filename = '%s.pickle' % input_filename
    with open(input_filename, 'rb') as handle:
        loaded_object = pickle.load(handle)
    return loaded_object


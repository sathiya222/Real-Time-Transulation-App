# beam_search_decoder.py
import numpy as np

def beam_search_decoder(predictions, beam_width):
    sequences = [[list(), 1.0]]
    for row in predictions:
        all_candidates = list()
        for seq, score in sequences:
            for j in range(len(row)):
                if row[j] > 0:  # Avoid log(0) issue
                    candidate = [seq + [j], score * -np.log(row[j])]
                    all_candidates.append(candidate)
                else:
                    candidate = [seq + [j], score]  # Assign the same score if probability is zero
                    all_candidates.append(candidate)
        ordered = sorted(all_candidates, key=lambda tup: tup[1])
        sequences = ordered[:beam_width]
    return sequences

# Example usage
if __name__ == "__main__":
    predictions = [
        [0.1, 0.4, 0.5],
        [0.3, 0.4, 0.3],
        [0.2, 0.3, 0.5]
    ]

    beam_width = 2
    result = beam_search_decoder(predictions, beam_width)
    print(result)

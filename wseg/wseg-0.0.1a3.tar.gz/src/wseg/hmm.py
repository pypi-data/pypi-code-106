import os
import sys
current_path = os.path.dirname(os.path.realpath(__file__))
sys.path.append(os.path.join(current_path,"libs"))

import HMM

def hmm_train(input_data,prob_start_file,prob_emit_file,prob_trans_file):
    return HMM.hmm_train(input_data,prob_start_file,prob_emit_file,prob_trans_file)

def hmm_cut(prob_start_file, prob_trans_file, prob_emit_file, test_str):
    result = HMM.hmm_cut_str(prob_start_file, prob_trans_file, prob_emit_file, test_str)
    return result
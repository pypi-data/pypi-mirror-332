import pandas as pd
import numpy as np
from dataclasses import dataclass
import pickle
from pathlib import Path
import fire
from importlib.resources import files
from scipy.spatial import KDTree


@dataclass
class RLModelBase:
    def compute_action_transition_proba(self, current_action=None):
        """
        Compute action transition probability matrix from episode transitions.
        
        Args:
            current_action: Optional[Union[int, str]] - Current action to compute transition probabilities for
            
        Returns:
            Union[dict, pd.DataFrame] - Transition probabilities or full transition matrix
        """
        try:
            # Load episode transitions
            episode_transitions = np.load(self.episodes_file, allow_pickle=True)
            
            # Extract action transitions
            action_transitions = [(t[1], episode_transitions[i + 1][1]) 
                                for i, t in enumerate(episode_transitions[:-1])]
            
            # Create DataFrame
            df_transitions = pd.DataFrame(action_transitions, columns=['current_action', 'next_action'])
            
            # Map action indices to names
            action_names = {0: 'go_long', 1: 'go_short', 2: 'do_nothing'}
            df_transitions['current_action'] = df_transitions['current_action'].map(action_names)
            df_transitions['next_action'] = df_transitions['next_action'].map(action_names)
            
            # Compute transition matrix
            transition_matrix = df_transitions.groupby(['current_action', 'next_action']).size().unstack(fill_value=0)
            
            # Normalize to get probabilities
            transition_matrix = transition_matrix.div(transition_matrix.sum(axis=1), axis=0)
            
            if current_action is not None:
                # Convert current_action to name if integer
                if isinstance(current_action, int):
                    current_action = action_names.get(current_action, current_action)
                
                # Check if current_action exists
                if current_action not in transition_matrix.index:
                    raise ValueError(f"Current action '{current_action}' not found in transition matrix")
                
                return transition_matrix.loc[current_action].to_dict()
                
            return transition_matrix
            
        except Exception as e:
            print(f"Error computing transition probabilities: {e}")
            return {} if current_action is not None else pd.DataFrame()


@dataclass
class RLmodel_small(RLModelBase):
    sma_05: float
    sma_07: float
    sma_25: float
    sma_compare: int
    is_short: int

    model_file_path: str = f'{Path(__file__).resolve().parent}/small_q_table.npy'
    state_index_file: str = f'{Path(__file__).resolve().parent}/small_state_to_index.npy'
    episodes_file: str = None

    def __post_init__(self):
        self.episodes_file = f'{Path(__file__).resolve().parent}/small_epitrans.npy'
    def load_qtable(self):
        with open(self.model_file_path, "rb") as f:
            q_table = np.load(f)
        return q_table

    def load_state_index(self):
        with open(self.state_index_file, "rb") as f:
            state_to_index = np.load(f, allow_pickle=True).item()
        return state_to_index

    def load_action_mapping(self):
        action_mapping = {"go_long": 0, "go_short": 1, "do_nothing": 2}
        return action_mapping

    def prep_state(self):
        state = np.array([[self.sma_05, self.sma_07, self.sma_25, self.sma_compare, self.is_short]])
        if not np.all(np.isfinite(state)):
            state = np.nan_to_num(state, nan=0.0, posinf=0.0, neginf=0.0)
        return state

    def predict_action(self):
        state = self.prep_state()
        loaded_qtable = self.load_qtable()
        loaded_state_to_index = self.load_state_index()
        loaded_mapping = self.load_action_mapping()


        state_tuple = tuple(state.flatten())
        state_index = loaded_state_to_index.get(state_tuple, -1)
        if not state_index == -1:
            try:
                q_values = loaded_qtable[state_index]
            except ValueError as e:
                print(e)
        else:
            # Create a KDTree from the states in the loaded_state_to_index mapping
            state_tuples = list(loaded_state_to_index.keys())
            kdtree = KDTree(state_tuples)

            # Find the nearest neighbor to the current state
            distance, index = kdtree.query(state.flatten())
            nearest_state_tuple = state_tuples[index]
            new_state_index = loaded_state_to_index[nearest_state_tuple]
            q_values = loaded_qtable[new_state_index]
            #raise ValueError("State not found in the state index mapping.")
        # Compute probabilities using softmax

        def softmax(x):
            exp_x = np.exp(x - np.max(x))  # Subtract max for numerical stability
            return exp_x / np.sum(exp_x)

        confidence = softmax(q_values)

        # Map probabilities to action names
        action_confidence = {
            action: confidence[index] for action, index in loaded_mapping.items()
        }
        best_action_index = np.argmax(q_values)

        action = [action for action, index in loaded_mapping.items() if index == best_action_index][0]
        # Get transition probabilities for the chosen action
        trans_proba = self.compute_action_transition_proba(current_action=action)
        trans_action = max(trans_proba.items(), key=lambda x: x[1])[0] if trans_proba else None

        results_dict = {
            "raw_state": state,
            "state_tuple": state_tuple,
            "best_action_index": best_action_index,
            "action": action,
            "confidence": action_confidence,
            "trans_proba": trans_proba,
            "trans_action": trans_action
        }
        return results_dict

@dataclass
class RLmodel_large(RLModelBase):
    opening: float
    high: float
    ema_26: float
    ema_12: float
    low: float
    mean_grad_hist: float
    close: float
    volume: float
    sma_25: float
    long_jcrosk: float
    short_kdj: int
    sma_compare: int
    ask: float
    bid: float
    is_short: int

    model_file_path: str = f'{Path(__file__).resolve().parent}/large_q_table.npy'
    state_index_file: str = f'{Path(__file__).resolve().parent}/large_state_to_index.npy'
    episodes_file: str = None

    def __post_init__(self):
        self.episodes_file = f'{Path(__file__).resolve().parent}/large_epitrans.npy'

    def load_qtable(self):
        with open(self.model_file_path, "rb") as f:
            q_table = np.load(f)
        return q_table

    def load_state_index(self):
        with open(self.state_index_file, "rb") as f:
            state_to_index = np.load(f, allow_pickle=True).item()
        return state_to_index

    def load_action_mapping(self):
        action_mapping = {"go_long": 0, "go_short": 1, "do_nothing": 2}
        return action_mapping

    def prep_state(self):
        state = np.array([[self.opening, self.high, \
                          self.ema_26, self.ema_12, self.low, self.mean_grad_hist, \
                          self.close, self.volume, self.sma_25, self.long_jcrosk, \
                          self.short_kdj, self.sma_compare, self.ask, self.bid, self.is_short]]
                    )

        # Check for NaN or Inf values in the state
        if not np.all(np.isfinite(state)):
            state = np.nan_to_num(state, nan=0.0, posinf=0.0, neginf=0.0)

        return state

    def predict_action(self):
        state = self.prep_state()
        loaded_qtable = self.load_qtable()
        loaded_state_to_index = self.load_state_index()
        loaded_mapping = self.load_action_mapping()


        state_tuple = tuple(state.flatten())
        state_index = loaded_state_to_index.get(state_tuple, -1)
        if not state_index == -1:
            try:
                q_values = loaded_qtable[state_index]
            except ValueError as e:
                print(e)
        else:
            # Create a KDTree from the states in the loaded_state_to_index mapping
            state_tuples = list(loaded_state_to_index.keys())
            kdtree = KDTree(state_tuples)

            # Find the nearest neighbor to the current state
            distance, index = kdtree.query(state.flatten())
            nearest_state_tuple = state_tuples[index]
            new_state_index = loaded_state_to_index[nearest_state_tuple]
            q_values = loaded_qtable[new_state_index]
            #raise ValueError("State not found in the state index mapping.")
        # Compute probabilities using softmax

        def softmax(x):
            exp_x = np.exp(x - np.max(x))  # Subtract max for numerical stability
            return exp_x / np.sum(exp_x)

        confidence = softmax(q_values)

        # Map probabilities to action names
        action_confidence = {
            action: confidence[index] for action, index in loaded_mapping.items()
        }
        best_action_index = np.argmax(q_values)

        action = [action for action, index in loaded_mapping.items() if index == best_action_index][0]
        # Get transition probabilities for the chosen action
        trans_proba = self.compute_action_transition_proba(current_action=action)
        trans_action = max(trans_proba.items(), key=lambda x: x[1])[0] if trans_proba else None

        results_dict = {
            "raw_state": state,
            "state_tuple": state_tuple,
            "best_action_index": best_action_index,
            "action": action,
            "confidence": action_confidence,
            "trans_proba": trans_proba,
            "trans_action": trans_action
        }
        return results_dict

@dataclass
class RLmodel_bids(RLModelBase):
    ask: float
    bid: float
    sma_compare: int
    is_short: int

    model_file_path: str = f'{Path(__file__).resolve().parent}/bids_q_table.npy'
    state_index_file: str = f'{Path(__file__).resolve().parent}/bids_state_to_index.npy'
    episodes_file: str = None

    def __post_init__(self):
        self.episodes_file = f'{Path(__file__).resolve().parent}/bids_epitrans.npy'

    def load_qtable(self):
        with open(self.model_file_path, "rb") as f:
            q_table = np.load(f)
        return q_table

    def load_state_index(self):
        with open(self.state_index_file, "rb") as f:
            state_to_index = np.load(f, allow_pickle=True).item()
        return state_to_index

    def load_action_mapping(self):
        action_mapping = {"go_long": 0, "go_short": 1, "do_nothing": 2}
        return action_mapping

    def prep_state(self):
        state = np.array([[self.ask, self.bid, self.sma_compare, self.is_short]])

        # Check for NaN or Inf values in the state
        if not np.all(np.isfinite(state)):
            state = np.nan_to_num(state, nan=0.0, posinf=0.0, neginf=0.0)

        return state

    def predict_action(self):
        state = self.prep_state()
        loaded_qtable = self.load_qtable()
        loaded_state_to_index = self.load_state_index()
        loaded_mapping = self.load_action_mapping()


        state_tuple = tuple(state.flatten())
        state_index = loaded_state_to_index.get(state_tuple, -1)
        if not state_index == -1:
            try:
                q_values = loaded_qtable[state_index]
            except ValueError as e:
                print(e)
        else:
            # Create a KDTree from the states in the loaded_state_to_index mapping
            state_tuples = list(loaded_state_to_index.keys())
            kdtree = KDTree(state_tuples)

            # Find the nearest neighbor to the current state
            distance, index = kdtree.query(state.flatten())
            nearest_state_tuple = state_tuples[index]
            new_state_index = loaded_state_to_index[nearest_state_tuple]
            q_values = loaded_qtable[new_state_index]
            #raise ValueError("State not found in the state index mapping.")
        
        # Compute probabilities using softmax
        def softmax(x):
            exp_x = np.exp(x - np.max(x))  # Subtract max for numerical stability
            return exp_x / np.sum(exp_x)

        confidence = softmax(q_values)

        # Map probabilities to action names
        action_confidence = {
            action: confidence[index] for action, index in loaded_mapping.items()
        }
        
        best_action_index = np.argmax(q_values)
        action = [action for action, index in loaded_mapping.items() if index == best_action_index][0]
        # Get transition probabilities for the chosen action
        trans_proba = self.compute_action_transition_proba(current_action=action)
        trans_action = max(trans_proba.items(), key=lambda x: x[1])[0] if trans_proba else None

        results_dict = {
            "raw_state": state,
            "state_tuple": state_tuple,
            "best_action_index": best_action_index,
            "action": action,
            "confidence": action_confidence,
            "trans_proba": trans_proba,
            "trans_action": trans_action
        }
        return results_dict


def main(model_type: str, sma_05: float = None, sma_07: float = None, 
         sma_25: float = None, sma_compare: int = None, is_short: int = None,
         opening: float = None, high: float = None, ema_26: float = None,
         ema_12: float = None, low: float = None, mean_grad_hist: float = None,
         close: float = None, volume: float = None, long_jcrosk: float = None,
         short_kdj: int = None, ask: float = None, bid: float = None):
    """
    Main function to handle command line interface.
    
    Args:
        model_type: str - Type of model to use ('small', 'large', or 'bids')
        ... (other parameters specific to each model)
    """
    if model_type.lower() == "small":
        if any(x is None for x in [sma_05, sma_07, sma_25, sma_compare, is_short]):
            raise ValueError("Small model requires: sma_05, sma_07, sma_25, sma_compare, is_short")
        model = RLmodel_small(
            sma_05=float(sma_05),
            sma_07=float(sma_07),
            sma_25=float(sma_25),
            sma_compare=int(sma_compare),
            is_short=int(is_short)
        )
    elif model_type.lower() == "large":
        # Check and create large model
        if any(x is None for x in [opening, high, ema_26, ema_12, low, mean_grad_hist,
                                 close, volume, sma_25, long_jcrosk, short_kdj,
                                 sma_compare, ask, bid, is_short]):
            raise ValueError("Large model requires all parameters")
        model = RLmodel_large(
            opening=float(opening),
            high=float(high),
            ema_26=float(ema_26),
            ema_12=float(ema_12),
            low=float(low),
            mean_grad_hist=float(mean_grad_hist),
            close=float(close),
            volume=float(volume),
            sma_25=float(sma_25),
            long_jcrosk=float(long_jcrosk),
            short_kdj=int(short_kdj),
            sma_compare=int(sma_compare),
            ask=float(ask),
            bid=float(bid),
            is_short=int(is_short)
        )
    elif model_type.lower() == "bids":
        if any(x is None for x in [ask, bid, sma_compare, is_short]):
            raise ValueError("Bids model requires: ask, bid, sma_compare, is_short")
        model = RLmodel_bids(
            ask=float(ask),
            bid=float(bid),
            sma_compare=int(sma_compare),
            is_short=int(is_short)
        )
    else:
        raise ValueError("Invalid model type. Choose 'small', 'large', or 'bids'")

    result = model.predict_action()
    print(result)
    return result

if __name__ == "__main__":
    fire.Fire(main)

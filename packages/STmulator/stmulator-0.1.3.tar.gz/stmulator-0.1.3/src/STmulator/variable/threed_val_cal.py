import numpy as np
import warnings
warnings.filterwarnings('ignore')
from scipy import sparse as sp
from scipy import stats
from .var_model_fit import fit_gig, calculate_aic
from .var_preprocess import extract_data, get_initial_params, fit_simple_ig
from .var_evaluation import evaluate_fit
from .var_sim_helper import assess_tail_discreteness, simulate_gig, interpolate_tail_data


class GIG_VarianceSimulator:
    def __init__(self):
        self.alpha = None
        self.beta = None
        self.theta = None
        self.k = None
        self.lambda_ = None
        self.threshold = None
        self.tail_data = None
        self.original_order = None
        self.original_data = np.array([])
        self.random_state = None
        self.model_type = None  # 'IG' or 'GIG'
        self.total_genes =  None

    def fit(self, adatas, percentile):
        """fit GIG and IG model"""
        try:
            all_variances = []
            for adata in adatas:
                if sp.issparse(adata.X):
                    variances = extract_data(adata.X.toarray())
                else:
                    variances = extract_data(adata.X)
                all_variances.extend(variances)
            
            self.original_data = np.array(all_variances)
            if not np.all(np.isfinite(self.original_data)):
                raise ValueError("Data contains non-finite values")

            self.original_order = np.argsort(self.original_data)
            sorted_data = np.sort(self.original_data)

            # simple IG fit
            ig_params = fit_simple_ig(sorted_data)

            best_score = 0
            best_evaluation = None
            chosen_threshold = None

            current_threshold = np.percentile(sorted_data, percentile)
            main_data = sorted_data[sorted_data <= current_threshold]
            tail_data = sorted_data[sorted_data > current_threshold]

            try:
                ig_aic = calculate_aic(-len(main_data) * np.log(stats.invgamma.pdf(main_data,
                                                                                ig_params['alpha'],
                                                                                scale=ig_params['scale'])).sum(), 2)

                # Pre-calculated the IG model; if it is good enough, we will choose it directly
                tem_main = stats.invgamma.rvs(ig_params['alpha'], scale=ig_params['scale'],
                                              size=len(main_data), random_state=self.random_state)
                tem_main = np.clip(tem_main, np.min(self.original_data), np.max(self.original_data))
                tem_main = np.sort(tem_main)
                tem_tail = np.sort(tail_data)

                tem_data = np.concatenate([tem_main, tem_tail])

                tem_evaluation = evaluate_fit(self.original_data, tem_data, percentile)
                # if the IG model is good enough, we will choose it directly
                if tem_evaluation["Correlation"] > 0.98 and tem_evaluation["KS Statistic"] < 0.05:
                    model_type = 'IG'
                    alpha = ig_params['alpha']
                    theta = ig_params['scale']
                    print("Choosing IG model in percentile, because is good enough", percentile)

                else:
                    # use IG model as initial guess
                    initial_guess = [ig_params['alpha'], 1, ig_params['scale'], 0.001, 0.001]
                    gig_params, gig_likelihood = fit_gig(main_data,initial_guess=initial_guess)
                    gig_aic = calculate_aic(gig_likelihood, 5)

                    if gig_aic < ig_aic:
                        model_type = 'IG'
                        alpha = ig_params['alpha']
                        theta = ig_params['scale']
                        
                    else:
                        model_type = 'GIG'
                        alpha = gig_params[0]
                        beta = gig_params[1]
                        theta = gig_params[2]
                        k = gig_params[3]
                        lambda_ = gig_params[4]
                       
                n_main = len(main_data)
                n_tail = len(tail_data)

                if model_type == 'IG':
                    new_main = stats.invgamma.rvs(alpha, scale=theta,
                                                  size=n_main, random_state=self.random_state)
                else:
                    new_main = simulate_gig(n_main, alpha, beta, theta, k, lambda_)

                # deal with tail data
                tail_type = assess_tail_discreteness(tail_data)
                if tail_type == 'discrete':
                    new_tail = self.random_state.choice(tail_data, size=n_tail, replace=True)
                else:
                    new_tail = interpolate_tail_data(tail_data, n_tail)

                # combine main and tail data
                new_samples = np.concatenate([new_main, new_tail])
                new_samples = np.clip(new_samples, np.min(self.original_data),
                                      np.max(self.original_data))

                evaluation = evaluate_fit(self.original_data, new_samples, percentile)

                score = (
                         evaluation["Relative Error"] +
                         evaluation["KS Statistic"] +
                         (1 - evaluation["Correlation"]))

                if score > best_score:
                    best_score = score
                    best_evaluation = evaluation
                    chosen_threshold = percentile
                    if model_type == 'IG':
                        self.alpha = alpha
                        self.theta = theta
                    else:
                        self.alpha = alpha
                        self.beta = beta
                        self.theta = theta
                        self.k = k
                        self.lambda_ = lambda_
                    self.model_type = model_type
                    self.threshold = chosen_threshold
                    self.tail_data = tail_data

            except Exception as e:
                raise
            if best_evaluation is None:
                raise ValueError("No valid fit found")

            return self, best_evaluation

        except Exception as e:
            print(f"Fitting failed: {str(e)}")
            # Fallback to simple IG
            ig_params = fit_simple_ig(self.original_data)
            self.model_type = 'IG'
            self.alpha = ig_params['alpha']
            self.theta = ig_params['scale']
            return self, {"Verdict": "Fallback to single component IG"}

    def simulate(self, n_samples ,tail_process=False):
        """simulate gene variances based on fitted model"""
        try:
            if self.threshold is None:
                print("Warning: Threshold is None, using default value of 95.")
                self.threshold = 95

            n_main = int(n_samples * self.threshold / 100)
            n_tail = n_samples - n_main

            # Generate main data
            if self.model_type == 'IG':
                new_main = stats.invgamma.rvs(self.alpha, scale=self.theta,
                                              size=n_main, random_state=self.random_state)
            else:
                new_main = simulate_gig(n_main, self.alpha, self.beta, self.theta, self.k, self.lambda_)

            # Generate tail data
            if tail_process:
                tail_type = assess_tail_discreteness(self.tail_data)
                if tail_type == 'discrete':
                    new_tail = self.random_state.choice(self.tail_data, size=n_tail, replace=True)
                else:
                    new_tail = interpolate_tail_data(self.tail_data, n_tail)
            else:
                # remain the same tail data
                new_tail = self.tail_data

            # Combine main and tail data
            new_samples = np.concatenate([new_main, new_tail])
            new_samples = np.clip(new_samples, np.min(self.original_data),
                                  np.max(self.original_data))
            new_samples = np.sort(new_samples)

            simulated_data = np.zeros_like(new_samples)
            simulated_data[self.original_order] = new_samples

            return simulated_data

        except Exception as e:
            return self.random_state.choice(self.original_data, size=n_samples, replace=True)

    def fit_and_simulate(self, adatas,n_samples, n_iterations=3,tail_process=False):
            self.total_genes = sum([adata.n_vars for adata in adatas])
            print(f"Starting fit and simulate process...")
            """fit and simulate gene variances(main process)"""
            best_overall_simulation = None
            best_overall_evaluation = None
            best_overall_score = float('-inf')
            best_overall_threshold = None
            best_overall_params = None
            # pre-defined thresholds
            thresholds = [95,90,96,99,98,97,92]
            best_threshold_evaluation = None  

            for threshold in thresholds:
                best_threshold_simulation = None
                best_threshold_score = float('-inf')
                best_threshold_params = None

                for iteration in range(n_iterations):
                    self.random_state = np.random.RandomState(iteration)
                    self.threshold = threshold

                    try:
                        self, evaluation = self.fit(adatas, threshold)
                        simulated_values = self.simulate(self.total_genes,tail_process=tail_process)
                        final_evaluation = evaluate_fit(self.original_data, simulated_values,percentile=threshold)
                        print(final_evaluation)
                        weight = [0.5, 1, 2]
                        score = (weight[0] * (1 - final_evaluation["Relative Error"]) +
                                weight[1] * (1 - final_evaluation["KS Statistic"]) +
                                weight[2] * final_evaluation["Correlation"])

                        if score > best_threshold_score:
                            best_threshold_score = score
                            best_threshold_simulation = simulated_values
                            best_threshold_evaluation = final_evaluation  
                            best_threshold_params = {
                                'threshold': self.threshold,
                                'alpha': self.alpha,
                                'beta': self.beta if hasattr(self, 'beta') else None,
                                'theta': self.theta,
                                'k': self.k if hasattr(self, 'k') else None,
                                'lambda_': self.lambda_ if hasattr(self, 'lambda_') else None,
                                'model_type': self.model_type
                            }

                    except Exception as e:
                        continue
                
                if best_overall_evaluation and best_threshold_evaluation["KS Statistic"] < 0.06 and best_threshold_evaluation["Correlation"] > 0.95:
                    print(f"Early stopping at threshold {threshold}")
                    break

                if best_threshold_score > best_overall_score:
                    best_overall_score = best_threshold_score
                    best_overall_simulation = best_threshold_simulation
                    best_overall_evaluation = best_threshold_evaluation  
                    best_overall_threshold = threshold
                    best_overall_params = best_threshold_params
                print(f"Threshold {threshold} finished")
                print(f"Best score: {best_overall_score:.3f}")

            self.threshold = best_overall_threshold
            self.model_type = best_overall_params['model_type']
            self.alpha = best_overall_params['alpha']
            self.theta = best_overall_params['theta']

            if self.model_type == 'GIG':
                self.beta = best_overall_params['beta']
                self.k = best_overall_params['k']
                self.lambda_ = best_overall_params['lambda_']

            sim_variances = self.simulate(n_samples=n_samples,tail_process=tail_process)

            

            return sim_variances, best_overall_evaluation



def threeD_simulate_gene_variances_advanced(adatas,sim_adata, n_iterations=5, var_adjust_ratio=None):
    simulator = GIG_VarianceSimulator()
    try:
        original_variances = np.var(sim_adata.X, axis=0)
        gene_var_pairs = list(zip(sim_adata.var_names, original_variances))
        gene_var_pairs.sort(key=lambda x: x[1])  # 按方差升序排序
        ordered_genes = [pair[0] for pair in gene_var_pairs]
        simulated_values, final_evaluation = simulator.fit_and_simulate(adatas, 
                                                    len(ordered_genes), n_iterations)

        
        result_dict = dict(zip(ordered_genes, np.sort(simulated_values)))
        
        
        return result_dict,simulator.threshold, final_evaluation
        
    except Exception as e:
        print(f"Simulation failed: {str(e)}")
        raise

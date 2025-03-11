import numpy as np
from scipy import stats


def relative_error(x1, x2, method='mean', threshold=None):
    x1 = np.asarray(x1)
    x2 = np.asarray(x2)
    
    if x1.shape != x2.shape:
        raise ValueError("Arrays must have the same shape")
    
    if threshold is not None:
        mask = (np.abs(x1) > threshold) & (x1 != 0)
    else:
        mask = (x1 != 0)
    
    if not np.any(mask):
        return 0.0
        
    relative_errors = np.zeros_like(x1, dtype=float)
    relative_errors[mask] = np.abs(x1[mask] - x2[mask]) / np.abs(x1[mask])
    
    if method == 'mean':
        return np.mean(relative_errors[mask])
    elif method == 'median':
        return np.median(relative_errors[mask])
    elif method == 'max':
        return np.max(relative_errors[mask])
    else:
        raise ValueError("Unknown method")

def evaluate_fit(original, generated, percentile):
    
    threshold_orig = np.percentile(original, percentile)
    threshold_gen = np.percentile(generated, percentile)
    
    filtered_orig = original[original <= threshold_orig]

    filtered_gen = generated[generated <= threshold_gen]

    min_length = min(len(filtered_orig), len(filtered_gen))
    filtered_orig = np.sort(filtered_orig)[:min_length]
    filtered_gen = np.sort(filtered_gen)[:min_length]
    rel_error = relative_error(filtered_orig, filtered_gen)

    ks_stat, _ = stats.ks_2samp(filtered_orig, filtered_gen)


    correlation = np.corrcoef(filtered_orig, filtered_gen)[0, 1]

    # evaluate the fit
    results = {
        "Relative Error": rel_error,
        "KS Statistic": ks_stat,
        "Correlation": correlation,
    }
    

    fair = (rel_error < 0.2 and
            ks_stat < 0.2 and 
            correlation > 0.85)
    
    results["Verdict"] = "Fit" if fair else "Poor fit"
    
    return results
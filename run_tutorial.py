# import opencor as oc
import numpy as np
import os
from opencor_helper import SimulationHelper
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
root_dir = os.path.join(os.path.dirname(__file__))

# Modify the file path for the model you want to run
file_path = os.path.join(root_dir, 'example_models/3compartment.cellml')

# where you want your outputs to be saved
output_file_path = "outputs"

if not os.path.exists(output_file_path):
    os.makedirs(output_file_path)

# time to run the simulation to reach steady state (to reach the time where you want to evaluate outputs)
pre_time = 20

# Amount of simulation that you care about
sim_time = 2

# the output time step
dt = 0.01

# Choose parameter names that you want to vary
param_names = ['heart/q_lv_init', 'venous_svc/C']

# choose the values of the initial guess for parameter identification
param_vals_current = [1.8e-3, 1.1e-6]
param_vals_mins = [0.5e-3, 1e-6]
param_vals_maxs = [2e-3  , 3e-6]
param_vals_history = []

output_names = ['aortic_root/u']
ground_truth = 12000

# run param_id until your cost decreases below this value
cost_tolerance = 0.001
# maximum number of iterations
max_iter = 100 

# this sets up the simulation object for your cellml model
sim_object = SimulationHelper(file_path, dt, sim_time, solver_info={'MaximumStep':0.001, 'MaximumNumberOfSteps':500000}, pre_time=pre_time)

def run_and_get_results(param_vals):
    sim_object.set_param_vals(param_names, param_vals)
    sim_object.reset_states()
    sim_object.run()
    
    y = sim_object.get_results(output_names)
    t = sim_object.tSim - pre_time
    return y, t

def squared_cost(y, ground_truth):
    # simple squared percentage error cost function
    cost = np.sum(((np.mean(outputs) - ground_truth)/ground_truth)**2)
    return cost

##!!!!! CREATE A NEW COST FUNCTION HERE



##!!!!!

def random_walk_take_step(param_vals, step_weighting = 0.1):
    new_param_vals = np.zeros(len(param_vals))
    for II in range(len(param_vals)):
        new_param_vals[II] = param_vals[II] + step_weighting*np.random.randn()*(param_vals_maxs[II] - param_vals_mins[II])

        # if param val is outside of the range, set it to the limit
        if new_param_vals[II] > param_vals_maxs[II]:
            new_param_vals[II] = param_vals_maxs[II]
        if new_param_vals[II] < param_vals_mins[II]:
            new_param_vals[II] = param_vals_mins[II]
    
    return new_param_vals

##!!!!! CREATE A NEW FUNCTION FOR STEPPING THROUGH PARAMETER VALUES HERE



##!!!!!


# intialise cost to something big
cost = 9999
best_cost = cost
iter_idx = 0
while cost > cost_tolerance and iter_idx < max_iter:

    outputs, t = run_and_get_results(param_vals_current)

    # You can make a new cost function and use it here 
    cost = squared_cost(outputs, ground_truth)


    if (cost < best_cost):
        best_cost = cost
        # save best fit param vals in history list
        param_vals_history.append(param_vals_current)

    else:
        # if the cost was worse (higher) move back to the best param values so far
        param_vals_current = param_vals_history[-1]
        pass

    print(f"Iteration {iter_idx} best cost is :  {best_cost}, with param vals {param_vals_current}")

    # here is where you can implement any scheme for stepping through parameter guesses
    # Currently we implement a very naive random walk that should be improved
    param_vals_current = random_walk_take_step(param_vals_current)

    iter_idx += 1

print(f"Finished after {iter_idx} iterations")
print(f"Best cost is {best_cost}")
print(f"Best parameters are {param_vals_current}")

# Create plots of your best fit compared to the ground truth




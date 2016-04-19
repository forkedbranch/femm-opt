import femm
import nlopt
import os
from shutil import move
from functools import partial

def objective_function(x, grad, experiment_name, output_folder):
    objective_function.eval_count += 1
    
    E_max, failed, image = femm.run_femm(x[0], x[1], "out", output_folder)
    print(objective_function.eval_count, x, E_max, failed)
    
    objective_function.evaluations.append(
        {'evaluation_number' : objective_function.eval_count, 
         'center' : x[0], 
         'radius' : x[1], 
         'objective' : E_max, 
         'failed' : failed})
        
    move(image,
         os.path.join(output_folder,
                      "%s_%s.bmp" % 
                      (experiment_name, 
                       '{0:03d}'.format(objective_function.eval_count))))
    
    return E_max

def optimize(algorithm, experiment_name, output_folder):
    objective_function.eval_count = 0
    objective_function.evaluations = []
        
    opt = nlopt.opt(algorithm, 2)
    
    opt.set_lower_bounds([-0.5, 0.1]) 
    opt.set_upper_bounds([0.5, 1.4])
    opt.set_min_objective(partial(objective_function,
                                  experiment_name=experiment_name,
                                  output_folder=output_folder))
    opt.set_xtol_abs(0.01)
    opt.set_maxeval(50)
    
    
    x = opt.optimize([0, 0.65])
    minf = opt.last_optimum_value()
    print ("optimum at ", x[0],x[1])
    print ("minimum value = ", minf)
    print ("result code = ", opt.last_optimize_result())
    
    return objective_function.evaluations
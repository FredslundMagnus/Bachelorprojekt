
# Parameters

    Name :                      maze_size_19_low_rest_chance-0
    Main :                      teleport
    Hours :                     10.0
    Batch :                     100
    Width :                     19
    Height :                    19
    Network1 :                  Networks.Teleporter
    Network2 :                  Networks.Mini
    Learner1 :                  Learners.Qlearn
    Learner2 :                  Learners.Qlearn
    Exploration1 :              Explorations.softmaxer
    Exploration2 :              Explorations.epsilonGreedy
    Layer blocks :              True
    Layer goal :                True
    Layer gold :                False
    Layer keys :                False
    Layer door :                False
    Layer holder :              False
    Layer putter :              False
    K :                         200000
    Epsilon cap :               0.2
    Softmax cap :               0.03
    Gamma :                     0.98
    Update :                    10000
    Reset chance :              0.002
    Modified done chance :      0.05
    Miss intervention cost :    -0.2
    Intervention cost :         -0.05
    Replay size :               50000
    Sample size :               50
    Minutes used :              595 minutes.
    Hours used :                9 hours.

# Profiling


      15469749852 function calls (15314589725 primitive calls) in 35677.52 seconds

##    Ordered by: cumulative time
   List reduced from 457 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 35710.432 35710.432 {built-in method builtins.exec}
                      1    0.851    0.851 35710.432 35710.432 <string>:1(<module>)
                      1  112.486  112.486 35709.580 35709.580 main.py:10(teleport)
                5544346   18.635    0.000 11792.019    0.002 agent.py:26(learn)
                5544346  312.269    0.000 9929.736    0.002 learner.py:42(Qlearn)
                2772173  253.739    0.000 9189.165    0.003 collector.py:36(collect)
               13860865 7865.874    0.001 8905.102    0.001 {built-in method builtins.sum}
                2772173   90.451    0.000 7042.375    0.003 agent.py:50(_learn)
                2772173    9.992    0.000 5280.915    0.002 game.py:21(step)
        174485374/19392786  645.642    0.000 5234.795    0.000 module.py:866(_call_impl)
               13848440   37.799    0.000 4859.313    0.000 network.py:24(forward)
               13848440  162.079    0.000 4740.234    0.000 container.py:117(forward)
                2772173   76.424    0.000 4715.443    0.002 agent.py:101(_learn)
                2772173   12.309    0.000 4592.027    0.002 layers.py:212(step)
                5544346   43.253    0.000 3851.215    0.001 optimizer.py:84(wrapper)
                5544346   21.726    0.000 3656.780    0.001 grad_mode.py:24(decorate_context)
                5544346  145.144    0.000 3584.578    0.001 adam.py:55(step)
                5531921  118.068    0.000 3263.917    0.001 agent.py:45(__call__)
                5544346  746.712    0.000 3262.943    0.001 _functional.py:53(adam)
                2772173  996.043    0.000 2614.780    0.001 agent.py:77(interveen)
                5544346   20.893    0.000 2568.054    0.000 tensor.py:195(backward)
                5544346   20.021    0.000 2546.493    0.000 __init__.py:68(backward)
                5544346 2424.846    0.000 2424.846    0.000 {method 'run_backward' of 'torch._C._EngineBase' objects}
                2772173  178.674    0.000 2338.835    0.001 layers.py:17(step)
                2772174  232.559    0.000 2223.723    0.001 layers.py:192(update)
              277217300  191.835    0.000 2134.301    0.000 layer.py:66(move)
                2772173 1095.091    0.000 1898.308    0.001 replaybuffer.py:27(teleporter_save_data)
                2772173  950.131    0.000 1751.198    0.001 replaybuffer.py:23(sample_data)
               27696880   58.510    0.000 1735.026    0.000 conv.py:398(forward)
               27696880   35.312    0.000 1650.190    0.000 conv.py:390(_conv_forward)
              277217300  114.859    0.000 1620.910    0.000 layers.py:223(isFree)
               27696880 1614.878    0.000 1614.878    0.000 {built-in method conv2d}
                2772173  894.585    0.000 1579.814    0.001 agent.py:59(modify)
              389630020 1438.038    0.000 1506.051    0.000 layer.py:63(isFree)
               36000974   74.619    0.000 1344.327    0.000 linear.py:93(forward)
               36000974   29.826    0.000 1236.677    0.000 functional.py:1737(linear)
               36000974 1200.044    0.000 1200.044    0.000 {built-in method torch._C._nn.linear}
               16634144   27.739    0.000 1076.697    0.000 tensor.py:575(__iter__)
               11717790 1065.273    0.000 1065.273    0.000 {built-in method tensor}
                2772173   34.839    0.000 1035.592    0.000 agent.py:96(__call__)
               16634144 1024.663    0.000 1024.663    0.000 {method 'unbind' of 'torch._C._TensorBase' objects}
                8304094   49.189    0.000 1021.708    0.000 agent.py:54(modify_board)
                5544346    7.378    0.000  911.101    0.000 game.py:17(board)
                 621362    7.430    0.000  891.406    0.001 layers.py:233(restart)
               22164959  769.607    0.000  769.607    0.000 {built-in method cat}
                 621362    1.474    0.000  737.795    0.001 levels.py:8(__init__)
                 621362    2.828    0.000  736.320    0.001 level.py:8(__init__)
                 621362  142.870    0.000  726.944    0.001 levels.py:11(generate)
               78448801  711.347    0.000  711.347    0.000 {built-in method clone}
               49849414   39.889    0.000  709.409    0.000 activation.py:713(forward)
                8304094  679.672    0.000  679.672    0.000 {built-in method torch._C._nn.one_hot}
              277217400   70.330    0.000  670.053    0.000 {built-in method builtins.all}
               49849414   38.890    0.000  669.520    0.000 functional.py:1364(leaky_relu)
              831719594  179.589    0.000  629.155    0.000 layers.py:197(<genexpr>)
               99798228  628.790    0.000  628.790    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
               49849414  622.921    0.000  622.921    0.000 {built-in method torch._C._nn.leaky_relu}
                2772173   44.206    0.000  613.210    0.000 replaybuffer.py:19(stacker)
                5544346  104.866    0.000  584.396    0.000 optimizer.py:189(zero_grad)
               99798228  565.134    0.000  565.134    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
              277217400  279.507    0.000  428.021    0.000 layers.py:65(isDone)
                 621362  201.964    0.000  398.365    0.001 levels.py:76(RFS)
               49899114  376.762    0.000  376.762    0.000 {method 'add' of 'torch._C._TensorBase' objects}
                8316522  156.920    0.000  359.399    0.000 layer.py:90(update)
                5531921  123.773    0.000  339.436    0.000 exploration.py:53(softmaxer)
               49899114  326.713    0.000  326.713    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
               49899114  308.198    0.000  308.198    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
               49899114  297.519    0.000  297.519    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
              349293852  221.179    0.000  273.864    0.000 tensor.py:906(grad)
              277217300  192.111    0.000  249.453    0.000 layers.py:229(check)
               49899114  231.071    0.000  231.071    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
                5544346    7.342    0.000  222.889    0.000 loss.py:527(forward)
                5544346   19.880    0.000  215.547    0.000 functional.py:2898(mse_loss)
                3393535   71.180    0.000  189.153    0.000 random.py:315(sample)
               86752895  162.921    0.000  162.921    0.000 {method 'unsqueeze' of 'torch._C._TensorBase' objects}
              379883387  147.258    0.000  147.258    0.000 layer.py:85(elements)
                1864086   13.407    0.000  145.440    0.000 layer.py:40(restart)
        838060737/838060735   96.543    0.000  136.570    0.000 {built-in method builtins.len}
                5544346  131.885    0.000  131.885    0.000 {built-in method torch._C._nn.mse_loss}
             1442847028  125.610    0.000  125.610    0.000 layer.py:59(positions)
               27696880   18.453    0.000  122.484    0.000 flatten.py:39(forward)
                5545176  120.971    0.000  120.971    0.000 {built-in method max}
              190258374   78.929    0.000  114.893    0.000 random.py:250(_randbelow_with_getrandbits)
                8316519   11.059    0.000  113.510    0.000 tensor.py:525(__rsub__)
                2772173    9.748    0.000  111.384    0.000 exploration.py:47(epsilonGreedy)
              191119518  105.026    0.000  105.026    0.000 {built-in method torch._C._get_tracing_state}
               27696880  104.031    0.000  104.031    0.000 {method 'flatten' of 'torch._C._TensorBase' objects}
                5531921  102.457    0.000  102.457    0.000 {built-in method multinomial}
              372907151   70.025    0.000  100.669    0.000 enum.py:646(__hash__)
                8316519  100.540    0.000  100.540    0.000 {built-in method rsub}
                5544346   20.741    0.000   97.211    0.000 __init__.py:28(_make_grads)
                5544346   95.343    0.000   95.343    0.000 {built-in method gather}
                 621462   56.540    0.000   95.302    0.000 layers.py:37(reset)
               11088692   20.269    0.000   93.215    0.000 profiler.py:615(__enter__)
              198835840   61.123    0.000   92.809    0.000 levels.py:33(<genexpr>)
              181728684   62.185    0.000   83.855    0.000 layer.py:76(add)
              141257740   81.280    0.000   81.288    0.000 module.py:934(__getattr__)
               11088692   12.910    0.000   80.574    0.000 profiler.py:607(__init__)
                2772174   79.701    0.000   79.701    0.000 {built-in method nonzero}
               11088692   72.947    0.000   72.947    0.000 {built-in method torch._ops.profiler._record_function_enter}
                5544346   72.345    0.000   72.345    0.000 {built-in method ones_like}


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@n-62-20-4>
Subject: Job 9393248: <maze_size_19_low_rest_chance_0> in cluster <dcc> Done

Job <maze_size_19_low_rest_chance_0> was submitted from host <gbarlogin1> by user <s183914> in cluster <dcc> at Mon Mar  8 02:11:20 2021
Job was executed on host(s) <n-62-20-4>, in queue <gpuv100>, as user <s183914> in cluster <dcc> at Mon Mar  8 11:54:10 2021
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Mon Mar  8 11:54:10 2021
Terminated at Mon Mar  8 21:49:39 2021
Results reported at Mon Mar  8 21:49:39 2021

Your job looked like:

------------------------------------------------------------
# LSBATCH: User input
#!/bin/sh
#BSUB -q hpc
#BSUB -q gpuv100
#BSUB -gpu "num=1:mode=exclusive_process"
#BSUB -n 1
#BSUB -R "rusage[mem=8G]"
#BSUB -R "span[hosts=1]"
#BSUB -W 1440
# end of BSUB options
cd ..
module -s load python3
source ../project-env/bin/activate

python main.py $LSB_PROJECT_NAME


------------------------------------------------------------

Successfully completed.

Resource usage summary:

    CPU time :                                   35620.64 sec.
    Max Memory :                                 6226 MB
    Average Memory :                             4378.71 MB
    Total Requested Memory :                     8192.00 MB
    Delta Memory :                               1966.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                8
    Run time :                                   35729 sec.
    Turnaround time :                            70699 sec.

The output (if any) is above this job summary.


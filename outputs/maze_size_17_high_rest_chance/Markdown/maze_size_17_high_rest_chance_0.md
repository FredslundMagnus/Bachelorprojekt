
# Parameters

    Name :                      maze_size_17_high_rest_chance-0
    Main :                      teleport
    Hours :                     10.0
    Batch :                     100
    Width :                     17
    Height :                    17
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
    Reset chance :              0.005
    Modified done chance :      0.05
    Miss intervention cost :    -0.2
    Intervention cost :         -0.05
    Replay size :               50000
    Sample size :               50
    Minutes used :              595 minutes.
    Hours used :                9 hours.

# Profiling


      17247526645 function calls (17098255778 primitive calls) in 35652.60 seconds

##    Ordered by: cumulative time
   List reduced from 457 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 35712.496 35712.496 {built-in method builtins.exec}
                      1    0.913    0.913 35712.495 35712.495 <string>:1(<module>)
                      1  110.060  110.060 35711.583 35711.583 main.py:10(teleport)
                5332442   18.011    0.000 11540.464    0.002 agent.py:26(learn)
                5332442  307.385    0.000 9720.958    0.002 learner.py:42(Qlearn)
                2666221  248.307    0.000 8990.027    0.003 collector.py:36(collect)
               13331105 7681.048    0.001 8711.353    0.001 {built-in method builtins.sum}
                2666221   86.705    0.000 6882.736    0.003 agent.py:50(_learn)
                2666221    9.884    0.000 5834.528    0.002 game.py:21(step)
                2666221   12.044    0.000 5228.802    0.002 layers.py:212(step)
        167860877/18655005  632.174    0.000 5148.270    0.000 module.py:866(_call_impl)
               13322563   36.954    0.000 4776.353    0.000 network.py:24(forward)
               13322563  158.032    0.000 4660.346    0.000 container.py:117(forward)
                2666221   75.449    0.000 4624.744    0.002 agent.py:101(_learn)
                5332442   42.776    0.000 3757.820    0.001 optimizer.py:84(wrapper)
                5332442   22.488    0.000 3566.998    0.001 grad_mode.py:24(decorate_context)
                5332442  139.864    0.000 3495.396    0.001 adam.py:55(step)
                5323900  117.706    0.000 3210.930    0.001 agent.py:45(__call__)
                5332442  727.263    0.000 3186.676    0.001 _functional.py:53(adam)
                2666222  230.232    0.000 3069.888    0.001 layers.py:192(update)
                2666221 1020.921    0.000 2622.762    0.001 agent.py:77(interveen)
                5332442   21.534    0.000 2525.997    0.000 tensor.py:195(backward)
                5332442   20.591    0.000 2503.838    0.000 __init__.py:68(backward)
                5332442 2381.885    0.000 2381.885    0.000 {method 'run_backward' of 'torch._C._EngineBase' objects}
                2666221  172.087    0.000 2130.016    0.001 layers.py:17(step)
                2666221 1134.550    0.000 1952.935    0.001 replaybuffer.py:27(teleporter_save_data)
              266622100  187.180    0.000 1932.840    0.000 layer.py:66(move)
               26645126   57.540    0.000 1716.034    0.000 conv.py:398(forward)
                2666221  906.222    0.000 1689.166    0.001 replaybuffer.py:23(sample_data)
                1463882   15.438    0.000 1666.966    0.001 layers.py:233(restart)
               26645126   32.964    0.000 1634.247    0.000 conv.py:390(_conv_forward)
               26645126 1601.284    0.000 1601.284    0.000 {built-in method conv2d}
                2666221  897.304    0.000 1570.984    0.001 agent.py:59(modify)
              266622100  111.457    0.000 1424.838    0.000 layers.py:223(isFree)
                1463882    2.964    0.000 1365.440    0.001 levels.py:8(__init__)
                1463882    6.537    0.000 1362.476    0.001 level.py:8(__init__)
                1463882  266.779    0.000 1339.443    0.001 levels.py:11(generate)
               34635247   69.590    0.000 1317.717    0.000 linear.py:93(forward)
              383680404 1244.131    0.000 1313.381    0.000 layer.py:63(isFree)
               34635247   28.835    0.000 1217.065    0.000 functional.py:1737(linear)
               34635247 1181.709    0.000 1181.709    0.000 {built-in method torch._C._nn.linear}
               15998390   27.510    0.000 1065.634    0.000 tensor.py:575(__iter__)
                2666221   34.919    0.000 1017.497    0.000 agent.py:96(__call__)
               15998390 1014.173    0.000 1014.173    0.000 {method 'unbind' of 'torch._C._TensorBase' objects}
                7990121   49.326    0.000 1003.738    0.000 agent.py:54(modify_board)
               11271599  910.085    0.000  910.085    0.000 {built-in method tensor}
                5332442    6.084    0.000  760.409    0.000 game.py:17(board)
               21321226  755.330    0.000  755.330    0.000 {built-in method cat}
                1463882  371.998    0.000  722.520    0.000 levels.py:76(RFS)
               79816552  721.886    0.000  721.886    0.000 {built-in method clone}
               47957810   37.256    0.000  697.094    0.000 activation.py:713(forward)
              266622200   69.622    0.000  671.249    0.000 {built-in method builtins.all}
                7990121  669.223    0.000  669.223    0.000 {built-in method torch._C._nn.one_hot}
               47957810   39.683    0.000  659.838    0.000 functional.py:1364(leaky_relu)
              799998260  179.996    0.000  630.580    0.000 layers.py:197(<genexpr>)
               47957810  612.757    0.000  612.757    0.000 {built-in method torch._C._nn.leaky_relu}
               95983956  612.756    0.000  612.756    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
                2666221   42.588    0.000  602.443    0.000 replaybuffer.py:19(stacker)
                5332442  102.979    0.000  568.834    0.000 optimizer.py:189(zero_grad)
               95983956  553.538    0.000  553.538    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
                7998666  215.667    0.000  433.457    0.000 layer.py:90(update)
              266622200  285.024    0.000  429.768    0.000 layers.py:65(isDone)
               47991978  371.622    0.000  371.622    0.000 {method 'add' of 'torch._C._TensorBase' objects}
                5323900  121.756    0.000  326.863    0.000 exploration.py:53(softmaxer)
               47991978  318.178    0.000  318.178    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
               47991978  297.888    0.000  297.888    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
               47991978  293.246    0.000  293.246    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
                4391646   25.918    0.000  284.316    0.000 layer.py:40(restart)
              335943900  212.805    0.000  263.234    0.000 tensor.py:906(grad)
              266622100  188.543    0.000  244.870    0.000 layers.py:229(check)
               47991978  226.423    0.000  226.423    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
                5332442    7.100    0.000  222.146    0.000 loss.py:527(forward)
                5332442   22.411    0.000  215.045    0.000 functional.py:2898(mse_loss)
                4130103   71.185    0.000  190.017    0.000 random.py:315(sample)
                1463982  112.182    0.000  189.906    0.000 layers.py:37(reset)
              368898264  114.833    0.000  173.678    0.000 levels.py:33(<genexpr>)
               87806673  165.057    0.000  165.057    0.000 {method 'unsqueeze' of 'torch._C._TensorBase' objects}
              612775415  164.578    0.000  164.578    0.000 layer.py:85(elements)
              230016929   99.178    0.000  143.306    0.000 random.py:250(_randbelow_with_getrandbits)
        852278857/852278855   95.901    0.000  135.387    0.000 {built-in method builtins.len}
              298612200   99.953    0.000  134.672    0.000 layer.py:76(add)
                5332442  131.163    0.000  131.163    0.000 {built-in method torch._C._nn.mse_loss}
             1392972074  122.348    0.000  122.348    0.000 layer.py:59(positions)
               26645126   18.376    0.000  120.563    0.000 flatten.py:39(forward)
              448143571   83.956    0.000  120.344    0.000 enum.py:646(__hash__)
                5333240  117.995    0.000  117.995    0.000 {built-in method max}
                7998663   10.760    0.000  111.518    0.000 tensor.py:525(__rsub__)
                2666221   10.164    0.000  109.834    0.000 exploration.py:47(epsilonGreedy)
               93688448   38.497    0.000  107.510    0.000 random.py:285(choice)
              183859267  103.973    0.000  103.973    0.000 {built-in method torch._C._get_tracing_state}
               26645126  102.186    0.000  102.186    0.000 {method 'flatten' of 'torch._C._TensorBase' objects}
                5323900  100.682    0.000  100.682    0.000 {built-in method multinomial}
                7998663   99.012    0.000   99.012    0.000 {built-in method rsub}
                5332442   20.784    0.000   96.877    0.000 __init__.py:28(_make_grads)
                5332442   91.637    0.000   91.637    0.000 {built-in method gather}
               10664884   19.938    0.000   91.027    0.000 profiler.py:615(__enter__)
               10664884   14.760    0.000   80.081    0.000 profiler.py:607(__init__)
                2666222   78.799    0.000   78.799    0.000 {built-in method nonzero}
             1141178448   77.194    0.000   77.194    0.000 {method 'append' of 'list' objects}
              135896373   76.234    0.000   76.242    0.000 module.py:934(__getattr__)


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@n-62-20-2>
Subject: Job 9393251: <maze_size_17_high_rest_chance_0> in cluster <dcc> Done

Job <maze_size_17_high_rest_chance_0> was submitted from host <gbarlogin1> by user <s183914> in cluster <dcc> at Mon Mar  8 02:11:21 2021
Job was executed on host(s) <n-62-20-2>, in queue <gpuv100>, as user <s183914> in cluster <dcc> at Mon Mar  8 12:06:44 2021
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Mon Mar  8 12:06:44 2021
Terminated at Mon Mar  8 22:02:15 2021
Results reported at Mon Mar  8 22:02:15 2021

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

    CPU time :                                   35623.77 sec.
    Max Memory :                                 6099 MB
    Average Memory :                             4332.03 MB
    Total Requested Memory :                     8192.00 MB
    Delta Memory :                               2093.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                8
    Run time :                                   35731 sec.
    Turnaround time :                            71454 sec.

The output (if any) is above this job summary.


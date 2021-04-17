
# Parameters

    Name :                      Rock_level_epslow-0
    Main :                      teleport
    Level :                     Levels.Rocks
    Hours :                     12.0
    Batch :                     100
    Width :                     9
    Height :                    9
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
    Layer rock :                True
    Layer dirt :                True
    Layer diamond1 :            True
    Layer diamond2 :            True
    Layer diamond3 :            True
    Layer diamond4 :            True
    K :                         200000
    Epsilon cap :               0.0
    Softmax cap :               0.02
    Gamma :                     0.98
    Update :                    10000
    Reset chance :              0.002
    Modified done chance :      0.05
    Miss intervention cost :    -0.2
    Intervention cost :         -0.05
    Replay size :               50000
    Sample size :               50
    Minutes used :              715 minutes.
    Hours used :                11 hours.

# Profiling


      38282482894 function calls (38161409235 primitive calls) in 42917.93 seconds

##    Ordered by: cumulative time
   List reduced from 470 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 42917.926 42917.926 {built-in method builtins.exec}
                      1    1.034    1.034 42917.926 42917.926 <string>:1(<module>)
                      1  132.617  132.617 42916.892 42916.892 main.py:13(teleport)
                2162039   10.895    0.000 17445.490    0.008 game.py:27(step)
                2162039   14.900    0.000 16882.427    0.008 layers.py:373(step)
                4324078   20.258    0.000 10848.652    0.003 agent.py:26(learn)
                2162039  205.008    0.000 10763.738    0.005 layers.py:18(step)
              216203900  514.667    0.000 10538.453    0.000 layer.py:74(move)
                4324078  292.994    0.000 9094.486    0.002 learner.py:42(Qlearn)
              216203900  701.306    0.000 7597.012    0.000 layers.py:390(check)
                2162039   81.330    0.000 6418.406    0.003 agent.py:50(_learn)
                2162040  269.106    0.000 6081.889    0.003 layers.py:344(update)
                2162039 3192.784    0.001 5334.526    0.002 replaybuffer.py:27(teleporter_save_data)
        136206793/15134145  601.494    0.000 4810.153    0.000 module.py:866(_call_impl)
               10810067   34.960    0.000 4443.307    0.000 network.py:24(forward)
                2162039   68.452    0.000 4397.939    0.002 agent.py:101(_learn)
               10810067  145.177    0.000 4331.334    0.000 container.py:117(forward)
              216203900 3499.783    0.000 4159.849    0.000 layers.py:76(check)
                2162039 2265.581    0.001 3707.313    0.002 agent.py:77(interveen)
                4324078   45.640    0.000 3434.398    0.001 optimizer.py:84(wrapper)
                4324078   24.070    0.000 3238.208    0.001 grad_mode.py:24(decorate_context)
                4324078  137.420    0.000 3161.384    0.001 adam.py:55(step)
                4323950  124.092    0.000 3001.529    0.001 agent.py:45(__call__)
                4324078  665.702    0.000 2874.322    0.001 _functional.py:53(adam)
                8545977   83.329    0.000 2563.548    0.000 layers.py:394(restart)
               19458360 1713.746    0.000 2520.302    0.000 layer.py:119(update)
                4324078   20.960    0.000 2419.970    0.001 tensor.py:195(backward)
                4324078   21.775    0.000 2398.373    0.001 __init__.py:68(backward)
                4324078 2275.766    0.001 2275.766    0.001 {method 'run_backward' of 'torch._C._EngineBase' objects}
                2162039 1443.755    0.001 2203.702    0.001 replaybuffer.py:23(sample_data)
              216203900  412.624    0.000 2136.550    0.000 layers.py:384(isFree)
              193627870 1766.576    0.000 1766.576    0.000 {built-in method clone}
             1851195273 1481.328    0.000 1723.926    0.000 layer.py:71(isFree)
                2162039 1030.328    0.000 1687.389    0.001 agent.py:59(modify)
               21620134   53.934    0.000 1645.878    0.000 conv.py:398(forward)
                8545977   38.047    0.000 1596.308    0.000 level.py:8(__init__)
               21620134   33.003    0.000 1566.648    0.000 conv.py:390(_conv_forward)
               21620134 1533.645    0.000 1533.645    0.000 {built-in method conv2d}
                8545977  224.799    0.000 1424.328    0.000 levels.py:95(generate)
               28106123   61.624    0.000 1194.190    0.000 linear.py:93(forward)
               28106123   24.220    0.000 1100.175    0.000 functional.py:1737(linear)
               28106123 1070.582    0.000 1070.582    0.000 {built-in method torch._C._nn.linear}
             3887520532  687.109    0.000  982.240    0.000 enum.py:646(__hash__)
                6485989   44.881    0.000  940.623    0.000 agent.py:54(modify_board)
                2162039   38.275    0.000  897.633    0.000 agent.py:96(__call__)
               76913793  114.162    0.000  859.043    0.000 layer.py:48(restart)
               17091954  112.827    0.000  799.709    0.000 level.py:41(notUsed)
                8756101  780.802    0.000  780.802    0.000 {built-in method tensor}
               19458223  728.794    0.000  728.794    0.000 {built-in method cat}
                4324078    6.437    0.000  656.423    0.000 game.py:23(board)
               38916190   46.770    0.000  634.624    0.000 activation.py:713(forward)
              216204000   68.660    0.000  629.120    0.000 {built-in method builtins.all}
                6485989  624.522    0.000  624.522    0.000 {built-in method torch._C._nn.one_hot}
              216203900  405.699    0.000  600.521    0.000 layers.py:63(check)
              216203900  366.205    0.000  596.712    0.000 layers.py:244(check)
              216203900  372.063    0.000  596.471    0.000 layers.py:216(check)
              697934833  178.161    0.000  590.628    0.000 layers.py:350(<genexpr>)
                2162039   42.984    0.000  587.964    0.000 replaybuffer.py:19(stacker)
             2238576374  587.889    0.000  587.889    0.000 layer.py:114(elements)
               38916190   33.498    0.000  587.853    0.000 functional.py:1364(leaky_relu)
             1106293444  432.179    0.000  582.907    0.000 layer.py:98(add)
              216203900  357.381    0.000  579.946    0.000 layers.py:230(check)
               77833404  548.778    0.000  548.778    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
               38916190  548.139    0.000  548.139    0.000 {built-in method torch._C._nn.leaky_relu}
              506072918  259.159    0.000  509.832    0.000 layer.py:94(remove)
                4324078   88.428    0.000  491.753    0.000 optimizer.py:189(zero_grad)
               77833404  491.433    0.000  491.433    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
             5068048316  489.035    0.000  489.035    0.000 layer.py:67(positions)
                8546077  222.664    0.000  453.579    0.000 layers.py:33(reset)
               10708016  154.121    0.000  431.420    0.000 random.py:315(sample)
              470028735  421.219    0.000  421.219    0.000 level.py:32(inverse)
              200113859  420.349    0.000  420.349    0.000 {method 'unsqueeze' of 'torch._C._TensorBase' objects}
              216204000  264.497    0.000  385.961    0.000 layers.py:110(isDone)
                2162039  198.109    0.000  339.721    0.000 collector.py:54(collect)
               38916702  332.210    0.000  332.210    0.000 {method 'add' of 'torch._C._TensorBase' objects}
                4323950  114.039    0.000  319.744    0.000 exploration.py:53(softmaxer)
              216203900  199.323    0.000  303.226    0.000 layers.py:203(check)
             3887536483  295.134    0.000  295.134    0.000 {built-in method builtins.hash}
               38916702  292.730    0.000  292.730    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
               38916702  266.202    0.000  266.202    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
               38916702  265.571    0.000  265.571    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
              216203900   99.161    0.000  244.923    0.000 layers.py:99(<listcomp>)
             3336365679  242.216    0.000  242.216    0.000 {method 'append' of 'list' objects}
              272416968  184.973    0.000  228.865    0.000 tensor.py:906(grad)
                4324078    8.498    0.000  222.200    0.000 loss.py:527(forward)
                4324078   21.618    0.000  213.702    0.000 functional.py:2898(mse_loss)
              506072918  208.262    0.000  208.262    0.000 {method 'remove' of 'list' objects}
              321804600  140.703    0.000  205.055    0.000 random.py:250(_randbelow_with_getrandbits)
               17091954   15.256    0.000  204.371    0.000 level.py:38(elementsIn)
        2184335954/2184335952  159.467    0.000  192.795    0.000 {built-in method builtins.len}
               38916702  190.914    0.000  190.914    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
             1851195273  185.284    0.000  185.284    0.000 layer.py:175(isBlocking)
               12972234  151.646    0.000  151.646    0.000 {built-in method sum}
                4324078  128.749    0.000  128.749    0.000 {built-in method torch._C._nn.mse_loss}
                4324726  115.735    0.000  115.735    0.000 {built-in method max}
                6486117   12.024    0.000  113.338    0.000 tensor.py:525(__rsub__)
               17091954   57.409    0.000  113.282    0.000 level.py:39(<listcomp>)
                8545977   51.286    0.000  108.271    0.000 level.py:16(<dictcomp>)
               21620134   16.236    0.000  107.234    0.000 flatten.py:39(forward)
                4323950  103.169    0.000  103.169    0.000 {built-in method multinomial}


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@n-62-20-12>
Subject: Job 9441984: <Rock_level_epslow_0> in cluster <dcc> Done

Job <Rock_level_epslow_0> was submitted from host <gbarlogin1> by user <s183914> in cluster <dcc> at Sat Mar 20 01:13:11 2021
Job was executed on host(s) <n-62-20-12>, in queue <gpuv100>, as user <s183914> in cluster <dcc> at Sat Mar 20 01:13:12 2021
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Sat Mar 20 01:13:12 2021
Terminated at Sat Mar 20 13:08:41 2021
Results reported at Sat Mar 20 13:08:41 2021

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

    CPU time :                                   42800.64 sec.
    Max Memory :                                 5375 MB
    Average Memory :                             4046.59 MB
    Total Requested Memory :                     8192.00 MB
    Delta Memory :                               2817.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                8
    Run time :                                   42967 sec.
    Turnaround time :                            42930 sec.

The output (if any) is above this job summary.


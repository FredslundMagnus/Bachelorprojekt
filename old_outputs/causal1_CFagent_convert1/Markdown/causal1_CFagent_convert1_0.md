
# Parameters

    Name :                      causal1_CFagent_convert1-0
    Main :                      CFagent
    Level :                     Levels.Causal1
    Hours :                     13.0
    Batch :                     100
    Width :                     9
    Height :                    9
    Network1 :                  Networks.Teleporter
    K1 :                        5000000
    Learner1 :                  Learners.Qlearn
    Exploration1 :              Explorations.softmaxer
    Gamma1 :                    0.98
    Network2 :                  Networks.Mini
    K2 :                        1000000
    Learner2 :                  Learners.Qlearn
    Exploration2 :              Explorations.epsilonGreedy
    Gamma2 :                    0.95
    Layer blocks :              True
    Layer goal :                True
    Layer gold :                True
    Layer keys :                True
    Layer door :                True
    Layer holder :              True
    Layer putter :              True
    Layer rock :                True
    Layer dirt :                True
    Layer diamond1 :            True
    Layer diamond2 :            True
    Layer diamond3 :            True
    Layer diamond4 :            True
    Layer reddoors :            True
    Layer redkeys :             True
    Layer bluedoors :           True
    Layer bluekeys :            True
    Layer pink1 :               True
    Layer pink2 :               True
    Layer pink3 :               True
    Layer brown1 :              True
    Layer brown2 :              True
    Layer brown3 :              True
    Epsilon cap :               0.2
    Softmax cap :               0.02
    Update :                    10000
    Reset chance :              0.001
    Modified done chance :      0.05
    Miss intervention cost :    -0.15
    Intervention cost :         -0.05
    Replay size :               100000
    Sample size :               50
    Cf convert :                0
    Minutes used :              775 minutes.
    Hours used :                12 hours.

# Profiling


      23265227425 function calls (23076957078 primitive calls) in 46518.14 seconds

##    Ordered by: cumulative time
   List reduced from 485 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 46518.138 46518.138 {built-in method builtins.exec}
                      1    4.602    4.602 46518.138 46518.138 <string>:1(<module>)
                      1  142.226  142.226 46513.536 46513.536 main.py:96(CFagent)
                5979360   24.074    0.000 17935.573    0.003 agent.py:28(learn)
                5979360  440.281    0.000 14989.878    0.003 learner.py:42(Qlearn)
        210601444/22332788  857.675    0.000 7654.784    0.000 module.py:866(_call_impl)
               16353428   43.000    0.000 7182.555    0.000 network.py:24(forward)
               16353428  220.311    0.000 7039.537    0.000 container.py:117(forward)
                1993120  200.758    0.000 6915.174    0.003 agent.py:53(_learn)
                1993120  200.572    0.000 6417.399    0.003 agent.py:189(_learn)
                5979360   52.856    0.000 6269.491    0.001 optimizer.py:84(wrapper)
                5979360   26.229    0.000 6022.491    0.001 grad_mode.py:24(decorate_context)
                5979360  178.607    0.000 5936.939    0.001 adam.py:55(step)
                1993120    9.999    0.000 5793.426    0.003 game.py:36(step)
                5979360 1212.490    0.000 5566.735    0.001 _functional.py:53(adam)
                1993120   12.826    0.000 5380.960    0.003 layers.py:594(step)
                1993120 2814.982    0.001 5243.610    0.003 replaybuffer.py:28(teleporter_save_data)
                1993120  458.785    0.000 4571.536    0.002 agent.py:197(counterfact)
                1993120   56.212    0.000 4566.493    0.002 agent.py:114(_learn)
                5979360   29.614    0.000 3913.633    0.001 tensor.py:195(backward)
                5979360   23.970    0.000 3883.136    0.001 __init__.py:68(backward)
                5979360 3726.251    0.001 3726.251    0.001 {method 'run_backward' of 'torch._C._EngineBase' objects}
                5186603  128.271    0.000 3689.878    0.001 agent.py:48(__call__)
                1993120 2207.391    0.001 3610.582    0.002 agent.py:85(interveen)
                1993120  168.361    0.000 3065.941    0.002 layers.py:18(step)
                1993120 2361.293    0.001 3051.926    0.002 replaybuffer.py:22(sample_data)
              199044596  234.160    0.000 2881.325    0.000 layer.py:82(move)
                1993120 1965.736    0.001 2582.858    0.001 replaybuffer.py:49(sample_data)
               32706856   73.443    0.000 2541.209    0.000 conv.py:398(forward)
               32706856   47.160    0.000 2432.261    0.000 conv.py:390(_conv_forward)
               32706856 2385.101    0.000 2385.101    0.000 {built-in method conv2d}
                1993121  205.980    0.000 2283.183    0.001 layers.py:565(update)
              171806894 2170.609    0.000 2170.609    0.000 {built-in method clone}
               45074044   93.716    0.000 2041.767    0.000 linear.py:93(forward)
               45074044   36.528    0.000 1901.838    0.000 functional.py:1737(linear)
               45074044 1856.073    0.000 1856.073    0.000 {built-in method torch._C._nn.linear}
                1201225   12.065    0.000 1825.185    0.002 agent.py:167(choose_action)
               25175346 1801.704    0.000 1801.704    0.000 {built-in method tensor}
               19402487   14.088    0.000 1626.157    0.000 game.py:32(board)
               23917446  881.942    0.000 1556.498    0.000 layer.py:143(NoRock_update)
                1993120  921.629    0.000 1529.264    0.001 agent.py:66(modify)
              198943636  213.122    0.000 1240.905    0.000 layers.py:605(isFree)
              199044596  310.574    0.000 1184.176    0.000 layers.py:611(check)
               29104043 1141.185    0.000 1141.185    0.000 {built-in method cat}
              111614720 1131.360    0.000 1131.360    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
               61427472   48.253    0.000 1124.775    0.000 activation.py:713(forward)
               61427472   49.801    0.000 1076.522    0.000 functional.py:1364(leaky_relu)
                7179723   52.531    0.000 1028.588    0.000 agent.py:58(modify_board)
             1091778961  876.050    0.000 1027.783    0.000 layer.py:79(isFree)
               61427472 1016.410    0.000 1016.410    0.000 {built-in method torch._C._nn.leaky_relu}
                1993120   35.222    0.000  996.594    0.001 agent.py:163(__call__)
              111614720  994.333    0.000  994.333    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
                1993120   33.878    0.000  934.117    0.000 agent.py:109(__call__)
                5979360  140.821    0.000  864.376    0.000 optimizer.py:189(zero_grad)
                2256304   21.514    0.000  682.578    0.000 layers.py:615(restart)
                7179723  653.175    0.000  653.175    0.000 {built-in method torch._C._nn.one_hot}
               55807360  643.954    0.000  643.954    0.000 {method 'add' of 'torch._C._TensorBase' objects}
                1993120   41.507    0.000  551.904    0.000 replaybuffer.py:18(stacker)
                1993120  224.296    0.000  543.294    0.000 replaybuffer.py:55(CF_save_data)
               55807360  540.619    0.000  540.619    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
              180979737  525.961    0.000  525.961    0.000 {method 'unsqueeze' of 'torch._C._TensorBase' objects}
               55807360  515.333    0.000  515.333    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
               55807360  511.389    0.000  511.389    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
                2256304   12.136    0.000  507.061    0.000 level.py:8(__init__)
              199312100   53.794    0.000  505.522    0.000 {built-in method builtins.all}
                1993120   39.362    0.000  481.158    0.000 replaybuffer.py:45(stacker)
              619002053  139.019    0.000  474.154    0.000 layers.py:571(<genexpr>)
                2256304   26.543    0.000  412.225    0.000 levels.py:122(generate)
                1993120  244.517    0.000  404.759    0.000 collector.py:54(collect)
               55807360  394.592    0.000  394.592    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
              568411023  387.263    0.000  387.263    0.000 layer.py:122(elements)
                5186603  138.855    0.000  383.838    0.000 exploration.py:53(softmaxer)
                8799294   72.705    0.000  362.922    0.000 level.py:41(notUsed)
              199044596  217.341    0.000  341.415    0.000 layers.py:143(check)
             1312268215  222.273    0.000  321.469    0.000 enum.py:646(__hash__)
              390651604  255.210    0.000  316.452    0.000 tensor.py:906(grad)
              199312100  218.730    0.000  316.388    0.000 layers.py:111(isDone)
                5979360    8.094    0.000  288.676    0.000 loss.py:527(forward)
                1201225  225.623    0.000  284.771    0.000 agent.py:178(convert_values)
                5979360   21.462    0.000  280.582    0.000 functional.py:2898(mse_loss)
        3352235058/3352235055  231.089    0.000  269.777    0.000 {built-in method builtins.len}
                3986240   98.982    0.000  267.478    0.000 random.py:315(sample)
                3194345   17.049    0.000  267.423    0.000 exploration.py:47(epsilonGreedy)
                5979361  262.772    0.000  262.772    0.000 {built-in method nonzero}
              199044596  168.681    0.000  247.791    0.000 layers.py:47(check)
              199044596  157.055    0.000  239.754    0.000 layers.py:124(check)
               32706856   24.601    0.000  187.239    0.000 flatten.py:39(forward)
             2242420583  184.633    0.000  184.633    0.000 layer.py:75(positions)
                5979360  183.814    0.000  183.814    0.000 {built-in method torch._C._nn.mse_loss}
               11958720  170.876    0.000  170.876    0.000 {built-in method sum}
                9173705   13.520    0.000  164.726    0.000 tensor.py:525(__rsub__)
                5980197  163.377    0.000  163.377    0.000 {built-in method max}
               32706856  162.638    0.000  162.638    0.000 {method 'flatten' of 'torch._C._TensorBase' objects}
              176033088  108.833    0.000  152.551    0.000 layer.py:102(remove)
               13537824   14.399    0.000  149.287    0.000 layer.py:56(restart)
                9173705  148.952    0.000  148.952    0.000 {built-in method rsub}
              215789945  147.599    0.000  147.599    0.000 {built-in method torch._C._get_tracing_state}
                8799294    6.980    0.000  143.304    0.000 level.py:38(elementsIn)
              261055440  103.380    0.000  142.346    0.000 layer.py:106(add)
                1775475   62.289    0.000  138.188    0.000 {method 'choice' of 'numpy.random.mtrand.RandomState' objects}


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@n-62-20-7>
Subject: Job 9493314: <causal1_CFagent_convert1_0> in cluster <dcc> Done

Job <causal1_CFagent_convert1_0> was submitted from host <gbarlogin1> by user <s183914> in cluster <dcc> at Fri Apr  2 22:10:08 2021
Job was executed on host(s) <n-62-20-7>, in queue <gpuv100>, as user <s183914> in cluster <dcc> at Fri Apr  2 22:10:09 2021
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Fri Apr  2 22:10:09 2021
Terminated at Sat Apr  3 11:06:45 2021
Results reported at Sat Apr  3 11:06:45 2021

Your job looked like:

------------------------------------------------------------
# LSBATCH: User input
#!/bin/sh
#BSUB -q hpc
#BSUB -q gpuv100
#BSUB -gpu "num=1:mode=exclusive_process"
#BSUB -n 1
#BSUB -R "rusage[mem=16G]"
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

    CPU time :                                   46508.65 sec.
    Max Memory :                                 3581 MB
    Average Memory :                             3538.72 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               12803.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                8
    Run time :                                   46659 sec.
    Turnaround time :                            46597 sec.

The output (if any) is above this job summary.


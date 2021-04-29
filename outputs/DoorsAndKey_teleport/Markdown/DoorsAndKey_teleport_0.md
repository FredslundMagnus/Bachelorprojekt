
# Parameters

    Name :                      DoorsAndKey_teleport-0
    Main :                      teleport
    Level :                     Levels.Causal1
    Failed actions chance :     0.0
    Hours :                     24.0
    Batch :                     100
    Width :                     9
    Height :                    9
    Graphmode :                 GraphMode.UCB1
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
    Layer reddoor :             True
    Layer redkeys :             True
    Layer bluedoor :            True
    Layer bluekeys :            True
    Layer pink1 :               True
    Layer pink2 :               True
    Layer pink3 :               True
    Layer brown1 :              True
    Layer brown2 :              True
    Layer brown3 :              True
    Layer greendown :           True
    Layer greenup :             True
    Layer greenstar :           True
    Layer yellowstar :          True
    Layer bluestar :            True
    Layer coconut :             True
    Layer monster :             True
    Layer greencross :          True
    Layer bluecross :           True
    Layer redcross :            True
    Layer purplecross :         True
    Epsilon cap :               0.2
    Softmax cap :               0.02
    Update :                    10000
    Reset chance :              0.002
    Modified done chance :      0.05
    Miss intervention cost :    -0.15
    Intervention cost :         -0.05
    Replay size :               100000
    Sample size :               50
    Cf convert :                3
    Counterfacts :              1
    Topn :                      6
    Random counterfacts :       False
    Minutes used :              1435 minutes.
    Hours used :                23 hours.

# Profiling


      67559855722 function calls (67315371219 primitive calls) in 86105.29 seconds

##    Ordered by: cumulative time
   List reduced from 474 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 86105.289 86105.289 {built-in method builtins.exec}
                      1    1.506    1.506 86105.289 86105.289 <string>:1(<module>)
                      1  202.008  202.008 86103.783 86103.783 main.py:45(teleport)
                8732314   31.139    0.000 29674.191    0.003 agent.py:29(learn)
                8732314  708.409    0.000 25396.971    0.003 learner.py:42(Qlearn)
                4366157  143.327    0.000 17843.141    0.004 agent.py:54(_learn)
                4366157   17.441    0.000 17336.763    0.004 game.py:41(step)
                4366157   21.148    0.000 16378.743    0.004 layers.py:718(step)
                4366157 7409.163    0.002 14126.688    0.003 replaybuffer.py:28(teleporter_save_data)
                4366157  119.853    0.000 11783.368    0.003 agent.py:117(_learn)
        275044816/30561324 1059.470    0.000 11598.934    0.000 module.py:715(_call_impl)
               21829010   52.735    0.000 10870.283    0.000 network.py:27(forward)
                8732314   50.105    0.000 10846.818    0.001 grad_mode.py:23(decorate_context)
                4366157 7213.224    0.002 10760.103    0.002 agent.py:88(interveen)
                8732314  272.697    0.000 10700.595    0.001 adam.py:55(step)
               21829010  277.933    0.000 10687.065    0.000 container.py:115(forward)
                8732314 1968.164    0.000 9255.663    0.001 functional.py:53(adam)
                4366158  572.602    0.000 8862.505    0.002 layers.py:684(update)
                4366157  322.541    0.000 7465.277    0.002 layers.py:17(step)
                8730539  194.979    0.000 7131.537    0.001 agent.py:49(__call__)
              436615700  647.976    0.000 7107.582    0.000 layer.py:98(move)
                8732314   51.392    0.000 5824.281    0.001 tensor.py:181(backward)
                8732314   29.293    0.000 5772.889    0.001 __init__.py:68(backward)
                8732314 5519.931    0.001 5519.931    0.001 {method 'run_backward' of 'torch._C._EngineBase' objects}
              382604854 5275.362    0.000 5275.362    0.000 {built-in method clone}
                4366157 3258.000    0.001 5252.181    0.001 replaybuffer.py:22(sample_data)
                4366157 2790.115    0.001 5025.418    0.001 agent.py:67(modify)
               12480029   90.040    0.000 4032.869    0.000 layers.py:740(restart)
               43658020   72.171    0.000 3872.632    0.000 conv.py:422(forward)
               43658020   78.458    0.000 3772.401    0.000 conv.py:414(_conv_forward)
               43658020 3677.909    0.000 3677.909    0.000 {built-in method conv2d}
              436615700 1066.870    0.000 3529.609    0.000 layers.py:735(check)
               56754716  122.887    0.000 3480.457    0.000 linear.py:92(forward)
               56754716  208.760    0.000 3300.449    0.000 functional.py:1669(linear)
               12480029   48.996    0.000 3134.511    0.000 level.py:8(__init__)
               12480029  131.945    0.000 2640.977    0.000 levels.py:122(generate)
               48671365  418.041    0.000 2387.255    0.000 level.py:41(notUsed)
               56754716 2379.020    0.000 2379.020    0.000 {built-in method addmm}
              436615700  519.312    0.000 2274.672    0.000 layers.py:729(isFree)
                4366157   58.498    0.000 2250.058    0.001 agent.py:112(__call__)
              550135836 1390.366    0.000 2192.840    0.000 tensor.py:933(grad)
                8732314  198.402    0.000 2143.776    0.000 optimizer.py:167(zero_grad)
               13096696   94.266    0.000 2139.993    0.000 agent.py:59(modify_board)
               34927481 2090.322    0.000 2090.322    0.000 {built-in method cat}
              157181652 1931.820    0.000 1931.820    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
               26196948 1150.376    0.000 1914.536    0.000 layer.py:167(NoRock_update)
             1214401030  570.260    0.000 1855.125    0.000 {built-in method builtins.any}
             2564328197 1405.161    0.000 1755.360    0.000 layer.py:95(isFree)
                4366157   75.974    0.000 1694.850    0.000 replaybuffer.py:18(stacker)
              157181652 1638.268    0.000 1638.268    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
               78583726   63.288    0.000 1602.328    0.000 activation.py:713(forward)
              395701550 1569.935    0.000 1569.935    0.000 {method 'unsqueeze' of 'torch._C._TensorBase' objects}
               78583726   99.153    0.000 1539.040    0.000 functional.py:1292(leaky_relu)
               78583726 1430.310    0.000 1430.310    0.000 {built-in method torch._C._nn.leaky_relu}
               13096696 1344.649    0.000 1344.649    0.000 {built-in method torch._C._nn.one_hot}
               18673802 1287.567    0.000 1287.567    0.000 {built-in method tensor}
             4814057896  793.450    0.000 1149.259    0.000 enum.py:646(__hash__)
               30565319  160.558    0.000 1143.905    0.000 tensor.py:21(wrapped)
              716045914  363.195    0.000 1095.688    0.000 overrides.py:1070(has_torch_function)
               48671365   34.714    0.000 1089.638    0.000 level.py:38(elementsIn)
               78590826 1062.316    0.000 1062.316    0.000 {method 'add' of 'torch._C._TensorBase' objects}
              467181119  165.539    0.000 1055.063    0.000 {built-in method builtins.all}
                4366157  608.293    0.000 1025.574    0.000 collector.py:46(collect)
               78590826  969.466    0.000  969.466    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
                8732314    9.805    0.000  950.774    0.000 game.py:37(board)
             1700096452  409.887    0.000  919.317    0.000 layers.py:690(<genexpr>)
               78590826  876.057    0.000  876.057    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
             2968950397  711.809    0.000  870.121    0.000 layers.py:700(<genexpr>)
               78590826  786.502    0.000  786.502    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
               74880174   70.548    0.000  783.226    0.000 layer.py:69(restart)
                8730539  275.595    0.000  771.262    0.000 exploration.py:53(softmaxer)
              436615700  455.385    0.000  714.109    0.000 layers.py:141(check)
               48671365  343.032    0.000  697.531    0.000 level.py:39(<listcomp>)
               78590826  619.321    0.000  619.321    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
               12480129  294.968    0.000  590.238    0.000 layers.py:36(reset)
             2245090563  556.018    0.000  556.018    0.000 level.py:32(inverse)
              436615700  356.959    0.000  546.495    0.000 layers.py:48(check)
              436615700  325.721    0.000  514.054    0.000 layers.py:124(check)
                8732314   12.081    0.000  487.583    0.000 loss.py:445(forward)
             1845956745  481.359    0.000  481.359    0.000 layer.py:146(elements)
               21830785  477.804    0.000  477.804    0.000 {method 'eq' of 'torch._C._TensorBase' objects}
                8732314   45.687    0.000  475.502    0.000 functional.py:2637(mse_loss)
              902841037  336.269    0.000  465.261    0.000 layer.py:130(add)
             5468771083  463.573    0.000  463.573    0.000 layer.py:91(positions)
               56754716  463.488    0.000  463.488    0.000 {method 't' of 'torch._C._TensorBase' objects}
        4171381133/4171381131  307.339    0.000  432.675    0.000 {built-in method builtins.len}
              436615700  288.970    0.000  430.335    0.000 layers.py:23(check)
               12480029  230.730    0.000  418.609    0.000 level.py:16(<dictcomp>)
               26196942  415.297    0.000  415.297    0.000 {built-in method sum}
             1519410990  321.683    0.000  409.381    0.000 overrides.py:1083(<genexpr>)
             2201451638  375.436    0.000  375.436    0.000 enum.py:352(<genexpr>)
               48671365  221.934    0.000  357.393    0.000 {built-in method _functools.reduce}
             4814089687  355.814    0.000  355.814    0.000 {built-in method builtins.hash}
               43658020   37.851    0.000  303.962    0.000 flatten.py:39(forward)
              183862317  200.891    0.000  302.734    0.000 layers.py:113(isDone)
                8732314  300.641    0.000  300.641    0.000 {built-in method torch._C._nn.mse_loss}
              435150106  201.473    0.000  296.568    0.000 layer.py:126(remove)
                4366157  107.797    0.000  291.382    0.000 random.py:315(sample)
                4367903  279.109    0.000  279.109    0.000 {method 'ne' of 'torch._C._TensorBase' objects}
                8733623  271.948    0.000  271.948    0.000 {built-in method max}


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@hpc.dtu.dk>
Subject: Job 9550926: <DoorsAndKey_teleport_0> in cluster <dcc> Done

Job <DoorsAndKey_teleport_0> was submitted from host <n-62-30-4> by user <s183905> in cluster <dcc> at Tue Apr 20 16:21:52 2021
Job was executed on host(s) <n-62-20-2>, in queue <gpuv100>, as user <s183905> in cluster <dcc> at Tue Apr 27 08:23:24 2021
</zhome/ee/d/137643> was used as the home directory.
</zhome/ee/d/137643/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Tue Apr 27 08:23:24 2021
Terminated at Wed Apr 28 08:18:34 2021
Results reported at Wed Apr 28 08:18:34 2021

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

    CPU time :                                   85895.90 sec.
    Max Memory :                                 2680 MB
    Average Memory :                             2677.56 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               13704.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                8
    Run time :                                   86111 sec.
    Turnaround time :                            662202 sec.

The output (if any) is above this job summary.


/zhome/ee/d/137643/Desktop/Bachelor/project-env/lib/python3.8/site-packages/torch/cuda/__init__.py:52: UserWarning: CUDA initialization: Found no NVIDIA driver on your system. Please check that you have an NVIDIA GPU and installed a driver from http://www.nvidia.com/Download/index.aspx (Triggered internally at  /pytorch/c10/cuda/CUDAFunctions.cpp:100.)
  return torch._C._cuda_getDeviceCount() > 0
Start
True
True
['main.py', '-name', 'Test_CPU_9-0', '-level', 'Levels.Causal3', '-batch', '25']
{'name': 'Test_CPU_9-0', 'main': <function teleport at 0x7febc68c2ee0>, 'level': <Levels.Causal3: <class 'levels.Causal3'>>, 'failed_actions_chance': 0, 'use_model': True, 'depth': 3, 'model_explore': 1000000, 'samples': 5, 'hours': 0.1, 'batch': 25, 'width': 9, 'height': 9, 'graphMode': <GraphMode.UCB1: 1>, 'network1': <Networks.Teleporter: 1>, 'K1': 5000000, 'learner1': <Learners.Qlearn: 1>, 'exploration1': <Explorations.softmaxer: 2>, 'gamma1': 0.98, 'network2': <Networks.Mini: 2>, 'K2': 1000000, 'learner2': <Learners.Qlearn: 1>, 'exploration2': <Explorations.epsilonGreedy: 1>, 'gamma2': 0.95, 'layer_Blocks': True, 'layer_Goal': True, 'layer_Gold': True, 'layer_Keys': True, 'layer_Door': True, 'layer_Holder': True, 'layer_Putter': True, 'layer_Rock': True, 'layer_Dirt': True, 'layer_Diamond1': True, 'layer_Diamond2': True, 'layer_Diamond3': True, 'layer_Diamond4': True, 'layer_Reddoor': True, 'layer_Redkeys': True, 'layer_Bluedoor': True, 'layer_Bluekeys': True, 'layer_Pink1': True, 'layer_Pink2': True, 'layer_Pink3': True, 'layer_Brown1': True, 'layer_Brown2': True, 'layer_Brown3': True, 'layer_Greendown': True, 'layer_Greenup': True, 'layer_Greenstar': True, 'layer_Yellowstar': True, 'layer_Bluestar': True, 'layer_Coconut': True, 'layer_Monster': True, 'layer_Greencross': True, 'layer_Bluecross': True, 'layer_Redcross': True, 'layer_Purplecross': True, 'layer_Super1': True, 'layer_Super2': True, 'layer_Super3': True, 'layer_Super4': True, 'layer_Super5': True, 'layer_Super6': True, 'layer_Super7': True, 'epsilon_cap': 0.2, 'softmax_cap': 0.02, 'update': 10000, 'reset_chance': 0.002, 'modified_done_chance': 0.05, 'miss_intervention_cost': -0.15, 'intervention_cost': -0.05, 'replay_size': 100000, 'sample_size': 50, 'CF_convert': 3, 'Counterfacts': 1, 'TopN': 6, 'Random_counterfacts': False}

# Parameters

    Name :                      Test_CPU_9-0
    Main :                      teleport
    Level :                     Levels.Causal3
    Failed actions chance :     0
    Use model :                 True
    Depth :                     3
    Model explore :             1000000
    Samples :                   5
    Hours :                     0.1
    Batch :                     25
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
    Layer super1 :              True
    Layer super2 :              True
    Layer super3 :              True
    Layer super4 :              True
    Layer super5 :              True
    Layer super6 :              True
    Layer super7 :              True
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
    Minutes used :              0 minutes.
    Hours used :                0 hours.

# Profiling


      56765 function calls (56551 primitive calls) in 0.04 seconds

##    Ordered by: cumulative time
   List reduced from 191 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000    0.042    0.042 {built-in method builtins.exec}
                      1    0.000    0.000    0.042    0.042 <string>:1(<module>)
                      1    0.000    0.000    0.042    0.042 main.py:46(teleport)
                      1    0.001    0.001    0.020    0.020 game.py:9(__init__)
                      2    0.000    0.000    0.017    0.009 agent.py:16(__init__)
                      2    0.000    0.000    0.017    0.008 network.py:37(__init__)
                      6    0.000    0.000    0.015    0.002 network.py:17(__init__)
                      1    0.000    0.000    0.012    0.012 layers.py:793(update)
                     25    0.000    0.000    0.011    0.000 layers.py:849(restart)
                      1    0.000    0.000    0.010    0.010 agent.py:39(__init__)
                     27    0.000    0.000    0.009    0.000 init.py:352(kaiming_uniform_)
                     54    0.008    0.000    0.008    0.000 {method 'uniform_' of 'torch._C._TensorBase' objects}
                     25    0.000    0.000    0.008    0.000 level.py:8(__init__)
                      1    0.000    0.000    0.007    0.007 agent.py:109(__init__)
                     12    0.000    0.000    0.007    0.001 conv.py:394(__init__)
                     12    0.001    0.000    0.006    0.001 conv.py:37(__init__)
                     25    0.001    0.000    0.006    0.000 levels.py:164(generate)
                     15    0.000    0.000    0.006    0.000 linear.py:74(__init__)
                     15    0.000    0.000    0.005    0.000 linear.py:85(reset_parameters)
                     12    0.000    0.000    0.005    0.000 conv.py:85(reset_parameters)
                     50    0.001    0.000    0.005    0.000 level.py:41(notUsed)
                      1    0.000    0.000    0.004    0.004 layers.py:751(__init__)
                      7    0.000    0.000    0.004    0.001 layers.py:782(add)
                      1    0.000    0.000    0.004    0.004 replaybuffer.py:8(__init__)
                      1    0.004    0.004    0.004    0.004 replaybuffer.py:11(<listcomp>)
                     50    0.002    0.000    0.003    0.000 layers.py:36(reset)
                      8    0.000    0.000    0.003    0.000 layer.py:61(__init__)
                      1    0.000    0.000    0.003    0.003 game.py:30(<setcomp>)
                    200    0.000    0.000    0.003    0.000 layer.py:77(restart)
                     41    0.001    0.000    0.003    0.000 game.py:30(<listcomp>)
                   1030    0.002    0.000    0.003    0.000 module.py:781(__setattr__)
                     74    0.001    0.000    0.002    0.000 module.py:223(__init__)
                     50    0.000    0.000    0.002    0.000 level.py:38(elementsIn)
                      6    0.000    0.000    0.002    0.000 module.py:529(to)
                   72/6    0.000    0.000    0.002    0.000 module.py:357(_apply)
                   1636    0.002    0.000    0.002    0.000 level.py:32(inverse)
                   4498    0.001    0.000    0.001    0.000 enum.py:646(__hash__)
                   5347    0.001    0.000    0.001    0.000 enum.py:352(<genexpr>)
                   2087    0.001    0.000    0.001    0.000 layer.py:138(add)
                     50    0.001    0.000    0.001    0.000 level.py:39(<listcomp>)
                   2360    0.001    0.000    0.001    0.000 types.py:171(__get__)
                     25    0.000    0.000    0.001    0.000 level.py:16(<dictcomp>)
                      8    0.001    0.000    0.001    0.000 layer.py:175(NoRock_update)
                   4756    0.001    0.000    0.001    0.000 layer.py:190(grid)
                      7    0.000    0.000    0.001    0.000 inspect.py:325(getmembers)
                     54    0.001    0.000    0.001    0.000 init.py:271(_calculate_fan_in_and_fan_out)
                     21    0.000    0.000    0.001    0.000 activation.py:708(__init__)
                   2965    0.000    0.000    0.001    0.000 {built-in method builtins.isinstance}
                     50    0.000    0.000    0.001    0.000 {built-in method _functools.reduce}
                     50    0.000    0.000    0.001    0.000 random.py:315(sample)
                      2    0.000    0.000    0.001    0.000 learner.py:16(__init__)
                     27    0.000    0.000    0.001    0.000 init.py:342(_calculate_correct_fan)
                      2    0.000    0.000    0.001    0.000 adam.py:34(__init__)
                      2    0.000    0.000    0.001    0.000 optimizer.py:33(__init__)
                      6    0.000    0.000    0.000    0.000 container.py:60(__init__)
                   5015    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
                   4498    0.000    0.000    0.000    0.000 {built-in method builtins.hash}
                      8    0.000    0.000    0.000    0.000 layer.py:71(<listcomp>)
                     12    0.000    0.000    0.000    0.000 flatten.py:34(__init__)
                    168    0.000    0.000    0.000    0.000 {built-in method builtins.hasattr}
                     54    0.000    0.000    0.000    0.000 module.py:294(register_parameter)
                     54    0.000    0.000    0.000    0.000 tensor.py:933(grad)
                     27    0.000    0.000    0.000    0.000 init.py:109(uniform_)
                   2359    0.000    0.000    0.000    0.000 enum.py:659(name)
                     27    0.000    0.000    0.000    0.000 init.py:12(_no_grad_uniform_)
                    200    0.000    0.000    0.000    0.000 layer.py:147(clear2)
                   2976    0.000    0.000    0.000    0.000 {method 'get' of 'dict' objects}
                     20    0.000    0.000    0.000    0.000 module.py:1068(parameters)
                    222    0.000    0.000    0.000    0.000 module.py:765(__getattr__)
                     20    0.000    0.000    0.000    0.000 module.py:1092(named_parameters)
                    126    0.000    0.000    0.000    0.000 overrides.py:1070(has_torch_function)
                    138    0.000    0.000    0.000    0.000 module.py:1166(children)
                   2103    0.000    0.000    0.000    0.000 layer.py:154(elements)
                     20    0.000    0.000    0.000    0.000 module.py:1055(_named_members)
                   1792    0.000    0.000    0.000    0.000 {method 'split' of 'str' objects}
                    160    0.000    0.000    0.000    0.000 abc.py:96(__instancecheck__)
                     54    0.000    0.000    0.000    0.000 module.py:607(convert)
                   2100    0.000    0.000    0.000    0.000 level.py:39(<lambda>)
                    108    0.000    0.000    0.000    0.000 grad_mode.py:85(__enter__)
                     72    0.000    0.000    0.000    0.000 tensor.py:596(__hash__)
                     60    0.000    0.000    0.000    0.000 module.py:333(add_module)
                     60    0.000    0.000    0.000    0.000 utils.py:8(parse)
                    216    0.000    0.000    0.000    0.000 grad_mode.py:166(__init__)
                     54    0.000    0.000    0.000    0.000 module.py:361(compute_should_use_set_data)
                     25    0.000    0.000    0.000    0.000 {built-in method builtins.all}
                    160    0.000    0.000    0.000    0.000 {built-in method _abc._abc_instancecheck}
                    215    0.000    0.000    0.000    0.000 random.py:250(_randbelow_with_getrandbits)
                    138    0.000    0.000    0.000    0.000 module.py:1175(named_children)
                     54    0.000    0.000    0.000    0.000 parameter.py:23(__new__)
                    108    0.000    0.000    0.000    0.000 grad_mode.py:89(__exit__)
                    225    0.000    0.000    0.000    0.000 layers.py:799(<genexpr>)
                      1    0.000    0.000    0.000    0.000 server.py:15(getvals)
                      2    0.000    0.000    0.000    0.000 optimizer.py:207(add_param_group)
                      1    0.000    0.000    0.000    0.000 layers.py:306(__init__)
                    462    0.000    0.000    0.000    0.000 inspect.py:72(isclass)
                    126    0.000    0.000    0.000    0.000 {built-in method builtins.any}
                    763    0.000    0.000    0.000    0.000 {method 'add' of 'set' objects}
                    108    0.000    0.000    0.000    0.000 grad_mode.py:80(__init__)
                     54    0.000    0.000    0.000    0.000 {built-in method _make_subclass}
                   44/3    0.000    0.000    0.000    0.000 abc.py:100(__subclasscheck__)


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@hpc.dtu.dk>
Subject: Job 9605521: <Test_CPU_9_0> in cluster <dcc> Done

Job <Test_CPU_9_0> was submitted from host <n-62-27-18> by user <s183905> in cluster <dcc> at Sun May  2 14:17:44 2021
Job was executed on host(s) <n-62-31-3>, in queue <hpc>, as user <s183905> in cluster <dcc> at Sun May  2 14:17:46 2021
</zhome/ee/d/137643> was used as the home directory.
</zhome/ee/d/137643/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Sun May  2 14:17:46 2021
Terminated at Sun May  2 14:17:48 2021
Results reported at Sun May  2 14:17:48 2021

Your job looked like:

------------------------------------------------------------
# LSBATCH: User input
#!/bin/sh
#BSUB -q hpc
#BSUB -n 1
#BSUB -R "rusage[mem=16G]"
#BSUB -R "span[hosts=1]"
#BSUB -W 20
# end of BSUB options
cd ..
module -s load python3
source ../project-env/bin/activate

python main.py $MYARGS
------------------------------------------------------------

Successfully completed.

Resource usage summary:

    CPU time :                                   1.35 sec.
    Max Memory :                                 -
    Average Memory :                             -
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               -
    Max Swap :                                   -
    Max Processes :                              -
    Max Threads :                                -
    Run time :                                   34 sec.
    Turnaround time :                            4 sec.

The output (if any) is above this job summary.


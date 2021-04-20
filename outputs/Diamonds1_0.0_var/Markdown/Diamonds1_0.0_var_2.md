
# Parameters

    Name :                      Diamonds1_0.0_var-2
    Main :                      graphTrain
    Level :                     Levels.Causal2
    Failed actions chance :     0.0
    Hours :                     10.0
    Batch :                     100
    Width :                     9
    Height :                    9
    Graphmode :                 GraphMode.var
    Network1 :                  Networks.Teleporter
    K1 :                        200000.0
    Learner1 :                  Learners.Qlearn
    Exploration1 :              Explorations.softmaxer
    Gamma1 :                    0.98
    Network2 :                  Networks.Mini
    K2 :                        100000.0
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
    Softmax cap :               0.0
    Update :                    10000
    Reset chance :              0.002
    Modified done chance :      0.05
    Miss intervention cost :    -0.15
    Intervention cost :         -0.05
    Replay size :               100000
    Sample size :               50
    Cf convert :                3
    Counterfacts :              2
    Topn :                      5
    Random counterfacts :       False
    Minutes used :              595 minutes.
    Hours used :                9 hours.

# Profiling


      22046639304 function calls (21492675949 primitive calls) in 35703.49 seconds

##    Ordered by: cumulative time
   List reduced from 463 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 35703.487 35703.487 {built-in method builtins.exec}
                      1    0.001    0.001 35703.487 35703.487 <string>:1(<module>)
                      1  171.124  171.124 35703.486 35703.486 allGraphsTrain.py:10(graphTrain)
                 731169 5517.261    0.008 13147.163    0.018 allGraphs.py:146(transformNot)
              731175248 8448.300    0.000 8448.300    0.000 {method 'item' of 'torch._C._TensorBase' objects}
                 731169   17.827    0.000 8256.790    0.011 allGraphsTrain.py:29(<listcomp>)
               73848170 1947.479    0.000 8238.982    0.000 allGraphs.py:110(states)
              658052500 6182.632    0.000 6182.632    0.000 {method 'sum' of 'torch._C._TensorBase' objects}
                 731169    2.655    0.000 4435.147    0.006 game.py:41(step)
                 731169    3.413    0.000 4286.886    0.006 layers.py:718(step)
                 731169  668.585    0.001 2930.953    0.004 allGraphsTrain.py:35(<listcomp>)
                 731170  105.187    0.000 2502.536    0.003 layers.py:684(update)
               11023554   19.575    0.000 2262.367    0.000 allGraphs.py:158(getInterventions)
                 731169  137.197    0.000 2071.198    0.003 allGraphsTrain.py:37(<listcomp>)
                 731169   56.981    0.000 1776.899    0.002 layers.py:17(step)
               73116900  123.954    0.000 1713.592    0.000 layer.py:98(move)
                 731169    2.399    0.000 1608.438    0.002 agent.py:29(learn)
                 731169   14.907    0.000 1604.487    0.002 agent.py:117(_learn)
                 731169   46.780    0.000 1589.579    0.002 learner.py:42(Qlearn)
                3868818   31.268    0.000 1469.583    0.000 layers.py:740(restart)
               17783501 1427.469    0.000 1427.469    0.000 {built-in method tensor}
               14679400    9.197    0.000 1329.745    0.000 game.py:37(board)
               77503914  178.715    0.000 1282.796    0.000 tensor.py:21(wrapped)
                 731169   60.874    0.000 1223.601    0.002 allGraphsTrain.py:44(<listcomp>)
               10452809   10.263    0.000 1198.727    0.000 allGraphs.py:129(rightIntervention)
                3868818   14.215    0.000 1173.962    0.000 level.py:8(__init__)
        118381796/10452809   87.219    0.000 1147.452    0.000 {built-in method builtins.min}
               29730722   14.249    0.000 1127.333    0.000 allGraphs.py:130(<lambda>)
        226310783/29730722  346.061    0.000 1113.085    0.000 allGraphs.py:74(expected_moves)
               73116900  225.618    0.000 1070.202    0.000 layers.py:735(check)
               11023554   47.891    0.000 1034.516    0.000 allGraphs.py:153(format)
                3868818   43.337    0.000 1027.200    0.000 levels.py:151(generate)
               18569290  170.751    0.000  937.562    0.000 level.py:41(notUsed)
        304509048/69678504   99.353    0.000  935.208    0.000 allGraphs.py:78(<genexpr>)
               76772745  879.533    0.000  879.533    0.000 {method 'eq' of 'torch._C._TensorBase' objects}
               73116900  813.412    0.000  813.412    0.000 {method 'argmax' of 'torch._C._TensorBase' objects}
             3175068726  548.664    0.000  800.192    0.000 enum.py:646(__hash__)
                 731169  421.271    0.001  738.391    0.001 agent.py:67(modify)
                 731169    4.373    0.000  634.930    0.001 grad_mode.py:23(decorate_context)
                 731169   22.226    0.000  622.602    0.001 adam.py:55(step)
        16816887/2193507   66.504    0.000  620.372    0.000 module.py:715(_call_impl)
                1462338    3.843    0.000  567.139    0.000 network.py:27(forward)
                1462338   15.256    0.000  554.532    0.000 container.py:115(forward)
                 731169  113.894    0.000  510.839    0.001 functional.py:53(adam)
               18569290   13.760    0.000  439.465    0.000 level.py:38(elementsIn)
               73116900  109.686    0.000  403.122    0.000 layers.py:729(isFree)
              200858737  112.933    0.000  383.918    0.000 {built-in method builtins.any}
                5118190  222.175    0.000  373.562    0.000 layer.py:167(NoRock_update)
                 731169    4.482    0.000  372.878    0.001 tensor.py:181(backward)
                 731169    2.529    0.000  368.395    0.001 __init__.py:68(backward)
                 731169  349.944    0.000  349.944    0.000 {method 'run_backward' of 'torch._C._EngineBase' objects}
              118952541   73.232    0.000  349.730    0.000 allGraphs.py:83(layers_not_in)
              150620914   66.971    0.000  335.800    0.000 {built-in method builtins.all}
                 731169    8.766    0.000  329.016    0.000 agent.py:112(__call__)
              500631492  230.282    0.000  293.435    0.000 layer.py:95(isFree)
               18569290  138.625    0.000  284.128    0.000 level.py:39(<listcomp>)
              118952541  136.764    0.000  276.498    0.000 allGraphs.py:84(<listcomp>)
               76041576  260.773    0.000  260.773    0.000 {method 'flatten' of 'torch._C._TensorBase' objects}
               27081726   20.632    0.000  254.644    0.000 layer.py:69(restart)
             3175071155  251.529    0.000  251.529    0.000 {built-in method builtins.hash}
              377749247  105.348    0.000  249.813    0.000 layers.py:690(<genexpr>)
                2193507    8.725    0.000  248.412    0.000 tensor.py:576(__iter__)
                2193507  234.239    0.000  234.239    0.000 {method 'unbind' of 'torch._C._TensorBase' objects}
                2924676    5.579    0.000  220.131    0.000 conv.py:422(forward)
              127223540   65.811    0.000  216.475    0.000 overrides.py:1070(has_torch_function)
                2924676    6.354    0.000  212.632    0.000 conv.py:414(_conv_forward)
               73116900  129.011    0.000  211.440    0.000 layers.py:219(check)
                2924676  205.200    0.000  205.200    0.000 {built-in method conv2d}
               73116900  123.223    0.000  203.845    0.000 layers.py:231(check)
               73116900  121.179    0.000  203.103    0.000 layers.py:207(check)
                3868918  100.545    0.000  202.132    0.000 layers.py:36(reset)
              891559297  193.093    0.000  193.093    0.000 level.py:32(inverse)
              553985456  151.661    0.000  185.628    0.000 layers.py:700(<genexpr>)
              226310783  117.449    0.000  171.679    0.000 allGraphs.py:45(p)
                2924676    6.979    0.000  163.256    0.000 linear.py:92(forward)
               40945518   95.856    0.000  160.214    0.000 tensor.py:933(grad)
                2924676   12.063    0.000  153.256    0.000 functional.py:1669(linear)
              807773381  145.638    0.000  145.638    0.000 enum.py:352(<genexpr>)
               18569290   88.871    0.000  141.577    0.000 {built-in method _functools.reduce}
                 731169   14.245    0.000  140.868    0.000 optimizer.py:167(zero_grad)
             1463410316  139.757    0.000  139.757    0.000 layer.py:91(positions)
               73117000   81.220    0.000  126.001    0.000 layers.py:113(isDone)
                3868818   61.756    0.000  122.666    0.000 level.py:16(<dictcomp>)
              212694864   84.700    0.000  115.483    0.000 layer.py:130(add)
                 731169    5.372    0.000  111.409    0.000 agent.py:59(modify_board)
                 731169   64.263    0.000  110.148    0.000 collector.py:46(collect)
                2924676  108.181    0.000  108.181    0.000 {built-in method addmm}
               11698704  101.783    0.000  101.783    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
              431774490   94.894    0.000   94.894    0.000 layer.py:146(elements)
               73116900   59.172    0.000   93.060    0.000 layers.py:196(check)
              334875670   71.549    0.000   84.868    0.000 overrides.py:1083(<genexpr>)
               11698704   84.561    0.000   84.561    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
               73116900   54.627    0.000   78.844    0.000 layers.py:23(check)
                 731169   52.422    0.000   78.710    0.000 allGraphsTrain.py:43(<listcomp>)
                4387014    4.035    0.000   73.384    0.000 activation.py:713(forward)
                 731169   73.161    0.000   73.161    0.000 {built-in method torch._C._nn.one_hot}
                4387014    6.466    0.000   69.348    0.000 functional.py:1292(leaky_relu)
                5849352   63.848    0.000   63.848    0.000 {method 'add' of 'torch._C._TensorBase' objects}
                4387014   62.272    0.000   62.272    0.000 {built-in method torch._C._nn.leaky_relu}
                 731169   17.030    0.000   61.754    0.000 allGraphs.py:137(transform)


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@hpc.dtu.dk>
Subject: Job 9532036: <Diamonds1_0.0_var_2> in cluster <dcc> Done

Job <Diamonds1_0.0_var_2> was submitted from host <n-62-30-7> by user <s183905> in cluster <dcc> at Sat Apr 17 13:28:45 2021
Job was executed on host(s) <n-62-11-13>, in queue <gpuv100>, as user <s183905> in cluster <dcc> at Tue Apr 20 02:33:56 2021
</zhome/ee/d/137643> was used as the home directory.
</zhome/ee/d/137643/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Tue Apr 20 02:33:56 2021
Terminated at Tue Apr 20 12:29:03 2021
Results reported at Tue Apr 20 12:29:03 2021

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
#BSUB -W 720
# end of BSUB options
cd ..
module -s load python3
source ../project-env/bin/activate

python main.py $LSB_PROJECT_NAME


------------------------------------------------------------

Successfully completed.

Resource usage summary:

    CPU time :                                   35640.60 sec.
    Max Memory :                                 2061 MB
    Average Memory :                             2060.79 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               14323.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                8
    Run time :                                   35707 sec.
    Turnaround time :                            255618 sec.

The output (if any) is above this job summary.


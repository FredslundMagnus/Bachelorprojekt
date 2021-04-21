
# Parameters

    Name :                      Diamonds4_0.0_UCB1-2
    Main :                      graphTrain
    Level :                     Levels.Causal7
    Failed actions chance :     0.0
    Hours :                     10.0
    Batch :                     100
    Width :                     9
    Height :                    9
    Graphmode :                 GraphMode.UCB1
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


      16642520948 function calls (16274671483 primitive calls) in 35709.13 seconds

##    Ordered by: cumulative time
   List reduced from 464 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 35709.132 35709.132 {built-in method builtins.exec}
                      1    0.002    0.002 35709.132 35709.132 <string>:1(<module>)
                      1  149.508  149.508 35709.131 35709.131 allGraphsTrain.py:10(graphTrain)
                 604334 6446.206    0.011 14480.502    0.024 allGraphs.py:146(transformNot)
                 604334   15.680    0.000 8804.299    0.015 allGraphsTrain.py:29(<listcomp>)
               61037835 2303.960    0.000 8788.678    0.000 allGraphs.py:110(states)
              604339232 8186.257    0.000 8186.257    0.000 {method 'item' of 'torch._C._TensorBase' objects}
              543901000 7024.319    0.000 7024.319    0.000 {method 'sum' of 'torch._C._TensorBase' objects}
                 604334    2.140    0.000 3101.211    0.005 game.py:41(step)
                 604334    2.843    0.000 2966.635    0.005 layers.py:718(step)
                 604334  671.755    0.001 2443.241    0.004 allGraphsTrain.py:35(<listcomp>)
                 604334  163.434    0.000 2166.127    0.004 allGraphsTrain.py:37(<listcomp>)
                8991186   13.121    0.000 1771.486    0.000 allGraphs.py:158(getInterventions)
                 604334    1.981    0.000 1606.148    0.003 agent.py:29(learn)
                 604334   12.367    0.000 1602.875    0.003 agent.py:117(_learn)
                 604334   46.889    0.000 1590.509    0.003 learner.py:42(Qlearn)
                 604335   79.740    0.000 1571.278    0.003 layers.py:684(update)
                 604334   41.563    0.000 1389.248    0.002 layers.py:17(step)
               60433400   92.656    0.000 1342.635    0.000 layer.py:98(move)
               64059404  159.581    0.000 1307.884    0.000 tensor.py:21(wrapped)
                 604334   56.596    0.000 1254.737    0.002 allGraphsTrain.py:44(<listcomp>)
               14584157 1241.400    0.000 1241.400    0.000 {built-in method tensor}
               12012857    7.388    0.000 1151.622    0.000 game.py:37(board)
               63455070  971.629    0.000  971.629    0.000 {method 'eq' of 'torch._C._TensorBase' objects}
               60433400  893.825    0.000  893.825    0.000 {method 'argmax' of 'torch._C._TensorBase' objects}
                8991186   41.418    0.000  890.229    0.000 allGraphs.py:153(format)
                2429843   18.187    0.000  872.761    0.000 layers.py:740(restart)
                8991186    7.971    0.000  868.135    0.000 allGraphs.py:133(UCB1)
               60433400  176.307    0.000  834.100    0.000 layers.py:735(check)
        80928542/8991186   52.261    0.000  826.688    0.000 {built-in method builtins.min}
               22757120    9.544    0.000  812.663    0.000 allGraphs.py:134(<lambda>)
        152865898/22757120  217.490    0.000  803.119    0.000 allGraphs.py:68(expected_moves_UCB1)
                2429843    8.554    0.000  699.445    0.000 level.py:8(__init__)
                 604334  403.096    0.001  697.928    0.001 agent.py:67(modify)
                 604334    3.401    0.000  674.362    0.001 grad_mode.py:23(decorate_context)
                 604334   17.297    0.000  664.125    0.001 adam.py:55(step)
        202046134/48329866   57.032    0.000  657.320    0.000 allGraphs.py:72(<genexpr>)
                2429843   25.212    0.000  609.410    0.000 levels.py:441(generate)
        13899682/1813002   55.099    0.000  577.590    0.000 module.py:715(_call_impl)
                 604334  121.370    0.000  572.206    0.001 functional.py:53(adam)
               11663301  101.717    0.000  556.989    0.000 level.py:41(notUsed)
             2251105662  369.673    0.000  532.108    0.000 enum.py:646(__hash__)
                1208668    3.187    0.000  529.057    0.000 network.py:27(forward)
                1208668   13.143    0.000  518.665    0.000 container.py:115(forward)
                 604334    3.298    0.000  362.033    0.001 tensor.py:181(backward)
                 604334    2.070    0.000  358.735    0.001 __init__.py:68(backward)
                 604334  341.368    0.001  341.368    0.001 {method 'run_backward' of 'torch._C._EngineBase' objects}
               60433400   88.123    0.000  327.138    0.000 layers.py:729(isFree)
                 604334    7.567    0.000  305.385    0.001 agent.py:112(__call__)
               62850736  296.494    0.000  296.494    0.000 {method 'flatten' of 'torch._C._TensorBase' objects}
              166783912   85.892    0.000  290.470    0.000 {built-in method builtins.any}
                4230345  160.079    0.000  271.785    0.000 layer.py:167(NoRock_update)
               11663301    8.054    0.000  262.195    0.000 level.py:38(elementsIn)
              418263016  188.095    0.000  239.015    0.000 layer.py:95(isFree)
               80928542   48.626    0.000  226.495    0.000 allGraphs.py:83(layers_not_in)
              152865898  134.629    0.000  217.644    0.000 allGraphs.py:60(UCB1)
                2417336    3.995    0.000  204.271    0.000 conv.py:422(forward)
                1813002    7.308    0.000  200.543    0.000 tensor.py:576(__iter__)
                2417336    4.542    0.000  198.757    0.000 conv.py:414(_conv_forward)
                2417336  193.411    0.000  193.411    0.000 {built-in method conv2d}
                1813002  188.254    0.000  188.254    0.000 {method 'unbind' of 'torch._C._TensorBase' objects}
              124492904   40.162    0.000  185.107    0.000 {built-in method builtins.all}
               80928542   87.866    0.000  177.868    0.000 allGraphs.py:84(<listcomp>)
               11663301   83.314    0.000  169.378    0.000 level.py:39(<listcomp>)
              105154250   51.414    0.000  169.296    0.000 overrides.py:1070(has_torch_function)
               60433400  101.286    0.000  164.220    0.000 layers.py:632(check)
             2251107675  162.436    0.000  162.436    0.000 {built-in method builtins.hash}
               60433400   96.139    0.000  159.121    0.000 layers.py:617(check)
               60433400   96.800    0.000  159.006    0.000 layers.py:602(check)
                2417336    5.438    0.000  154.398    0.000 linear.py:92(forward)
               17008901   13.068    0.000  149.563    0.000 layer.py:69(restart)
                2417336    9.802    0.000  146.490    0.000 functional.py:1669(linear)
               33842758   88.269    0.000  139.260    0.000 tensor.py:933(grad)
              464029256  112.315    0.000  138.023    0.000 layers.py:700(<genexpr>)
                 604334   12.656    0.000  135.365    0.000 optimizer.py:167(zero_grad)
              203628320   51.687    0.000  129.818    0.000 layers.py:690(<genexpr>)
                9669344  119.702    0.000  119.702    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
                2429943   58.420    0.000  117.522    0.000 layers.py:36(reset)
                 604334   69.421    0.000  116.768    0.000 collector.py:46(collect)
              559983353  113.911    0.000  113.911    0.000 level.py:32(inverse)
             1204825082  110.724    0.000  110.724    0.000 layer.py:91(positions)
                2417336  105.478    0.000  105.478    0.000 {built-in method addmm}
                9669344  102.339    0.000  102.339    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
                 604334    4.458    0.000  101.587    0.000 agent.py:59(modify_board)
              507354677   86.521    0.000   86.521    0.000 enum.py:352(<genexpr>)
               11663301   53.154    0.000   84.763    0.000 {built-in method _functools.reduce}
                2429843   39.346    0.000   75.916    0.000 level.py:16(<dictcomp>)
              147469485   54.550    0.000   74.634    0.000 layer.py:130(add)
                3626004    3.173    0.000   73.480    0.000 activation.py:713(forward)
               60433400   46.091    0.000   72.310    0.000 layers.py:588(check)
                3626004    5.200    0.000   70.307    0.000 functional.py:1292(leaky_relu)
              300983228   68.624    0.000   68.624    0.000 layer.py:146(elements)
              276785240   55.635    0.000   66.187    0.000 overrides.py:1083(<genexpr>)
                4834672   65.561    0.000   65.561    0.000 {method 'add' of 'torch._C._TensorBase' objects}
                 604334   64.711    0.000   64.711    0.000 {built-in method torch._C._nn.one_hot}
                3626004   64.625    0.000   64.625    0.000 {built-in method torch._C._nn.leaky_relu}
               60433400   41.827    0.000   62.127    0.000 layers.py:23(check)
                 604334   40.851    0.000   61.197    0.000 allGraphsTrain.py:43(<listcomp>)
                4834672   58.721    0.000   58.721    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
                4834672   54.576    0.000   54.576    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@hpc.dtu.dk>
Subject: Job 9532033: <Diamonds4_0.0_UCB1_2> in cluster <dcc> Done

Job <Diamonds4_0.0_UCB1_2> was submitted from host <n-62-30-7> by user <s183905> in cluster <dcc> at Sat Apr 17 13:28:44 2021
Job was executed on host(s) <n-62-20-2>, in queue <gpuv100>, as user <s183905> in cluster <dcc> at Mon Apr 19 20:05:50 2021
</zhome/ee/d/137643> was used as the home directory.
</zhome/ee/d/137643/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Mon Apr 19 20:05:50 2021
Terminated at Tue Apr 20 06:01:06 2021
Results reported at Tue Apr 20 06:01:06 2021

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

    CPU time :                                   35619.34 sec.
    Max Memory :                                 2063 MB
    Average Memory :                             2060.89 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               14321.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                8
    Run time :                                   35715 sec.
    Turnaround time :                            232342 sec.

The output (if any) is above this job summary.


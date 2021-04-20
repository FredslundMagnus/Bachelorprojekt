
# Parameters

    Name :                      Diamonds3_0.5_var-2
    Main :                      graphTrain
    Level :                     Levels.Causal6
    Failed actions chance :     0.5
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


      28148323607 function calls (25406783408 primitive calls) in 35708.88 seconds

##    Ordered by: cumulative time
   List reduced from 465 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 35708.881 35708.881 {built-in method builtins.exec}
                      1    0.001    0.001 35708.881 35708.881 <string>:1(<module>)
                      1  114.616  114.616 35708.879 35708.879 allGraphsTrain.py:10(graphTrain)
                 461780 5909.213    0.013 13263.183    0.029 allGraphs.py:146(transformNot)
                 461780   12.891    0.000 8325.206    0.018 allGraphsTrain.py:29(<listcomp>)
               46639881 2151.569    0.000 8312.367    0.000 allGraphs.py:110(states)
              554140188 7493.159    0.000 7493.159    0.000 {method 'item' of 'torch._C._TensorBase' objects}
              507958500 6536.759    0.000 6536.759    0.000 {method 'sum' of 'torch._C._TensorBase' objects}
                 461780  552.720    0.001 6494.752    0.014 allGraphsTrain.py:35(<listcomp>)
                9518709   18.059    0.000 5942.033    0.001 allGraphs.py:158(getInterventions)
                8711703    7.526    0.000 4873.874    0.001 allGraphs.py:129(rightIntervention)
        490938312/8711703  257.025    0.000 4829.740    0.001 {built-in method builtins.min}
               33675554   13.369    0.000 4812.576    0.000 allGraphs.py:130(<lambda>)
        973164921/33675554 1415.026    0.000 4799.207    0.000 allGraphs.py:74(expected_moves)
        1421715976/111127736  382.537    0.000 4585.128    0.000 allGraphs.py:78(<genexpr>)
                 461780    1.703    0.000 2332.044    0.005 game.py:41(step)
                 461780    2.170    0.000 2225.940    0.005 layers.py:718(step)
                 461780  128.555    0.000 1654.348    0.004 allGraphsTrain.py:37(<listcomp>)
             6895499326 1079.725    0.000 1598.374    0.000 enum.py:646(__hash__)
              491745318  260.921    0.000 1501.601    0.000 allGraphs.py:83(layers_not_in)
                 461781   63.052    0.000 1344.082    0.003 layers.py:684(update)
               13799883 1304.656    0.000 1304.656    0.000 {built-in method tensor}
                 461780    1.552    0.000 1242.421    0.003 agent.py:29(learn)
              491745318  582.700    0.000 1240.680    0.000 allGraphs.py:84(<listcomp>)
                 461780    9.452    0.000 1239.927    0.003 agent.py:117(_learn)
               11827610    7.195    0.000 1235.477    0.000 game.py:37(board)
                 461780   35.354    0.000 1230.475    0.003 learner.py:42(Qlearn)
                9518709   46.223    0.000 1036.893    0.000 allGraphs.py:153(format)
               48948680  123.951    0.000 1009.525    0.000 tensor.py:21(wrapped)
                 461780   43.485    0.000  968.892    0.002 allGraphsTrain.py:44(<listcomp>)
                 461780   32.755    0.000  877.226    0.002 layers.py:17(step)
               46178000   68.990    0.000  840.139    0.000 layer.py:98(move)
               48486900  746.038    0.000  746.038    0.000 {method 'eq' of 'torch._C._TensorBase' objects}
                1653328   13.010    0.000  717.704    0.000 layers.py:740(restart)
              973164921  461.622    0.000  694.637    0.000 allGraphs.py:45(p)
               46178000  680.224    0.000  680.224    0.000 {method 'argmax' of 'torch._C._TensorBase' objects}
                1653328    6.186    0.000  593.419    0.000 level.py:8(__init__)
                1653328   20.783    0.000  530.369    0.000 levels.py:288(generate)
                 461780  300.089    0.001  525.310    0.001 agent.py:67(modify)
                 461780    2.643    0.000  519.020    0.001 grad_mode.py:23(decorate_context)
             6895500891  518.650    0.000  518.650    0.000 {built-in method builtins.hash}
                 461780   13.285    0.000  511.247    0.001 adam.py:55(step)
                9919529   87.579    0.000  486.636    0.000 level.py:41(notUsed)
               46178000  107.507    0.000  452.992    0.000 layers.py:735(check)
        10620940/1385340   42.602    0.000  443.812    0.000 module.py:715(_call_impl)
                 461780   92.109    0.000  438.501    0.001 functional.py:53(adam)
                 923560    2.403    0.000  407.011    0.000 network.py:27(forward)
                 923560   10.325    0.000  399.021    0.000 container.py:115(forward)
                 461780    2.798    0.000  285.207    0.001 tensor.py:181(backward)
                 461780    1.821    0.000  282.409    0.001 __init__.py:68(backward)
                 461780  269.000    0.001  269.000    0.001 {method 'run_backward' of 'torch._C._EngineBase' objects}
               46178000   66.972    0.000  252.505    0.000 layers.py:729(isFree)
              127645307   69.563    0.000  250.896    0.000 {built-in method builtins.any}
                 461780    5.769    0.000  234.989    0.001 agent.py:112(__call__)
                9919529    6.846    0.000  229.353    0.000 level.py:38(elementsIn)
               48025120  228.616    0.000  228.616    0.000 {method 'flatten' of 'torch._C._TensorBase' objects}
                3694248  126.020    0.000  224.679    0.000 layer.py:167(NoRock_update)
               95126780   35.557    0.000  191.497    0.000 {built-in method builtins.all}
              341509756  145.287    0.000  185.534    0.000 layer.py:95(isFree)
              975357267  170.802    0.000  175.568    0.000 {built-in method builtins.max}
                1847120    3.124    0.000  155.353    0.000 conv.py:422(forward)
                1385340    5.321    0.000  154.254    0.000 tensor.py:576(__iter__)
                9919529   72.371    0.000  151.186    0.000 level.py:39(<listcomp>)
                1847120    3.532    0.000  151.044    0.000 conv.py:414(_conv_forward)
                1847120  146.860    0.000  146.860    0.000 {built-in method conv2d}
                1385340  145.127    0.000  145.127    0.000 {method 'unbind' of 'torch._C._TensorBase' objects}
              200913022   51.415    0.000  142.495    0.000 layers.py:690(<genexpr>)
               80349854   40.155    0.000  133.265    0.000 overrides.py:1070(has_torch_function)
              400722948  103.140    0.000  127.187    0.000 layers.py:700(<genexpr>)
                1847120    4.415    0.000  119.279    0.000 linear.py:92(forward)
                1847120    8.003    0.000  113.047    0.000 functional.py:1669(linear)
               25859734   69.688    0.000  110.055    0.000 tensor.py:933(grad)
               13226624    9.540    0.000  106.815    0.000 layer.py:69(restart)
                 461780    9.700    0.000  105.338    0.000 optimizer.py:167(zero_grad)
              470517217  103.005    0.000  103.005    0.000 level.py:32(inverse)
               23086006   59.347    0.000  100.250    0.000 layers.py:424(check)
                7388480   91.408    0.000   91.408    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
                 461780   52.911    0.000   89.014    0.000 collector.py:46(collect)
                1653428   40.828    0.000   82.457    0.000 layers.py:36(reset)
                1847120   81.003    0.000   81.003    0.000 {built-in method addmm}
                7388480   77.575    0.000   77.575    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
                 461780    3.364    0.000   77.214    0.000 agent.py:59(modify_board)
               46178100   47.885    0.000   75.429    0.000 layers.py:113(isDone)
                9919529   44.626    0.000   71.321    0.000 {built-in method _functools.reduce}
              416624381   69.853    0.000   69.853    0.000 enum.py:352(<genexpr>)
              695879670   67.414    0.000   67.414    0.000 layer.py:91(positions)
               23089149   38.869    0.000   65.261    0.000 layers.py:452(check)
               23078912   37.990    0.000   63.544    0.000 layers.py:437(check)
              214782978   57.997    0.000   57.997    0.000 layer.py:146(elements)
                2770680    2.457    0.000   56.487    0.000 activation.py:713(forward)
                2770680    3.945    0.000   54.030    0.000 functional.py:1292(leaky_relu)
              211495508   45.005    0.000   53.857    0.000 overrides.py:1083(<genexpr>)
              104354851   38.495    0.000   53.438    0.000 layer.py:130(add)
                1653328   27.283    0.000   52.534    0.000 level.py:16(<dictcomp>)
                3694240   52.403    0.000   52.403    0.000 {method 'add' of 'torch._C._TensorBase' objects}
                2770680   49.722    0.000   49.722    0.000 {built-in method torch._C._nn.leaky_relu}
                 461780   49.145    0.000   49.145    0.000 {built-in method torch._C._nn.one_hot}
                 461780   32.178    0.000   48.601    0.000 allGraphsTrain.py:43(<listcomp>)
                3694240   45.104    0.000   45.104    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
                3694240   41.856    0.000   41.856    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@hpc.dtu.dk>
Subject: Job 9532017: <Diamonds3_0.5_var_2> in cluster <dcc> Done

Job <Diamonds3_0.5_var_2> was submitted from host <n-62-30-7> by user <s183905> in cluster <dcc> at Sat Apr 17 13:28:42 2021
Job was executed on host(s) <n-62-20-7>, in queue <gpuv100>, as user <s183905> in cluster <dcc> at Sun Apr 18 19:10:12 2021
</zhome/ee/d/137643> was used as the home directory.
</zhome/ee/d/137643/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Sun Apr 18 19:10:12 2021
Terminated at Mon Apr 19 05:05:27 2021
Results reported at Mon Apr 19 05:05:27 2021

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

    CPU time :                                   35655.86 sec.
    Max Memory :                                 2064 MB
    Average Memory :                             2062.93 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               14320.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                8
    Run time :                                   35772 sec.
    Turnaround time :                            142605 sec.

The output (if any) is above this job summary.


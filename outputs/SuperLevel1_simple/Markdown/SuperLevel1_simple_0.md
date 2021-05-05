
# Parameters

    Name :                      SuperLevel1_simple-0
    Main :                      simple
    Level :                     Levels.SuperLevel
    Failed actions chance :     0
    Use model :                 True
    Depth :                     3
    Model explore :             1000000
    Samples :                   5
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
    Network2 :                  Networks.MiniBig
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
    Minutes used :              1435 minutes.
    Hours used :                23 hours.

# Profiling


      170024057119 function calls (169835112852 primitive calls) in 86119.88 seconds

##    Ordered by: cumulative time
   List reduced from 424 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 86119.885 86119.885 {built-in method builtins.exec}
                      1    0.001    0.001 86119.885 86119.885 <string>:1(<module>)
                      1  138.222  138.222 86119.883 86119.883 main.py:67(simple)
                7872663   31.402    0.000 59241.134    0.008 game.py:42(step)
                7872663   39.815    0.000 57041.003    0.007 layers.py:827(step)
                7872663  694.425    0.000 42335.868    0.005 layers.py:17(step)
              787266300 2561.807    0.000 41572.582    0.000 layer.py:106(move)
              787266300 5293.997    0.000 30795.681    0.000 layers.py:844(check)
                7872663   27.848    0.000 20500.355    0.003 agent.py:29(learn)
                7872663  188.936    0.000 20454.085    0.003 agent.py:117(_learn)
                7872663  538.927    0.000 20265.148    0.003 learner.py:42(Qlearn)
                7872664 1105.413    0.000 14613.289    0.002 layers.py:793(update)
                7872663   51.447    0.000 8193.996    0.001 grad_mode.py:23(decorate_context)
        212561901/23617989  820.966    0.000 8153.908    0.000 module.py:715(_call_impl)
                7872663  275.665    0.000 8048.433    0.001 adam.py:55(step)
               15745326   39.463    0.000 7537.314    0.000 network.py:28(forward)
               15745326  196.225    0.000 7396.864    0.000 container.py:115(forward)
              787266300 5233.645    0.000 7259.536    0.000 layers.py:471(check)
              787266300 1579.643    0.000 6802.100    0.000 layers.py:838(isFree)
                7872663 1464.605    0.000 6585.370    0.001 functional.py:53(adam)
              102344632 3315.891    0.000 5823.854    0.000 layer.py:159(update)
            23371272299 4067.462    0.000 5789.227    0.000 enum.py:646(__hash__)
             1517720333 1250.732    0.000 5247.981    0.000 {built-in method builtins.any}
             6687364152 3986.716    0.000 5222.458    0.000 layer.py:103(isFree)
                7872663   47.068    0.000 4569.415    0.001 tensor.py:181(backward)
                7872663   29.138    0.000 4522.346    0.001 __init__.py:68(backward)
              787266300 3158.490    0.000 4445.155    0.000 layers.py:77(check)
                7872663 4302.068    0.001 4302.068    0.001 {method 'run_backward' of 'torch._C._EngineBase' objects}
                7872663   99.473    0.000 4227.985    0.001 agent.py:112(__call__)
            10887659020 2971.738    0.000 3605.274    0.000 layers.py:809(<genexpr>)
               33401560 3279.810    0.000 3279.810    0.000 {built-in method tensor}
               15745326   19.315    0.000 2746.831    0.000 game.py:38(board)
               31490652   54.089    0.000 2688.040    0.000 conv.py:422(forward)
               31490652   68.039    0.000 2611.742    0.000 conv.py:414(_conv_forward)
               31490652 2532.489    0.000 2532.489    0.000 {built-in method conv2d}
            26193586919 2508.464    0.000 2508.464    0.000 layer.py:99(positions)
               47235978  106.829    0.000 2462.107    0.000 linear.py:92(forward)
              787266300 1559.983    0.000 2456.606    0.000 layers.py:286(check)
               47235978  183.477    0.000 2306.457    0.000 functional.py:1669(linear)
              787266300 1410.275    0.000 2272.548    0.000 layers.py:246(check)
              551086440 1280.860    0.000 2132.723    0.000 tensor.py:933(grad)
                7872663  178.966    0.000 1848.036    0.000 optimizer.py:167(zero_grad)
            23371303888 1721.770    0.000 1721.770    0.000 {built-in method builtins.hash}
                9576470  110.273    0.000 1709.088    0.000 layers.py:849(restart)
               47235978 1613.296    0.000 1613.296    0.000 {built-in method addmm}
             2218669584 1408.595    0.000 1408.595    0.000 layer.py:154(elements)
              787266300  919.961    0.000 1396.374    0.000 layers.py:141(check)
              787266300  867.276    0.000 1354.610    0.000 layers.py:273(check)
              157453260 1336.493    0.000 1336.493    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
              787266300  809.222    0.000 1272.260    0.000 layers.py:313(check)
              787266300  803.380    0.000 1156.518    0.000 layers.py:62(check)
              157453260 1120.828    0.000 1120.828    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
              787266400  212.542    0.000 1077.732    0.000 {built-in method builtins.all}
              677049098  353.642    0.000 1050.363    0.000 overrides.py:1070(has_torch_function)
              787266300  687.049    0.000 1033.087    0.000 layers.py:48(check)
               62981304   54.147    0.000 1025.815    0.000 activation.py:713(forward)
              787266300  670.332    0.000 1017.826    0.000 layers.py:124(check)
               62981304   87.908    0.000  971.668    0.000 functional.py:1292(leaky_relu)
             2361870460  576.489    0.000  958.898    0.000 layers.py:799(<genexpr>)
            11058330273  887.521    0.000  887.521    0.000 {method 'random' of '_random.Random' objects}
               62981304  875.065    0.000  875.065    0.000 {built-in method torch._C._nn.leaky_relu}
              787266300  603.361    0.000  870.852    0.000 layers.py:23(check)
              124494110  128.064    0.000  837.418    0.000 layer.py:77(restart)
               78726630  753.204    0.000  753.204    0.000 {method 'add' of 'torch._C._TensorBase' objects}
        11515389336/11515389335  680.624    0.000  731.152    0.000 {built-in method builtins.len}
                9576470   47.202    0.000  722.136    0.000 level.py:8(__init__)
               78726630  710.354    0.000  710.354    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
                7872663  397.612    0.000  685.359    0.000 collector.py:46(collect)
               78726630  622.403    0.000  622.403    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
             4830968409  613.874    0.000  613.874    0.000 layer.py:211(isBlocking)
             9332279160  577.319    0.000  577.319    0.000 layer.py:92(isDead)
             1008509524  409.603    0.000  555.289    0.000 layer.py:138(add)
               78726630  552.455    0.000  552.455    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
                9576570  242.498    0.000  494.667    0.000 layers.py:36(reset)
             1574532600  491.099    0.000  491.099    0.000 {method 'union' of 'set' objects}
               78726630  424.593    0.000  424.593    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
                7872663   11.747    0.000  409.267    0.000 loss.py:445(forward)
              486723748  267.211    0.000  407.064    0.000 layer.py:134(remove)
                7872663   47.016    0.000  397.520    0.000 functional.py:2637(mse_loss)
             1401334174  313.527    0.000  386.528    0.000 overrides.py:1083(<genexpr>)
                9576470  177.660    0.000  363.014    0.000 level.py:16(<dictcomp>)
                7872663   29.559    0.000  362.961    0.000 exploration.py:47(epsilonGreedy)
              102344632  328.886    0.000  328.886    0.000 layer.py:171(<listcomp>)
              787266400  231.403    0.000  319.766    0.000 layers.py:508(isDone)
              102344632  306.124    0.000  306.124    0.000 layer.py:172(<listcomp>)
               47235978  293.474    0.000  293.474    0.000 {method 't' of 'torch._C._TensorBase' objects}
                9576470  175.559    0.000  272.831    0.000 levels.py:316(generate)
             3135155334  249.528    0.000  249.528    0.000 {method 'append' of 'list' objects}
                7872663  244.795    0.000  244.795    0.000 {method 'tolist' of 'torch._C._TensorBase' objects}
                7872663  226.200    0.000  226.200    0.000 {built-in method torch._C._nn.mse_loss}
               15745326  221.607    0.000  221.607    0.000 {built-in method sum}
               78726680   94.735    0.000  215.111    0.000 tensor.py:596(__hash__)
                7873450  209.819    0.000  209.819    0.000 {built-in method max}
                7872663   39.499    0.000  183.820    0.000 __init__.py:28(_make_grads)
               31490652   24.996    0.000  173.832    0.000 flatten.py:39(forward)
                7872663  170.631    0.000  170.631    0.000 {built-in method gather}
                7872663   39.882    0.000  163.014    0.000 tensor.py:506(__rsub__)
              787266300  132.534    0.000  160.850    0.000 layers.py:506(<listcomp>)
             1574532600  155.033    0.000  155.033    0.000 layer.py:86(check)
              212561901  151.806    0.000  151.806    0.000 {built-in method torch._C._get_tracing_state}


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@hpc.dtu.dk>
Subject: Job 9578846: <SuperLevel1_simple_0> in cluster <dcc> Done

Job <SuperLevel1_simple_0> was submitted from host <n-62-30-3> by user <s183905> in cluster <dcc> at Mon Apr 26 20:44:06 2021
Job was executed on host(s) <n-62-20-12>, in queue <gpuv100>, as user <s183905> in cluster <dcc> at Mon May  3 06:21:17 2021
</zhome/ee/d/137643> was used as the home directory.
</zhome/ee/d/137643/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Mon May  3 06:21:17 2021
Terminated at Tue May  4 06:16:48 2021
Results reported at Tue May  4 06:16:48 2021

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

    CPU time :                                   85890.01 sec.
    Max Memory :                                 2065 MB
    Average Memory :                             2062.12 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               14319.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                8
    Run time :                                   86131 sec.
    Turnaround time :                            639162 sec.

The output (if any) is above this job summary.


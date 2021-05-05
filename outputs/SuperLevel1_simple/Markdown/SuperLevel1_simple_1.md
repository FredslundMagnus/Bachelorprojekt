
# Parameters

    Name :                      SuperLevel1_simple-1
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


      168864319852 function calls (168680896497 primitive calls) in 86109.37 seconds

##    Ordered by: cumulative time
   List reduced from 423 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 86109.375 86109.375 {built-in method builtins.exec}
                      1    0.002    0.002 86109.374 86109.374 <string>:1(<module>)
                      1  136.583  136.583 86109.372 86109.372 main.py:67(simple)
                7642625   29.211    0.000 59684.644    0.008 game.py:42(step)
                7642625   37.426    0.000 57547.337    0.008 layers.py:827(step)
                7642625  697.678    0.000 43429.628    0.006 layers.py:17(step)
              764262500 2482.092    0.000 42660.889    0.000 layer.py:106(move)
              764262500 5188.639    0.000 30571.718    0.000 layers.py:844(check)
                7642625   29.396    0.000 20204.872    0.003 agent.py:29(learn)
                7642625  184.239    0.000 20158.190    0.003 agent.py:117(_learn)
                7642625  530.421    0.000 19973.951    0.003 learner.py:42(Qlearn)
                7642626 1090.101    0.000 14030.096    0.002 layers.py:793(update)
              764262500 2009.847    0.000 8172.961    0.000 layers.py:838(isFree)
                7642625   48.374    0.000 8080.011    0.001 grad_mode.py:23(decorate_context)
        206350875/22927875  817.166    0.000 7971.303    0.000 module.py:715(_call_impl)
                7642625  279.777    0.000 7939.317    0.001 adam.py:55(step)
               15285250   38.521    0.000 7365.110    0.000 network.py:28(forward)
               15285250  194.464    0.000 7230.314    0.000 container.py:115(forward)
              764262500 5079.170    0.000 7141.862    0.000 layers.py:471(check)
                7642625 1438.268    0.000 6450.764    0.001 functional.py:53(adam)
             8865820076 4718.447    0.000 6163.114    0.000 layer.py:103(isFree)
            22720561449 4079.951    0.000 5894.597    0.000 enum.py:646(__hash__)
               99354138 3252.520    0.000 5724.856    0.000 layer.py:159(update)
             1473021128 1223.224    0.000 5143.116    0.000 {built-in method builtins.any}
                7642625   49.528    0.000 4489.482    0.001 tensor.py:181(backward)
              764262500 3162.723    0.000 4460.988    0.000 layers.py:77(check)
                7642625   28.001    0.000 4439.955    0.001 __init__.py:68(backward)
                7642625 4227.867    0.001 4227.867    0.001 {method 'run_backward' of 'torch._C._EngineBase' objects}
                7642625   91.041    0.000 4134.657    0.001 agent.py:112(__call__)
            10564600158 2921.318    0.000 3533.769    0.000 layers.py:809(<genexpr>)
               32434068 3181.561    0.000 3181.561    0.000 {built-in method tensor}
               15285250   17.874    0.000 2660.716    0.000 game.py:38(board)
               30570500   55.726    0.000 2611.281    0.000 conv.py:422(forward)
            25684584264 2566.446    0.000 2566.446    0.000 layer.py:99(positions)
               30570500   63.370    0.000 2534.095    0.000 conv.py:414(_conv_forward)
               30570500 2459.572    0.000 2459.572    0.000 {built-in method conv2d}
              764262500 1529.843    0.000 2412.235    0.000 layers.py:286(check)
               45855750  111.762    0.000 2409.849    0.000 linear.py:92(forward)
              764262500 1412.634    0.000 2299.564    0.000 layers.py:246(check)
               45855750  174.227    0.000 2250.917    0.000 functional.py:1669(linear)
              534983780 1335.483    0.000 2175.548    0.000 tensor.py:933(grad)
                7642625  179.833    0.000 1866.895    0.000 optimizer.py:167(zero_grad)
            22720592118 1814.652    0.000 1814.652    0.000 {built-in method builtins.hash}
                9648303  115.452    0.000 1754.020    0.000 layers.py:849(restart)
               45855750 1579.082    0.000 1579.082    0.000 {built-in method addmm}
              764262500  913.528    0.000 1388.282    0.000 layers.py:313(check)
             2182197727 1385.728    0.000 1385.728    0.000 layer.py:154(elements)
              764262500  821.788    0.000 1294.897    0.000 layers.py:273(check)
              152852500 1293.483    0.000 1293.483    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
              764262500  815.456    0.000 1281.776    0.000 layers.py:141(check)
              764262500  780.796    0.000 1140.804    0.000 layers.py:62(check)
              152852500 1087.951    0.000 1087.951    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
              764262500  697.151    0.000 1053.626    0.000 layers.py:124(check)
              657265830  346.744    0.000 1033.881    0.000 overrides.py:1070(has_torch_function)
              764262500  679.917    0.000 1032.274    0.000 layers.py:48(check)
               61141000   53.132    0.000  992.054    0.000 activation.py:713(forward)
               61141000   79.523    0.000  938.922    0.000 functional.py:1292(leaky_relu)
              764262500  629.414    0.000  913.341    0.000 layers.py:23(check)
            10736262534  880.760    0.000  880.760    0.000 {method 'random' of '_random.Random' objects}
              125427939  129.203    0.000  861.219    0.000 layer.py:77(restart)
               61141000  850.972    0.000  850.972    0.000 {built-in method torch._C._nn.leaky_relu}
               76426250  747.832    0.000  747.832    0.000 {method 'add' of 'torch._C._TensorBase' objects}
             6714638913  744.539    0.000  744.539    0.000 layer.py:211(isBlocking)
                9648303   49.595    0.000  737.343    0.000 level.py:8(__init__)
        11336197924/11336197923  678.065    0.000  730.653    0.000 {built-in method builtins.len}
               76426250  698.560    0.000  698.560    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
                7642625  389.555    0.000  674.533    0.000 collector.py:46(collect)
              764262600  135.763    0.000  665.262    0.000 {built-in method builtins.all}
             1528593854  318.601    0.000  623.446    0.000 layers.py:799(<genexpr>)
               76426250  619.948    0.000  619.948    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
              993232474  414.409    0.000  561.869    0.000 layer.py:138(add)
             9055371564  548.872    0.000  548.872    0.000 layer.py:92(isDead)
               76426250  540.553    0.000  540.553    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
                9648403  250.396    0.000  510.773    0.000 layers.py:36(reset)
             1528525000  494.093    0.000  494.093    0.000 {method 'union' of 'set' objects}
               76426250  420.352    0.000  420.352    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
                7642625   11.438    0.000  402.865    0.000 loss.py:445(forward)
              466931228  267.478    0.000  401.808    0.000 layer.py:134(remove)
                7642625   45.746    0.000  391.427    0.000 functional.py:2637(mse_loss)
             1360387410  308.198    0.000  380.438    0.000 overrides.py:1083(<genexpr>)
                7642625   29.793    0.000  364.931    0.000 exploration.py:47(epsilonGreedy)
                9648303  175.971    0.000  364.067    0.000 level.py:16(<dictcomp>)
               99354138  324.285    0.000  324.285    0.000 layer.py:171(<listcomp>)
              764262600  219.524    0.000  304.832    0.000 layers.py:508(isDone)
               99354138  299.645    0.000  299.645    0.000 layer.py:172(<listcomp>)
               45855750  287.187    0.000  287.187    0.000 {method 't' of 'torch._C._TensorBase' objects}
                9648303  181.726    0.000  282.364    0.000 levels.py:316(generate)
             3074798698  251.367    0.000  251.367    0.000 {method 'append' of 'list' objects}
                7642625  239.294    0.000  239.294    0.000 {method 'tolist' of 'torch._C._TensorBase' objects}
                7642625  224.750    0.000  224.750    0.000 {built-in method torch._C._nn.mse_loss}
               15285250  216.921    0.000  216.921    0.000 {built-in method sum}
               76426300   96.186    0.000  215.892    0.000 tensor.py:596(__hash__)
                7643389  206.941    0.000  206.941    0.000 {built-in method max}
                7642625   34.297    0.000  177.148    0.000 __init__.py:28(_make_grads)
               30570500   24.987    0.000  171.820    0.000 flatten.py:39(forward)
                7642625  169.419    0.000  169.419    0.000 {built-in method gather}
                7642625   38.057    0.000  158.864    0.000 tensor.py:506(__rsub__)
              764262500  129.357    0.000  157.070    0.000 layers.py:506(<listcomp>)
             1528525000  152.218    0.000  152.218    0.000 layer.py:86(check)
              206350875  146.908    0.000  146.908    0.000 {built-in method torch._C._get_tracing_state}


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@hpc.dtu.dk>
Subject: Job 9578847: <SuperLevel1_simple_1> in cluster <dcc> Done

Job <SuperLevel1_simple_1> was submitted from host <n-62-30-3> by user <s183905> in cluster <dcc> at Mon Apr 26 20:44:06 2021
Job was executed on host(s) <n-62-20-11>, in queue <gpuv100>, as user <s183905> in cluster <dcc> at Mon May  3 06:27:16 2021
</zhome/ee/d/137643> was used as the home directory.
</zhome/ee/d/137643/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Mon May  3 06:27:16 2021
Terminated at Tue May  4 06:22:31 2021
Results reported at Tue May  4 06:22:31 2021

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

    CPU time :                                   85901.22 sec.
    Max Memory :                                 2065 MB
    Average Memory :                             2063.84 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               14319.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                8
    Run time :                                   86115 sec.
    Turnaround time :                            639505 sec.

The output (if any) is above this job summary.


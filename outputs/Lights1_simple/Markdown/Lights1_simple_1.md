
# Parameters

    Name :                      Lights1_simple-1
    Main :                      simple
    Level :                     Levels.Causal3
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


      168672707150 function calls (168418814139 primitive calls) in 86113.43 seconds

##    Ordered by: cumulative time
   List reduced from 414 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 86113.433 86113.433 {built-in method builtins.exec}
                      1    0.001    0.001 86113.433 86113.433 <string>:1(<module>)
                      1  156.987  156.987 86113.432 86113.432 main.py:66(simple)
               10578860   36.798    0.000 51015.099    0.005 game.py:41(step)
               10578860   47.765    0.000 48789.522    0.005 layers.py:718(step)
               10578860   30.421    0.000 27325.837    0.003 agent.py:29(learn)
               10578860  242.361    0.000 27274.641    0.003 agent.py:117(_learn)
               10578860  701.787    0.000 27032.279    0.003 learner.py:42(Qlearn)
               10578860  848.241    0.000 26104.965    0.002 layers.py:17(step)
             1057886000 1620.124    0.000 25167.030    0.000 layer.py:98(move)
               10578861 1458.161    0.000 22575.265    0.002 layers.py:684(update)
             1057886000 3657.626    0.000 16823.240    0.000 layers.py:735(check)
               10578860   62.393    0.000 11248.675    0.001 grad_mode.py:23(decorate_context)
               10578860  363.262    0.000 11067.283    0.001 adam.py:55(step)
        285629220/31736580 1076.858    0.000 10572.238    0.000 module.py:715(_call_impl)
               21157720   51.405    0.000 9806.586    0.000 network.py:27(forward)
               21157720  258.300    0.000 9632.905    0.000 container.py:115(forward)
               10578860 2057.857    0.000 9159.598    0.001 functional.py:53(adam)
               29774412  254.646    0.000 8683.460    0.000 layers.py:740(restart)
               29774412  113.242    0.000 6133.228    0.000 level.py:8(__init__)
               10578860   64.508    0.000 6079.101    0.001 tensor.py:181(backward)
               10578860   35.990    0.000 6014.593    0.001 __init__.py:68(backward)
               10578860 5745.581    0.001 5745.581    0.001 {method 'run_backward' of 'torch._C._EngineBase' objects}
             1057886000 1284.924    0.000 5744.875    0.000 layers.py:729(isFree)
               10578860  122.459    0.000 5503.890    0.001 agent.py:112(__call__)
               29774412  563.556    0.000 5048.446    0.000 levels.py:164(generate)
               84630888 2821.001    0.000 5016.608    0.000 layer.py:167(NoRock_update)
             2022524609 1251.792    0.000 4612.993    0.000 {built-in method builtins.any}
            18137478453 3176.569    0.000 4601.494    0.000 enum.py:646(__hash__)
             5676956139 3478.317    0.000 4459.952    0.000 layer.py:95(isFree)
               59548824  501.014    0.000 3715.426    0.000 level.py:41(notUsed)
               42315440   72.255    0.000 3449.955    0.000 conv.py:422(forward)
               42315440   81.362    0.000 3351.029    0.000 conv.py:414(_conv_forward)
               42315440 3254.932    0.000 3254.932    0.000 {built-in method conv2d}
             1057886100  614.887    0.000 3248.007    0.000 {built-in method builtins.all}
             1057886000 2007.681    0.000 3244.195    0.000 layers.py:286(check)
               63473160  136.765    0.000 3196.100    0.000 linear.py:92(forward)
             1057886000 1923.817    0.000 3178.247    0.000 layers.py:246(check)
               44774579 3121.087    0.000 3121.087    0.000 {built-in method tensor}
               63473160  225.571    0.000 2999.601    0.000 functional.py:1669(linear)
             9253005192 2358.430    0.000 2858.902    0.000 layers.py:700(<genexpr>)
              740520230 1672.825    0.000 2770.650    0.000 tensor.py:933(grad)
             6565368554 1696.257    0.000 2764.322    0.000 layers.py:690(<genexpr>)
               21157720   23.545    0.000 2470.043    0.000 game.py:37(board)
               10578860  240.500    0.000 2450.939    0.000 optimizer.py:167(zero_grad)
              238195296  259.881    0.000 2213.328    0.000 layer.py:69(restart)
               63473160 2117.352    0.000 2117.352    0.000 {built-in method addmm}
              211577200 1832.556    0.000 1832.556    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
             1057886000 1106.352    0.000 1763.577    0.000 layers.py:273(check)
            18771231422 1692.783    0.000 1692.783    0.000 layer.py:91(positions)
             1057886000 1042.692    0.000 1662.127    0.000 layers.py:313(check)
              211577200 1541.700    0.000 1541.700    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
               59548824   52.935    0.000 1509.095    0.000 level.py:38(elementsIn)
               29774512  747.906    0.000 1474.721    0.000 layers.py:36(reset)
            18137520842 1424.933    0.000 1424.933    0.000 {built-in method builtins.hash}
             1057886000  889.119    0.000 1368.522    0.000 layers.py:48(check)
               84630880   74.804    0.000 1364.572    0.000 activation.py:713(forward)
              909782040  445.828    0.000 1342.624    0.000 overrides.py:1070(has_torch_function)
               84630880  114.805    0.000 1289.768    0.000 functional.py:1292(leaky_relu)
             4075052746 1279.193    0.000 1279.193    0.000 layer.py:146(elements)
             1953320144 1270.048    0.000 1270.048    0.000 level.py:32(inverse)
               84630880 1163.922    0.000 1163.922    0.000 {built-in method torch._C._nn.leaky_relu}
             1057886000  766.131    0.000 1120.589    0.000 layers.py:23(check)
              105788600 1112.525    0.000 1112.525    0.000 {method 'add' of 'torch._C._TensorBase' objects}
              105788600  980.447    0.000  980.447    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
             1955589839  721.166    0.000  979.485    0.000 layer.py:130(add)
               59548824  462.275    0.000  924.846    0.000 level.py:39(<listcomp>)
               10578860  536.046    0.000  922.065    0.000 collector.py:46(collect)
               29774412  424.218    0.000  893.284    0.000 level.py:16(<dictcomp>)
              105788600  861.068    0.000  861.068    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
        11264541935/11264541934  699.407    0.000  765.010    0.000 {built-in method builtins.len}
             9668517723  749.775    0.000  749.775    0.000 {method 'random' of '_random.Random' objects}
              105788600  742.115    0.000  742.115    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
             3215638027  602.645    0.000  602.645    0.000 enum.py:352(<genexpr>)
              105788600  590.211    0.000  590.211    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
               59548824  319.057    0.000  531.313    0.000 {built-in method _functools.reduce}
               59548824  208.009    0.000  530.049    0.000 random.py:315(sample)
               10578860   15.843    0.000  516.751    0.000 loss.py:445(forward)
               10578860   54.339    0.000  500.908    0.000 functional.py:2637(mse_loss)
             8224893504  500.472    0.000  500.472    0.000 layer.py:84(isDead)
             1883037240  399.517    0.000  495.308    0.000 overrides.py:1083(<genexpr>)
               10578860   36.401    0.000  432.012    0.000 exploration.py:47(epsilonGreedy)
             1057886100  302.474    0.000  414.028    0.000 layers.py:52(isDone)
             3574654942  407.397    0.000  407.397    0.000 layer.py:203(isBlocking)
             5453814782  392.523    0.000  392.523    0.000 {method 'append' of 'list' objects}
               63473160  382.614    0.000  382.614    0.000 {method 't' of 'torch._C._TensorBase' objects}
              217965858  245.374    0.000  379.028    0.000 layers.py:113(isDone)
              423429226  215.061    0.000  321.514    0.000 layer.py:126(remove)
               10578860  303.161    0.000  303.161    0.000 {method 'tolist' of 'torch._C._TensorBase' objects}
               21157720  300.068    0.000  300.068    0.000 {built-in method sum}
               10578860  292.925    0.000  292.925    0.000 {built-in method torch._C._nn.mse_loss}
             2441510640  292.751    0.000  292.751    0.000 layer.py:182(grid)
              369550855  202.211    0.000  288.910    0.000 random.py:250(_randbelow_with_getrandbits)
              105788650  120.254    0.000  276.692    0.000 tensor.py:596(__hash__)
             4231630496  275.009    0.000  275.009    0.000 layer.py:81(isDone)
               84630888  266.620    0.000  266.620    0.000 layer.py:178(<listcomp>)
               10579917  265.497    0.000  265.497    0.000 {built-in method max}
               84630888  249.022    0.000  249.022    0.000 layer.py:179(<listcomp>)
               42315440   30.863    0.000  228.283    0.000 flatten.py:39(forward)
               10578860   41.301    0.000  223.820    0.000 __init__.py:28(_make_grads)


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@hpc.dtu.dk>
Subject: Job 9578829: <Lights1_simple_1> in cluster <dcc> Done

Job <Lights1_simple_1> was submitted from host <n-62-30-3> by user <s183905> in cluster <dcc> at Mon Apr 26 20:44:03 2021
Job was executed on host(s) <n-62-11-13>, in queue <gpuv100>, as user <s183905> in cluster <dcc> at Wed Apr 28 10:58:26 2021
</zhome/ee/d/137643> was used as the home directory.
</zhome/ee/d/137643/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Wed Apr 28 10:58:26 2021
Terminated at Thu Apr 29 10:53:49 2021
Results reported at Thu Apr 29 10:53:49 2021

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

    CPU time :                                   86010.66 sec.
    Max Memory :                                 2064 MB
    Average Memory :                             2061.21 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               14320.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                8
    Run time :                                   86122 sec.
    Turnaround time :                            223786 sec.

The output (if any) is above this job summary.


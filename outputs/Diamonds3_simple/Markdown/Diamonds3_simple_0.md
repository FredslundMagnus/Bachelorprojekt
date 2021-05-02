
# Parameters

    Name :                      Diamonds3_simple-0
    Main :                      simple
    Level :                     Levels.Causal6
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


      147672217383 function calls (147454916660 primitive calls) in 86110.05 seconds

##    Ordered by: cumulative time
   List reduced from 409 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 86110.047 86110.047 {built-in method builtins.exec}
                      1    0.001    0.001 86110.047 86110.047 <string>:1(<module>)
                      1  152.405  152.405 86110.046 86110.046 main.py:66(simple)
                9054182   34.358    0.000 46369.260    0.005 game.py:41(step)
                9054182   46.189    0.000 44172.442    0.005 layers.py:718(step)
                9054182   30.728    0.000 31548.921    0.003 agent.py:29(learn)
                9054182  220.020    0.000 31498.885    0.003 agent.py:117(_learn)
                9054182  781.920    0.000 31278.865    0.003 learner.py:42(Qlearn)
                9054182  705.016    0.000 26069.359    0.003 layers.py:17(step)
              905418200 1538.067    0.000 25276.915    0.000 layer.py:98(move)
                9054183 1299.761    0.000 17999.789    0.002 layers.py:684(update)
              905418200 3361.331    0.000 16985.430    0.000 layers.py:735(check)
                9054182   56.098    0.000 13720.094    0.002 grad_mode.py:23(decorate_context)
                9054182  330.532    0.000 13555.436    0.001 adam.py:55(step)
                9054182 2491.033    0.000 11731.272    0.001 functional.py:53(adam)
        244462914/27162546 1051.276    0.000 11349.705    0.000 module.py:715(_call_impl)
               18108364   47.437    0.000 10554.007    0.001 network.py:27(forward)
               18108364  259.027    0.000 10388.368    0.001 container.py:115(forward)
                9054182   53.506    0.000 6904.941    0.001 tensor.py:181(backward)
                9054182   33.711    0.000 6851.435    0.001 __init__.py:68(backward)
                9054182 6565.705    0.001 6565.705    0.001 {method 'run_backward' of 'torch._C._EngineBase' objects}
               12448112  125.014    0.000 6088.125    0.000 layers.py:740(restart)
                9054182  119.810    0.000 5881.182    0.001 agent.py:112(__call__)
              905418200 1470.154    0.000 5371.546    0.000 layers.py:729(isFree)
               12448112   56.093    0.000 5031.307    0.000 level.py:8(__init__)
            17292348643 3138.480    0.000 4620.373    0.000 enum.py:646(__hash__)
               12448112  182.536    0.000 4501.075    0.000 levels.py:288(generate)
             1744063377 1152.837    0.000 4340.689    0.000 {built-in method builtins.any}
               72433464 2387.658    0.000 4277.121    0.000 layer.py:167(NoRock_update)
              905418200 2509.102    0.000 4160.462    0.000 layers.py:424(check)
               74691671  734.812    0.000 4123.682    0.000 level.py:41(notUsed)
             6641731205 3048.793    0.000 3901.392    0.000 layer.py:95(isFree)
               36216728   68.273    0.000 3609.854    0.000 conv.py:422(forward)
               54325092  129.067    0.000 3530.096    0.000 linear.py:92(forward)
               36216728   72.096    0.000 3515.086    0.000 conv.py:414(_conv_forward)
               36216728 3429.751    0.000 3429.751    0.000 {built-in method conv2d}
               54325092  215.905    0.000 3343.332    0.000 functional.py:1669(linear)
               38363736 3001.704    0.000 3001.704    0.000 {built-in method tensor}
              633792770 1814.940    0.000 2836.023    0.000 tensor.py:933(grad)
                9054182  258.922    0.000 2780.185    0.000 optimizer.py:167(zero_grad)
             8036731692 2211.456    0.000 2723.586    0.000 layers.py:700(<genexpr>)
              905418200 1644.009    0.000 2655.077    0.000 layers.py:452(check)
              905418200 1601.236    0.000 2590.901    0.000 layers.py:437(check)
              181083640 2451.899    0.000 2451.899    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
              905418300  209.345    0.000 2402.245    0.000 {built-in method builtins.all}
               54325092 2394.849    0.000 2394.849    0.000 {built-in method addmm}
             2089439457  524.618    0.000 2319.206    0.000 layers.py:690(<genexpr>)
               18108364   20.215    0.000 2272.358    0.000 game.py:37(board)
            19901306724 2118.337    0.000 2118.337    0.000 layer.py:91(positions)
              181083640 2097.907    0.000 2097.907    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
               74691671   55.831    0.000 1946.354    0.000 level.py:38(elementsIn)
              905418300 1027.846    0.000 1588.985    0.000 layers.py:113(isDone)
               72433456   63.325    0.000 1572.589    0.000 activation.py:713(forward)
               72433456   98.798    0.000 1509.265    0.000 functional.py:1292(leaky_relu)
            17292384952 1481.900    0.000 1481.900    0.000 {built-in method builtins.hash}
               72433456 1400.577    0.000 1400.577    0.000 {built-in method torch._C._nn.leaky_relu}
               90541820 1324.203    0.000 1324.203    0.000 {method 'add' of 'torch._C._TensorBase' objects}
               74691671  633.712    0.000 1275.602    0.000 level.py:39(<listcomp>)
              778659732  430.342    0.000 1254.367    0.000 overrides.py:1070(has_torch_function)
              905418200  785.962    0.000 1222.537    0.000 layers.py:402(check)
               90541820 1217.324    0.000 1217.324    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
              905418200  769.901    0.000 1200.679    0.000 layers.py:413(check)
               90541820 1117.158    0.000 1117.158    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
                9054182  635.557    0.000 1071.986    0.000 collector.py:46(collect)
             2652662145 1042.497    0.000 1042.497    0.000 layer.py:146(elements)
              905418200  704.842    0.000 1023.712    0.000 layers.py:23(check)
               90541820 1002.165    0.000 1002.165    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
               99584896   83.136    0.000  896.136    0.000 layer.py:69(restart)
             3542867798  863.507    0.000  863.507    0.000 level.py:32(inverse)
               90541820  788.407    0.000  788.407    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
             1258129776  536.875    0.000  739.428    0.000 layer.py:130(add)
        9797548315/9797548314  647.234    0.000  712.694    0.000 {built-in method builtins.len}
             6641731205  690.866    0.000  690.866    0.000 layer.py:203(isBlocking)
               12448212  339.489    0.000  685.423    0.000 layers.py:36(reset)
             8220058542  683.562    0.000  683.562    0.000 {method 'random' of '_random.Random' objects}
             3137033719  616.720    0.000  616.720    0.000 enum.py:352(<genexpr>)
               74691671  382.461    0.000  614.921    0.000 {built-in method _functools.reduce}
              791628986  399.813    0.000  587.053    0.000 layer.py:126(remove)
                9054182   13.434    0.000  545.790    0.000 loss.py:445(forward)
                9054182   48.913    0.000  532.355    0.000 functional.py:2637(mse_loss)
             7143761504  512.129    0.000  512.129    0.000 layer.py:84(isDead)
               54325092  470.022    0.000  470.022    0.000 {method 't' of 'torch._C._TensorBase' objects}
             1611644556  366.692    0.000  458.061    0.000 overrides.py:1083(<genexpr>)
                9054182   36.000    0.000  443.288    0.000 exploration.py:47(epsilonGreedy)
               12448112  221.645    0.000  439.231    0.000 level.py:16(<dictcomp>)
               18108364  348.855    0.000  348.855    0.000 {built-in method sum}
                9054182  339.143    0.000  339.143    0.000 {built-in method torch._C._nn.mse_loss}
             3844425259  334.911    0.000  334.911    0.000 {method 'append' of 'list' objects}
                9054182  305.078    0.000  305.078    0.000 {method 'tolist' of 'torch._C._TensorBase' objects}
                9055087  295.202    0.000  295.202    0.000 {built-in method max}
               36216728   29.315    0.000  271.846    0.000 flatten.py:39(forward)
               90541870  115.160    0.000  259.744    0.000 tensor.py:596(__hash__)
                9054182  251.259    0.000  251.259    0.000 {built-in method gather}
               72433464  243.941    0.000  243.941    0.000 layer.py:178(<listcomp>)
                9054182   41.634    0.000  243.674    0.000 __init__.py:28(_make_grads)
               36216728  242.531    0.000  242.531    0.000 {method 'flatten' of 'torch._C._TensorBase' objects}
              244462914  235.650    0.000  235.650    0.000 {built-in method torch._C._get_tracing_state}
             2614208485  232.460    0.000  232.460    0.000 level.py:39(<lambda>)
               72433464  230.398    0.000  230.398    0.000 layer.py:179(<listcomp>)
                9054182   45.257    0.000  224.603    0.000 tensor.py:506(__rsub__)


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@hpc.dtu.dk>
Subject: Job 9578840: <Diamonds3_simple_0> in cluster <dcc> Done

Job <Diamonds3_simple_0> was submitted from host <n-62-30-3> by user <s183905> in cluster <dcc> at Mon Apr 26 20:44:05 2021
Job was executed on host(s) <n-62-20-16>, in queue <gpuv100>, as user <s183905> in cluster <dcc> at Fri Apr 30 22:24:03 2021
</zhome/ee/d/137643> was used as the home directory.
</zhome/ee/d/137643/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Fri Apr 30 22:24:03 2021
Terminated at Sat May  1 22:19:20 2021
Results reported at Sat May  1 22:19:20 2021

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

    CPU time :                                   85897.05 sec.
    Max Memory :                                 2072 MB
    Average Memory :                             2070.99 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               14312.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                8
    Run time :                                   86119 sec.
    Turnaround time :                            437715 sec.

The output (if any) is above this job summary.



# Parameters

    Name :                      Diamonds3_simple-1
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


      193769482370 function calls (193562245927 primitive calls) in 86121.57 seconds

##    Ordered by: cumulative time
   List reduced from 408 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 86121.572 86121.572 {built-in method builtins.exec}
                      1    0.002    0.002 86121.572 86121.572 <string>:1(<module>)
                      1  135.366  135.366 86121.570 86121.570 main.py:66(simple)
                8634837   29.858    0.000 57124.931    0.007 game.py:41(step)
                8634837   40.957    0.000 55158.263    0.006 layers.py:718(step)
                8634838 1225.978    0.000 31126.009    0.004 layers.py:684(update)
                8634837  669.351    0.000 23938.027    0.003 layers.py:17(step)
              863483700 1389.121    0.000 23190.055    0.000 layer.py:98(move)
                8634837   27.694    0.000 22479.619    0.003 agent.py:29(learn)
                8634837  199.234    0.000 22431.201    0.003 agent.py:117(_learn)
                8634837  587.726    0.000 22231.967    0.003 learner.py:42(Qlearn)
               40450525  327.699    0.000 18200.906    0.000 layers.py:740(restart)
              863483700 2990.584    0.000 15296.107    0.000 layers.py:735(check)
               40450525  158.074    0.000 15033.389    0.000 level.py:8(__init__)
               40450525  528.721    0.000 13555.181    0.000 levels.py:288(generate)
              242700955 2186.787    0.000 12448.871    0.000 level.py:41(notUsed)
                8634837   53.104    0.000 9117.628    0.001 grad_mode.py:23(decorate_context)
                8634837  292.964    0.000 8967.740    0.001 adam.py:55(step)
        233140599/25904511  900.433    0.000 8795.641    0.000 module.py:715(_call_impl)
               17269674   40.010    0.000 8132.191    0.000 network.py:27(forward)
               17269674  207.206    0.000 7986.999    0.000 container.py:115(forward)
                8634837 1681.443    0.000 7402.673    0.001 functional.py:53(adam)
            25181029320 4252.045    0.000 6253.821    0.000 enum.py:646(__hash__)
              242700955  168.406    0.000 5852.180    0.000 level.py:38(elementsIn)
              863483700 1343.993    0.000 5157.798    0.000 layers.py:729(isFree)
                8634837   48.883    0.000 5027.030    0.001 tensor.py:181(backward)
                8634837   33.082    0.000 4978.147    0.001 __init__.py:68(backward)
                8634837 4745.828    0.001 4745.828    0.001 {method 'run_backward' of 'torch._C._EngineBase' objects}
               69078704 2737.559    0.000 4677.175    0.000 layer.py:167(NoRock_update)
                8634837  104.672    0.000 4570.728    0.001 agent.py:112(__call__)
             1634708034 1037.032    0.000 3930.236    0.000 {built-in method builtins.any}
              242700955 1916.250    0.000 3841.358    0.000 level.py:39(<listcomp>)
             6590082480 2963.187    0.000 3813.805    0.000 layer.py:95(isFree)
              863483700 2151.014    0.000 3565.040    0.000 layers.py:424(check)
              863483800  336.971    0.000 3446.256    0.000 {built-in method builtins.all}
             3417064083  954.346    0.000 3218.405    0.000 layers.py:690(<genexpr>)
               34539348   59.154    0.000 2884.985    0.000 conv.py:422(forward)
               34539348   70.132    0.000 2801.400    0.000 conv.py:414(_conv_forward)
               36604573 2752.003    0.000 2752.003    0.000 {built-in method tensor}
              323604200  236.408    0.000 2731.401    0.000 layer.py:69(restart)
               34539348 2718.772    0.000 2718.772    0.000 {built-in method conv2d}
               51809022  110.905    0.000 2670.004    0.000 linear.py:92(forward)
            11512122375 2647.957    0.000 2647.957    0.000 level.py:32(inverse)
              863483700 1560.524    0.000 2521.575    0.000 layers.py:437(check)
               51809022  191.335    0.000 2505.568    0.000 functional.py:1669(linear)
             7407299475 2048.743    0.000 2478.075    0.000 layers.py:700(<genexpr>)
              863483700 1487.918    0.000 2390.904    0.000 layers.py:452(check)
              604438620 1367.753    0.000 2275.354    0.000 tensor.py:933(grad)
               17269674   17.905    0.000 2181.517    0.000 game.py:37(board)
               40450625 1047.755    0.000 2105.806    0.000 layers.py:36(reset)
            25181063949 2001.782    0.000 2001.782    0.000 {built-in method builtins.hash}
                8634837  180.395    0.000 1973.375    0.000 optimizer.py:167(zero_grad)
            10193454811 1854.750    0.000 1854.750    0.000 enum.py:352(<genexpr>)
              242700955 1150.524    0.000 1842.416    0.000 {built-in method _functools.reduce}
            19020119460 1819.805    0.000 1819.805    0.000 layer.py:91(positions)
               51809022 1764.947    0.000 1764.947    0.000 {built-in method addmm}
              863483800  937.068    0.000 1500.779    0.000 layers.py:442(isDone)
              172696740 1479.737    0.000 1479.737    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
             2355206495  908.471    0.000 1258.648    0.000 layer.py:130(add)
              172696740 1252.457    0.000 1252.457    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
               40450525  571.098    0.000 1217.028    0.000 level.py:16(<dictcomp>)
             4808955913 1195.553    0.000 1195.553    0.000 layer.py:146(elements)
              863483700  712.597    0.000 1107.750    0.000 layers.py:402(check)
              863483700  718.646    0.000 1107.291    0.000 layers.py:413(check)
              742596062  366.073    0.000 1105.330    0.000 overrides.py:1070(has_torch_function)
               69078696   55.476    0.000 1097.819    0.000 activation.py:713(forward)
               69078696   91.356    0.000 1042.343    0.000 functional.py:1292(leaky_relu)
               69078696  941.759    0.000  941.759    0.000 {built-in method torch._C._nn.leaky_relu}
              863483700  621.191    0.000  917.988    0.000 layers.py:23(check)
               86348370  845.686    0.000  845.686    0.000 {method 'add' of 'torch._C._TensorBase' objects}
               86348370  790.372    0.000  790.372    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
                8634837  434.950    0.000  758.813    0.000 collector.py:46(collect)
               86348370  714.193    0.000  714.193    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
             6590082480  697.414    0.000  697.414    0.000 layer.py:203(isBlocking)
             8494533425  691.892    0.000  691.892    0.000 level.py:39(<lambda>)
        9239160377/9239160376  591.406    0.000  646.331    0.000 {built-in method builtins.len}
             7982240762  643.611    0.000  643.611    0.000 {method 'random' of '_random.Random' objects}
              897224657  423.332    0.000  636.662    0.000 layer.py:126(remove)
               86348370  615.304    0.000  615.304    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
             6290793277  504.202    0.000  504.202    0.000 {method 'append' of 'list' objects}
               86348370  465.256    0.000  465.256    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
                8634837   14.129    0.000  447.715    0.000 loss.py:445(forward)
                8634837   50.720    0.000  433.586    0.000 functional.py:2637(mse_loss)
             6584266200  429.332    0.000  429.332    0.000 layer.py:84(isDead)
             3316951906  412.043    0.000  412.043    0.000 layer.py:182(grid)
             1537001146  328.314    0.000  409.358    0.000 overrides.py:1083(<genexpr>)
                8634837   34.936    0.000  401.721    0.000 exploration.py:47(epsilonGreedy)
              237646393  269.390    0.000  396.818    0.000 layers.py:113(isDone)
              242700955  133.402    0.000  378.899    0.000 random.py:285(choice)
               51809022  324.160    0.000  324.160    0.000 {method 't' of 'torch._C._TensorBase' objects}
                8634837  270.949    0.000  270.949    0.000 {method 'tolist' of 'torch._C._TensorBase' objects}
              237646393  176.417    0.000  270.663    0.000 layers.py:457(isDone)
                8634837  250.803    0.000  250.803    0.000 {built-in method torch._C._nn.mse_loss}
               17269674  249.463    0.000  249.463    0.000 {built-in method sum}
              323604200  234.379    0.000  234.379    0.000 layer.py:139(clear2)
               86348420  102.109    0.000  230.755    0.000 tensor.py:596(__hash__)
                8635700  229.462    0.000  229.462    0.000 {built-in method max}
              242700955  152.843    0.000  220.301    0.000 random.py:250(_randbelow_with_getrandbits)
               69078704  218.874    0.000  218.874    0.000 layer.py:178(<listcomp>)
               69078704  205.666    0.000  205.666    0.000 layer.py:179(<listcomp>)


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@hpc.dtu.dk>
Subject: Job 9578841: <Diamonds3_simple_1> in cluster <dcc> Done

Job <Diamonds3_simple_1> was submitted from host <n-62-30-3> by user <s183905> in cluster <dcc> at Mon Apr 26 20:44:05 2021
Job was executed on host(s) <n-62-20-11>, in queue <gpuv100>, as user <s183905> in cluster <dcc> at Sat May  1 01:31:18 2021
</zhome/ee/d/137643> was used as the home directory.
</zhome/ee/d/137643/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Sat May  1 01:31:18 2021
Terminated at Sun May  2 01:26:44 2021
Results reported at Sun May  2 01:26:44 2021

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

    CPU time :                                   85902.64 sec.
    Max Memory :                                 2062 MB
    Average Memory :                             2059.73 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               14322.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                8
    Run time :                                   86130 sec.
    Turnaround time :                            448959 sec.

The output (if any) is above this job summary.


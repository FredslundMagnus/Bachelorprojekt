
# Parameters

    Name :                      DoorsAndKey_simple-1
    Main :                      simple
    Level :                     Levels.Causal1
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
    Num :                       1
    Load name :                 Causal4_Conver4_3counterfacts
    Minutes used :              1435 minutes.
    Hours used :                23 hours.

# Profiling


      171361956024 function calls (171126673205 primitive calls) in 86113.67 seconds

##    Ordered by: cumulative time
   List reduced from 408 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 86113.673 86113.673 {built-in method builtins.exec}
                      1    0.001    0.001 86113.673 86113.673 <string>:1(<module>)
                      1  150.443  150.443 86113.672 86113.672 main.py:67(simple)
                9803436   33.388    0.000 47699.264    0.005 game.py:42(step)
                9803436   45.358    0.000 45612.253    0.005 layers.py:827(step)
                9803436   28.566    0.000 30573.063    0.003 agent.py:29(learn)
                9803436  211.502    0.000 30525.426    0.003 agent.py:117(_learn)
                9803436  758.376    0.000 30313.924    0.003 learner.py:42(Qlearn)
                9803437 1287.312    0.000 28886.574    0.003 layers.py:793(update)
               53743569  358.793    0.000 18233.350    0.000 layers.py:849(restart)
                9803436  669.150    0.000 16626.828    0.002 layers.py:17(step)
              980343600 1480.501    0.000 15874.055    0.000 layer.py:106(move)
               53743569  172.292    0.000 14460.375    0.000 level.py:8(__init__)
                9803436   56.039    0.000 13279.296    0.001 grad_mode.py:23(decorate_context)
                9803436  323.173    0.000 13121.797    0.001 adam.py:55(step)
               53743569  563.241    0.000 12467.698    0.000 levels.py:122(generate)
              209598450 1857.892    0.000 11386.986    0.000 level.py:41(notUsed)
                9803436 2386.889    0.000 11366.490    0.001 functional.py:53(adam)
        264692772/29410308  991.045    0.000 10985.445    0.000 module.py:715(_call_impl)
               19606872   42.304    0.000 10222.788    0.001 network.py:28(forward)
               19606872  250.613    0.000 10068.833    0.001 container.py:115(forward)
              980343600 2405.340    0.000 8041.388    0.000 layers.py:844(check)
                9803436   55.898    0.000 6725.327    0.001 tensor.py:181(backward)
                9803436   32.160    0.000 6669.429    0.001 __init__.py:68(backward)
                9803436 6391.768    0.001 6391.768    0.001 {method 'run_backward' of 'torch._C._EngineBase' objects}
                9803436  115.964    0.000 5672.834    0.001 agent.py:112(__call__)
              209598450  143.603    0.000 5521.240    0.000 level.py:38(elementsIn)
              980343600 1193.959    0.000 4900.695    0.000 layers.py:838(isFree)
               58820622 2704.292    0.000 4405.774    0.000 layer.py:175(NoRock_update)
            17623209376 2749.396    0.000 4016.746    0.000 enum.py:646(__hash__)
             5702599989 2912.149    0.000 3706.736    0.000 layer.py:103(isFree)
              209598450 1762.329    0.000 3554.820    0.000 level.py:39(<listcomp>)
               39213744   65.084    0.000 3531.831    0.000 conv.py:422(forward)
               39213744   71.157    0.000 3443.214    0.000 conv.py:414(_conv_forward)
               58820616  128.410    0.000 3431.566    0.000 linear.py:92(forward)
               39213744 3359.175    0.000 3359.175    0.000 {built-in method conv2d}
             1848123196  959.566    0.000 3317.937    0.000 {built-in method builtins.any}
              322461414  263.655    0.000 3303.312    0.000 layer.py:77(restart)
               58820616  211.761    0.000 3248.735    0.000 functional.py:1669(linear)
               41515859 2780.075    0.000 2780.075    0.000 {built-in method tensor}
              686240550 1710.081    0.000 2698.524    0.000 tensor.py:933(grad)
                9803436  243.677    0.000 2646.201    0.000 optimizer.py:167(zero_grad)
               53743669 1286.806    0.000 2582.697    0.000 layers.py:36(reset)
              196068720 2381.239    0.000 2381.239    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
             9668219234 2348.258    0.000 2348.258    0.000 level.py:32(inverse)
               58820616 2327.194    0.000 2327.194    0.000 {built-in method addmm}
               19606872   19.748    0.000 2061.538    0.000 game.py:38(board)
              196068720 2044.976    0.000 2044.976    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
              980343700  295.677    0.000 2028.560    0.000 {built-in method builtins.all}
            11323708858 1924.179    0.000 1924.179    0.000 enum.py:352(<genexpr>)
             6486200917 1557.754    0.000 1920.820    0.000 layers.py:809(<genexpr>)
             3220778911  785.242    0.000 1846.482    0.000 layers.py:799(<genexpr>)
              209598450 1134.113    0.000 1822.818    0.000 {built-in method _functools.reduce}
               53743569  785.827    0.000 1715.570    0.000 level.py:16(<dictcomp>)
              980343600  986.470    0.000 1571.830    0.000 layers.py:141(check)
             3034192469 1111.608    0.000 1518.195    0.000 layer.py:138(add)
               78427488   64.829    0.000 1504.846    0.000 activation.py:713(forward)
               78427488   94.748    0.000 1440.017    0.000 functional.py:1292(leaky_relu)
               78427488 1335.745    0.000 1335.745    0.000 {built-in method torch._C._nn.leaky_relu}
               98034360 1289.054    0.000 1289.054    0.000 {method 'add' of 'torch._C._TensorBase' objects}
            17623248685 1267.357    0.000 1267.357    0.000 {built-in method builtins.hash}
              980343600  807.527    0.000 1265.401    0.000 layers.py:48(check)
              980343600  769.537    0.000 1221.526    0.000 layers.py:124(check)
              843095576  424.690    0.000 1211.149    0.000 overrides.py:1070(has_torch_function)
               98034360 1172.181    0.000 1172.181    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
             6133067331 1102.500    0.000 1102.500    0.000 layer.py:154(elements)
            12275991516 1090.940    0.000 1090.940    0.000 layer.py:99(positions)
               98034360 1086.393    0.000 1086.393    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
                9803436  614.743    0.000 1038.133    0.000 collector.py:46(collect)
              980343600  650.857    0.000  980.052    0.000 layers.py:23(check)
               98034360  977.182    0.000  977.182    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
               98034360  762.974    0.000  762.974    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
             8803134900  688.704    0.000  688.704    0.000 level.py:39(<lambda>)
             1020523369  464.836    0.000  679.859    0.000 layer.py:134(remove)
        8504675953/8504675952  563.030    0.000  627.280    0.000 {built-in method builtins.len}
              385961589  408.620    0.000  625.829    0.000 layers.py:113(isDone)
             7972837541  579.577    0.000  579.577    0.000 {method 'append' of 'list' objects}
             7163946047  539.027    0.000  539.027    0.000 {method 'random' of '_random.Random' objects}
                9803436   12.564    0.000  533.899    0.000 loss.py:445(forward)
                9803436   49.734    0.000  521.335    0.000 functional.py:2637(mse_loss)
             4406981350  500.006    0.000  500.006    0.000 layer.py:190(grid)
             4752275787  463.439    0.000  463.439    0.000 layer.py:211(isBlocking)
               58820616  457.025    0.000  457.025    0.000 {method 't' of 'torch._C._TensorBase' objects}
             1745011768  346.555    0.000  431.841    0.000 overrides.py:1083(<genexpr>)
                9803436   33.341    0.000  431.258    0.000 exploration.py:47(epsilonGreedy)
              980343700  276.581    0.000  369.900    0.000 layers.py:52(isDone)
             5559600786  363.066    0.000  363.066    0.000 layer.py:92(isDead)
               19606872  337.720    0.000  337.720    0.000 {built-in method sum}
                9803436  331.781    0.000  331.781    0.000 {built-in method torch._C._nn.mse_loss}
              209598450  107.944    0.000  314.402    0.000 random.py:285(choice)
                9803436  308.890    0.000  308.890    0.000 {method 'tolist' of 'torch._C._TensorBase' objects}
                9804416  291.199    0.000  291.199    0.000 {built-in method max}
               39213744   28.358    0.000  261.854    0.000 flatten.py:39(forward)
               98034410  108.950    0.000  245.979    0.000 tensor.py:596(__hash__)
                9803436  244.595    0.000  244.595    0.000 {built-in method gather}
                9803436   39.006    0.000  237.124    0.000 __init__.py:28(_make_grads)
               39213744  233.496    0.000  233.496    0.000 {method 'flatten' of 'torch._C._TensorBase' objects}
              322461414  230.853    0.000  230.853    0.000 layer.py:147(clear2)
                9803436   46.645    0.000  225.518    0.000 tensor.py:506(__rsub__)
              264692772  220.398    0.000  220.398    0.000 {built-in method torch._C._get_tracing_state}


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@hpc.dtu.dk>
Subject: Job 9624001: <DoorsAndKey_simple_1> in cluster <dcc> Done

Job <DoorsAndKey_simple_1> was submitted from host <n-62-30-2> by user <s183905> in cluster <dcc> at Sat May  8 23:34:13 2021
Job was executed on host(s) <n-62-20-4>, in queue <gpuv100>, as user <s183905> in cluster <dcc> at Sun May  9 23:29:44 2021
</zhome/ee/d/137643> was used as the home directory.
</zhome/ee/d/137643/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Sun May  9 23:29:44 2021
Terminated at Mon May 10 23:25:06 2021
Results reported at Mon May 10 23:25:06 2021

Your job looked like:

------------------------------------------------------------
# LSBATCH: User input
#!/bin/sh
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

python main.py $MYARGS


------------------------------------------------------------

Successfully completed.

Resource usage summary:

    CPU time :                                   85896.21 sec.
    Max Memory :                                 2064 MB
    Average Memory :                             2060.49 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               14320.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                8
    Run time :                                   86123 sec.
    Turnaround time :                            172253 sec.

The output (if any) is above this job summary.


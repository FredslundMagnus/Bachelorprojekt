
# Parameters

    Name :                      SuperLevel2_simple-0
    Main :                      simple
    Level :                     Levels.SuperLevel2
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


      165657540626 function calls (165465397951 primitive calls) in 86110.49 seconds

##    Ordered by: cumulative time
   List reduced from 419 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 86110.490 86110.490 {built-in method builtins.exec}
                      1    0.001    0.001 86110.490 86110.490 <string>:1(<module>)
                      1  131.045  131.045 86110.489 86110.489 main.py:67(simple)
                8005930   28.482    0.000 58720.692    0.007 game.py:42(step)
                8005930   41.708    0.000 56757.450    0.007 layers.py:827(step)
                8005930  698.346    0.000 41988.512    0.005 layers.py:17(step)
              800593000 2344.034    0.000 41206.978    0.000 layer.py:106(move)
              800593000 4799.070    0.000 30678.597    0.000 layers.py:844(check)
                8005930   27.745    0.000 21094.434    0.003 agent.py:29(learn)
                8005930  183.212    0.000 21048.897    0.003 agent.py:117(_learn)
                8005930  537.959    0.000 20865.685    0.003 learner.py:42(Qlearn)
                8005931 1149.636    0.000 14676.959    0.002 layers.py:793(update)
                8005930   47.626    0.000 8571.622    0.001 grad_mode.py:23(decorate_context)
                8005930  283.183    0.000 8432.929    0.001 adam.py:55(step)
        216160110/24017790  846.634    0.000 8334.960    0.000 module.py:715(_call_impl)
               16011860   42.117    0.000 7727.602    0.000 network.py:28(forward)
               16011860  201.967    0.000 7582.439    0.000 container.py:115(forward)
                8005930 1537.328    0.000 6895.305    0.001 functional.py:53(adam)
              800593000 1725.712    0.000 6769.520    0.000 layers.py:838(isFree)
              800593000 4669.464    0.000 6563.209    0.000 layers.py:471(check)
            21835395006 4152.158    0.000 5998.146    0.000 enum.py:646(__hash__)
               88065241 3141.114    0.000 5456.152    0.000 layer.py:159(update)
             7162076880 3858.109    0.000 5043.808    0.000 layer.py:103(isFree)
             1540413959 1202.638    0.000 4748.514    0.000 {built-in method builtins.any}
                8005930   44.443    0.000 4648.725    0.001 tensor.py:181(backward)
                8005930   27.209    0.000 4604.282    0.001 __init__.py:68(backward)
                8005930 4394.055    0.001 4394.055    0.001 {method 'run_backward' of 'torch._C._EngineBase' objects}
                8005930   94.800    0.000 4335.400    0.001 agent.py:112(__call__)
              800593000 2955.144    0.000 4234.534    0.000 layers.py:77(check)
              800593000 2327.260    0.000 4083.408    0.000 layers.py:246(check)
              800593000 2171.097    0.000 3957.379    0.000 layers.py:286(check)
             9454277496 2579.885    0.000 3139.468    0.000 layers.py:809(<genexpr>)
               33960660 2863.078    0.000 2863.078    0.000 {built-in method tensor}
               32023720   56.775    0.000 2720.125    0.000 conv.py:422(forward)
               32023720   64.861    0.000 2641.124    0.000 conv.py:414(_conv_forward)
               32023720 2564.200    0.000 2564.200    0.000 {built-in method conv2d}
               12736642  132.254    0.000 2555.640    0.000 layers.py:849(restart)
               48035580  111.199    0.000 2532.488    0.000 linear.py:92(forward)
            23600975093 2388.368    0.000 2388.368    0.000 layer.py:99(positions)
               48035580  184.710    0.000 2370.865    0.000 functional.py:1669(linear)
               16011860   19.111    0.000 2342.148    0.000 game.py:38(board)
              560415130 1356.544    0.000 2260.228    0.000 tensor.py:933(grad)
                8005930  185.540    0.000 1944.297    0.000 optimizer.py:167(zero_grad)
            21835427115 1845.995    0.000 1845.995    0.000 {built-in method builtins.hash}
               48035580 1659.932    0.000 1659.932    0.000 {built-in method addmm}
              800593000  943.498    0.000 1463.479    0.000 layers.py:273(check)
              160118600 1392.799    0.000 1392.799    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
              800593000  863.865    0.000 1368.431    0.000 layers.py:313(check)
              992122442  508.383    0.000 1331.877    0.000 random.py:285(choice)
             2742937201 1314.879    0.000 1314.879    0.000 layer.py:154(elements)
              800593000  837.125    0.000 1226.060    0.000 layers.py:62(check)
               12736642   61.177    0.000 1207.958    0.000 level.py:8(__init__)
              160118600 1177.742    0.000 1177.742    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
              140103062  165.406    0.000 1168.156    0.000 layer.py:77(restart)
              800593000  765.985    0.000 1161.003    0.000 layers.py:48(check)
              800593100  223.444    0.000 1129.006    0.000 {built-in method builtins.all}
              688510060  383.212    0.000 1109.558    0.000 overrides.py:1070(has_torch_function)
               64047440   55.934    0.000 1060.375    0.000 activation.py:713(forward)
             2401780200  607.847    0.000 1005.609    0.000 layers.py:799(<genexpr>)
               64047440   86.247    0.000 1004.441    0.000 functional.py:1292(leaky_relu)
              800593000  609.042    0.000  918.443    0.000 layers.py:23(check)
               64047440  909.145    0.000  909.145    0.000 {built-in method torch._C._nn.leaky_relu}
             9717015066  822.826    0.000  822.826    0.000 {method 'random' of '_random.Random' objects}
               80059300  790.312    0.000  790.312    0.000 {method 'add' of 'torch._C._TensorBase' objects}
        10989710251/10989710250  716.323    0.000  767.416    0.000 {built-in method builtins.len}
               80059300  739.513    0.000  739.513    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
             1285497813  548.439    0.000  739.227    0.000 layer.py:138(add)
              992122442  519.235    0.000  735.810    0.000 random.py:250(_randbelow_with_getrandbits)
             6312255503  720.158    0.000  720.158    0.000 layer.py:211(isBlocking)
                8005930  410.303    0.000  704.493    0.000 collector.py:46(collect)
               12736742  338.604    0.000  694.042    0.000 layers.py:36(reset)
               80059300  657.878    0.000  657.878    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
               12736642  339.063    0.000  632.089    0.000 levels.py:368(generate)
               80059300  575.287    0.000  575.287    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
             7878564580  502.001    0.000  502.001    0.000 layer.py:92(isDead)
               12736642  217.593    0.000  467.407    0.000 level.py:16(<dictcomp>)
               80059300  437.688    0.000  437.688    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
              508564403  277.867    0.000  429.773    0.000 layer.py:134(remove)
             1425055700  323.745    0.000  400.859    0.000 overrides.py:1083(<genexpr>)
                8005930   10.556    0.000  399.989    0.000 loss.py:445(forward)
                8005930   44.058    0.000  389.433    0.000 functional.py:2637(mse_loss)
             1601186000  352.460    0.000  352.460    0.000 {method 'union' of 'set' objects}
                8005930   29.181    0.000  344.673    0.000 exploration.py:47(epsilonGreedy)
              800593100  243.577    0.000  335.574    0.000 layers.py:508(isDone)
             3857297595  312.053    0.000  312.053    0.000 {method 'append' of 'list' objects}
               88065241  304.352    0.000  304.352    0.000 layer.py:171(<listcomp>)
               48035580  303.373    0.000  303.373    0.000 {method 't' of 'torch._C._TensorBase' objects}
               88065241  288.053    0.000  288.053    0.000 layer.py:172(<listcomp>)
                8005930  236.172    0.000  236.172    0.000 {method 'tolist' of 'torch._C._TensorBase' objects}
               16011860  227.078    0.000  227.078    0.000 {built-in method sum}
                8005930  226.743    0.000  226.743    0.000 {built-in method torch._C._nn.mse_loss}
               80059350   97.918    0.000  225.034    0.000 tensor.py:596(__hash__)
                8006730  209.111    0.000  209.111    0.000 {built-in method max}
               32023720   24.752    0.000  179.133    0.000 flatten.py:39(forward)
                8005930   33.997    0.000  176.345    0.000 __init__.py:28(_make_grads)
                8005930  170.867    0.000  170.867    0.000 {built-in method gather}
             1601186000  166.134    0.000  166.134    0.000 layer.py:86(check)
                8005930   34.691    0.000  156.101    0.000 tensor.py:506(__rsub__)
               32023720  154.380    0.000  154.380    0.000 {method 'flatten' of 'torch._C._TensorBase' objects}
              216160110  153.359    0.000  153.359    0.000 {built-in method torch._C._get_tracing_state}


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@hpc.dtu.dk>
Subject: Job 9578849: <SuperLevel2_simple_0> in cluster <dcc> Done

Job <SuperLevel2_simple_0> was submitted from host <n-62-30-3> by user <s183905> in cluster <dcc> at Mon Apr 26 20:44:06 2021
Job was executed on host(s) <n-62-20-13>, in queue <gpuv100>, as user <s183905> in cluster <dcc> at Mon May  3 16:37:18 2021
</zhome/ee/d/137643> was used as the home directory.
</zhome/ee/d/137643/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Mon May  3 16:37:18 2021
Terminated at Tue May  4 16:32:34 2021
Results reported at Tue May  4 16:32:34 2021

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

    CPU time :                                   85896.26 sec.
    Max Memory :                                 2078 MB
    Average Memory :                             2076.75 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               14306.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                8
    Run time :                                   86115 sec.
    Turnaround time :                            676108 sec.

The output (if any) is above this job summary.


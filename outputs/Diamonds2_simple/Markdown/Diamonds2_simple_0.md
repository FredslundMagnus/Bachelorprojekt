
# Parameters

    Name :                      Diamonds2_simple-0
    Main :                      simple
    Level :                     Levels.Causal5
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


      154661702771 function calls (154455125560 primitive calls) in 86104.63 seconds

##    Ordered by: cumulative time
   List reduced from 410 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 86104.628 86104.628 {built-in method builtins.exec}
                      1    0.001    0.001 86104.628 86104.628 <string>:1(<module>)
                      1  144.630  144.630 86104.627 86104.627 main.py:66(simple)
                8607369   33.873    0.000 48221.327    0.006 game.py:41(step)
                8607369   43.727    0.000 46047.125    0.005 layers.py:718(step)
                8607369   28.433    0.000 30035.189    0.003 agent.py:29(learn)
                8607369  211.369    0.000 29987.929    0.003 agent.py:117(_learn)
                8607369  745.295    0.000 29776.559    0.003 learner.py:42(Qlearn)
                8607369  690.112    0.000 26697.380    0.003 layers.py:17(step)
              860736900 1461.988    0.000 25926.663    0.000 layer.py:98(move)
                8607370 1253.397    0.000 19251.940    0.002 layers.py:684(update)
              860736900 3518.234    0.000 17692.270    0.000 layers.py:735(check)
                8607369   52.308    0.000 13111.773    0.002 grad_mode.py:23(decorate_context)
                8607369  322.343    0.000 12954.043    0.002 adam.py:55(step)
                8607369 2400.364    0.000 11194.246    0.001 functional.py:53(adam)
        232398963/25822107  966.950    0.000 10741.192    0.000 module.py:715(_call_impl)
               17214738   44.918    0.000 9991.446    0.001 network.py:27(forward)
               17214738  240.773    0.000 9839.894    0.001 container.py:115(forward)
                8607369   52.936    0.000 6580.280    0.001 tensor.py:181(backward)
                8607369   30.811    0.000 6527.344    0.001 __init__.py:68(backward)
                8607369 6258.914    0.001 6258.914    0.001 {method 'run_backward' of 'torch._C._EngineBase' objects}
               11351185  111.054    0.000 5848.514    0.001 layers.py:740(restart)
                8607369  116.020    0.000 5579.614    0.001 agent.py:112(__call__)
              860736900 1693.501    0.000 5539.994    0.000 layers.py:729(isFree)
               11351185   52.730    0.000 4879.373    0.000 level.py:8(__init__)
            17326623265 3202.528    0.000 4657.962    0.000 enum.py:646(__hash__)
             1658478582 1190.881    0.000 4581.756    0.000 {built-in method builtins.any}
               11351185  180.669    0.000 4397.116    0.000 levels.py:249(generate)
               77466330 2339.747    0.000 4302.462    0.000 layer.py:167(NoRock_update)
               73781411  717.585    0.000 4027.810    0.000 level.py:41(notUsed)
             6577062504 2964.467    0.000 3846.494    0.000 layer.py:95(isFree)
              860737000  491.038    0.000 3651.213    0.000 {built-in method builtins.all}
               34429476   63.452    0.000 3446.279    0.000 conv.py:422(forward)
               34429476   72.472    0.000 3359.915    0.000 conv.py:414(_conv_forward)
               51644214  118.017    0.000 3333.610    0.000 linear.py:92(forward)
             5220563081 1475.642    0.000 3277.445    0.000 layers.py:690(<genexpr>)
               34429476 3275.235    0.000 3275.235    0.000 {built-in method conv2d}
               51644214  201.763    0.000 3163.199    0.000 functional.py:1669(linear)
               36488029 3019.222    0.000 3019.222    0.000 {built-in method tensor}
             8493858150 2420.848    0.000 2951.917    0.000 layers.py:700(<genexpr>)
              602515860 1725.673    0.000 2704.541    0.000 tensor.py:933(grad)
                8607369  238.650    0.000 2631.059    0.000 optimizer.py:167(zero_grad)
              860736900 1638.222    0.000 2606.377    0.000 layers.py:349(check)
              860736900 1577.422    0.000 2535.648    0.000 layers.py:375(check)
              860736900 1508.817    0.000 2454.774    0.000 layers.py:387(check)
              860736900 1477.563    0.000 2404.566    0.000 layers.py:337(check)
               17214738   18.451    0.000 2320.172    0.000 game.py:37(board)
              172147380 2318.477    0.000 2318.477    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
               51644214 2271.530    0.000 2271.530    0.000 {built-in method addmm}
            20488234371 2070.550    0.000 2070.550    0.000 layer.py:91(positions)
              172147380 1992.825    0.000 1992.825    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
               73781411   56.403    0.000 1883.852    0.000 level.py:38(elementsIn)
              860737000  991.168    0.000 1536.674    0.000 layers.py:113(isDone)
               68858952   63.457    0.000 1497.585    0.000 activation.py:713(forward)
            17326657774 1455.441    0.000 1455.441    0.000 {built-in method builtins.hash}
               68858952   95.227    0.000 1434.128    0.000 functional.py:1292(leaky_relu)
               68858952 1329.347    0.000 1329.347    0.000 {built-in method torch._C._nn.leaky_relu}
               86073690 1265.628    0.000 1265.628    0.000 {method 'add' of 'torch._C._TensorBase' objects}
              860736900  829.329    0.000 1259.268    0.000 layers.py:364(check)
               73781411  603.699    0.000 1218.399    0.000 level.py:39(<listcomp>)
              740233814  414.052    0.000 1199.287    0.000 overrides.py:1070(has_torch_function)
              860736900  763.689    0.000 1175.005    0.000 layers.py:326(check)
               86073690 1163.547    0.000 1163.547    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
               86073690 1070.919    0.000 1070.919    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
             2355896044 1065.167    0.000 1065.167    0.000 layer.py:146(elements)
                8607369  597.918    0.000 1013.826    0.000 collector.py:46(collect)
               86073690  950.517    0.000  950.517    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
              860736900  629.889    0.000  948.692    0.000 layers.py:23(check)
             3479792161  863.856    0.000  863.856    0.000 level.py:32(inverse)
              102160665   81.184    0.000  822.821    0.000 layer.py:69(restart)
               86073690  752.376    0.000  752.376    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
             6577062504  732.265    0.000  732.265    0.000 layer.py:203(isBlocking)
        10162374832/10162374831  658.955    0.000  724.021    0.000 {built-in method builtins.len}
             8684083479  720.504    0.000  720.504    0.000 {method 'random' of '_random.Random' objects}
             1102831165  455.479    0.000  630.082    0.000 layer.py:130(add)
               11351285  310.107    0.000  619.576    0.000 layers.py:36(reset)
               73781411  381.833    0.000  609.050    0.000 {built-in method _functools.reduce}
             3064775023  587.763    0.000  587.763    0.000 enum.py:352(<genexpr>)
             7644472335  531.068    0.000  531.068    0.000 layer.py:84(isDead)
              674877475  363.207    0.000  524.255    0.000 layer.py:126(remove)
                8607369   15.274    0.000  520.946    0.000 loss.py:445(forward)
                8607369   47.211    0.000  505.671    0.000 functional.py:2637(mse_loss)
               51644214  444.604    0.000  444.604    0.000 {method 't' of 'torch._C._TensorBase' objects}
             1532111842  347.821    0.000  433.057    0.000 overrides.py:1083(<genexpr>)
                8607369   34.218    0.000  422.534    0.000 exploration.py:47(epsilonGreedy)
               11351185  200.722    0.000  393.266    0.000 level.py:16(<dictcomp>)
               17214738  329.931    0.000  329.931    0.000 {built-in method sum}
                8607369  321.087    0.000  321.087    0.000 {built-in method torch._C._nn.mse_loss}
             3393374799  294.163    0.000  294.163    0.000 {method 'append' of 'list' objects}
                8607369  292.285    0.000  292.285    0.000 {method 'tolist' of 'torch._C._TensorBase' objects}
                8608229  282.205    0.000  282.205    0.000 {built-in method max}
               77466330  256.496    0.000  256.496    0.000 layer.py:178(<listcomp>)
               34429476   27.379    0.000  256.018    0.000 flatten.py:39(forward)
               86073740  109.860    0.000  248.831    0.000 tensor.py:596(__hash__)
             3447522184  243.427    0.000  243.427    0.000 layer.py:81(isDone)
               77466330  242.311    0.000  242.311    0.000 layer.py:179(<listcomp>)
                8607369  238.314    0.000  238.314    0.000 {built-in method gather}
                8607369   38.473    0.000  229.976    0.000 __init__.py:28(_make_grads)
               34429476  228.639    0.000  228.639    0.000 {method 'flatten' of 'torch._C._TensorBase' objects}
             2582349385  227.217    0.000  227.217    0.000 level.py:39(<lambda>)


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@hpc.dtu.dk>
Subject: Job 9578837: <Diamonds2_simple_0> in cluster <dcc> Done

Job <Diamonds2_simple_0> was submitted from host <n-62-30-3> by user <s183905> in cluster <dcc> at Mon Apr 26 20:44:05 2021
Job was executed on host(s) <n-62-20-13>, in queue <gpuv100>, as user <s183905> in cluster <dcc> at Thu Apr 29 14:38:18 2021
</zhome/ee/d/137643> was used as the home directory.
</zhome/ee/d/137643/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Thu Apr 29 14:38:18 2021
Terminated at Fri Apr 30 14:33:27 2021
Results reported at Fri Apr 30 14:33:27 2021

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

    CPU time :                                   85897.48 sec.
    Max Memory :                                 2076 MB
    Average Memory :                             2075.56 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               14308.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                8
    Run time :                                   86108 sec.
    Turnaround time :                            323362 sec.

The output (if any) is above this job summary.


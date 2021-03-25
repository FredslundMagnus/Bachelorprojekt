
# Parameters

    Name :                      causal3_9x9-2
    Main :                      teleport
    Level :                     Levels.Causal3
    Hours :                     12.0
    Batch :                     100
    Width :                     9
    Height :                    9
    Network1 :                  Networks.Teleporter
    Network2 :                  Networks.Mini
    Learner1 :                  Learners.Qlearn
    Learner2 :                  Learners.Qlearn
    Exploration1 :              Explorations.softmaxer
    Exploration2 :              Explorations.epsilonGreedy
    Layer blocks :              True
    Layer goal :                True
    Layer gold :                True
    Layer keys :                False
    Layer door :                False
    Layer holder :              False
    Layer putter :              False
    Layer rock :                False
    Layer dirt :                True
    Layer diamond1 :            False
    Layer diamond2 :            False
    Layer diamond3 :            False
    Layer diamond4 :            False
    Layer reddoors :            True
    Layer redkeys :             True
    Layer bluedoors :           True
    Layer bluekeys :            True
    K :                         200000
    Epsilon cap :               0.1
    Softmax cap :               0.025
    Gamma :                     0.98
    Update :                    10000
    Reset chance :              0.002
    Modified done chance :      0.04
    Miss intervention cost :    -0.15
    Intervention cost :         -0.05
    Replay size :               100000
    Sample size :               50
    Minutes used :              715 minutes.
    Hours used :                11 hours.

# Profiling


      33993077205 function calls (33843515750 primitive calls) in 42915.44 seconds

##    Ordered by: cumulative time
   List reduced from 475 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 42915.444 42915.444 {built-in method builtins.exec}
                      1    1.916    1.916 42915.444 42915.444 <string>:1(<module>)
                      1  128.504  128.504 42913.528 42913.528 main.py:43(teleport)
                5342086   19.678    0.000 15171.619    0.003 agent.py:27(learn)
                5342086  395.684    0.000 12975.432    0.002 learner.py:42(Qlearn)
                2671043   11.528    0.000 10815.931    0.004 game.py:27(step)
                2671043   14.926    0.000 10181.440    0.004 layers.py:475(step)
                2671043   92.931    0.000 9081.691    0.003 agent.py:51(_learn)
                2671043  207.357    0.000 6886.872    0.003 layers.py:18(step)
              267104300  325.315    0.000 6657.544    0.000 layer.py:76(move)
        168256248/18695804  686.245    0.000 6238.120    0.000 module.py:866(_call_impl)
                2671043   79.106    0.000 6058.382    0.002 agent.py:110(_learn)
               13353718   39.034    0.000 5809.793    0.000 network.py:24(forward)
               13353718  182.611    0.000 5687.195    0.000 container.py:117(forward)
                5342086   48.689    0.000 5389.087    0.001 optimizer.py:84(wrapper)
                2671043 2949.744    0.001 5343.637    0.002 replaybuffer.py:27(teleporter_save_data)
                5342086   23.516    0.000 5170.669    0.001 grad_mode.py:24(decorate_context)
                5342086  150.631    0.000 5092.499    0.001 adam.py:55(step)
                5342086 1056.268    0.000 4768.671    0.001 _functional.py:53(adam)
                2671043 2259.570    0.001 4161.183    0.002 agent.py:81(interveen)
              267104300  656.058    0.000 4000.123    0.000 layers.py:492(check)
                5340589  136.475    0.000 3879.256    0.001 agent.py:46(__call__)
                5342086   23.258    0.000 3280.363    0.001 tensor.py:195(backward)
                2671044  270.953    0.000 3261.087    0.001 layers.py:446(update)
                5342086   20.646    0.000 3256.349    0.001 __init__.py:68(backward)
                2671043 2188.397    0.001 3197.124    0.001 replaybuffer.py:23(sample_data)
                5342086 3115.769    0.001 3115.769    0.001 {method 'run_backward' of 'torch._C._EngineBase' objects}
               26707436   59.942    0.000 2082.880    0.000 conv.py:398(forward)
              267104300  418.008    0.000 2045.431    0.000 layers.py:486(isFree)
                2671043 1196.973    0.000 2006.393    0.001 agent.py:63(modify)
               26707436   35.288    0.000 1997.303    0.000 conv.py:390(_conv_forward)
               26707436 1962.016    0.000 1962.016    0.000 {built-in method conv2d}
              162997498 1958.693    0.000 1958.693    0.000 {built-in method clone}
             2085239855 1326.761    0.000 1627.423    0.000 layer.py:73(isFree)
               34719068   72.539    0.000 1621.540    0.000 linear.py:93(forward)
               34719068   28.990    0.000 1515.402    0.000 functional.py:1737(linear)
               34719068 1479.476    0.000 1479.476    0.000 {built-in method torch._C._nn.linear}
               24039396  782.395    0.000 1407.848    0.000 layer.py:137(NoRock_update)
                2671043   40.744    0.000 1192.174    0.000 agent.py:105(__call__)
                8011632   54.767    0.000 1167.705    0.000 agent.py:55(modify_board)
               24037890 1011.820    0.000 1011.820    0.000 {built-in method cat}
               96157548  963.395    0.000  963.395    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
             3835103807  644.771    0.000  919.373    0.000 enum.py:646(__hash__)
               48072786   38.105    0.000  914.359    0.000 activation.py:713(forward)
               11041956  888.877    0.000  888.877    0.000 {built-in method tensor}
               48072786   39.990    0.000  876.254    0.000 functional.py:1364(leaky_relu)
               96157548  855.016    0.000  855.016    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
                3028748   32.083    0.000  830.510    0.000 layers.py:496(restart)
               48072786  828.302    0.000  828.302    0.000 {built-in method torch._C._nn.leaky_relu}
                2671043   53.612    0.000  820.649    0.000 replaybuffer.py:19(stacker)
              267104300  512.262    0.000  801.101    0.000 layers.py:302(check)
              267104300  468.577    0.000  762.557    0.000 layers.py:261(check)
                5342086  121.930    0.000  760.592    0.000 optimizer.py:189(zero_grad)
                8011632  748.479    0.000  748.479    0.000 {built-in method torch._C._nn.one_hot}
                5342086    6.166    0.000  712.987    0.000 game.py:23(board)
              267104400   71.639    0.000  653.249    0.000 {built-in method builtins.all}
              809812996  178.591    0.000  610.711    0.000 layers.py:452(<genexpr>)
                2671043  325.285    0.000  542.943    0.000 collector.py:54(collect)
                3028748   16.442    0.000  536.157    0.000 level.py:8(__init__)
               48078774  531.824    0.000  531.824    0.000 {method 'add' of 'torch._C._TensorBase' objects}
              171009130  522.512    0.000  522.512    0.000 {method 'unsqueeze' of 'torch._C._TensorBase' objects}
              267104300  376.818    0.000  502.084    0.000 layers.py:63(check)
               48078774  465.923    0.000  465.923    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
                3028748   78.535    0.000  460.767    0.000 levels.py:163(generate)
              267104300  290.997    0.000  448.753    0.000 layers.py:328(check)
               48078774  441.482    0.000  441.482    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
               48078774  439.886    0.000  439.886    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
             5153930413  436.519    0.000  436.519    0.000 layer.py:69(positions)
              267104300  266.846    0.000  413.532    0.000 layers.py:287(check)
              267104400  274.897    0.000  410.386    0.000 layers.py:110(isDone)
                5340589  144.807    0.000  405.612    0.000 exploration.py:53(softmaxer)
              907898354  398.048    0.000  398.048    0.000 layer.py:116(elements)
              267104300  232.919    0.000  350.378    0.000 layers.py:47(check)
               48078774  342.203    0.000  342.203    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
                6057496   38.181    0.000  306.011    0.000 level.py:41(notUsed)
              336551472  233.687    0.000  287.186    0.000 tensor.py:906(grad)
             3835123430  274.605    0.000  274.605    0.000 {built-in method builtins.hash}
                5342086    8.682    0.000  266.657    0.000 loss.py:527(forward)
                5342086   20.902    0.000  257.975    0.000 functional.py:2898(mse_loss)
               27258732   36.473    0.000  253.688    0.000 layer.py:50(restart)
               16026258  231.140    0.000  231.140    0.000 {built-in method sum}
        2531891538/2531891536  185.823    0.000  225.576    0.000 {built-in method builtins.len}
                8728539   84.461    0.000  224.644    0.000 random.py:315(sample)
              430611867  163.796    0.000  223.439    0.000 layer.py:100(add)
              251099767  118.837    0.000  181.423    0.000 layer.py:96(remove)
                5342086  168.180    0.000  168.180    0.000 {built-in method torch._C._nn.mse_loss}
             1627483824  163.070    0.000  163.070    0.000 layer.py:177(isBlocking)
               26707436   20.268    0.000  158.986    0.000 flatten.py:39(forward)
              127208125  152.782    0.000  152.782    0.000 level.py:32(inverse)
                5342887  149.068    0.000  149.068    0.000 {built-in method max}
                8013129   11.897    0.000  148.075    0.000 tensor.py:525(__rsub__)
                3028848   72.311    0.000  145.302    0.000 layers.py:33(reset)
               26707436  138.718    0.000  138.718    0.000 {method 'flatten' of 'torch._C._TensorBase' objects}
                8013129  134.072    0.000  134.072    0.000 {built-in method rsub}
                5340589  131.863    0.000  131.863    0.000 {built-in method multinomial}
              170928359  119.895    0.000  119.895    0.000 {built-in method torch._C._get_tracing_state}
                5342086  116.085    0.000  116.085    0.000 {built-in method gather}
                5342086   21.433    0.000  115.423    0.000 __init__.py:28(_make_grads)
              177694767   77.507    0.000  113.140    0.000 random.py:250(_randbelow_with_getrandbits)
               10684172   23.725    0.000  111.971    0.000 profiler.py:615(__enter__)


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@n-62-20-3>
Subject: Job 9458196: <causal3_9x9_2> in cluster <dcc> Done

Job <causal3_9x9_2> was submitted from host <gbarlogin1> by user <s183914> in cluster <dcc> at Thu Mar 25 01:18:04 2021
Job was executed on host(s) <n-62-20-3>, in queue <gpuv100>, as user <s183914> in cluster <dcc> at Thu Mar 25 01:18:05 2021
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Thu Mar 25 01:18:05 2021
Terminated at Thu Mar 25 13:13:30 2021
Results reported at Thu Mar 25 13:13:30 2021

Your job looked like:

------------------------------------------------------------
# LSBATCH: User input
#!/bin/sh
#BSUB -q hpc
#BSUB -q gpuv100
#BSUB -gpu "num=1:mode=exclusive_process"
#BSUB -n 1
#BSUB -R "rusage[mem=8G]"
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

    CPU time :                                   42801.66 sec.
    Max Memory :                                 6342 MB
    Average Memory :                             4638.70 MB
    Total Requested Memory :                     8192.00 MB
    Delta Memory :                               1850.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                8
    Run time :                                   42948 sec.
    Turnaround time :                            42926 sec.

The output (if any) is above this job summary.


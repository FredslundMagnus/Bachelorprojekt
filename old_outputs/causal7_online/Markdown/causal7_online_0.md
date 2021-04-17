
# Parameters

    Name :                      causal7_online-0
    Main :                      graphTrain
    Level :                     Levels.Causal7
    Hours :                     12.0
    Batch :                     100
    Width :                     9
    Height :                    9
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
    Reset chance :              0.001
    Modified done chance :      0.05
    Miss intervention cost :    -0.15
    Intervention cost :         -0.05
    Replay size :               100000
    Sample size :               50
    Cf convert :                2
    Counterfacts :              1
    Topn :                      7
    Minutes used :              715 minutes.
    Hours used :                11 hours.

# Profiling


      25257239377 function calls (25240726554 primitive calls) in 42907.42 seconds

##    Ordered by: cumulative time
   List reduced from 461 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 42907.418 42907.418 {built-in method builtins.exec}
                      1    0.002    0.002 42907.418 42907.418 <string>:1(<module>)
                      1  276.581  276.581 42907.416 42907.416 allGraphsTrain.py:5(graphTrain)
                 825622 6173.073    0.007 15571.483    0.019 allGraphs.py:220(transformNot)
              825629000 10986.370    0.000 10986.370    0.000 {method 'item' of 'torch._C._TensorBase' objects}
                 825622   19.380    0.000 9878.329    0.012 allGraphsTrain.py:27(<listcomp>)
               83387923 2167.053    0.000 9858.961    0.000 allGraphs.py:141(states)
              743060200 6981.063    0.000 6981.063    0.000 {method 'sum' of 'torch._C._TensorBase' objects}
                 825622    4.591    0.000 4679.785    0.006 game.py:41(step)
                 825622    5.602    0.000 4495.734    0.005 layers.py:710(step)
                 825622  861.153    0.001 4227.670    0.005 allGraphsTrain.py:33(<listcomp>)
               12598409   71.165    0.000 3366.517    0.000 allGraphs.py:228(getInterventions)
                 825623  131.890    0.000 2482.927    0.003 layers.py:676(update)
                 825622  153.578    0.000 2430.166    0.003 allGraphsTrain.py:35(<listcomp>)
               11919203   51.054    0.000 2032.349    0.000 allGraphs.py:188(rightIntervention)
                 825622   78.546    0.000 2000.340    0.002 layers.py:17(step)
                 825622    4.839    0.000 1988.743    0.002 agent.py:29(learn)
                 825622   20.727    0.000 1981.445    0.002 agent.py:117(_learn)
                 825622   62.072    0.000 1960.717    0.002 learner.py:42(Qlearn)
               82562200  140.211    0.000 1912.658    0.000 layer.py:98(move)
               20227364 1744.514    0.000 1744.514    0.000 {built-in method tensor}
              181842146  505.314    0.000 1684.068    0.000 allGraphs.py:163(flip_chance)
               16726520   11.150    0.000 1620.688    0.000 game.py:37(board)
                8827146   95.266    0.000 1514.627    0.000 allGraphs.py:192(<dictcomp>)
               87515932  211.908    0.000 1443.988    0.000 tensor.py:21(wrapped)
                 825622   64.432    0.000 1357.134    0.002 allGraphsTrain.py:42(<listcomp>)
                3365390   28.835    0.000 1328.198    0.000 layers.py:731(restart)
             4611212943  751.240    0.000 1112.693    0.000 enum.py:646(__hash__)
                3365390   15.134    0.000 1057.636    0.000 level.py:8(__init__)
               82562200  175.315    0.000 1044.491    0.000 layers.py:727(check)
             1122648490  696.506    0.000 1001.118    0.000 allGraphs.py:157(compress)
               86690310  977.154    0.000  977.154    0.000 {method 'eq' of 'torch._C._TensorBase' objects}
                3365390   40.420    0.000  913.614    0.000 levels.py:446(generate)
                 825622  487.285    0.001  910.403    0.001 agent.py:67(modify)
               82562200  900.158    0.000  900.158    0.000 {method 'argmax' of 'torch._C._TensorBase' objects}
        18989306/2476866   93.113    0.000  858.981    0.000 module.py:715(_call_impl)
               16155323  153.153    0.000  831.050    0.000 level.py:41(notUsed)
                1651244    5.420    0.000  777.020    0.000 network.py:24(forward)
                1651244   22.614    0.000  756.338    0.000 container.py:115(forward)
                 825622    7.106    0.000  731.230    0.001 grad_mode.py:23(decorate_context)
                 825622   29.416    0.000  711.427    0.001 adam.py:55(step)
              369043341  174.264    0.000  587.903    0.000 {built-in method builtins.any}
               82562200  128.920    0.000  585.702    0.000 layers.py:721(isFree)
                 825622  129.548    0.000  578.511    0.001 functional.py:53(adam)
                 825622    5.720    0.000  486.744    0.001 tensor.py:181(backward)
                 825622   17.786    0.000  485.085    0.001 agent.py:112(__call__)
                 825622    4.361    0.000  481.023    0.001 __init__.py:68(backward)
              569696443  385.766    0.000  456.782    0.000 layer.py:95(isFree)
                 825622  454.207    0.001  454.207    0.001 {method 'run_backward' of 'torch._C._EngineBase' objects}
                5779361  264.703    0.000  448.392    0.000 layer.py:167(NoRock_update)
               16155323   12.120    0.000  389.270    0.000 level.py:38(elementsIn)
             4611215660  361.453    0.000  361.453    0.000 {built-in method builtins.hash}
                2476866   13.109    0.000  339.816    0.000 tensor.py:576(__iter__)
                2476866  318.139    0.000  318.139    0.000 {method 'unbind' of 'torch._C._TensorBase' objects}
              170078232   55.361    0.000  311.581    0.000 {built-in method builtins.all}
                3302488    7.463    0.000  310.619    0.000 conv.py:422(forward)
                3302488   10.347    0.000  300.072    0.000 conv.py:414(_conv_forward)
                3302488  288.354    0.000  288.354    0.000 {built-in method conv2d}
               85864688  287.119    0.000  287.119    0.000 {method 'flatten' of 'torch._C._TensorBase' objects}
               16155323  125.054    0.000  251.012    0.000 level.py:39(<listcomp>)
               82562200  159.072    0.000  248.311    0.000 layers.py:610(check)
              143658362   75.203    0.000  243.394    0.000 overrides.py:1070(has_torch_function)
               82562200  147.466    0.000  241.677    0.000 layers.py:595(check)
               82562200  151.357    0.000  239.159    0.000 layers.py:625(check)
              249139320   67.906    0.000  234.908    0.000 layers.py:682(<genexpr>)
               23557730   19.881    0.000  233.355    0.000 layer.py:69(restart)
              633575280  184.375    0.000  223.776    0.000 layers.py:692(<genexpr>)
                3302488    9.031    0.000  222.958    0.000 linear.py:92(forward)
                3302488   17.151    0.000  209.326    0.000 functional.py:1669(linear)
               46234886  109.162    0.000  181.503    0.000 tensor.py:933(grad)
                3365490   88.930    0.000  177.463    0.000 layers.py:30(reset)
              775654344  171.793    0.000  171.793    0.000 level.py:32(inverse)
                8827146   22.661    0.000  159.994    0.000 allGraphs.py:198(<dictcomp>)
                 825622   37.250    0.000  159.260    0.000 allGraphs.py:209(transform)
                 825622    7.786    0.000  157.000    0.000 agent.py:59(modify_board)
                 825622   15.706    0.000  155.498    0.000 optimizer.py:167(zero_grad)
             1526578225  154.059    0.000  154.059    0.000 layer.py:91(positions)
                3302488  151.153    0.000  151.153    0.000 {built-in method addmm}
              702747158  129.051    0.000  129.051    0.000 enum.py:352(<genexpr>)
                 825622   73.906    0.000  126.849    0.000 collector.py:53(collect)
               16155323   78.871    0.000  126.138    0.000 {built-in method _functools.reduce}
               65956791   85.039    0.000  125.041    0.000 layers.py:107(isDone)
                3365390   65.124    0.000  120.334    0.000 level.py:16(<dictcomp>)
              203666884   85.483    0.000  119.047    0.000 layer.py:130(add)
               82562200   79.455    0.000  118.797    0.000 layers.py:581(check)
              415537738  117.886    0.000  117.886    0.000 layer.py:146(elements)
               13209952  115.700    0.000  115.700    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
                 825622   73.328    0.000  104.085    0.000 allGraphsTrain.py:41(<listcomp>)
                 825622  103.956    0.000  103.956    0.000 {built-in method torch._C._nn.one_hot}
              378135144   80.233    0.000   96.094    0.000 overrides.py:1083(<genexpr>)
                4953732    6.665    0.000   94.781    0.000 activation.py:713(forward)
               13209952   94.755    0.000   94.755    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
              282468672   60.117    0.000   93.111    0.000 allGraphs.py:192(<genexpr>)
                4953732   10.729    0.000   88.116    0.000 functional.py:1292(leaky_relu)
               34282179   41.381    0.000   82.238    0.000 allGraphs.py:150(expand)
                4953732   76.544    0.000   76.544    0.000 {built-in method torch._C._nn.leaky_relu}
                2476866   75.544    0.000   75.544    0.000 {method 'tolist' of 'torch._C._TensorBase' objects}
               89088958   48.176    0.000   71.534    0.000 layer.py:126(remove)
        821315039/821315037   57.757    0.000   71.503    0.000 {built-in method builtins.len}
              750658560   69.972    0.000   69.972    0.000 {method 'append' of 'list' objects}


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@n-62-20-11>
Subject: Job 9507356: <causal7_online_0> in cluster <dcc> Done

Job <causal7_online_0> was submitted from host <n-62-27-21> by user <s183905> in cluster <dcc> at Fri Apr  9 21:49:00 2021
Job was executed on host(s) <n-62-20-11>, in queue <gpuv100>, as user <s183905> in cluster <dcc> at Fri Apr  9 22:51:45 2021
</zhome/ee/d/137643> was used as the home directory.
</zhome/ee/d/137643/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Fri Apr  9 22:51:45 2021
Terminated at Sat Apr 10 10:46:58 2021
Results reported at Sat Apr 10 10:46:58 2021

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

    CPU time :                                   42803.51 sec.
    Max Memory :                                 2085 MB
    Average Memory :                             2084.26 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               14299.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                8
    Run time :                                   42913 sec.
    Turnaround time :                            46678 sec.

The output (if any) is above this job summary.

